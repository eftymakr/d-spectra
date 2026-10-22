"""
Add extra d_ev targets (default 4 and 16) to already-fitted operators,
for a chosen subset of queries (e.g. the design queries), without
refitting the main operators. Workers split the subset like fit_worker.py.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dspectra.model import FitConfig, fit_to_target, modes  # noqa: E402
from pilot_selection import load_graph  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids_from", required=True, help="pool folders defining the query subset")
    ap.add_argument("--graphs", required=True)
    ap.add_argument("--operators", required=True)
    ap.add_argument("--worker", default="0/1", help="k/N")
    ap.add_argument("--targets", type=float, nargs="+", default=[4.0, 16.0])
    ap.add_argument("--rank", type=int, default=32)
    ap.add_argument("--epochs", type=int, default=6000)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--device", default="cuda")
    args = ap.parse_args()

    ids = sorted(re.search(r"(\d{4}\.\d{4,5})", os.path.basename(os.path.normpath(d))).group(1)
                 for d in glob.glob(os.path.join(args.ids_from, "*/")))
    k, N = map(int, args.worker.split("/"))
    cfg = FitConfig(rank=args.rank, epochs=args.epochs, device=args.device)
    for aid in ids[k::N]:
        base = f"{args.operators}/{aid}"
        if not os.path.isfile(base + ".json"):
            print(f"{aid}: no main fit yet, skipped", flush=True)
            continue
        with open(base + ".json") as f:
            info = json.load(f)
        todo = [t for t in args.targets if f"dspectra_d{t:g}" not in info]
        if not todo:
            continue
        arrays = dict(np.load(base + ".npz"))
        _, A = load_graph(f"{args.graphs}/{aid}.json")
        for t in todo:
            res = fit_to_target(A, t, "directed", cfg, seed=args.seed)
            md = modes(res.model)
            arrays[f"dspectra_d{t:g}_V"], arrays[f"dspectra_d{t:g}_p"] = md["V"], md["p"]
            info[f"dspectra_d{t:g}"] = {"eta": res.eta, "probes": len(res.probes), "d_ev": res.d_ev}
        np.savez(base + ".npz", **arrays)
        with open(base + ".json", "w") as f:
            json.dump(info, f)
        print(f"{aid}: added targets {todo}", flush=True)


if __name__ == "__main__":
    main()
