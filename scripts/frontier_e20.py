"""
E20: the capacity frontier of frontier_e19.py redrawn with three rank caps (32, 64, 128):
mean held-out AUC against mean realized dimension along the cv fits' eta grid, one curve
per cap (SPECTRA's Figure 2 with r varied). Descriptive (rules: scratchpad/e19_e20_rules.md).
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

SURFACE, TEXT, TEXT2, MUTED = "#fcfcfb", "#0b0b0b", "#52514e", "#b9b8b1"
SERIES = {32: "#2a78d6", 64: "#d9822b", 128: "#3f9c6b"}  # three fixed categorical hues
STYLE = {32: "-", 64: (0, (4, 2)), 128: (0, (1, 1.5))}


def curves(folder):
    D, A = [], []
    for f in sorted(glob.glob(os.path.join(folder, "*.json"))):
        pts = sorted(json.load(open(f))["dspectra_cv"]["heldout"], key=lambda p: p["eta"])
        D.append([p["d_ev"] for p in pts]); A.append([p["auc"] for p in pts])
    return np.array(D), np.array(A), [p["eta"] for p in pts]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/e19_linkpred/frontier_caps.png")
    args = ap.parse_args()
    folders = {32: "results/e8_small/operators", 64: "results/e20_r64/operators", 128: "results/e20_r128/operators"}
    fig, ax = plt.subplots(figsize=(6.4, 4.0), dpi=160, facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    for r, folder in folders.items():
        D, A, etas = curves(folder)
        ax.plot(D.mean(0), A.mean(0), color=SERIES[r], lw=2.0, ls=STYLE[r], marker="o", ms=4.5, markerfacecolor=SURFACE,
                markeredgewidth=1.5, label=f"rank cap {r}", zorder=3)
        ax.annotate(f"cap {r}", (D.mean(0)[-1], A.mean(0)[-1]), xytext=(6, 0), textcoords="offset points", fontsize=8, color=TEXT2, va="center")
        print(f"cap {r}: d_ev {D.mean(0).round(1).tolist()} AUC {A.mean(0).round(4).tolist()}")
    ax.set_xlabel("realized dimension d_ev (mean over the 63 graphs)", color=TEXT2, fontsize=9)
    ax.set_ylabel("held-out citation AUC (mean)", color=TEXT2, fontsize=9)
    ax.set_title("Capacity frontiers at three rank caps (cv fits, same eta grid)", color=TEXT, fontsize=10, loc="left")
    ax.legend(frameon=False, fontsize=8, loc="lower left", labelcolor=TEXT2)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(MUTED)
    ax.tick_params(colors=TEXT2, labelsize=8)
    ax.grid(axis="y", color=MUTED, lw=0.5, alpha=0.5)
    fig.tight_layout()
    fig.savefig(args.out, facecolor=SURFACE)


if __name__ == "__main__":
    main()
