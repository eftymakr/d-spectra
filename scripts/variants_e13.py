"""
E13: can the fitted SPECTRA model itself win? Evaluation only, on existing
d_ev = 8 and eta = 0 fits (fit_variants.py, *_full.npz).

  scocite_<fit>_k<k>_m<m>[_obs]   SPECTRA co-citation: the relevance-weighted mean of
                                   the m most relevant pool papers' predicted citation
                                   probabilities P(i cites j) (self-citation excluded),
                                   with the kernel truncated to its top k modes
                                   (k = 32: all); _obs adds the observed citations;
                                   mixed with relevance (weight 0.75 on the score)
  learned / learned_nospectra      logistic regression (fixed settings) trained on the
                                   design queries, ranking papers by relevance,
                                   co-citation, USVT co-citation, SPECTRA co-citation,
                                   SPECTRA's popularity offset b_j, in-graph citations
                                   and paper type; _nospectra drops the two SPECTRA features
  usvt_cocite_rel, cocite_rel, qlink_rel   E10/E11's frozen methods, for paired tests

Writes one row per query, method and budget to <out>/rows.csv.
"""
from __future__ import annotations

import argparse
import glob
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from pilot_selection import BUDGETS, load_graph, rank_pct, relevance, usvt_threshold  # noqa: E402
from tune_selection import kept_indices  # noqa: E402

PREFIXES = [2, 4, 8, 16, 32]
ANCHOR_COUNTS = [5, 10]
LAM = 0.75
FEATURES = ["relevance", "cocite", "usvt_cocite", "spectra_cocite", "popularity_b", "in_degree",
            "is_pool", "is_ref"]
SPECTRA_FEATURES = {"spectra_cocite", "popularity_b"}


def mix(r, s, lam=LAM):
    return (1 - lam) * rank_pct(r) + lam * rank_pct(s)


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def main():
    from dspectra.selection import query_link_scores, top_k
    from sklearn.linear_model import LogisticRegression
    import pandas as pd
    ap = argparse.ArgumentParser()
    ap.add_argument("--graphs", required=True)
    ap.add_argument("--emb_dir", required=True)
    ap.add_argument("--operators", required=True)
    ap.add_argument("--kept_dir", required=True)
    ap.add_argument("--design_pools", default="pools/qwen3-8b-awq_k50")
    ap.add_argument("--learned_config", default="scocite_eta0_k32_m10",
                    help="the SPECTRA co-citation score used as a feature of the learned ranker")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    dev = {os.path.basename(os.path.normpath(d)).split("_")[1][:10] for d in glob.glob(f"{args.design_pools}/*/")}
    rows, feats, per_query = [], [], {}
    for path in sorted(glob.glob(f"{args.graphs}/*.json")):
        aid = os.path.basename(path)[:-5]
        full = f"{args.operators}/{aid}_full.npz"
        if not os.path.isfile(full):
            continue
        g, A = load_graph(path)
        kept = kept_indices(g, args.kept_dir)
        if not kept:
            continue
        z = np.load(f"{args.emb_dir}/{aid}.npz")
        r = relevance(z["query"], z["nodes"])
        zf = np.load(full)
        n = A.shape[0]
        seeds = np.array([k for k, nd in enumerate(g["nodes"]) if nd["source"] == "seed"])
        linked = seeds[A[seeds].sum(1) > 0]
        pool = linked if len(linked) else seeds
        anchors = {m: pool[np.argsort(-r[pool], kind="stable")[:m]] for m in ANCHOR_COUNTS}
        weights = {m: r[a] / max(r[a].sum(), 1e-12) for m, a in anchors.items()}

        scores = {}
        for fit in ("eta0", "d8"):
            P = {k: zf[f"{fit}_{k}"] for k in ("U", "V", "sigma", "a", "b", "beta")}
            norm = P["sigma"].sum()
            for k in PREFIXES:
                K = n * (P["U"][:, :k] * P["sigma"][:k]) @ P["V"][:, :k].T / norm
                for m, anc in anchors.items():
                    prob = sigmoid(P["a"][anc, None] + P["b"][None, :] + float(P["beta"]) * K[anc])
                    prob[np.arange(len(anc)), anc] = 0.0  # P(i cites i) is not modelled
                    pred = weights[m] @ prob + 1e-6 * r
                    obs = weights[m] @ (A[anc] + prob) + 1e-6 * r
                    scores[f"scocite_{fit}_k{k}_m{m}"] = mix(r, pred)
                    scores[f"scocite_{fit}_k{k}_m{m}_obs"] = mix(r, obs)
                    if f"scocite_{fit}_k{k}_m{m}" == args.learned_config:
                        spectra_feat = pred
        # E10/E11's frozen methods
        U_, s_, Vt_ = np.linalg.svd(A, full_matrices=False)
        k_ = max(1, int((s_ > usvt_threshold(A)).sum()))
        A_hat = (U_[:, :k_] * s_[:k_]) @ Vt_[:k_]
        cocite = weights[10] @ A[anchors[10]] + 1e-6 * r
        usvt_cocite = weights[5] @ A_hat[anchors[5]] + 1e-6 * r
        P0 = {k: zf[f"eta0_{k}"] for k in ("U", "V", "sigma", "p", "a", "b", "beta")}
        scores["usvt_cocite_rel"] = mix(r, usvt_cocite)
        scores["cocite_rel"] = mix(r, cocite)
        scores["qlink_rel"] = mix(r, query_link_scores(P0, r, anchors[10]))

        node_key = {int(k): v for k, v in g["gt"]["node_keys"].items()}
        label = np.zeros(n)
        label[list(node_key)] = 1.0
        src = np.array([nd["source"] for nd in g["nodes"]])
        F = np.column_stack([rank_pct(r), rank_pct(cocite), rank_pct(usvt_cocite), rank_pct(spectra_feat),
                             rank_pct(P0["b"]), rank_pct(A.sum(0) + 1e-6 * r), src == "seed", src == "ref"]).astype(float)
        feats.append(pd.DataFrame(F, columns=FEATURES).assign(arxiv_id=aid, node=np.arange(n), label=label))
        per_query[aid] = (scores, kept, node_key, max(g["gt"]["n_cited_in_related_work"], 1),
                          len(set(node_key.values())) > 0)
        print(f"{aid} scored", flush=True)

    # learned rankers: trained on the design queries only, fixed settings
    X = pd.concat(feats, ignore_index=True)
    train = X[X.arxiv_id.isin(dev)]
    for name, cols in (("learned", FEATURES), ("learned_nospectra", [c for c in FEATURES if c not in SPECTRA_FEATURES])):
        clf = LogisticRegression(C=1.0, class_weight="balanced", max_iter=2000).fit(train[cols], train.label)
        X[name] = clf.decision_function(X[cols])
        coef = dict(zip(cols, np.round(clf.coef_[0], 3)))
        print(f"{name} coefficients: {coef}", flush=True)
    for aid, (scores, kept, node_key, n_gt, reachable) in per_query.items():
        q = X[X.arxiv_id == aid].sort_values("node")
        scores["learned"] = q["learned"].values
        scores["learned_nospectra"] = q["learned_nospectra"].values
        for B_label in BUDGETS + [0]:
            B = len(kept) if B_label == 0 else B_label
            for method, s in scores.items():
                hit = {node_key[i] for i in top_k(s, B) if i in node_key}
                rows.append({"arxiv_id": aid, "method": method, "B": B_label, "recall": len(hit) / n_gt,
                             "reachable": reachable, "split": "design" if aid in dev else "held-out"})
    os.makedirs(args.out, exist_ok=True)
    pd.DataFrame(rows).to_csv(f"{args.out}/rows.csv", index=False)


if __name__ == "__main__":
    main()
