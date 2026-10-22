"""
Export each method's selected papers, at the matched budget (as many papers
as DeepScholar's filter kept for that query), for the shared writer + judge.

One CSV per method and setting:
  selections/<run>/<setting>/<method>.csv
  columns: query, rank, arxiv_id, s2_id, title, abstract, date, in_pool, source
`query` is the pool folder name (e.g. 000_2506.02838v1); `rank` is the
selection order; papers added from the citation graph have in_pool = False.
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import re

NAMES = {"search_only": "fixed_k", "relevance_only": "relevance_only", "most_cited": "most_cited",
         "vendi": "vendi", "semantic_modes": "semantic_modes", "symmetrized": "symmetrized",
         "raw_svd": "raw_svd", "usvt": "usvt", "dspectra_eta0": "dspectra_eta0",
         "dspectra": "dspectra", "dspectra_d4": "dspectra_d4", "dspectra_d16": "dspectra_d16"}
COLUMNS = ["query", "rank", "arxiv_id", "s2_id", "title", "abstract", "date", "in_pool", "source"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pools", required=True, help="pool folders (for the query names)")
    ap.add_argument("--graphs", required=True)
    ap.add_argument("--results", required=True, nargs="+",
                    help="setting=results_dir pairs, e.g. expanded=results/pilot_dsf")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    folder = {re.search(r"(\d{4}\.\d{4,5})", os.path.basename(os.path.normpath(d))).group(1):
              os.path.basename(os.path.normpath(d)) for d in glob.glob(os.path.join(args.pools, "*/"))}
    for pair in args.results:
        setting, res = pair.split("=", 1)
        rows = {}
        skipped = []
        for f in sorted(glob.glob(f"{res}/per_query/*.json")):
            q = json.load(open(f))
            aid = q["arxiv_id"]
            g = json.load(open(f"{args.graphs}/{aid}.json"))
            matched = {k.split("@")[0]: S for k, S in q["selections"].items() if k.endswith("@0")}
            if not matched:
                skipped.append(aid)
                continue
            for method, S in matched.items():
                if method not in NAMES:
                    continue  # DeepScholar's own picks are already in Mateo's outputs
                for rank, i in enumerate(S, 1):
                    nd = g["nodes"][i]
                    rows.setdefault(NAMES[method], []).append({
                        "query": folder.get(aid, aid), "rank": rank, "arxiv_id": nd.get("arxiv_id") or "",
                        "s2_id": nd.get("s2_id") or "", "title": nd["title"], "abstract": nd.get("abstract") or "",
                        "date": nd.get("publication_date") or "", "in_pool": nd["source"] == "seed",
                        "source": {"seed": "pool", "ref": "reference", "citer": "citing"}[nd["source"]]})
        os.makedirs(f"{args.out}/{setting}", exist_ok=True)
        for name, rs in sorted(rows.items()):
            with open(f"{args.out}/{setting}/{name}.csv", "w", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=COLUMNS)
                w.writeheader()
                w.writerows(rs)
        n_q = len({r["query"] for rs in rows.values() for r in rs})
        print(f"{setting}: {len(rows)} methods, {n_q} queries"
              f"{f', skipped (no kept list): {skipped}' if skipped else ''}")


if __name__ == "__main__":
    main()
