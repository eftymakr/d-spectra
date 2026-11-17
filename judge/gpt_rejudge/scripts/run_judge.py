#!/usr/bin/env python3
"""
run_judge.py - judge many systems with DeepScholar-Bench's evaluation code, the paper's judges, resumably.

For each system (a folder in the evaluator's layout: <row>/intro.md + paper list) it runs
  pass 1: nugget_coverage                              with --nugget-model (default gpt-4.1, as the paper)
  pass 2: reference_coverage cite_p claim_coverage     with --model        (default gpt-4o, as the paper)
into <out>/<system>/{nugget,other}/. A pass whose results.csv already exists is skipped (no double cost).
Then it collects every per-query score into <out>/per_query.csv and prints means by split
(design = rows < --design-upto, held-out = the rest).

Run from project/ with the key loaded:  set -a; source deepscholar/.env; set +a
  python run_judge.py --system dsbase_qwen=eval_inputs/dsbase_s0 --system dsbase_mini=eval_inputs/writer_gpt41mini/dsbase_s0 \
      --file-id 0 1 2 3 4 --out eval_results/judge_test
  # all held-out queries of every system folder under one directory:
  python run_judge.py --systems-dir eval_inputs/efty_s0 --heldout --out eval_results/rejudge_s0
Options: --dry-run prints the commands; --deepscholar-dir points at the (possibly patched) eval code.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import pandas as pd


def parse_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--system", action="append", default=[], help="name=DIR (DIR/<row>/intro.md)")
    p.add_argument("--systems-dir", default=None, help="every subfolder is one system, named by the folder")
    p.add_argument("--out", required=True)
    p.add_argument("--file-id", type=int, nargs="*", default=None)
    p.add_argument("--heldout", action="store_true", help="only rows >= --design-upto")
    p.add_argument("--design-upto", type=int, default=20)
    p.add_argument("--nugget-model", default="gpt-4.1")
    p.add_argument("--model", default="gpt-4o")
    p.add_argument("--other-evals", nargs="*", default=["reference_coverage", "cite_p", "claim_coverage"])
    p.add_argument("--mode", default="deepscholar_base", help="evaluator parser to use")
    p.add_argument("--deepscholar-dir", default="deepscholar")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def rows_for(sys_dir: Path, args) -> list[int]:
    rows = sorted(int(p.name) for p in sys_dir.iterdir() if p.is_dir() and p.name.isdigit()
                  and (p / "intro.md").exists())
    if args.file_id is not None:
        rows = [r for r in rows if r in args.file_id]
    if args.heldout:
        rows = [r for r in rows if r >= args.design_upto]
    return rows


def run_pass(name, sys_dir, rows, evals, model, out_dir, args):
    if (out_dir / "results.csv").exists():
        print(f"  [skip] {name}: {'/'.join(evals)} already judged")
        return
    cmd = [sys.executable, "-m", "eval.main", "--modes", args.mode, "--evals", *evals,
           "--input-folder", str(sys_dir.resolve()), "--file-id", *map(str, rows),
           "--model-name", model, "--output-folder", str(out_dir.resolve())]
    print(f"  [run ] {name}: {'/'.join(evals)} with {model} on {len(rows)} queries")
    if args.dry_run:
        print("        " + " ".join(cmd))
        return
    log = out_dir.with_suffix(".log")
    out_dir.parent.mkdir(parents=True, exist_ok=True)
    with open(log, "w") as f:
        r = subprocess.run(cmd, cwd=args.deepscholar_dir, stdout=f, stderr=subprocess.STDOUT)
    if r.returncode != 0 or not (out_dir / "results.csv").exists():
        print(f"  [FAIL] {name}: see {log}")
        return
    # The eval code scores a query 0 when its judge calls fail after retries (e.g. rate limits)
    # instead of stopping, so count those failures and flag them.
    text = log.read_text(errors="replace")
    fails = sum(1 for line in text.splitlines()
                if "Failed to assign nuggets" in line or "Failed to create nuggets" in line
                or "Reached max of" in line)
    if fails:
        print(f"  [WARN] {name}: {fails} failed judge calls in {log} -> those queries scored 0. "
              f"Delete {out_dir} and {log} and rerun to redo this pass.")


def collect(out_root: Path, systems: dict) -> pd.DataFrame:
    rows = []
    for name in systems:
        for part in ("nugget", "other"):
            for f in (out_root / name / part).glob("*/*.csv"):
                df = pd.read_csv(f)
                if "folder_path" not in df.columns:
                    continue
                metric = [c for c in df.columns if c != "folder_path"]
                for _, r in df.iterrows():
                    row_id = Path(str(r["folder_path"])).name
                    for m in metric:
                        rows.append({"system": name, "row": int(row_id) if row_id.isdigit() else row_id,
                                     "metric": m, "value": r[m]})
    long = pd.DataFrame(rows)
    if long.empty:
        return long
    return long.pivot_table(index=["system", "row"], columns="metric", values="value").reset_index()


def main():
    args = parse_args()
    systems = dict(s.split("=", 1) for s in args.system)
    if args.systems_dir:
        for d in sorted(Path(args.systems_dir).iterdir()):
            if d.is_dir():
                systems.setdefault(d.name, str(d))
    if not systems:
        sys.exit("No systems given (--system name=DIR or --systems-dir)")
    out_root = Path(args.out)

    for name, d in systems.items():
        sys_dir = Path(d)
        rows = rows_for(sys_dir, args)
        if not rows:
            print(f"  [none] {name}: no matching queries in {sys_dir}")
            continue
        run_pass(name, sys_dir, rows, ["nugget_coverage"], args.nugget_model, out_root / name / "nugget", args)
        run_pass(name, sys_dir, rows, args.other_evals, args.model, out_root / name / "other", args)

    if args.dry_run:
        return
    wide = collect(out_root, systems)
    if wide.empty:
        print("No per-query results found.")
        return
    wide["split"] = wide["row"].map(lambda r: "design" if isinstance(r, int) and r < args.design_upto else "heldout")
    wide.to_csv(out_root / "per_query.csv", index=False)
    metrics = [c for c in wide.columns if c not in ("system", "row", "split")]
    for split, part in [("all", wide), *list(wide.groupby("split"))]:
        print(f"\n== {split}")
        print(part.groupby("system")[metrics].agg("mean").round(3).assign(
            n=part.groupby("system").size()).to_string())
    print(f"\nPer query: {out_root / 'per_query.csv'}")


if __name__ == "__main__":
    main()
