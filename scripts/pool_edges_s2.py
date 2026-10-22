"""
Diagnostic: how many citations exist *between* the papers of each
DeepScholar-base pool, according to Semantic Scholar (which has reference
lists for arXiv preprints, unlike OpenAlex's arXiv records)?

One batch request per pool (all papers by arXiv id); unauthenticated
requests are paced, retried on 429, and cached under data/s2_cache.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import sys
import time

import numpy as np
import pandas as pd
import requests

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from build_graphs import arxiv_core  # noqa: E402

BATCH = "https://api.semanticscholar.org/graph/v1/paper/batch"


def s2_batch(ids, fields, cache_dir="data/s2_cache", max_tries=20):
    key = hashlib.sha1(json.dumps([sorted(ids), fields]).encode()).hexdigest()
    path = os.path.join(cache_dir, key + ".json")
    if os.path.isfile(path):
        with open(path) as f:
            return json.load(f)
    delay, status = 5.0, None
    for _ in range(max_tries):
        try:
            r = requests.post(BATCH, params={"fields": fields}, json={"ids": ids}, timeout=120)
            status = r.status_code
        except requests.RequestException as e:
            r, status = None, type(e).__name__
        if r is not None and r.status_code == 200:
            os.makedirs(cache_dir, exist_ok=True)
            with open(path, "w") as f:
                json.dump(r.json(), f)
            return r.json()
        time.sleep(delay)
        delay = min(delay * 2, 120)
    raise RuntimeError(f"S2 batch failed after {max_tries} tries: {status}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pools", default="data/ds_pools_pilot/pools/qwen3-8b-awq_k50")
    ap.add_argument("--out", default="data/pool_graphs/s2_edges.csv")
    args = ap.parse_args()
    rows = []
    for qdir in sorted(glob.glob(os.path.join(args.pools, "*/"))):
        # read IDs as text: as numbers, 2411.16260 would become 2411.1626
        pool = pd.read_csv(os.path.join(qdir, "pool_all.csv"), dtype={"arxiv_id_from_url": str})
        ax = sorted({a for a in pool.arxiv_id_from_url.map(arxiv_core) if a})
        round_of = {}
        for a, c in zip(pool.arxiv_id_from_url.map(arxiv_core), pool._call):
            round_of[a] = min(round_of.get(a, 99), int(c))
        data = s2_batch([f"ARXIV:{a}" for a in ax], "externalIds,referenceCount,references.paperId")
        pid_of = {a: d["paperId"] for a, d in zip(ax, data) if d}
        idx = {pid: a for a, pid in pid_of.items()}
        edges = {(a, idx[r["paperId"]]) for a, d in zip(ax, data) if d
                 for r in (d.get("references") or []) if r.get("paperId") in idx and idx[r["paperId"]] != a}
        with_refs = sum(1 for d in data if d and d.get("references"))
        for label, keep in [("3 rounds", set(ax)), ("2 rounds", {a for a in ax if round_of[a] <= 1})]:
            E = [(i, j) for i, j in edges if i in keep and j in keep]
            touched = {x for e in E for x in e}
            rows.append({"query": os.path.basename(os.path.normpath(qdir)), "pool": label,
                         "n_papers": len(keep), "frac_resolved": len(set(pid_of) & keep) / max(len(keep), 1),
                         "frac_with_refs": with_refs / max(len(ax), 1) if label == "3 rounds" else np.nan,
                         "n_edges": len(E), "edges_per_paper": len(E) / max(len(keep), 1),
                         "frac_isolated": 1 - len(touched) / max(len(keep), 1)})
        print(f"{rows[-2]['query']}: {rows[-2]['n_papers']} papers, {rows[-2]['n_edges']} within-pool citations, "
              f"{rows[-2]['frac_with_refs']:.0%} with reference lists", flush=True)
        time.sleep(1.5)
    df = pd.DataFrame(rows)
    df.to_csv(args.out, index=False)
    print(df.drop(columns="query").groupby("pool").agg(["mean", "min", "max"]).T.round(3).to_string())


if __name__ == "__main__":
    main()
