"""
E23 (rules/e23_sparse_selection_rules.md): selection recall on citation graphs thinned to a
fraction of their citations. Evaluation only, from fit_variants.py --fits d8 eta0 cv
--edge_keep <keep> --edge_seed <s>. Every method sees only the thinned graph.

  python scripts/sparse_select_e23.py --operators results/e23_k50_e0 results/e23_k50_e1 ... \
      --edge_keep 0.5 --out results/e23            # rows.csv, then summary.md / tests.csv
  python scripts/sparse_select_e23.py --operators results/e8_small --edge_keep 1.0 \
      --out results/e23_check                      # the script check at full density
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from pilot_selection import load_graph, rank_pct, relevance, svd_modes, usvt_threshold  # noqa: E402
from tune_selection import kept_indices  # noqa: E402

PRIMARY = [("P1", "dspectra_cv", "dspectra_eta0"), ("P2", "dspectra_d8", "dspectra_eta0"),
           ("P3", "qlink_rel_cv", "qlink_rel_eta0"), ("P4", "scocite_rel_cv", "usvt_cocite_rel"),
           ("P5", "qlink_rel_cv", "usvt_cocite_rel"), ("P6", "dspectra_cv", "usvt")]


def mix(r, s, lam=0.75):
    return (1 - lam) * rank_pct(r) + lam * rank_pct(s)


def thin(A, keep, seed):
    """The thinning of fit_variants.py, reproduced exactly."""
    if keep >= 1.0:
        return A
    A = A.copy()
    ii, jj = np.nonzero(A)
    drop = np.random.default_rng(seed).random(len(ii)) >= keep
    A[ii[drop], jj[drop]] = 0.0
    return A


def select(g, A, r, zf, B, rank=32):
    from dspectra.selection import greedy_select, query_link_scores, top_k
    n = A.shape[0]
    seeds = np.array([k for k, nd in enumerate(g["nodes"]) if nd["source"] == "seed"])
    linked = seeds[A[seeds].sum(1) > 0]
    pool = linked if len(linked) else seeds

    def anchors(m):
        return pool[np.argsort(-r[pool], kind="stable")[:m]]

    def cocite(M, m):
        anc = anchors(m)
        return (r[anc] / max(r[anc].sum(), 1e-12)) @ M[anc] + 1e-6 * r

    def scocite(P, m):
        anc = anchors(m)
        K = n * (P["U"][anc] * P["sigma"]) @ P["V"].T / P["sigma"].sum()
        prob = 1.0 / (1.0 + np.exp(-(P["a"][anc, None] + P["b"][None, :] + float(P["beta"]) * K)))
        prob[np.arange(len(anc)), anc] = 0.0
        return (r[anc] / max(r[anc].sum(), 1e-12)) @ prob + 1e-6 * r

    U_, s_, Vt_ = np.linalg.svd(A, full_matrices=False)
    k_ = max(1, int((s_ > usvt_threshold(A)).sum()))
    A_hat = (U_[:, :k_] * s_[:k_]) @ Vt_[:k_]
    out = {
        "fixed_k": top_k(r, B, candidates=seeds),
        "relevance_only": top_k(r, B),
        "most_cited": top_k(A.sum(0) + 1e-6 * r, B),
        "cocite_rel": top_k(mix(r, cocite(A, 10)), B),
        "usvt_cocite_rel": top_k(mix(r, cocite(A_hat, 5)), B),
        "usvt": greedy_select(*svd_modes(A, rank, paper_axis=1, threshold=usvt_threshold(A)), r, B, 0.5, 5.0),
        "raw_svd": greedy_select(*svd_modes(A, rank, paper_axis=1), r, B, 0.5, 5.0),
    }
    for fit in ("eta0", "cv", "d8"):
        P = {k: zf[f"{fit}_{k}"] for k in ("U", "V", "sigma", "p", "a", "b", "beta")}
        out[f"dspectra_{fit}"] = greedy_select(P["V"], P["p"], r, B, 0.5, 5.0)
        if fit != "d8":
            out[f"qlink_rel_{fit}"] = top_k(mix(r, query_link_scores(P, r, anchors(10))), B)
            out[f"scocite_rel_{fit}"] = top_k(mix(r, scocite(P, 5)), B)
    return out, k_


def rows_for(op_dir, args, dev):
    cfg_seed = None
    rows = []
    for path in sorted(glob.glob(f"{args.graphs}/*.json")):
        aid = os.path.basename(path)[:-5]
        full, info_path = f"{op_dir}/operators/{aid}_full.npz", f"{op_dir}/operators/{aid}.json"
        if not os.path.isfile(full):
            continue
        info = json.load(open(info_path))
        cfg = info["_config"]
        keep, eseed = cfg.get("edge_keep", 1.0), cfg.get("edge_seed", 0)
        assert abs(keep - args.edge_keep) < 1e-9, (op_dir, keep)
        cfg_seed = eseed
        g, A0 = load_graph(path)
        A = thin(A0, keep, eseed)
        assert int(A.sum()) == cfg.get("n_edges_fit", int(A.sum())), (aid, int(A.sum()), cfg.get("n_edges_fit"))
        kept = kept_indices(g, args.kept_dir)
        if not kept:
            continue
        z = np.load(f"{args.emb_dir}/{aid}.npz")
        r = relevance(z["query"], z["nodes"])
        sel, k_usvt = select(g, A, r, np.load(full), len(kept))
        node_key = {int(k): v for k, v in g["gt"]["node_keys"].items()}
        n_gt = max(g["gt"]["n_cited_in_related_work"], 1)
        hp = {p["eta"]: p["auc"] for p in info["dspectra_cv"]["heldout"]}
        for method, S in sel.items():
            hit = {node_key[i] for i in S if i in node_key}
            rows.append({"arxiv_id": aid, "edge_seed": eseed, "keep": keep, "method": method, "B": len(kept),
                         "recall": len(hit) / n_gt, "reachable": len(set(node_key.values())) > 0,
                         "split": "design" if aid in dev else "held-out",
                         "eta_cv": info["dspectra_cv"]["eta"], "d_ev_cv": info["dspectra_cv"]["d_ev"],
                         "d_ev_eta0": info["dspectra_eta0"]["d_ev"], "d_ev_d8": info["dspectra"]["d_ev"],
                         "auc_gain_cv": max(hp.values()) - hp[0.0], "usvt_rank": k_usvt, "n_edges": int(A.sum())})
    return rows, cfg_seed


def holm(p):
    """Holm step-down adjusted p-values."""
    p = np.asarray(p, float); order = np.argsort(p); m = len(p)
    adj = np.empty(m); run = 0.0
    for rank, i in enumerate(order):
        run = max(run, (m - rank) * p[i]); adj[i] = min(run, 1.0)
    return adj


def summarize(df, out):
    import pandas as pd
    from scipy.stats import spearmanr, wilcoxon
    seeds = sorted(df.edge_seed.unique())
    q = df.groupby(["arxiv_id", "split", "method"]).recall.mean().unstack("method")   # mean over thinnings
    held = q.xs("held-out", level="split")
    lines = [f"# E23: selection on graphs with {df.keep.iloc[0]:g} of the citations (rules/e23_sparse_selection_rules.md)", "",
             f"Thinnings (edge seeds): {seeds}; queries: {held.shape[0]} held-out, {q.xs('design', level='split').shape[0]} design; "
             f"mean citations per graph {df.drop_duplicates(['arxiv_id', 'edge_seed']).n_edges.mean():.0f}.", ""]
    one = df.drop_duplicates(["arxiv_id", "edge_seed"])
    lines += [f"cv rule: eta < 0 on {(one.eta_cv < 0).mean():.0%} of fits (median eta {one.eta_cv.median():+.2f}); mean d_ev: cv "
              f"{one.d_ev_cv.mean():.1f}, eta = 0 {one.d_ev_eta0.mean():.1f}, d8 {one.d_ev_d8.mean():.1f}; "
              f"USVT rank median {one.usvt_rank.median():.0f}.", "",
              "## Recall at B = kept (mean over thinnings, then over queries)", "", "| method | held-out (43) | design (20) |", "|---|---|---|"]
    des = q.xs("design", level="split")
    for m in held.mean().sort_values(ascending=False).index:
        lines.append(f"| {m} | {held[m].mean():.3f} | {des[m].mean():.3f} |")
    tests = []
    for name, a, b in PRIMARY:
        d = held[a] - held[b]
        p = wilcoxon(held[a], held[b]).pvalue if (d != 0).any() else 1.0
        tests.append({"test": name, "a": a, "b": b, "diff": d.mean(), "wins": int((d > 0).sum()), "losses": int((d < 0).sum()), "p": p})
    t = pd.DataFrame(tests)
    t["holm"] = holm(t.p.values)
    t.to_csv(f"{out}/tests.csv", index=False)
    lines += ["", "## Primary family (held-out, paired Wilcoxon, Holm over 6)", "", "| test | comparison | difference | wins/losses | p | Holm p |", "|---|---|---|---|---|---|"]
    for _, x in t.iterrows():
        lines.append(f"| {x.test} | {x.a} - {x.b} | {x['diff']:+.4f} | {x.wins}/{x.losses} | {x.p:.3f} | {x.holm:.3f} |")
    g = df[df.method.isin(["dspectra_cv", "dspectra_eta0"])].pivot_table(index=["arxiv_id", "edge_seed"], columns="method", values="recall")
    gain = one.set_index(["arxiv_id", "edge_seed"]).auc_gain_cv
    rho, pr = spearmanr(gain.loc[g.index], g.dspectra_cv - g.dspectra_eta0)
    lines += ["", f"Per fit, Spearman between the cv fit's held-out AUC gain over eta = 0 and the recall difference of P1: rho = {rho:+.2f} (p = {pr:.3f}, n = {len(g)})."]
    open(f"{out}/summary.md", "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


def main():
    import pandas as pd
    ap = argparse.ArgumentParser()
    ap.add_argument("--operators", nargs="+", required=True)
    ap.add_argument("--edge_keep", type=float, required=True)
    ap.add_argument("--graphs", default="data/graphs_small")
    ap.add_argument("--emb_dir", default="data/embeddings_small")
    ap.add_argument("--kept_dir", default="outputs/dsbase_final/s0")
    ap.add_argument("--design_pools", default="pools/qwen3-8b-awq_k50")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    dev = {os.path.basename(os.path.normpath(d)).split("_")[1][:10] for d in glob.glob(f"{args.design_pools}/*/")}
    rows = []
    for op in args.operators:
        r, s = rows_for(op, args, dev)
        print(f"{op}: {len({x['arxiv_id'] for x in r})} graphs, edge seed {s}", flush=True)
        rows += r
    os.makedirs(args.out, exist_ok=True)
    df = pd.DataFrame(rows)
    df.to_csv(f"{args.out}/rows.csv", index=False)
    summarize(df, args.out)


if __name__ == "__main__":
    main()
