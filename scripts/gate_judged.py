"""
The proposal's step-2 gate on judged coverage: does d_ev of a baseline's
citation set track the judge's coverage scores, across queries, better than
the size of that set?

For each query: S = the papers DeepScholar-base's report cites (and, separately,
all papers its filter passed to the writer), mapped to our graph by arXiv id;
d_ev(S) on the d_ev = 8 fit, as in the E6 premise check. Spearman correlations
with each judged metric, plus the partial correlation of d_ev(S) given |S|.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from build_graphs import arxiv_core  # noqa: E402
from pilot_selection import load_graph, relevance  # noqa: E402

METRICS = ["nugget_coverage", "reference_coverage", "document_importance", "cite_p", "claim_coverage",
           "coverage_relevance_rate"]


def partial_spearman(x, y, z):
    """Spearman correlation of x and y after removing the rank-linear effect of z."""
    rx, ry, rz = (pd.Series(v).rank().values for v in (x, y, z))
    res = lambda a: a - np.polyval(np.polyfit(rz, a, 1), rz)  # noqa: E731
    return spearmanr(res(rx), res(ry))


def main():
    from dspectra.selection import set_d_ev
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge_results", required=True, help="judge output folder (one subfolder per metric)")
    ap.add_argument("--judge_inputs", required=True, help="the judged reports (to_judge_format.py output)")
    ap.add_argument("--outputs", required=True, help="DeepScholar-base outputs with kept.csv")
    ap.add_argument("--graphs", required=True)
    ap.add_argument("--emb_dir", required=True)
    ap.add_argument("--operators", required=True)
    ap.add_argument("--dataset", default="/home/eftychia/Spectra/deepscholar-bench/dataset/papers_with_related_works.csv")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    order = pd.read_csv(args.dataset).arxiv_id.astype(str).map(arxiv_core).tolist()
    scores = None
    for m in METRICS:
        f = os.path.join(args.judge_results, m, "deepscholar_base.csv")
        d = pd.read_csv(f)[["folder_path", m]]
        d["row"] = d.folder_path.map(lambda p: int(os.path.basename(os.path.normpath(p))))
        scores = d[["row", m]] if scores is None else scores.merge(d[["row", m]], on="row")
    rows = []
    for _, s in scores.iterrows():
        aid = order[int(s.row)]
        g, A = load_graph(f"{args.graphs}/{aid}.json")
        z = np.load(f"{args.emb_dir}/{aid}.npz")
        r = relevance(z["query"], z["nodes"])
        zf = np.load(f"{args.operators}/{aid}_full.npz")
        by_ax = {nd["arxiv_id"]: k for k, nd in enumerate(g["nodes"]) if nd.get("arxiv_id")}
        cited = pd.read_csv(os.path.join(args.judge_inputs, str(int(s.row)), "paper.csv"), dtype=str)
        S_cited = sorted({by_ax[a] for a in cited.id.map(arxiv_core) if a in by_ax})
        kdir = glob.glob(f"{args.outputs}/*_{aid}v*/")[0]
        kept = pd.read_csv(kdir + "kept.csv", dtype=str).arxiv_id.map(arxiv_core)
        S_kept = sorted({by_ax[a] for a in kept if a in by_ax})
        row = {"arxiv_id": aid, **{m: s[m] for m in METRICS}, "n_cited": len(S_cited), "n_kept": len(S_kept),
               "d_ev_cited": set_d_ev(zf["d8_V"], zf["d8_p"], r, S_cited) if S_cited else np.nan,
               "d_ev_kept": set_d_ev(zf["d8_V"], zf["d8_p"], r, S_kept) if S_kept else np.nan}
        rows.append(row)
    df = pd.DataFrame(rows)
    os.makedirs(args.out, exist_ok=True)
    df.to_csv(os.path.join(args.out, "per_query.csv"), index=False)
    out = []
    for which in ("cited", "kept"):
        d = df.dropna(subset=[f"d_ev_{which}"])
        for m in METRICS:
            rho_d, p_d = spearmanr(d[f"d_ev_{which}"], d[m])
            rho_n, p_n = spearmanr(d[f"n_{which}"], d[m])
            rho_part, p_part = partial_spearman(d[f"d_ev_{which}"].values, d[m].values, d[f"n_{which}"].values)
            out.append({"set": which, "metric": m, "queries": len(d), "rho_d_ev": rho_d, "p_d_ev": p_d,
                        "rho_size": rho_n, "p_size": p_n, "rho_d_ev_given_size": rho_part, "p_partial": p_part})
    pd.DataFrame(out).to_csv(os.path.join(args.out, "gate.csv"), index=False)
    print(pd.DataFrame(out).round(3).to_string(index=False))


if __name__ == "__main__":
    main()
