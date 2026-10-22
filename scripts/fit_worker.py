"""
Fit worker that can run while graphs are still being built.

Queries are assigned to workers from a fixed list (the pool folders), so
running N workers fits every query exactly once. Each worker waits for
its graphs to appear, fits them with pilot_selection.fit_query, and saves
the operators in the same format as `pilot_selection.py --fit`.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pilot_selection import fit_query  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pools", required=True, help="pool folders defining the query list")
    ap.add_argument("--graphs", required=True)
    ap.add_argument("--worker", required=True, help="k/N")
    ap.add_argument("--out", required=True)
    ap.add_argument("--rank", type=int, default=32)
    ap.add_argument("--epochs", type=int, default=6000)
    ap.add_argument("--target", type=float, default=8.0)
    ap.add_argument("--sensitivity", type=float, nargs="*", default=[])
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--timeout_hours", type=float, default=6.0)
    args = ap.parse_args()

    ids = sorted(re.search(r"(\d{4}\.\d{4,5})", os.path.basename(os.path.normpath(d))).group(1)
                 for d in glob.glob(os.path.join(args.pools, "*/")))
    k, N = map(int, args.worker.split("/"))
    todo = ids[k::N]
    os.makedirs(f"{args.out}/operators", exist_ok=True)
    deadline = time.time() + args.timeout_hours * 3600
    while todo and time.time() < deadline:
        for aid in list(todo):
            out = f"{args.out}/operators/{aid}"
            path = f"{args.graphs}/{aid}.json"
            if os.path.isfile(out + ".json"):
                todo.remove(aid)
                continue
            if not os.path.isfile(path) or time.time() - os.path.getmtime(path) < 5:
                continue
            try:
                with open(path) as f:
                    json.load(f)
            except ValueError:
                continue  # still being written
            arrays, info = fit_query(path, args)
            np.savez(out + ".npz", **arrays)
            with open(out + ".json", "w") as f:
                json.dump(info, f)
            todo.remove(aid)
            print(f"{aid} fitted in {info['_seconds']:.0f}s  d_ev={info['dspectra']['d_ev']:.2f}",
                  flush=True)
        if todo:
            time.sleep(30)
    print(f"worker {args.worker} finished; {len(todo)} left", flush=True)


if __name__ == "__main__":
    main()
