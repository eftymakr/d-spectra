"""
The final methods averaged over search seeds 0-2 (recall at the matched budget,
per query), with paired Wilcoxon tests and a Holm correction over every
comparison listed in COMPARISONS (the proposal asks for seed-averaged,
corrected tests). All queries count, with recall 0 where nothing is reachable.
"""
from __future__ import annotations

import argparse
import glob
import json
import os

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

BASE = {"deepscholar_kept": "DeepScholar-base's own picks", "search_only": "fixed-k",
        "relevance_only": "relevance only", "most_cited": "most-cited", "usvt": "USVT",
        "dspectra": "D-SPECTRA"}
EXTRA = {"qlinkrel10_eta0_l0.75": "query link + relevance", "cocite10_l0.75": "co-citation + relevance",
         "usvtlink5_l0.75": "USVT co-citation + relevance"}
COMPARISONS = [
    ("D-SPECTRA", "DeepScholar-base's own picks"), ("D-SPECTRA", "fixed-k"), ("D-SPECTRA", "relevance only"),
    ("D-SPECTRA", "USVT"), ("D-SPECTRA", "most-cited"),
    ("query link + relevance", "D-SPECTRA"), ("query link + relevance", "USVT"),
    ("query link + relevance", "relevance only"), ("query link + relevance", "co-citation + relevance"),
    ("co-citation + relevance", "D-SPECTRA"), ("co-citation + relevance", "USVT"),
    ("USVT co-citation + relevance", "D-SPECTRA"), ("USVT co-citation + relevance", "USVT"),
    ("USVT co-citation + relevance", "query link + relevance"),
    ("USVT co-citation + relevance", "co-citation + relevance"),
    ("USVT co-citation + relevance", "DeepScholar-base's own picks"),
]


def holm(p):
    p = np.asarray(p, dtype=float)
    order = np.argsort(p)
    adj = np.empty_like(p)
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, (len(p) - rank) * p[i])
        adj[i] = min(running, 1.0)
    return adj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs=3, required=True, help="pilot_selection results for seeds 0, 1, 2")
    ap.add_argument("--extra", nargs=3, required=True, help="E11 rows.csv for seeds 0, 1, 2")
    ap.add_argument("--design_pools", default="pools/qwen3-8b-awq_k50")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    dev = {os.path.basename(os.path.normpath(d)).split("_")[1][:10] for d in glob.glob(f"{args.design_pools}/*/")}
    frames = []
    for seed, (run, extra) in enumerate(zip(args.runs, args.extra)):
        rows = [r for f in glob.glob(f"{run}/per_query/*.json") for r in json.load(open(f))["rows"]]
        b = pd.DataFrame(rows)
        b = b[(b.B == 0) & b.method.isin(BASE)].assign(method=lambda d: d.method.map(BASE))
        e = pd.read_csv(extra, dtype={"arxiv_id": str})
        e = e[(e.B == 0) & e.method.isin(EXTRA)].assign(method=lambda d: d.method.map(EXTRA))
        frames.append(pd.concat([b[["arxiv_id", "method", "recall"]], e[["arxiv_id", "method", "recall"]]])
                      .assign(seed=seed))
    df = pd.concat(frames)
    wide = df.pivot_table(index=["arxiv_id", "method"], columns="seed", values="recall").dropna()
    mean = wide.mean(axis=1).unstack("method")
    mean["split"] = np.where(mean.index.isin(dev), "design", "held-out")

    methods = list(BASE.values()) + list(EXTRA.values())
    summary = {}
    for split in ["design", "held-out"]:
        m = mean[mean.split == split]
        per_seed = {s: wide[s].unstack("method").loc[m.index] for s in range(3)}
        for meth in methods:
            vals = [per_seed[s][meth].mean() for s in range(3)]
            summary.setdefault(meth, {})[f"{split} ({len(m)}): mean over seeds"] = f"{m[meth].mean():.3f}"
            summary[meth][f"{split}: per-seed range"] = f"{min(vals):.3f}–{max(vals):.3f}"
    ho = mean[mean.split == "held-out"]
    tests = []
    for a, b in COMPARISONS:
        d = ho[a] - ho[b]
        p = wilcoxon(ho[a], ho[b]).pvalue if (d != 0).any() else 1.0
        tests.append({"comparison": f"{a} vs {b}", "mean difference": d.mean(),
                      "wins/losses": f"{(d > 0).sum()}/{(d < 0).sum()}", "p": p})
    tests = pd.DataFrame(tests)
    tests["p (Holm, all 16)"] = holm(tests.p)
    os.makedirs(args.out, exist_ok=True)
    pd.DataFrame(summary).T.to_csv(f"{args.out}/means.csv")
    tests.to_csv(f"{args.out}/tests.csv", index=False)
    mean.to_csv(f"{args.out}/per_query_seed_mean.csv")
    print(pd.DataFrame(summary).T.to_string())
    print(tests.round(4).to_string(index=False))


if __name__ == "__main__":
    main()
