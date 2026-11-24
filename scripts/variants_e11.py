"""
E11: what else helps the query link, on E8's fits (no refitting).

Families (anchors = the m most relevant pool papers with a reference list,
weighted by relevance; "+rel" = averaged with relevance on a rank scale with
weight lam on the other score, as in E10):

  cocite<m>[_l<lam>]      model-free: relevance-weighted count of anchors citing
                          the paper (bibliographic coupling)
  usvtlink<m>[_l<lam>]    the same on the USVT-denoised citation matrix
  v2_a<alpha>_g<gamma>    D-SPECTRA's greedy F(S) on the eta = 0 fit, with the
                          query-link + relevance score (lam = 0.75) in place of
                          text relevance r_i
  rrf<w>                  reciprocal-rank fusion (k = 60) of query link +
                          relevance (lam = 0.75, weight w) and USVT's selection
  qtext<ridge>[_l<lam>]   query link with the query's citing factor and offset
                          predicted from its own text: ridge regression, per
                          graph, from paper text embeddings to their fitted
                          citing factors (papers with a reference list)

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
from pilot_selection import (BUDGETS, load_graph, rank_pct, relevance, svd_modes,  # noqa: E402
                             usvt_threshold)
from tune_selection import kept_indices  # noqa: E402

ANCHOR_COUNTS = [5, 10, 20]
LAMS = [0.5, 0.75]


def mix(r, s, lam):
    return (1 - lam) * rank_pct(r) + lam * rank_pct(s)


def main():
    from sklearn.linear_model import Ridge
    from dspectra.selection import greedy_select, query_link_scores, top_k
    import pandas as pd
    ap = argparse.ArgumentParser()
    ap.add_argument("--graphs", required=True)
    ap.add_argument("--emb_dir", required=True)
    ap.add_argument("--operators", required=True, help="fit_variants.py output with *_full.npz")
    ap.add_argument("--kept_dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--rank", type=int, default=32)
    args = ap.parse_args()

    rows = []
    for path in sorted(glob.glob(f"{args.graphs}/*.json")):
        aid = os.path.basename(path)[:-5]
        full = f"{args.operators}/{aid}_full.npz"
        if not os.path.isfile(full):
            continue
        g, A = load_graph(path)
        z = np.load(f"{args.emb_dir}/{aid}.npz")
        En, Eq = z["nodes"], z["query"]
        r = relevance(Eq, En)
        zf = np.load(full)
        P = {k: zf[f"eta0_{k}"] for k in ("U", "V", "sigma", "p", "a", "b", "beta")}
        seeds = np.array([k for k, nd in enumerate(g["nodes"]) if nd["source"] == "seed"])
        linked = seeds[A[seeds].sum(1) > 0]
        pool = linked if len(linked) else seeds
        anchors = {m: pool[np.argsort(-r[pool], kind="stable")[:m]] for m in ANCHOR_COUNTS}

        # USVT-denoised citation matrix
        U_, s_, Vt_ = np.linalg.svd(A, full_matrices=False)
        k_ = max(1, int((s_ > usvt_threshold(A)).sum()))
        A_hat = (U_[:, :k_] * s_[:k_]) @ Vt_[:k_]

        scores = {}
        for m, anc in anchors.items():
            wt = r[anc] / max(r[anc].sum(), 1e-12)
            for name, M in (("cocite", A), ("usvtlink", A_hat)):
                s = wt @ M[anc] + 1e-6 * r  # ties broken by relevance
                scores[f"{name}{m}"] = s
                for lam in LAMS:
                    scores[f"{name}{m}_l{lam:g}"] = mix(r, s, lam)

        # query's citing role predicted from its text
        out_deg = A.sum(1)
        train = np.flatnonzero(out_deg > 0)
        for ridge in (1, 10, 100):
            reg = Ridge(alpha=ridge).fit(En[train], np.column_stack([P["U"][train], P["a"][train]]))
            pred = reg.predict(Eq[None])[0]
            u_q, a_q = pred[:-1], pred[-1]
            n = P["V"].shape[0]
            link = a_q + P["b"] + float(P["beta"]) * n * (P["V"] @ (u_q * P["sigma"])) / P["sigma"].sum()
            scores[f"qtext{ridge}"] = link
            for lam in LAMS:
                scores[f"qtext{ridge}_l{lam:g}"] = mix(r, link, lam)

        qlr = mix(r, query_link_scores(P, r, anchors[10]), 0.75)  # E10's tuned query link + relevance
        usvt_modes = svd_modes(A, args.rank, paper_axis=1, threshold=usvt_threshold(A))
        kept = kept_indices(g, args.kept_dir)
        node_key = {int(k): v for k, v in g["gt"]["node_keys"].items()}
        n_gt = max(g["gt"]["n_cited_in_related_work"], 1)
        reachable = len(set(node_key.values())) > 0
        for B_label in BUDGETS + ([0] if kept else []):
            B = len(kept) if B_label == 0 else B_label
            sel = {name: top_k(s, B) for name, s in scores.items()}
            sel["qlinkrel10_eta0_l0.75"] = top_k(qlr, B)
            for a in (0.25, 0.5, 0.75, 0.9):
                for gm in (1, 2, 5, 10):
                    sel[f"v2_a{a:g}_g{gm:g}"] = greedy_select(P["V"], P["p"], qlr, B, a, gm)
            usvt_sel = greedy_select(*usvt_modes, r, B, 0.5, 5.0)
            rank_q = np.empty(len(r)); rank_q[np.argsort(-qlr, kind="stable")] = np.arange(len(r))
            rank_u = np.full(len(r), np.inf); rank_u[usvt_sel] = np.arange(len(usvt_sel))
            for w in (0.25, 0.5, 0.75):
                rrf = w / (60 + rank_q) + (1 - w) / (60 + rank_u)
                sel[f"rrf{w:g}"] = top_k(rrf, B)
            for method, S in sel.items():
                hit = {node_key[i] for i in S if i in node_key}
                rows.append({"arxiv_id": aid, "method": method, "B": B_label,
                             "recall": len(hit) / n_gt, "reachable": reachable})
        print(f"{aid} done", flush=True)
    os.makedirs(args.out, exist_ok=True)
    pd.DataFrame(rows).to_csv(f"{args.out}/rows.csv", index=False)


if __name__ == "__main__":
    main()
