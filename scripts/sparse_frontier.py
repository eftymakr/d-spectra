"""
Sparsification frontier (rules: scratchpad/sparse_rules.md). Per graph and keep level, from the
cv fits' held-out points: gain = best AUC on the eta grid - AUC at eta = 0; low = AUC at the
most negative eta - AUC at eta = 0; d_ev at eta = 0 and at the best eta. Paired Wilcoxon of
gain(keep) and low(keep) against keep = 1.0, Holm over the three levels. One figure, four
mean frontiers.

  python scripts/sparse_frontier.py
Writes results/sparse/{stats.csv,tests.csv,summary.md,frontier_sparse.png}.
"""
from __future__ import annotations

import glob
import json
import os

import matplotlib
import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SURFACE, TEXT, TEXT2, MUTED = "#fcfcfb", "#0b0b0b", "#52514e", "#b9b8b1"
LEVELS = {1.0: "results/e8_small/operators", 0.5: "results/sparse_k50/operators",
          0.25: "results/sparse_k25/operators", 0.1: "results/sparse_k10/operators"}
SHADE = {1.0: "#0b3d7a", 0.5: "#2a78d6", 0.25: "#6fa3e3", 0.1: "#aac7ec"}  # sequential, darkest = densest
STYLE = {1.0: "-", 0.5: (0, (4, 2)), 0.25: (0, (2, 1.5)), 0.1: (0, (1, 1.2))}


def load(folder):
    rows = {}
    for f in sorted(glob.glob(os.path.join(folder, "*.json"))):
        r = json.load(open(f))
        pts = sorted(r["dspectra_cv"]["heldout"], key=lambda p: p["eta"])
        rows[os.path.basename(f)[:-5]] = (pts, r["_config"].get("n_edges_fit"))
    return rows


def main():
    os.makedirs("results/sparse", exist_ok=True)
    data = {k: load(v) for k, v in LEVELS.items()}
    graphs = sorted(set.intersection(*(set(d) for d in data.values())))
    assert len(graphs) == 63, len(graphs)
    recs = []
    for keep in LEVELS:
        for g in graphs:
            pts, n = data[keep][g]
            a = {p["eta"]: p["auc"] for p in pts}
            d = {p["eta"]: p["d_ev"] for p in pts}
            best = max(a, key=a.get)
            recs.append(dict(graph=g, keep=keep, n_edges=n, auc0=a[0.0], auc_best=a[best], eta_best=best,
                             gain=a[best] - a[0.0], low=a[min(a)] - a[0.0], d_ev0=d[0.0], d_ev_best=d[best],
                             d_ev_low=d[min(a)]))
    df = pd.DataFrame(recs)
    df.to_csv("results/sparse/stats.csv", index=False)
    piv = {c: df.pivot(index="graph", columns="keep", values=c).loc[graphs] for c in ("gain", "low", "eta_best", "d_ev0", "d_ev_best", "auc0")}
    tests = []
    for stat in ("gain", "low"):
        ps = {}
        for keep in (0.5, 0.25, 0.1):
            x, y = piv[stat][keep].values, piv[stat][1.0].values
            dlt = x - y
            try:
                p = wilcoxon(x, y).pvalue if np.any(dlt != 0) else 1.0
            except ValueError:
                p = 1.0
            ps[keep] = (p, dlt.mean(), (dlt > 0).sum(), (dlt < 0).sum())
        order = sorted(ps, key=lambda k: ps[k][0])
        holm, run = {}, 0.0
        for i, k in enumerate(order):
            run = max(run, ps[k][0] * (3 - i))
            holm[k] = min(run, 1.0)
        for keep in (0.5, 0.25, 0.1):
            p, m, w, l = ps[keep]
            tests.append(dict(stat=stat, keep=keep, mean_level=piv[stat][keep].mean(), mean_full=piv[stat][1.0].mean(),
                              mean_delta=m, wins=w, losses=l, p=p, p_holm=holm[keep]))
    tdf = pd.DataFrame(tests)
    tdf.to_csv("results/sparse/tests.csv", index=False)
    # summary
    out = ["# Sparsification frontier (63 graphs, cv fits, rank 32)", "",
           "| keep | citations fit (mean) | AUC at eta = 0 | gain (mean) | low (mean) | low > 0 | best eta (median) | d_ev at eta = 0 | d_ev at best eta |",
           "|---|---|---|---|---|---|---|---|---|"]
    for keep in LEVELS:
        s = df[df.keep == keep]
        out.append(f"| {keep:g} | {s.n_edges.mean():.0f} | {s.auc0.mean():.4f} | {s.gain.mean():.4f} | {s.low.mean():+.4f} | "
                   f"{(s.low > 0).sum()}/63 | {s.eta_best.median():g} | {s.d_ev0.mean():.1f} | {s.d_ev_best.mean():.1f} |")
    out += ["", "## Tests (paired Wilcoxon vs keep = 1.0, Holm over the three levels per statistic)", "",
            "| stat | keep | mean at level | mean at 1.0 | mean delta | wins/losses | p | Holm p |", "|---|---|---|---|---|---|---|---|"]
    for r in tests:
        out.append(f"| {r['stat']} | {r['keep']:g} | {r['mean_level']:.4f} | {r['mean_full']:.4f} | {r['mean_delta']:+.4f} | "
                   f"{r['wins']}/{r['losses']} | {r['p']:.2g} | {r['p_holm']:.2g} |")
    out += ["", "## Best eta distribution (graphs per eta)", ""]
    etas = sorted(df.eta_best.unique())
    out.append("| keep | " + " | ".join(f"{e:g}" for e in etas) + " |")
    out.append("|---|" + "---|" * len(etas))
    for keep in LEVELS:
        s = df[df.keep == keep]
        out.append(f"| {keep:g} | " + " | ".join(str((s.eta_best == e).sum()) for e in etas) + " |")
    out += ["", "## Mean frontier per level (eta grid ascending)", ""]
    fig, ax = plt.subplots(figsize=(6.4, 4.0), dpi=160, facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    for keep in LEVELS:
        D = np.array([[p["d_ev"] for p in data[keep][g][0]] for g in graphs])
        A = np.array([[p["auc"] for p in data[keep][g][0]] for g in graphs])
        etas_g = [p["eta"] for p in data[keep][graphs[0]][0]]
        out.append(f"- keep {keep:g}: eta {etas_g}; d_ev {D.mean(0).round(1).tolist()}; AUC {A.mean(0).round(4).tolist()}")
        ax.plot(D.mean(0), A.mean(0), color=SHADE[keep], lw=2.0, ls=STYLE[keep], marker="o", ms=4.5, markerfacecolor=SURFACE,
                markeredgewidth=1.5, label=f"{keep:.0%} of citations kept", zorder=3)
    ax.set_xlabel("realized dimension d_ev (mean over the 63 graphs)", color=TEXT2, fontsize=9)
    ax.set_ylabel("held-out citation AUC (mean)", color=TEXT2, fontsize=9)
    ax.set_title("Capacity frontier as citations are removed (cv fits, rank 32, same eta grid)", color=TEXT, fontsize=10, loc="left")
    ax.legend(frameon=False, fontsize=8, loc="lower right", labelcolor=TEXT2)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(MUTED)
    ax.tick_params(colors=TEXT2, labelsize=8)
    ax.grid(axis="y", color=MUTED, lw=0.5, alpha=0.5)
    fig.tight_layout()
    fig.savefig("results/sparse/frontier_sparse.png", facecolor=SURFACE)
    open("results/sparse/summary.md", "w").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
