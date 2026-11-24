"""
E19a: the directed SPECTRA fit as a citation predictor, SPECTRA's own evaluation
(held-out link prediction) on the per-query citation graphs, against structural
baselines with no fitted parameters.

Split: the cv fits' split, heldout_split(A, 0.1, seed 0). The fit's AUC/AP at
eta = 0 come from the cv fit's recorded held-out points (a model fitted without
the held-out pairs); the baselines score on A with the held-out citations
removed. Rules: scratchpad/e19_e20_rules.md.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon
from sklearn.metrics import average_precision_score, roc_auc_score

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from dspectra.model import heldout_split  # noqa: E402
from pilot_selection import load_graph, usvt_threshold  # noqa: E402
from seed_tests import holm  # noqa: E402

BASELINES = ["svd32", "usvt", "pref_attach", "in_degree", "bib_coupling"]


def baseline_scores(A_tr, rank):
    U, s, Vt = np.linalg.svd(A_tr, full_matrices=False)
    k = max(1, int((s > usvt_threshold(A_tr)).sum()))
    outd, ind = A_tr.sum(1), A_tr.sum(0)
    return {"svd32": (U[:, :rank] * s[:rank]) @ Vt[:rank],
            "usvt": (U[:, :k] * s[:k]) @ Vt[:k],
            "pref_attach": np.outer(outd, ind),
            "in_degree": np.tile(ind, (len(ind), 1)),
            "bib_coupling": A_tr @ A_tr.T @ A_tr}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graphs", default="data/graphs_small")
    ap.add_argument("--operators", default="results/e8_small/operators")
    ap.add_argument("--rank", type=int, default=32)
    ap.add_argument("--out", default="results/e19_linkpred")
    args = ap.parse_args()
    rows = []
    for path in sorted(glob.glob(os.path.join(args.graphs, "*.json"))):
        aid = os.path.basename(path)[:-5]
        jpath = os.path.join(args.operators, f"{aid}.json")
        if not os.path.isfile(jpath):
            continue
        pts = json.load(open(jpath))["dspectra_cv"]["heldout"]
        at0 = [p for p in pts if p["eta"] == 0.0][0]
        g, A = load_graph(path)
        A = (np.asarray(A) > 0).astype(float)
        pos, neg = heldout_split(A, 0.1, 0)
        A_tr = A.copy()
        A_tr[pos[:, 0], pos[:, 1]] = 0.0
        y = np.concatenate([np.ones(len(pos)), np.zeros(len(neg))])
        row = {"arxiv_id": aid, "n": A.shape[0], "n_heldout": len(pos),
               "spectra_auc": at0["auc"], "spectra_ap": at0["ap"],
               "spectra_auc_min_eta": min(p["auc"] for p in pts), "spectra_auc_max_eta": max(p["auc"] for p in pts)}
        for name, S in baseline_scores(A_tr, args.rank).items():
            sc = np.concatenate([S[pos[:, 0], pos[:, 1]], S[neg[:, 0], neg[:, 1]]])
            row[f"{name}_auc"] = roc_auc_score(y, sc)
            row[f"{name}_ap"] = average_precision_score(y, sc)
        rows.append(row)
    df = pd.DataFrame(rows)
    os.makedirs(args.out, exist_ok=True)
    df.to_csv(os.path.join(args.out, "per_graph.csv"), index=False)
    tests = []
    for metric in ("auc", "ap"):
        t = []
        for b in BASELINES:
            d = df[f"spectra_{metric}"] - df[f"{b}_{metric}"]
            t.append({"metric": metric, "baseline": b, "spectra": df[f"spectra_{metric}"].mean(),
                      "baseline_mean": df[f"{b}_{metric}"].mean(), "diff": d.mean(),
                      "w/l": f"{(d > 0).sum()}/{(d < 0).sum()}",
                      "p": wilcoxon(d).pvalue if (d != 0).any() else 1.0, "n": len(d)})
        t = pd.DataFrame(t)
        t["holm"] = holm(t.p)
        tests.append(t)
    tests = pd.concat(tests)
    tests.to_csv(os.path.join(args.out, "tests.csv"), index=False)
    pd.set_option("display.width", 200)
    print(f"{len(df)} graphs, held-out citations per graph median {df.n_heldout.median():.0f}")
    print(f"SPECTRA fit AUC over the eta grid: min {df.spectra_auc_min_eta.mean():.4f} max {df.spectra_auc_max_eta.mean():.4f}")
    print(tests.round(4).to_string(index=False))


if __name__ == "__main__":
    main()
