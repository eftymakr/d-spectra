"""
Arrange DeepScholar-base style outputs for the DeepScholar-Bench judge
(deepscholar-bench/eval, parser "deepscholar_base"):

  <out>/<row>/intro.md    the report's related-work section (up to "## Research papers")
  <out>/<row>/paper.csv   id, title, url, snippet for every paper the report links to

<row> is the query's row in the benchmark's related_works_combined.csv, which
is the number at the start of the output folder name (000_2506.02838v1 -> 0).
Titles and abstracts come from the method's selection list (--selections,
export_final.py; matched by arXiv id or by URL, which covers papers outside
arXiv) and otherwise from the frozen pool (pool_all.csv, by arXiv id).
"""
from __future__ import annotations

import argparse
import csv
import glob
import os
import re
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_graphs import arxiv_core  # noqa: E402

LINK = re.compile(r"\[([^\]]+?)\]\((https?://[^\)]+)\)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outputs", required=True, help="one folder per query with report.md (e.g. outputs/dsbase_final/s0)")
    ap.add_argument("--pools", required=True, help="the matching frozen pools (e.g. pools/final_r2_s0)")
    ap.add_argument("--selections", default=None, help="the method's list (export_final.py), if not DeepScholar-base")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    listed = {}  # (query folder, arXiv id or URL) -> paper from the selection list
    if args.selections:
        for lp in csv.DictReader(open(args.selections, encoding="utf-8")):
            if lp["arxiv_id"]:
                listed[(lp["query"], arxiv_core(lp["arxiv_id"]))] = lp
            if lp["url"]:
                listed[(lp["query"], lp["url"].strip())] = lp

    n = 0
    for qdir in sorted(glob.glob(os.path.join(args.outputs, "*/"))):
        name = os.path.basename(os.path.normpath(qdir))
        report = os.path.join(qdir, "report.md")
        if not os.path.isfile(report):
            continue
        row = str(int(name.split("_")[0]))
        text = open(report, encoding="utf-8").read()
        intro = text.split("\n## Research papers")[0].strip() + "\n"
        pool = pd.read_csv(os.path.join(args.pools, name, "pool_all.csv"), dtype={"arxiv_id_from_url": str})
        abstract = {arxiv_core(a): s for a, s in zip(pool.arxiv_id_from_url, pool.snippet) if isinstance(s, str)}
        title = {arxiv_core(a): t for a, t in zip(pool.arxiv_id_from_url, pool.title) if isinstance(t, str)}
        papers = {}
        for visible, url in LINK.findall(intro):
            m = re.search(r"arxiv\.org/abs/([^)\s]+)", url)
            if m and m.group(1) not in papers:
                core = arxiv_core(m.group(1))
                lp = listed.get((name, core), {})
                papers[m.group(1)] = {"id": m.group(1), "title": lp.get("title") or title.get(core, visible),
                                      "url": url, "snippet": lp.get("abstract") or abstract.get(core, "")}
            elif not m and (name, url.strip()) in listed and url.strip() not in papers:
                lp = listed[(name, url.strip())]
                papers[url.strip()] = {"id": lp["s2_id"] or url.strip(), "title": lp["title"],
                                       "url": url.strip(), "snippet": lp["abstract"]}
        os.makedirs(os.path.join(args.out, row), exist_ok=True)
        with open(os.path.join(args.out, row, "intro.md"), "w", encoding="utf-8") as f:
            f.write(intro)
        with open(os.path.join(args.out, row, "paper.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["id", "title", "url", "snippet"])
            w.writeheader()
            w.writerows(papers.values())
        n += 1
    print(f"{n} reports written to {args.out}")


if __name__ == "__main__":
    main()
