#!/usr/bin/env python3
"""
compare_judges.py - our GPT judge vs Efty's Llama judge on the same reports, with paired tests.

Reads our per-query scores (run_judge.py's per_query.csv) and her raw Llama outputs
(d-spectra/judge/results/writer_s<seed>/<system>/<metric>/deepscholar_base.csv), then prints per system:
mean under each judge, the difference from the baseline system with a paired Wilcoxon test (Holm-corrected
over the other systems), and the per-query Spearman agreement between the two judges.

Usage (from project/):
  python compare_judges.py --ours eval_results/rejudge_s0/per_query.csv \
      --theirs d-spectra/judge/results/writer_s0 --metric nugget_coverage --heldout
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

import pandas as pd
from scipy.stats import spearmanr, wilcoxon


def holm(ps: dict) -> dict:
    items = sorted(ps.items(), key=lambda kv: kv[1])
    m, out, running = len(items), {}, 0.0
    for i, (k, p) in enumerate(items):
        running = max(running, min(1.0, (m - i) * p))
        out[k] = running
    return out


def load_theirs(root: Path, metric: str) -> pd.DataFrame:
    rows = []
    for sysdir in sorted(p for p in root.iterdir() if p.is_dir()):
        f = sysdir / metric / "deepscholar_base.csv"
        if not f.exists():
            continue
        d = pd.read_csv(f)
        for _, r in d.iterrows():
            row = os.path.basename(str(r["folder_path"]).rstrip("/"))
            if row.isdigit():
                rows.append({"system": sysdir.name, "row": int(row), "theirs": r[metric]})
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ours", required=True)
    ap.add_argument("--theirs", required=True)
    ap.add_argument("--metric", default="nugget_coverage")
    ap.add_argument("--baseline", default="dsbase_rerun")
    ap.add_argument("--heldout", action="store_true")
    ap.add_argument("--design-upto", type=int, default=20)
    args = ap.parse_args()

    ours = pd.read_csv(args.ours)[["system", "row", args.metric]].rename(columns={args.metric: "ours"})
    theirs = load_theirs(Path(args.theirs), args.metric)
    df = ours.merge(theirs, on=["system", "row"], how="left")
    if args.heldout:
        df = df[df["row"] >= args.design_upto]

    for judge in ("ours", "theirs"):
        wide = df.pivot_table(index="row", columns="system", values=judge)
        if args.baseline not in wide:
            continue
        ps, diffs = {}, {}
        for s in wide.columns:
            if s == args.baseline:
                continue
            pair = wide[[s, args.baseline]].dropna()
            d = pair[s] - pair[args.baseline]
            diffs[s] = (d.mean(), int((d > 0).sum()), int((d < 0).sum()), len(d))
            ps[s] = wilcoxon(d).pvalue if (d != 0).any() else 1.0
        hp = holm(ps)
        label = "GPT judge (ours)" if judge == "ours" else "Llama judge (Efty)"
        print(f"\n== {args.metric}, {label}: difference from {args.baseline}")
        print(f"   {args.baseline:16s} mean {wide[args.baseline].mean():.3f}")
        for s in sorted(diffs, key=lambda k: -diffs[k][0]):
            m, w, l, n = diffs[s]
            print(f"   {s:16s} mean {wide[s].mean():.3f} | diff {m:+.3f} ({w}/{l}, n={n}) | "
                  f"p {ps[s]:.3f} | Holm p {hp[s]:.3f}")

    print(f"\n== per-query agreement between judges (Spearman), {args.metric}")
    for s, g in df.dropna().groupby("system"):
        rho = spearmanr(g["ours"], g["theirs"]).correlation if len(g) > 2 else float("nan")
        print(f"   {s:16s} rho {rho:+.2f} (n={len(g)})")
    sys_means = df.dropna().groupby("system")[["ours", "theirs"]].mean()
    print(f"   system-level ranking agreement: rho {spearmanr(sys_means['ours'], sys_means['theirs']).correlation:+.2f} "
          f"over {len(sys_means)} systems")


if __name__ == "__main__":
    main()
