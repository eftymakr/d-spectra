"""
Citation graphs on DeepScholar-base's frozen candidate pools.

Every system selects from the same pool, so here the graph's nodes are
exactly the pool's papers and OpenAlex supplies only the citation edges
between them (no expansion). Each pool paper is looked up by its arXiv
DOI; a lookup counts only if the titles agree.

For each query this reports how many pool papers resolve, how many have
a reference list, how many within-pool citations exist, and how many of
the human-cited related-work references the pool contains, for the full
pool and for the first two search rounds (_call <= 1).

Output: data/pool_graphs/<pools name>/<arxiv_id>.json and a summary CSV.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from build_graphs import arxiv_core, norm_title, title_matcher, titles_agree  # noqa: E402
from dspectra.openalex import OpenAlexClient, abstract_text, bare_doi, short_id  # noqa: E402


def build_pool_graph(oa, pool: pd.DataFrame, cit_rows: pd.DataFrame):
    pool = pool.assign(ax=pool.arxiv_id_from_url.map(arxiv_core),
                       nt=pool.title.map(norm_title))
    pool = pool.drop_duplicates("ax").drop_duplicates("nt").reset_index(drop=True)
    recs = {bare_doi(w.get("doi")): w for w in
            oa.by_dois([f"10.48550/arxiv.{a}" for a in pool.ax if a],
                       select="id,title,doi,referenced_works")}
    nodes, oa_index = [], {}
    for k, row in pool.iterrows():
        w = recs.get(f"10.48550/arxiv.{row.ax}") if row.ax else None
        ok = w is not None and titles_agree(w.get("title") or "", row.title)
        refs = {short_id(r) for r in (w.get("referenced_works") or [])} if ok else set()
        nodes.append({"title": row.title, "arxiv_id": row.ax, "round": int(row._call),
                      "abstract": str(row.snippet) if isinstance(row.snippet, str) else "",
                      "openalex_id": short_id(w["id"]) if ok else None,
                      "n_refs_listed": len(refs), "_refs": refs})
        if ok:
            oa_index[short_id(w["id"])] = k
    edges = sorted({(k, oa_index[r]) for k, nd in enumerate(nodes)
                    for r in nd.pop("_refs") if r in oa_index and oa_index[r] != k})

    gt_ax = {arxiv_core(l): key for key, l in zip(cit_rows.citation_shorthand,
                                                   cit_rows.cited_paper_arxiv_link) if arxiv_core(l)}
    gt_titles = {norm_title(t): key for key, t in zip(cit_rows.citation_shorthand,
                                                      cit_rows.cited_paper_title)}
    match = title_matcher(gt_titles)
    node_keys = {}
    for k, nd in enumerate(nodes):
        key = gt_ax.get(nd["arxiv_id"])
        if key is None:
            t = match(nd["title"])
            key = gt_titles[t] if t else None
        if key is not None:
            node_keys[k] = key
    return nodes, edges, node_keys


def stats(nodes, edges, node_keys, n_gt, keep=None):
    keep = set(range(len(nodes))) if keep is None else set(keep)
    E = [(i, j) for i, j in edges if i in keep and j in keep]
    deg = np.zeros(len(nodes))
    for i, j in E:
        deg[i] += 1; deg[j] += 1
    n = len(keep)
    return {"n_nodes": n,
            "frac_resolved": float(np.mean([nodes[k]["openalex_id"] is not None for k in keep])),
            "frac_with_refs": float(np.mean([nodes[k]["n_refs_listed"] > 0 for k in keep])),
            "n_edges": len(E), "density": len(E) / max(n * (n - 1), 1),
            "frac_isolated": float(np.mean([deg[k] == 0 for k in keep])),
            "gt_in_pool": len({node_keys[k] for k in keep if k in node_keys}),
            "gt_reach": len({node_keys[k] for k in keep if k in node_keys}) / max(n_gt, 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pools", default="data/ds_pools_pilot/pools/qwen3-8b-awq_k50")
    ap.add_argument("--dataset_dir", default="data/deepscholar_bench")
    ap.add_argument("--out", default="data/pool_graphs")
    args = ap.parse_args()
    name = os.path.basename(os.path.normpath(args.pools))
    out_dir = os.path.join(args.out, name)
    os.makedirs(out_dir, exist_ok=True)
    cits = pd.read_csv(os.path.join(args.dataset_dir, "citations.csv"))
    oa = OpenAlexClient()

    rows = []
    for qdir in sorted(glob.glob(os.path.join(args.pools, "*/"))):
        with open(os.path.join(qdir, "query.json")) as f:
            q = json.load(f)
        # read IDs as text: as numbers, 2411.16260 would become 2411.1626
        pool = pd.read_csv(os.path.join(qdir, "pool_all.csv"), dtype={"arxiv_id_from_url": str})
        cit_rows = cits[cits.parent_paper_arxiv_id == q["arxiv_id"]]
        nodes, edges, node_keys = build_pool_graph(oa, pool, cit_rows)
        n_gt = int(cit_rows.citation_shorthand.nunique())
        aid = arxiv_core(q["arxiv_id"])
        with open(os.path.join(out_dir, f"{aid}.json"), "w") as f:
            json.dump({"arxiv_id": aid, "query": {"title": q["title"],
                       "published_date": q["published_date"]},
                       "nodes": nodes, "edges": edges,
                       "gt": {"n_cited_in_related_work": n_gt,
                              "node_keys": {str(k): v for k, v in node_keys.items()}}}, f)
        two_rounds = [k for k, nd in enumerate(nodes) if nd["round"] <= 1]
        for label, keep in [("3 rounds", None), ("2 rounds", two_rounds)]:
            rows.append({"arxiv_id": aid, "pool": label,
                         **stats(nodes, edges, node_keys, n_gt, keep)})
        print(f"{aid}: {rows[-2]['n_nodes']} papers, {rows[-2]['n_edges']} edges, "
              f"{rows[-2]['frac_with_refs']:.0%} with refs, gt {rows[-2]['gt_in_pool']}/{n_gt}",
              flush=True)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(out_dir, "summary.csv"), index=False)
    pd.set_option("display.width", 200)
    print(df.drop(columns="arxiv_id").groupby("pool").agg(["mean", "min", "max"])
          .T.round(3).to_string())


if __name__ == "__main__":
    main()
