"""
Is the pilot's epoch budget enough? For a few query graphs, fit directed
SPECTRA at eta = 0 and at the eta found by bisection (target d_ev 8) for
6,000 epochs (SPECTRA's default) and record NLL and d_ev every 100
epochs. Reports how much each still moves after --check epochs.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from dspectra.model import FitConfig, fit, fit_to_target  # noqa: E402
from pilot_selection import load_graph  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graphs", default="data/graphs_v2")
    ap.add_argument("--n_queries", type=int, default=3)
    ap.add_argument("--check", type=int, default=1500)
    ap.add_argument("--long", type=int, default=6000)
    ap.add_argument("--target", type=float, default=8.0)
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--out", default="results/convergence")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    files = sorted(glob.glob(f"{args.graphs}/*.json"))[:args.n_queries]
    rows = []
    for path in files:
        g, A = load_graph(path)
        short = FitConfig(rank=32, epochs=args.check, device=args.device)
        eta_star = fit_to_target(A, args.target, "directed", short).eta
        for eta in (0.0, eta_star):
            trace = []
            fit(A, "directed", eta, FitConfig(rank=32, epochs=args.long, device=args.device),
                trace=trace)
            at = {t["epoch"]: t for t in trace}
            c, e = at[args.check], at[args.long]
            rows.append({"arxiv_id": g["arxiv_id"], "eta": eta,
                         f"d_ev@{args.check}": c["d_ev"], f"d_ev@{args.long}": e["d_ev"],
                         f"nll@{args.check}": c["nll"], f"nll@{args.long}": e["nll"],
                         "d_ev_rel_change": (e["d_ev"] - c["d_ev"]) / c["d_ev"],
                         "nll_rel_change": (e["nll"] - c["nll"]) / c["nll"],
                         "trace": trace})
            print({k: (round(v, 4) if isinstance(v, float) else v)
                   for k, v in rows[-1].items() if k != "trace"}, flush=True)
    with open(f"{args.out}/convergence.json", "w") as f:
        json.dump(rows, f)


if __name__ == "__main__":
    main()
