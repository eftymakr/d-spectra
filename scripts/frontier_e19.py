"""
E19b: per-query capacity frontiers (SPECTRA's Figure 2 on our graphs): held-out
AUC against realized dimension d_ev along the eta grid of the cv fits, rank cap
32. One thin line per query, the mean curve in bold. Descriptive only (rules:
scratchpad/e19_e20_rules.md).
"""
from __future__ import annotations

import argparse
import glob
import json
import os

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SURFACE, TEXT, TEXT2, MUTED, SERIES1 = "#fcfcfb", "#0b0b0b", "#52514e", "#b9b8b1", "#2a78d6"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--operators", default="results/e8_small/operators")
    ap.add_argument("--out", default="results/e19_linkpred/frontier_r32.png")
    args = ap.parse_args()
    curves = []
    for f in sorted(glob.glob(os.path.join(args.operators, "*.json"))):
        pts = sorted(json.load(open(f))["dspectra_cv"]["heldout"], key=lambda p: p["eta"])
        curves.append((np.array([p["d_ev"] for p in pts]), np.array([p["auc"] for p in pts]),
                       np.array([p["eta"] for p in pts])))
    etas = curves[0][2]
    D = np.array([c[0] for c in curves]); A = np.array([c[1] for c in curves])
    fig, ax = plt.subplots(figsize=(6.4, 4.0), dpi=160, facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    for d, a, _ in curves:
        ax.plot(d, a, color=MUTED, lw=0.8, alpha=0.6, zorder=1)
    ax.plot(D.mean(0), A.mean(0), color=SERIES1, lw=2.2, zorder=3, marker="o", ms=4.5,
            markerfacecolor=SURFACE, markeredgewidth=1.6)
    for k in (0, len(etas) // 2, len(etas) - 1):
        ax.annotate(f"η = {etas[k]:g}", (D.mean(0)[k], A.mean(0)[k]), xytext=(0, 9), textcoords="offset points",
                    ha="center", fontsize=8, color=TEXT2)
    ax.set_xlabel("realized dimension d_ev (effective rank of the fitted kernel)", color=TEXT2, fontsize=9)
    ax.set_ylabel("held-out citation AUC", color=TEXT2, fontsize=9)
    ax.set_title(f"Capacity frontiers of the {len(curves)} per-query citation graphs (rank cap 32)",
                 color=TEXT, fontsize=10, loc="left")
    ax.axvline(32, color=MUTED, lw=0.8, ls=(0, (3, 3)), zorder=0)
    ax.text(32, ax.get_ylim()[0] + 0.002, " rank cap", color=TEXT2, fontsize=8, va="bottom")
    ax.text(D.mean(0)[0], A.mean(0)[0] - 0.008, "mean over queries", color=SERIES1, fontsize=8, ha="left", va="top")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(MUTED)
    ax.tick_params(colors=TEXT2, labelsize=8)
    ax.grid(axis="y", color=MUTED, lw=0.5, alpha=0.5)
    fig.tight_layout()
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    fig.savefig(args.out, facecolor=SURFACE)
    print(f"{args.out}: etas {etas.tolist()}")
    print("mean d_ev:", D.mean(0).round(1).tolist())
    print("mean AUC :", A.mean(0).round(4).tolist())
    print("AUC range across the grid, per query, median:", np.median(A.max(1) - A.min(1)).round(4))
    np.savetxt(args.out.replace(".png", ".csv"),
               np.column_stack([etas, D.mean(0), A.mean(0), A.std(0)]), delimiter=",",
               header="eta,mean_d_ev,mean_auc,sd_auc", comments="")


if __name__ == "__main__":
    main()
