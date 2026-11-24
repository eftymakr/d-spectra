"""
Selection hyperparameters on existing fits (E10), no refitting:

  dspectra_a<alpha>_g<gamma>   greedy F(S) on the d_ev = 8 fit, alpha in --alphas
                               (weight on relevance), gamma in --gammas (coverage
                               saturation); alpha = 0.5, gamma = 5 is D-SPECTRA
  qlinkrel10_eta0_l<lam>       query link (10 anchors, eta = 0 fit) mixed with
                               relevance on a rank scale, weight lam on the link
                               score; lam = 0.5 is E8's query link + relevance

Writes one row per query, method and budget (recall of the human-cited
references, as in pilot_selection.py) to <out>/rows.csv.
"""
from __future__ import annotations

import argparse
import glob
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from pilot_selection import BUDGETS, load_graph, rank_pct, relevance  # noqa: E402


def kept_indices(g, kept_dir):
    import pandas as pd
    qdirs = glob.glob(f"{kept_dir}/*_{g['arxiv_id']}v*/")
    if not qdirs or not os.path.isfile(qdirs[0] + "kept.csv"):
        return None
    kept = pd.read_csv(qdirs[0] + "kept.csv", dtype={"arxiv_id": str})
    by_ax = {nd["arxiv_id"]: k for k, nd in enumerate(g["nodes"]) if nd.get("arxiv_id")}
    core = kept.arxiv_id.astype(str).str.extract(r"(\d{4}\.\d{4,5})")[0].dropna()
    return list(dict.fromkeys(by_ax[a] for a in core if a in by_ax))


def main():
    from dspectra.selection import greedy_select, query_link_scores, top_k
    import pandas as pd
    ap = argparse.ArgumentParser()
    ap.add_argument("--graphs", required=True)
    ap.add_argument("--emb_dir", required=True)
    ap.add_argument("--operators", required=True, help="fit_variants.py output with *_full.npz")
    ap.add_argument("--kept_dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--alphas", type=float, nargs="+", default=[0.25, 0.5, 0.75, 0.9])
    ap.add_argument("--gammas", type=float, nargs="+", default=[1, 2, 5, 10, 20])
    ap.add_argument("--lams", type=float, nargs="+", default=[0.25, 0.5, 0.75])
    args = ap.parse_args()

    rows = []
    for path in sorted(glob.glob(f"{args.graphs}/*.json")):
        aid = os.path.basename(path)[:-5]
        full = f"{args.operators}/{aid}_full.npz"
        if not os.path.isfile(full):
            continue
        g, A = load_graph(path)
        z = np.load(f"{args.emb_dir}/{aid}.npz")
        r = relevance(z["query"], z["nodes"])
        zf = np.load(full)
        P8 = {k: zf[f"d8_{k}"] for k in ("V", "p")}
        P0 = {k: zf[f"eta0_{k}"] for k in ("U", "V", "sigma", "p", "a", "b", "beta")}
        seeds = np.array([k for k, nd in enumerate(g["nodes"]) if nd["source"] == "seed"])
        linked = seeds[A[seeds].sum(1) > 0]
        pool = linked if len(linked) else seeds
        anchors = pool[np.argsort(-r[pool], kind="stable")[:10]]
        link = rank_pct(query_link_scores(P0, r, anchors))
        kept = kept_indices(g, args.kept_dir)
        node_key = {int(k): v for k, v in g["gt"]["node_keys"].items()}
        n_gt = max(g["gt"]["n_cited_in_related_work"], 1)
        for B_label in BUDGETS + ([0] if kept else []):
            B = len(kept) if B_label == 0 else B_label
            sel = {f"dspectra_a{a:g}_g{gm:g}": greedy_select(P8["V"], P8["p"], r, B, a, gm)
                   for a in args.alphas for gm in args.gammas}
            sel.update({f"qlinkrel10_eta0_l{lam:g}": top_k((1 - lam) * rank_pct(r) + lam * link, B)
                        for lam in args.lams})
            for method, S in sel.items():
                hit = {node_key[i] for i in S if i in node_key}
                rows.append({"arxiv_id": aid, "method": method, "B": B_label,
                             "recall": len(hit) / n_gt, "reachable": len(set(node_key.values())) > 0})
        print(f"{aid} done", flush=True)
    os.makedirs(args.out, exist_ok=True)
    pd.DataFrame(rows).to_csv(f"{args.out}/rows.csv", index=False)


if __name__ == "__main__":
    main()
