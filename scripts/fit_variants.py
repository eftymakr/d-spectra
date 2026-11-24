"""
Fits for the method variants (E8, E9). For each query, the fits named in --fits:

  d8     dspectra         d_ev targeted to --target, as in pilot_selection.py --fit
  es8    dspectra_es      the same with early-stopped probes and a full refit at
                          the chosen eta (SPECTRA's cheap-probe protocol)
  eta0   dspectra_eta0    eta = 0
  cv     dspectra_cv      eta chosen by held-out link prediction (our addition;
                          SPECTRA itself uses eta = 0 or fixed d_ev targets): the
                          peak of held-out AUC over --etas, fitted without 10%
                          of the citations and as many non-citations, refitted
                          on the whole graph
  cvap   dspectra_cvap    the same, choosing by held-out average precision
  cvnll  dspectra_cvnll   the same, choosing by the lowest held-out NLL
  tmin   dspectra_tmin    SPECTRA's capacity targets (E14): d_ev targeted to the
  tmed   dspectra_tmed    minimum / median effective rank of the graph baselines
                          (USVT and raw SVD at the rank cap), measured like our
                          d_ev (occupancy proportional to the singular values)

The usual operators go to <out>/operators/<aid>.npz/.json, so
pilot_selection.py --evaluate runs unchanged, and every fitted quantity
(U, V, sigma, p, a, b, beta) of each fit to <aid>_full.npz, keyed by the
short name (d8_*, cv_*, ...), for the query-link and pool-anchored variants.
Queries are split over workers as in fit_worker.py.
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
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from pilot_selection import load_graph, svd_modes, usvt_threshold  # noqa: E402

ETAS = [-0.10, -0.06, -0.03, 0.0, 0.02, 0.04, 0.06]
FITS = {"d8": "dspectra", "es8": "dspectra_es", "eta0": "dspectra_eta0", "cv": "dspectra_cv",
        "cvap": "dspectra_cvap", "cvnll": "dspectra_cvnll", "tmin": "dspectra_tmin",
        "tmed": "dspectra_tmed"}


def baseline_ranks(A, rank):
    """Effective ranks exp(H(p)), p = s / sum(s), of USVT and of raw SVD at `rank`."""
    out = []
    for thr in (usvt_threshold(A), None):
        p = svd_modes(A, rank, paper_axis=1, threshold=thr)[1]
        out.append(float(np.exp(-(p * np.log(p)).sum())))
    return out
CRITERION = {"cv": "auc", "cvap": "ap", "cvnll": "nll"}


def fit_variants(path, args):
    from dspectra.model import (CRITERIA, FitConfig, diagnostics, fit, fit_to_target, modes,
                                parameters, select_eta_heldout)
    g, A = load_graph(path)
    if args.edge_keep < 1.0:
        # sparsification check (scratchpad/sparse_rules.md): keep a random fraction of the
        # citations, all nodes; the cv split is then made on the remaining citations
        ii, jj = np.nonzero(A)
        rng = np.random.default_rng(args.edge_seed)
        drop = rng.random(len(ii)) >= args.edge_keep
        A[ii[drop], jj[drop]] = 0.0
    cfg = FitConfig(rank=args.rank, epochs=args.epochs, device=args.device,
                    lr_schedule=args.lr_schedule, beta_max=args.beta_max)
    arrays, full, info = {}, {}, {}
    t0 = time.time()
    at_eta = {}  # full-graph fits at a fixed eta, shared between fit names

    def fixed(eta):
        if eta not in at_eta:
            trace = []
            m = fit(A, "directed", eta, cfg, seed=args.seed, trace=trace)
            last = [t["d_ev"] for t in trace if t["epoch"] > args.epochs - 1000]
            # convergence: d_ev drift over the last 1,000 epochs, and whether
            # the loss ends above its minimum (the E2 instability)
            m.convergence = {"d_ev_drift_last1000": (max(last) - min(last)) / last[-1],
                             "nll_end_minus_min": trace[-1]["nll"] - min(t["nll"] for t in trace)}
            at_eta[eta] = m
        return at_eta[eta]

    def keep(short, model, extra):
        name = FITS[short]
        md = modes(model)
        arrays[f"{name}_V"], arrays[f"{name}_p"] = md["V"], md["p"]
        full.update({f"{short}_{k}": v for k, v in parameters(model).items()})
        info[name] = dict(extra, d_ev=diagnostics(model)["d_ev"], beta=float(model.beta()),
                          train_nll=model.final_nll,
                          **getattr(model, "convergence", {}))

    for short, early in (("d8", False), ("es8", True)):
        if short in args.fits:
            t = time.time()
            res = fit_to_target(A, args.target, "directed", cfg, seed=args.seed,
                                probe_early_stop=early)
            keep(short, res.model, {"eta": res.eta, "probes": len(res.probes),
                                    "probe_epochs": sum(p["epochs"] for p in res.probes),
                                    "seconds": time.time() - t})
    if "eta0" in args.fits:
        keep("eta0", fixed(0.0), {"eta": 0.0})
    for short in [s for s in ("tmin", "tmed") if s in args.fits]:
        ranks = baseline_ranks(A, args.rank)
        target = min(ranks) if short == "tmin" else float(np.median(ranks))
        t = time.time()
        res = fit_to_target(A, target, "directed", cfg, seed=args.seed)
        keep(short, res.model, {"eta": res.eta, "target": target, "baseline_ranks": ranks,
                                "probes": len(res.probes), "seconds": time.time() - t})
    crit = [c for c in CRITERION if c in args.fits]
    if crit:
        _, points = select_eta_heldout(A, args.etas, cfg, seed=args.seed)
        for short in crit:
            key = CRITERION[short]
            eta = CRITERIA[key](points, key=lambda p: p[key])["eta"]
            keep(short, fixed(eta), {"eta": eta, "criterion": key, "heldout": points})
    info["_seconds"] = time.time() - t0
    info["_config"] = {"rank": args.rank, "epochs": args.epochs, "target": args.target,
                       "seed": args.seed, "etas": args.etas, "fits": args.fits,
                       "lr_schedule": args.lr_schedule, "beta_max": args.beta_max,
                       "edge_keep": args.edge_keep, "edge_seed": args.edge_seed, "n_edges_fit": int(A.sum())}
    return arrays, full, info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pools", required=True, help="pool folders defining the query list")
    ap.add_argument("--only", default=None, help="pool folders of a query subset (e.g. design)")
    ap.add_argument("--graphs", required=True)
    ap.add_argument("--worker", required=True, help="k/N")
    ap.add_argument("--out", required=True)
    ap.add_argument("--rank", type=int, default=32)
    ap.add_argument("--epochs", type=int, default=6000)
    ap.add_argument("--target", type=float, default=8.0)
    ap.add_argument("--etas", type=float, nargs="+", default=ETAS)
    ap.add_argument("--fits", nargs="+", choices=sorted(FITS), default=["d8", "eta0", "cv"])
    ap.add_argument("--lr_schedule", choices=["constant", "cosine"], default="constant")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--beta_max", type=float, default=5.0, help="bound on beta (SPECTRA's default 5)")
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--timeout_hours", type=float, default=12.0)
    ap.add_argument("--edge_keep", type=float, default=1.0, help="keep this fraction of the citations (sparsification check)")
    ap.add_argument("--edge_seed", type=int, default=0)
    args = ap.parse_args()

    def ids_of(pools):
        return sorted(re.search(r"(\d{4}\.\d{4,5})", os.path.basename(os.path.normpath(d))).group(1)
                      for d in glob.glob(os.path.join(pools, "*/")))
    ids = ids_of(args.pools)
    if args.only:
        subset = set(ids_of(args.only))
        ids = [a for a in ids if a in subset]
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
            arrays, full, info = fit_variants(path, args)
            np.savez(out + ".npz", **arrays)
            np.savez(out + "_full.npz", **full)
            with open(out + ".json", "w") as f:
                json.dump(info, f)
            todo.remove(aid)
            fits = "  ".join(f"{k}: eta={v['eta']:+.3f} d_ev={v['d_ev']:.2f}"
                             for k, v in info.items() if not k.startswith("_"))
            print(f"{aid} fitted in {info['_seconds']:.0f}s  {fits}", flush=True)
        if todo:
            time.sleep(30)
    print(f"worker {args.worker} finished; {len(todo)} left", flush=True)


if __name__ == "__main__":
    main()
