"""
Judged evaluation on search seeds 0, 1 and 2 (rules: scratchpad/seeds12_rules.md, an extension
of judged_rules.md). Reads the judge's per-report scores for each seed
(judge/results/writer_s<seed>/<system>/<metric>/deepscholar_base.csv), maps reports to queries
through the writer's stats.json, averages each query's score over the seeds that have it, and
writes

  results/judged_s12/rows.csv    one row per seed x system x query with every metric
  results/judged_s12/avg.csv     one row per system x query, seed-averaged
  results/judged_s12/tests.csv   paired Wilcoxon tests (families 1 and 2, secondary)
  <tables_out>                   markdown tables for the results document

Nothing is typed in by hand.
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
from tabulate import tabulate

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from judged_eval import LABEL, METRICS, MLABEL, PER_PAPER, SEARCH, FILTER, WRITER0, pv  # noqa: E402
from seed_tests import holm  # noqa: E402

SYSTEMS = ["dsbase_rerun", "fixed_k", "relevance_only", "dspectra", "cocite_rel", "usvt_cocite_rel", "qlink_rel", "oracle"]
JUDGE = "/home/eftychia/Spectra/judge"


def load_seed(seed, dev):
    out, missing = [], {}
    for sysname in SYSTEMS:
        stats = {int(os.path.basename(os.path.dirname(f))): json.load(open(f))
                 for f in glob.glob(f"{JUDGE}/writer/s{seed}/{sysname}/*/stats.json")}
        scores = None
        for m in METRICS:
            d = pd.read_csv(f"{JUDGE}/results/writer_s{seed}/{sysname}/{m}/deepscholar_base.csv")[["folder_path", m]]
            d["row"] = d.folder_path.map(lambda p: int(os.path.basename(os.path.normpath(p))))
            d = d[["row", m]]
            scores = d if scores is None else scores.merge(d, on="row", how="outer")
        for _, r in scores.iterrows():
            s = stats[int(r.row)]
            aid = s["query"].split("_", 1)[1][:10]
            n = s["n_papers"]
            tokens = SEARCH + (FILTER if sysname == "dsbase_rerun" else 0) + WRITER0 + PER_PAPER * n
            out.append({"seed": seed, "system": sysname, "row": int(r.row), "arxiv_id": aid,
                        "split": "design" if aid in dev else "held-out", "n_papers": n, "tokens": tokens, **{m: r[m] for m in METRICS}})
        got = {int(r.row) for _, r in scores.iterrows()}
        miss = sorted(set(range(63)) - got)
        if miss:
            missing[(seed, sysname)] = miss
    return pd.DataFrame(out), missing


def paired(avg, a, b, metric, split="held-out"):
    x = avg[(avg.system == a) & (avg.split == split)].set_index("arxiv_id")[metric]
    y = avg[(avg.system == b) & (avg.split == split)].set_index("arxiv_id")[metric]
    idx = x.index.intersection(y.index)
    x, y = x[idx], y[idx]
    diff = x - y
    p = 1.0 if (diff != 0).sum() == 0 else wilcoxon(x, y, zero_method="wilcox").pvalue
    return {"n": len(idx), "mean_a": x.mean(), "mean_b": y.mean(), "diff": diff.mean(), "wins": int((diff > 0).sum()),
            "losses": int((diff < 0).sum()), "p": p}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--design_pools", default="pools/qwen3-8b-awq_k50")
    ap.add_argument("--out", default="results/judged_s12")
    ap.add_argument("--tables_out", required=True)
    args = ap.parse_args()
    dev = {os.path.basename(os.path.normpath(d)).split("_")[1][:10] for d in glob.glob(f"{args.design_pools}/*/")}
    assert len(dev) == 20, len(dev)
    os.makedirs(args.out, exist_ok=True)
    parts, missing = [], {}
    for seed in (0, 1, 2):
        r, m = load_seed(seed, dev)
        parts.append(r); missing.update(m)
    rows = pd.concat(parts, ignore_index=True)
    rows.to_csv(f"{args.out}/rows.csv", index=False)
    avg = rows.groupby(["system", "arxiv_id", "split"], as_index=False).agg(
        n_seeds=("seed", "nunique"), n_papers=("n_papers", "mean"), tokens=("tokens", "mean"), **{m: (m, "mean") for m in METRICS})
    avg.to_csv(f"{args.out}/avg.csv", index=False)
    T = []

    def emit(title, df, note=None):
        T.append(f"\n#### {title}\n")
        T.append(tabulate(df, headers="keys", tablefmt="pipe", disable_numparse=True))
        if note:
            T.append(f"\n{note}")

    # ---- per-seed means, held-out, three metrics
    tab = {}
    for s in SYSTEMS:
        cell = {}
        for m in ("nugget_coverage", "reference_coverage", "coverage_relevance_rate"):
            for seed in (0, 1, 2):
                r = rows[(rows.system == s) & (rows.split == "held-out") & (rows.seed == seed)]
                cell[f"{MLABEL[m]}, s{seed}"] = f"{r[m].mean():.3f}" if m != "coverage_relevance_rate" else f"{r[m].mean():.2f}"
        tab[LABEL[s]] = cell
    note = "Held-out 43 queries per seed. " + "; ".join(f"seed {k[0]} {LABEL[k[1]]}: report{'s' if len(v) > 1 else ''} {v} not judged"
                                                       for k, v in missing.items())
    emit("Judged, seeds 0-2: per-seed means on the held-out queries (same writer and judge for every seed)", pd.DataFrame(tab).T, note)

    # ---- seed-averaged means, held-out and all
    for split, title in (("held-out", "held-out 43 queries"), (None, "all 63 queries")):
        tab = {}
        for s in SYSTEMS:
            r = avg[(avg.system == s) & ((avg.split == split) if split else True)]
            cell = {"queries": str(len(r)), "seeds / query": f"{r.n_seeds.mean():.2f}", "papers": f"{r.n_papers.mean():.1f}",
                    "tokens / query": f"{r.tokens.mean() / 1000:.0f}k"}
            for m in METRICS:
                if m in ("document_importance", "organization"):
                    continue
                cell[MLABEL[m]] = f"{r[m].mean():.3f}" if m != "coverage_relevance_rate" else f"{r[m].mean():.2f}"
            tab[LABEL[s]] = cell
        emit(f"Judged, seeds 0-2: seed-averaged scores, {title} (each query's score is its mean over the seeds that have it)",
             pd.DataFrame(tab).T,
             "Organization (0.5 on every report) and document importance (OpenAlex rate limit) are unusable and omitted; kept in rows.csv.")

    # ---- family 1
    tests, fam1 = [], []
    for s in SYSTEMS[1:]:
        t = paired(avg, s, "dsbase_rerun", "nugget_coverage")
        fam1.append({"family": "1: vs DeepScholar-base rerun, seed-averaged", "metric": "nugget_coverage", "a": s, "b": "dsbase_rerun", **t})
    for t, a in zip(fam1, holm([t["p"] for t in fam1])):
        t["p_holm"] = a
    tests += fam1
    tab = {LABEL[t["a"]]: {"n": str(t["n"]), "method": f"{t['mean_a']:.3f}", "DS-base rerun": f"{t['mean_b']:.3f}", "diff": f"{t['diff']:+.3f}",
                           "wins / losses": f"{t['wins']} / {t['losses']}", "p": pv(t["p"]), "Holm p (7)": pv(t["p_holm"])} for t in fam1}
    emit("Judged, seeds 0-2: each method vs DeepScholar-base's own picks on nugget coverage (seed-averaged, held-out 43, paired Wilcoxon, Holm over 7)",
         pd.DataFrame(tab).T)

    # ---- family 2
    fam2 = []
    for b in ("dspectra", "relevance_only"):
        t = paired(avg, "usvt_cocite_rel", b, "nugget_coverage")
        fam2.append({"family": "2: USVT co-citation vs, seed-averaged", "metric": "nugget_coverage", "a": "usvt_cocite_rel", "b": b, **t})
    for t, a in zip(fam2, holm([t["p"] for t in fam2])):
        t["p_holm"] = a
    tests += fam2
    tab = {LABEL[t["b"]]: {"n": str(t["n"]), "USVT co-citation + relevance": f"{t['mean_a']:.3f}", "other": f"{t['mean_b']:.3f}",
                           "diff": f"{t['diff']:+.3f}", "wins / losses": f"{t['wins']} / {t['losses']}", "p": pv(t["p"]),
                           "Holm p (2)": pv(t["p_holm"])} for t in fam2}
    emit("Judged, seeds 0-2: USVT co-citation + relevance vs D-SPECTRA and vs relevance only on nugget coverage (seed-averaged, held-out 43, Holm over 2)",
         pd.DataFrame(tab).T)

    # ---- secondary, uncorrected
    tab = {}
    for s in SYSTEMS[1:]:
        cell = {}
        for m in METRICS:
            if m in ("organization", "document_importance"):
                continue
            t = paired(avg, s, "dsbase_rerun", m)
            tests.append({"family": "secondary: vs rerun, seed-averaged (no claim)", "metric": m, "a": s, "b": "dsbase_rerun", **t, "p_holm": np.nan})
            cell[MLABEL[m]] = f"{t['diff']:+.3f} ({pv(t['p'])})"
        tab[LABEL[s]] = cell
    emit("Judged, seeds 0-2: the other metrics vs DeepScholar-base's own picks (seed-averaged, held-out 43; difference and uncorrected p, no claim)",
         pd.DataFrame(tab).T)
    pd.DataFrame(tests).to_csv(f"{args.out}/tests.csv", index=False)
    open(args.tables_out, "w").write("\n".join(T) + "\n")
    print("\n".join(T))
    print("missing:", missing)


if __name__ == "__main__":
    main()
