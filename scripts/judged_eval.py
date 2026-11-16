"""
Judged evaluation of the seed-0 selection lists (rules: scratchpad/judged_rules.md,
E18 rule in judge/e18_chain.sh). Reads the judge's per-report scores
(judge/results/writer_s0/<system>/<metric>/deepscholar_base.csv), maps reports to
queries through the writer's stats.json, and writes

  results/judged/rows.csv      one row per system x query with every metric, the split,
                               the number of papers and the token cost (E12 model)
  results/judged/tests.csv     paired Wilcoxon tests (families 1, 2 and E18)
  results/judged/frontier.png  tokens per query vs nugget coverage, held-out 43
  <tables_out>                 markdown tables for the results document

Nothing is typed in by hand.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

import matplotlib
import numpy as np
import pandas as pd
from scipy.stats import wilcoxon
from tabulate import tabulate

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seed_tests import holm  # noqa: E402

METRICS = ["nugget_coverage", "reference_coverage", "document_importance", "cite_p", "claim_coverage",
           "coverage_relevance_rate", "organization"]
MLABEL = {"nugget_coverage": "nugget coverage", "reference_coverage": "reference coverage",
          "document_importance": "document importance", "cite_p": "citation precision", "claim_coverage": "claim coverage",
          "coverage_relevance_rate": "coverage relevance (0-2)", "organization": "organization"}
SYSTEMS = ["dsbase_rerun", "fixed_k", "relevance_only", "dspectra", "cocite_rel", "usvt_cocite_rel", "scocite_rel",
           "qlink_rel", "oracle"]
E18 = {"dspectra": "dspectra_modes", "scocite_rel": "scocite_rel_modes", "usvt_cocite_rel": "usvt_cocite_rel_modes"}
LABEL = {"dsbase_rerun": "DeepScholar-base's own picks (rerun)", "fixed_k": "fixed-k", "relevance_only": "relevance only",
         "dspectra": "D-SPECTRA (d_ev = 8)", "cocite_rel": "co-citation + relevance", "usvt_cocite_rel": "USVT co-citation + relevance",
         "scocite_rel": "SPECTRA co-citation + relevance", "qlink_rel": "query link + relevance", "oracle": "oracle (human-cited refs)",
         "dspectra_modes": "D-SPECTRA, modes as taxonomy", "scocite_rel_modes": "SPECTRA co-citation + relevance, modes as taxonomy",
         "usvt_cocite_rel_modes": "USVT co-citation + relevance, modes as taxonomy"}
SEARCH, FILTER, WRITER0, PER_PAPER = 43_885, 199_785, 10_502, 1_626
SURFACE, TEXT, TEXT2, MUTED, SERIES1 = "#fcfcfb", "#0b0b0b", "#52514e", "#b9b8b1", "#2a78d6"


def pv(p):
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def load_rows(judge_dir, writer_dir, dev):
    out = []
    for sysname in SYSTEMS + list(E18.values()):
        stats = {}
        for f in glob.glob(f"{writer_dir}/{sysname}/*/stats.json"):
            s = json.load(open(f))
            stats[int(os.path.basename(os.path.dirname(f)))] = s
        scores = None
        for m in METRICS:
            d = pd.read_csv(f"{judge_dir}/{sysname}/{m}/deepscholar_base.csv")[["folder_path", m]]
            d["row"] = d.folder_path.map(lambda p: int(os.path.basename(os.path.normpath(p))))
            d = d[["row", m]]
            scores = d if scores is None else scores.merge(d, on="row", how="outer")
        for _, r in scores.iterrows():
            s = stats[int(r.row)]
            aid = s["query"].split("_", 1)[1][:10]
            n = s["n_papers"]
            tokens = SEARCH + (FILTER if sysname == "dsbase_rerun" else 0) + WRITER0 + PER_PAPER * n
            out.append({"system": sysname, "row": int(r.row), "arxiv_id": aid, "split": "design" if aid in dev else "held-out",
                        "n_papers": n, "n_linked": s["n_linked"], "tokens": tokens, **{m: r[m] for m in METRICS}})
    rows = pd.DataFrame(out)
    judged = rows.groupby("system").row.nunique()
    expected = {s: 63 for s in SYSTEMS + list(E18.values())}
    missing = {s: sorted(set(range(63)) - set(rows[rows.system == s].row)) for s in expected}
    return rows, {s: v for s, v in missing.items() if v}


def paired(rows, a, b, metric, split=None):
    """Paired difference a - b over the queries both systems have (a and b are system names)."""
    x = rows[rows.system == a].set_index("arxiv_id")[metric]
    y = rows[rows.system == b].set_index("arxiv_id")[metric]
    if split:
        keep = rows[(rows.system == a) & (rows.split == split)].arxiv_id
        x = x[x.index.isin(keep)]
    idx = x.index.intersection(y.index)
    x, y = x[idx], y[idx]
    diff = x - y
    if (diff != 0).sum() == 0:
        p = 1.0
    else:
        p = wilcoxon(x, y, zero_method="wilcox").pvalue
    return {"n": len(idx), "mean_a": x.mean(), "mean_b": y.mean(), "diff": diff.mean(), "wins": int((diff > 0).sum()),
            "losses": int((diff < 0).sum()), "p": p}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge_dir", default="/home/eftychia/Spectra/judge/results/writer_s0")
    ap.add_argument("--writer_dir", default="/home/eftychia/Spectra/judge/writer/s0")
    ap.add_argument("--design_pools", default="pools/qwen3-8b-awq_k50")
    ap.add_argument("--out", default="results/judged")
    ap.add_argument("--tables_out", required=True)
    args = ap.parse_args()
    dev = {os.path.basename(os.path.normpath(d)).split("_")[1][:10] for d in glob.glob(f"{args.design_pools}/*/")}
    assert len(dev) == 20, len(dev)
    os.makedirs(args.out, exist_ok=True)
    rows, missing = load_rows(args.judge_dir, args.writer_dir, dev)
    rows.to_csv(f"{args.out}/rows.csv", index=False)
    T = []

    def emit(title, df, note=None):
        T.append(f"\n#### {title}\n")
        T.append(tabulate(df, headers="keys", tablefmt="pipe", disable_numparse=True))
        if note:
            T.append(f"\n{note}")

    # ---- means per system, held-out 43 and all 63
    for split, title in (("held-out", "judged scores, held-out 43 queries (seed 0, same writer and judge)"),
                         (None, "judged scores, all 63 queries (seed 0, same writer and judge)")):
        tab = {}
        for s in SYSTEMS:
            r = rows[(rows.system == s) & ((rows.split == split) if split else True)]
            cell = {"n judged": str(len(r)), "papers": f"{r.n_papers.mean():.1f}", "tokens / query": f"{r.tokens.mean() / 1000:.0f}k"}
            for m in METRICS:
                if m == "document_importance":
                    continue
                cell[MLABEL[m]] = f"{r[m].mean():.3f}" if m != "coverage_relevance_rate" else f"{r[m].mean():.2f}"
            tab[LABEL[s]] = cell
        note = ("Tokens per query by the E12 model (search 43,885 + filter 199,785 for DeepScholar-base only + writer 10,502 + 1,626 per paper). "
                "Document importance is omitted: it looks every cited title up on OpenAlex, which answered 429 (rate limit) during most judge runs, "
                "so it is 0 on every report of 7 of the 9 systems (kept in rows.csv). "
                + "; ".join(f"{LABEL[s]}: report{'s' if len(v) > 1 else ''} {v} not judged (the writer linked no papers), means over the rest"
                            for s, v in missing.items() if s in SYSTEMS))
        emit(f"Judged: {title}", pd.DataFrame(tab).T, note)

    # ---- family 1: each vs the rerun, nugget coverage, held-out
    tests = []
    fam1 = []
    for s in SYSTEMS[1:]:
        t = paired(rows, s, "dsbase_rerun", "nugget_coverage", "held-out")
        fam1.append({"family": "1: vs DeepScholar-base rerun", "metric": "nugget_coverage", "a": s, "b": "dsbase_rerun", "split": "held-out", **t})
    adj = holm([t["p"] for t in fam1])
    for t, a in zip(fam1, adj):
        t["p_holm"] = a
    tests += fam1
    tab = {LABEL[t["a"]]: {"n": str(t["n"]), "method": f"{t['mean_a']:.3f}", "DS-base rerun": f"{t['mean_b']:.3f}", "diff": f"{t['diff']:+.3f}",
                           "wins / losses": f"{t['wins']} / {t['losses']}", "p": pv(t["p"]), "Holm p (8)": pv(t["p_holm"])} for t in fam1}
    emit("Judged: each method vs DeepScholar-base's own picks on nugget coverage (held-out 43, paired Wilcoxon, Holm over 8)",
         pd.DataFrame(tab).T)

    # ---- family 2: USVT co-citation vs D-SPECTRA and relevance only
    fam2 = []
    for b in ("dspectra", "relevance_only"):
        t = paired(rows, "usvt_cocite_rel", b, "nugget_coverage", "held-out")
        fam2.append({"family": "2: USVT co-citation vs", "metric": "nugget_coverage", "a": "usvt_cocite_rel", "b": b, "split": "held-out", **t})
    adj = holm([t["p"] for t in fam2])
    for t, a in zip(fam2, adj):
        t["p_holm"] = a
    tests += fam2
    tab = {LABEL[t["b"]]: {"n": str(t["n"]), "USVT co-citation + relevance": f"{t['mean_a']:.3f}", "other": f"{t['mean_b']:.3f}",
                           "diff": f"{t['diff']:+.3f}", "wins / losses": f"{t['wins']} / {t['losses']}", "p": pv(t["p"]),
                           "Holm p (2)": pv(t["p_holm"])} for t in fam2}
    emit("Judged: USVT co-citation + relevance vs D-SPECTRA and vs relevance only on nugget coverage (held-out 43, Holm over 2)",
         pd.DataFrame(tab).T)

    # ---- secondary metrics vs the rerun, uncorrected, held-out
    tab = {}
    for s in SYSTEMS[1:]:
        cell = {}
        for m in METRICS:
            if m in ("organization", "document_importance"):
                continue
            t = paired(rows, s, "dsbase_rerun", m, "held-out")
            tests.append({"family": "secondary: vs rerun (no claim)", "metric": m, "a": s, "b": "dsbase_rerun", "split": "held-out", **t, "p_holm": np.nan})
            cell[MLABEL[m]] = f"{t['diff']:+.3f} ({pv(t['p'])})"
        tab[LABEL[s]] = cell
    emit("Judged: the other metrics vs DeepScholar-base's own picks (held-out 43; difference and uncorrected p, no claim)",
         pd.DataFrame(tab).T, "Organization is 0.5 on every report (the judge prefers whichever section it sees first), so it is omitted.")

    # ---- E18: modes as taxonomy vs the writer's taxonomy, 63 queries
    e18 = []
    for base, modes in E18.items():
        for m in ("organization", "nugget_coverage"):
            t = paired(rows, modes, base, m)
            e18.append({"family": "E18: modes vs writer taxonomy", "metric": m, "a": modes, "b": base, "split": "all", **t})
    adj = holm([t["p"] for t in e18])
    for t, a in zip(e18, adj):
        t["p_holm"] = a
    tests += e18
    tab = {f"{LABEL[t['b']]}, {MLABEL[t['metric']]}": {"n": str(t["n"]), "modes": f"{t['mean_a']:.3f}", "writer's taxonomy": f"{t['mean_b']:.3f}",
                                                       "diff": f"{t['diff']:+.3f}", "wins / losses": f"{t['wins']} / {t['losses']}",
                                                       "p": pv(t["p"]), "Holm p (6)": pv(t["p_holm"])} for t in e18}
    emit("E18 the fitted modes as the report's taxonomy: primary metrics (63 queries, paired Wilcoxon, Holm over 3 lists x 2 metrics)",
         pd.DataFrame(tab).T)
    tab = {}
    for base, modes in E18.items():
        cell = {}
        for m in METRICS:
            if m in ("organization", "nugget_coverage", "document_importance"):
                continue
            t = paired(rows, modes, base, m)
            tests.append({"family": "E18 secondary (no claim)", "metric": m, "a": modes, "b": base, "split": "all", **t, "p_holm": np.nan})
            cell[MLABEL[m]] = f"{t['diff']:+.3f} ({pv(t['p'])})"
        tab[LABEL[base]] = cell
    emit("E18 the other judged metrics, modes minus writer's taxonomy (63 queries; uncorrected p, no claim)", pd.DataFrame(tab).T)
    pd.DataFrame(tests).to_csv(f"{args.out}/tests.csv", index=False)

    # ---- frontier figure: tokens vs nugget coverage, held-out
    ho = rows[rows.split == "held-out"].groupby("system").agg(tokens=("tokens", "mean"), cov=("nugget_coverage", "mean"),
                                                             claim=("claim_coverage", "mean"))
    fig, ax = plt.subplots(figsize=(6.4, 4.0), dpi=160, facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    for s in SYSTEMS:
        x, y = ho.loc[s, "tokens"] / 1000, ho.loc[s, "cov"]
        hollow = s in ("dsbase_rerun", "oracle")
        ax.plot(x, y, marker="o", ms=7, color=SERIES1, markerfacecolor=SURFACE if hollow else SERIES1, markeredgewidth=1.6, ls="none", zorder=3)
    short = {"dsbase_rerun": "DeepScholar-base's picks", "fixed_k": "fixed-k", "relevance_only": "relevance only", "dspectra": "D-SPECTRA",
             "cocite_rel": "co-citation + rel.", "usvt_cocite_rel": "USVT co-citation + rel.", "scocite_rel": "SPECTRA co-citation + rel.",
             "qlink_rel": "query link + rel.", "oracle": "oracle"}
    ys = ho.loc[SYSTEMS].sort_values("cov")
    for s in SYSTEMS:
        ax.annotate(short[s], (ho.loc[s, "tokens"] / 1000, ho.loc[s, "cov"]), xytext=(7, 0), textcoords="offset points", fontsize=7.5,
                    color=TEXT2, va="center")
    ax.set_xlabel("LLM tokens per query (thousands; search + filter + writer)", color=TEXT2, fontsize=9)
    ax.set_ylabel("judged nugget coverage (mean, held-out 43)", color=TEXT2, fontsize=9)
    ax.set_title("Cost and judged coverage of the selection lists (seed 0, same writer and judge)", color=TEXT, fontsize=10, loc="left")
    ax.set_xlim(0, ho.tokens.max() / 1000 * 1.35)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(MUTED)
    ax.tick_params(colors=TEXT2, labelsize=8)
    ax.grid(axis="y", color=MUTED, lw=0.5, alpha=0.5)
    fig.tight_layout()
    fig.savefig(f"{args.out}/frontier.png", facecolor=SURFACE)
    ho.to_csv(f"{args.out}/frontier.csv")

    open(args.tables_out, "w").write("\n".join(T) + "\n")
    print("\n".join(T))
    print("missing:", missing)


if __name__ == "__main__":
    main()
