"""
E15: the query's own citing role as the centre of selection. Evaluation only,
on the existing eta = 0 and d_ev = 8 fits (fit_variants.py, *_full.npz).

  qmodes_<fit>_m<m>_<score>_a<alpha>_g<gamma>
      D-SPECTRA's greedy F(S) with query-anchored mode weights
      w_k ∝ p_k (u_q,k sigma_k)^2, u_q the relevance-weighted mean citing
      factor of the m most relevant pool papers with a reference list:
      cover the modes the query cites, not the modes the graph has.
      <score> is the relevance term: r (text relevance) or ql (query link
      + relevance, weight 0.75 on the link, as tuned in E10).
  prf<k>_r<rounds>[_keep]
      pseudo-relevance feedback on the query link: after scoring with the
      10 most relevant anchors, re-estimate u_q and a_q from the top-k
      papers of the query link + relevance score (weighted by that score),
      for 1 or 2 rounds; _keep adds the feedback papers to the original
      anchors instead of replacing them. Fit eta = 0.
  sprf<k>_r<rounds>[_keep]
      the same on SPECTRA co-citation (predicted citation probabilities of
      the anchors, E13's chosen setting: eta = 0, 5 anchors, all modes).
  usvt_cocite_rel, cocite_rel, qlink_rel, scocite_rel
      the frozen comparison methods (E11, E13)

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
from variants_e13 import sigmoid  # noqa: E402

LAM = 0.75
ALPHAS = [0.25, 0.5, 0.75]
GAMMAS = [1, 2, 5]
ANCHOR_COUNTS = [5, 10]
PRF_K = [5, 10, 20]


def mix(r, s, lam=LAM):
    return (1 - lam) * rank_pct(r) + lam * rank_pct(s)


def citing_role(P, weights, anchors):
    wt = weights / max(weights.sum(), 1e-12)
    return wt @ P["U"][anchors], float(wt @ P["a"][anchors])


def link_from_role(P, u_q, a_q):
    n = P["V"].shape[0]
    return a_q + P["b"] + float(P["beta"]) * n * (P["V"] @ (u_q * P["sigma"])) / P["sigma"].sum()


def cocite_from_anchors(P, weights, anchors, n):
    wt = weights / max(weights.sum(), 1e-12)
    K = n * (P["U"][anchors] * P["sigma"]) @ P["V"].T / P["sigma"].sum()
    prob = sigmoid(P["a"][anchors, None] + P["b"][None, :] + float(P["beta"]) * K)
    prob[np.arange(len(anchors)), anchors] = 0.0
    return wt @ prob


def main():
    from dspectra.selection import greedy_select, top_k
    import pandas as pd
    ap = argparse.ArgumentParser()
    ap.add_argument("--graphs", required=True)
    ap.add_argument("--emb_dir", required=True)
    ap.add_argument("--operators", required=True)
    ap.add_argument("--kept_dir", required=True)
    ap.add_argument("--design_pools", default="pools/qwen3-8b-awq_k50")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    dev = {os.path.basename(os.path.normpath(d)).split("_")[1][:10] for d in glob.glob(f"{args.design_pools}/*/")}
    rows = []
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
        fits = {f: {k: zf[f"{f}_{k}"] for k in ("U", "V", "sigma", "p", "a", "b", "beta")} for f in ("eta0", "d8")}
        P0 = fits["eta0"]

        # frozen comparison methods
        U_, s_, Vt_ = np.linalg.svd(A, full_matrices=False)
        k_ = max(1, int((s_ > usvt_threshold(A)).sum()))
        A_hat = (U_[:, :k_] * s_[:k_]) @ Vt_[:k_]
        w5, w10 = r[anchors[5]], r[anchors[10]]
        scores = {"usvt_cocite_rel": mix(r, w5 / w5.sum() @ A_hat[anchors[5]] + 1e-6 * r),
                  "cocite_rel": mix(r, w10 / w10.sum() @ A[anchors[10]] + 1e-6 * r)}
        u10, a10 = citing_role(P0, w10, anchors[10])
        qlr = mix(r, link_from_role(P0, u10, a10))
        scores["qlink_rel"] = qlr
        sco = cocite_from_anchors(P0, w5, anchors[5], n) + 1e-6 * r
        scores["scocite_rel"] = mix(r, sco)

        # pseudo-relevance feedback
        for k in PRF_K:
            for keep in (False, True):
                cur_l, cur_s = qlr, mix(r, sco)
                for rnd in (1, 2):
                    top_l = np.array(top_k(cur_l, k))
                    anc = np.concatenate([anchors[10], top_l]) if keep else top_l
                    wt = np.concatenate([w10, cur_l[top_l]]) if keep else cur_l[top_l]
                    u, a = citing_role(P0, wt, anc)
                    cur_l = mix(r, link_from_role(P0, u, a))
                    top_s = np.array(top_k(cur_s, k))
                    anc = np.concatenate([anchors[5], top_s]) if keep else top_s
                    wt = np.concatenate([w5, cur_s[top_s]]) if keep else cur_s[top_s]
                    cur_s = mix(r, cocite_from_anchors(P0, wt, anc, n) + 1e-6 * r)
                    tag = f"{k}_r{rnd}" + ("_keep" if keep else "")
                    scores[f"prf{tag}"] = cur_l
                    scores[f"sprf{tag}"] = cur_s

        # query-anchored mode weights
        greedy = {}
        for f, P in fits.items():
            for m, anc in anchors.items():
                u_q, _ = citing_role(P, r[anc], anc)
                w = P["p"] * (u_q * P["sigma"]) ** 2
                w = w / max(w.sum(), 1e-12)
                for sname, s in (("r", r), ("ql", qlr)):
                    for a in ALPHAS:
                        for gm in GAMMAS:
                            greedy[f"qmodes_{f}_m{m}_{sname}_a{a:g}_g{gm:g}"] = (P["V"], P["p"], s, w, a, gm)

        node_key = {int(k): v for k, v in g["gt"]["node_keys"].items()}
        n_gt = max(g["gt"]["n_cited_in_related_work"], 1)
        reachable = len(set(node_key.values())) > 0
        split = "design" if aid in dev else "held-out"
        for B_label in BUDGETS + [0]:
            B = len(kept) if B_label == 0 else B_label
            sel = {name: top_k(s, B) for name, s in scores.items()}
            for name, (V, p, s, w, a, gm) in greedy.items():
                sel[name] = greedy_select(V, p, s, B, a, gm, weights=w)
            for method, S in sel.items():
                hit = {node_key[i] for i in S if i in node_key}
                rows.append({"arxiv_id": aid, "method": method, "B": B_label, "recall": len(hit) / n_gt,
                             "reachable": reachable, "split": split})
        print(f"{aid} done", flush=True)
    os.makedirs(args.out, exist_ok=True)
    pd.DataFrame(rows).to_csv(f"{args.out}/rows.csv", index=False)


if __name__ == "__main__":
    main()
