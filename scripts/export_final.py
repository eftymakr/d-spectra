"""
Final selection lists for the shared writer + judge, one folder per search seed.

The methods are frozen (chosen on the design queries in E6-E11), each at the
matched budget (as many papers as DeepScholar-base kept for the query):

  fixed_k            top-B pool papers by relevance (the course baseline)
  relevance_only     top-B by relevance over the expanded graph (the main ablation)
  dspectra           D-SPECTRA as proposed: greedy F(S), d_ev = 8, alpha 0.5, gamma 5
  qlink_rel          query link + relevance (10 anchors, eta = 0 fit, link weight 0.75; E10)
  cocite_rel         co-citation by the 10 most relevant pool papers + relevance (0.75; E11)
  usvt_cocite_rel    the same on the USVT-denoised citation matrix (5 anchors, 0.75; E11)
  scocite_rel        SPECTRA co-citation: the 5 anchors' predicted citation probabilities
                     under the eta = 0 fit, all modes + relevance (0.75; E13)
  oracle             the benchmark's important human-cited references (the ideal-sources
                     upper bound; up to 30, those with an abstract first)

DeepScholar-base's own picks are Mateo's kept.csv files. Columns:
  query, rank, arxiv_id, s2_id, url, title, abstract, date, in_pool, source
`url` is the arXiv link when there is one and the Semantic Scholar link
otherwise, so the writer cites a link the judge's parser can resolve.
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from build_graphs import arxiv_core  # noqa: E402
from pilot_selection import load_graph, rank_pct, relevance, usvt_threshold  # noqa: E402
from tune_selection import kept_indices  # noqa: E402

COLUMNS = ["query", "rank", "arxiv_id", "s2_id", "url", "title", "abstract", "date", "in_pool", "source"]
SOURCE = {"seed": "pool", "ref": "reference", "citer": "citing", "ref2": "second-hop reference"}


def url_of(arxiv_id, s2_id):
    if arxiv_id:
        return f"http://arxiv.org/abs/{arxiv_id}"
    return f"https://www.semanticscholar.org/paper/{s2_id}" if s2_id else ""


def mix(r, s, lam):
    return (1 - lam) * rank_pct(r) + lam * rank_pct(s)


def select(g, A, r, zf, B):
    from dspectra.selection import greedy_select, query_link_scores, top_k
    seeds = np.array([k for k, nd in enumerate(g["nodes"]) if nd["source"] == "seed"])
    linked = seeds[A[seeds].sum(1) > 0]
    pool = linked if len(linked) else seeds

    def anchors(m):
        return pool[np.argsort(-r[pool], kind="stable")[:m]]

    def cocite(M, m):
        anc = anchors(m)
        return (r[anc] / max(r[anc].sum(), 1e-12)) @ M[anc] + 1e-6 * r

    P0 = {k: zf[f"eta0_{k}"] for k in ("U", "V", "sigma", "p", "a", "b", "beta")}
    U_, s_, Vt_ = np.linalg.svd(A, full_matrices=False)
    k_ = max(1, int((s_ > usvt_threshold(A)).sum()))
    A_hat = (U_[:, :k_] * s_[:k_]) @ Vt_[:k_]

    def scocite(m):  # E13's chosen setting: eta = 0 fit, all modes, m anchors, predicted citations only
        anc = anchors(m)
        n = A.shape[0]
        K = n * (P0["U"][anc] * P0["sigma"]) @ P0["V"].T / P0["sigma"].sum()
        prob = 1.0 / (1.0 + np.exp(-(P0["a"][anc, None] + P0["b"][None, :] + float(P0["beta"]) * K)))
        prob[np.arange(len(anc)), anc] = 0.0
        return (r[anc] / max(r[anc].sum(), 1e-12)) @ prob + 1e-6 * r

    return {
        "fixed_k": top_k(r, B, candidates=seeds),
        "relevance_only": top_k(r, B),
        "dspectra": greedy_select(zf["d8_V"], zf["d8_p"], r, B, 0.5, 5.0),
        "qlink_rel": top_k(mix(r, query_link_scores(P0, r, anchors(10)), 0.75), B),
        "cocite_rel": top_k(mix(r, cocite(A, 10), 0.75), B),
        "usvt_cocite_rel": top_k(mix(r, cocite(A_hat, 5), 0.75), B),
        "scocite_rel": top_k(mix(r, scocite(5), 0.75), B),
    }


def oracle_rows(imp, aid, folder):
    rows = imp[imp.parent_paper_arxiv_id.astype(str).map(arxiv_core) == aid].copy()
    rows["has_abs"] = rows.cited_paper_abstract.notna()
    rows = rows.sort_values("has_abs", ascending=False, kind="stable").head(30)
    out = []
    for rank, (_, x) in enumerate(rows.iterrows(), 1):
        ax = arxiv_core(str(x.cited_paper_arxiv_link)) if pd.notna(x.cited_paper_arxiv_link) else ""
        out.append({"query": folder, "rank": rank, "arxiv_id": ax, "s2_id": "",
                    "url": url_of(ax, "") or (x.bib_paper_url if pd.notna(x.bib_paper_url) else ""),
                    "title": x.cited_paper_title, "abstract": x.cited_paper_abstract if x.has_abs else "",
                    "date": "", "in_pool": "", "source": "human-cited"})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pools", required=True)
    ap.add_argument("--graphs", required=True)
    ap.add_argument("--emb_dir", required=True)
    ap.add_argument("--operators", required=True, help="fit_variants.py output with d8 and eta0 fits")
    ap.add_argument("--kept_dir", required=True)
    ap.add_argument("--dataset_dir", default="data/deepscholar_bench")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    imp = pd.read_csv(os.path.join(args.dataset_dir, "important_citations.csv"))
    folders = {arxiv_core(os.path.basename(os.path.normpath(d)).split("_", 1)[1]): os.path.basename(os.path.normpath(d))
               for d in glob.glob(os.path.join(args.pools, "*/"))}
    lists, missing = {}, []
    for aid, folder in sorted(folders.items()):
        lists.setdefault("oracle", []).extend(oracle_rows(imp, aid, folder))
        path = f"{args.graphs}/{aid}.json"
        full = f"{args.operators}/{aid}_full.npz"
        if not (os.path.isfile(path) and os.path.isfile(full)):
            missing.append(aid)
            continue
        g, A = load_graph(path)
        kept = kept_indices(g, args.kept_dir)
        if not kept:
            missing.append(aid)
            continue
        z = np.load(f"{args.emb_dir}/{aid}.npz")
        r = relevance(z["query"], z["nodes"])
        for method, S in select(g, A, r, np.load(full), len(kept)).items():
            for rank, i in enumerate(S, 1):
                nd = g["nodes"][i]
                ax, s2 = nd.get("arxiv_id") or "", nd.get("s2_id") or ""
                lists.setdefault(method, []).append({
                    "query": folder, "rank": rank, "arxiv_id": ax, "s2_id": s2, "url": url_of(ax, s2),
                    "title": nd["title"], "abstract": nd.get("abstract") or "",
                    "date": nd.get("publication_date") or "", "in_pool": nd["source"] == "seed",
                    "source": SOURCE[nd["source"]]})
    os.makedirs(args.out, exist_ok=True)
    for method, rows in lists.items():
        with open(f"{args.out}/{method}.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=COLUMNS)
            w.writeheader()
            w.writerows(rows)
    print(f"{args.out}: {len(lists)} lists, {len(folders) - len(missing)} queries"
          f"{f'; missing graph, fit or kept list: {missing}' if missing else ''}")


if __name__ == "__main__":
    main()
