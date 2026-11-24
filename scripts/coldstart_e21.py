"""
E21: an inductive citing role for cold-start queries (rules: scratchpad/e21_rules.md).

The query has no reference list, so no fitted citing role; every selector so far
averages anchors instead. Here a ridge map from text embedding to fitted citing
factor U, learned on the graph's own nodes, gives the query a role of its own, and
the fit's row b_j + beta n (u_q sigma) . V_j / sum(sigma) scores the candidates.

Stages:
  fit   per graph, remove up to 20 pool papers with >= 5 in-graph references
        (the pseudo-queries) and fit the rest at eta = 0 (GPU; --worker k/N)
  eval  pseudo-queries: recall of their in-graph references at B = 15 and 30 for
        relevance only, USVT co-citation + rel, SPECTRA co-citation + rel,
        query link + rel, inductive, inductive + rel        -> results/e21/pseudo_rows.csv
  real  the benchmark queries on the E8 eta = 0 fits, B = kept -> results/e21/real_rows.csv
  tests the pre-registered tests                            -> results/e21/tests.csv
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from pilot_selection import load_graph, rank_pct, relevance, usvt_threshold  # noqa: E402
from tune_selection import kept_indices  # noqa: E402

LAM, M_COCITE, M_QLINK, MIN_REFS, N_PSEUDO = 0.75, 5, 10, 5, 20
ALPHAS = np.logspace(-2, 4, 13)
DEV = {os.path.basename(os.path.normpath(d)).split("_")[1][:10] for d in glob.glob("pools/qwen3-8b-awq_k50/*/")}
PRIMARY = [("inductive_rel", "usvt_cocite_rel"), ("inductive_rel", "scocite_rel")]


def mix(r, s, lam=LAM):
    return (1 - lam) * rank_pct(r) + lam * rank_pct(s)


def choose_pseudo(g, A):
    rng = np.random.default_rng(0)
    cand = np.array([k for k, nd in enumerate(g["nodes"]) if nd["source"] == "seed" and A[k].sum() >= MIN_REFS], dtype=int)
    if len(cand) == 0:
        return cand
    return np.sort(rng.choice(cand, min(N_PSEUDO, len(cand)), replace=False))


def inductive_map(Z, P, train):
    """Ridge (intercept, penalty by leave-one-out GCV) from text embedding to citing factor."""
    from sklearn.linear_model import RidgeCV
    return RidgeCV(alphas=ALPHAS).fit(Z[train], P["U"][train])


def role_row(P, u_q):
    n = P["V"].shape[0]
    return P["b"] + float(P["beta"]) * n * (P["V"] @ (u_q * P["sigma"])) / P["sigma"].sum()


def selector_scores(A, P, Z, z_q, seeds):
    """Every method's score over the candidates (rows of A), for a query with text
    embedding z_q; `seeds` = candidate indices that are pool papers."""
    from dspectra.selection import query_link_scores
    r = relevance(z_q, Z)
    linked = seeds[A[seeds].sum(1) > 0]
    pool = linked if len(linked) else seeds

    def anchors(m):
        return pool[np.argsort(-r[pool], kind="stable")[:m]]

    def cocite(M, m):
        anc = anchors(m)
        return (r[anc] / max(r[anc].sum(), 1e-12)) @ M[anc] + 1e-6 * r

    U_, s_, Vt_ = np.linalg.svd(A, full_matrices=False)
    k_ = max(1, int((s_ > usvt_threshold(A)).sum()))
    A_hat = (U_[:, :k_] * s_[:k_]) @ Vt_[:k_]

    def scocite(m):
        anc = anchors(m)
        n = A.shape[0]
        K = n * (P["U"][anc] * P["sigma"]) @ P["V"].T / P["sigma"].sum()
        prob = 1.0 / (1.0 + np.exp(-(P["a"][anc, None] + P["b"][None, :] + float(P["beta"]) * K)))
        prob[np.arange(len(anc)), anc] = 0.0
        return (r[anc] / max(r[anc].sum(), 1e-12)) @ prob + 1e-6 * r

    train = np.where(A.sum(1) > 0)[0]
    u_q = inductive_map(Z, P, train).predict(z_q[None])[0]
    ind = role_row(P, u_q)
    return {"relevance_only": r,
            "usvt_cocite_rel": mix(r, cocite(A_hat, M_COCITE)),
            "scocite_rel": mix(r, scocite(M_COCITE)),
            "qlink_rel": mix(r, query_link_scores(P, r, anchors(M_QLINK))),
            "inductive": ind,
            "inductive_rel": mix(r, ind)}


def load_params(z, prefix):
    return {k: z[f"{prefix}{k}"] for k in ("U", "V", "sigma", "p", "a", "b", "beta")}


def graphs(args):
    for path in sorted(glob.glob(os.path.join(args.graphs, "*.json"))):
        aid = os.path.basename(path)[:-5]
        if os.path.isfile(os.path.join(args.emb_dir, f"{aid}.npz")):
            yield aid, path


def stage_fit(args):
    import torch
    from dspectra.model import FitConfig, fit, parameters
    k, N = (int(x) for x in args.worker.split("/"))
    os.makedirs(f"{args.out}/fits", exist_ok=True)
    cfg = FitConfig(rank=32, epochs=6000, device="cuda" if torch.cuda.is_available() else "cpu")
    if args.epochs:
        cfg.epochs = args.epochs
    for i, (aid, path) in enumerate(graphs(args)):
        out = f"{args.out}/fits/{aid}.npz"
        if i % N != k or os.path.isfile(out):
            continue
        g, A = load_graph(path)
        pseudo = choose_pseudo(g, A)
        keep = np.array([j for j in range(A.shape[0]) if j not in set(pseudo.tolist())])
        m = fit(A[np.ix_(keep, keep)], "directed", 0.0, cfg, seed=0)
        np.savez(out, keep=keep, pseudo=pseudo, **parameters(m))
        print(f"{aid}: {len(pseudo)} pseudo-queries, fitted {len(keep)} nodes", flush=True)


def stage_eval(args):
    rows = []
    for aid, path in graphs(args):
        fpath = f"{args.out}/fits/{aid}.npz"
        if not os.path.isfile(fpath):
            continue
        g, A = load_graph(path)
        z = np.load(os.path.join(args.emb_dir, f"{aid}.npz"))["nodes"]
        f = np.load(fpath)
        keep, pseudo = f["keep"], f["pseudo"]
        P = {k: f[k] for k in ("U", "V", "sigma", "p", "a", "b", "beta")}
        A_sub, Z_sub = A[np.ix_(keep, keep)], z[keep]
        seeds = np.array([j for j, k0 in enumerate(keep) if g["nodes"][k0]["source"] == "seed"], dtype=int)
        split = "design" if aid in DEV else "held-out"
        for q in pseudo:
            refs = np.where(A[q, keep] > 0)[0]
            if len(refs) == 0:
                continue
            for method, s in selector_scores(A_sub, P, Z_sub, z[q], seeds).items():
                order = np.argsort(-s, kind="stable")
                for B in (15, 30):
                    rows.append({"arxiv_id": aid, "split": split, "pseudo": int(q), "n_refs": len(refs), "method": method,
                                 "B": B, "recall": len(set(order[:B]) & set(refs)) / len(refs)})
        print(f"{aid}: {len(pseudo)} pseudo-queries", flush=True)
    pd.DataFrame(rows).to_csv(f"{args.out}/pseudo_rows.csv", index=False)


def stage_real(args):
    rows = []
    for aid, path in graphs(args):
        full = os.path.join(args.operators, f"{aid}_full.npz")
        if not os.path.isfile(full):
            continue
        g, A = load_graph(path)
        kept = kept_indices(g, args.kept_dir)
        if not kept:
            continue
        zf = np.load(os.path.join(args.emb_dir, f"{aid}.npz"))
        P = load_params(np.load(full), "eta0_")
        seeds = np.array([k for k, nd in enumerate(g["nodes"]) if nd["source"] == "seed"])
        node_key = {int(k): v for k, v in g["gt"]["node_keys"].items()}
        n_gt = max(g["gt"]["n_cited_in_related_work"], 1)
        split = "design" if aid in DEV else "held-out"
        for method, s in selector_scores(A, P, zf["nodes"], zf["query"], seeds).items():
            S = np.argsort(-s, kind="stable")[:len(kept)]
            rows.append({"arxiv_id": aid, "split": split, "method": method, "B": 0,
                         "recall": len({node_key[k] for k in S if k in node_key}) / n_gt,
                         "reachable": len(node_key) > 0})
    pd.DataFrame(rows).to_csv(f"{args.out}/real_rows.csv", index=False)


def stage_tests(args):
    from scipy.stats import wilcoxon
    from seed_tests import holm
    out = []
    pr = pd.read_csv(f"{args.out}/pseudo_rows.csv", dtype={"arxiv_id": str})
    for B in (15, 30):
        d = pr[(pr.B == B) & (pr.split == "held-out")]
        by_graph = d.groupby(["arxiv_id", "method"]).recall.mean().unstack()
        by_pseudo = d.pivot_table(index=["arxiv_id", "pseudo"], columns="method", values="recall")
        for a, b in PRIMARY:
            for unit, tab in (("graph", by_graph), ("pseudo-query", by_pseudo)):
                x = (tab[a] - tab[b]).dropna()
                out.append({"set": f"pseudo B={B}", "unit": unit, "a": a, "b": b, "mean_a": tab[a].mean(), "mean_b": tab[b].mean(),
                            "diff": x.mean(), "w/l": f"{(x > 0).sum()}/{(x < 0).sum()}",
                            "p": wilcoxon(x).pvalue if (x != 0).any() else 1.0, "n": len(x)})
    rr = pd.read_csv(f"{args.out}/real_rows.csv", dtype={"arxiv_id": str})
    tab = rr[rr.split == "held-out"].pivot_table(index="arxiv_id", columns="method", values="recall")
    for a, b in PRIMARY:
        x = (tab[a] - tab[b]).dropna()
        out.append({"set": "real B=kept", "unit": "query", "a": a, "b": b, "mean_a": tab[a].mean(), "mean_b": tab[b].mean(),
                    "diff": x.mean(), "w/l": f"{(x > 0).sum()}/{(x < 0).sum()}",
                    "p": wilcoxon(x).pvalue if (x != 0).any() else 1.0, "n": len(x)})
    t = pd.DataFrame(out)
    t["holm"] = np.nan
    for key in [("pseudo B=15", "graph"), ("pseudo B=30", "graph"), ("real B=kept", "query")]:
        m = (t.set == key[0]) & (t.unit == key[1])
        t.loc[m, "holm"] = holm(t.loc[m, "p"])
    t.to_csv(f"{args.out}/tests.csv", index=False)
    pd.set_option("display.width", 220)
    print("means, held-out graphs (pseudo-queries, B=15 / B=30) and held-out real queries (B=kept):")
    for B in (15, 30):
        d = pr[(pr.B == B) & (pr.split == "held-out")]
        print(f"  pseudo B={B}:", d.groupby(["arxiv_id", "method"]).recall.mean().unstack().mean().round(3).to_dict())
    print("  real:", tab.mean().round(3).to_dict())
    print(t.round(4).to_string(index=False))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["fit", "eval", "real", "tests"], required=True)
    ap.add_argument("--worker", default="0/1")
    ap.add_argument("--graphs", default="data/graphs_small")
    ap.add_argument("--emb_dir", default="data/embeddings_small")
    ap.add_argument("--operators", default="results/e8_small/operators")
    ap.add_argument("--kept_dir", default="outputs/dsbase_final/s0")
    ap.add_argument("--out", default="results/e21")
    ap.add_argument("--epochs", type=int, default=0, help="override (smoke tests only)")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    {"fit": stage_fit, "eval": stage_eval, "real": stage_real, "tests": stage_tests}[args.stage](args)


if __name__ == "__main__":
    main()
