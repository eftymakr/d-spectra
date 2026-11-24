"""
Diagnostic: how many citations exist *between* the papers of each
DeepScholar-base pool, according to Semantic Scholar (which has reference
lists for arXiv preprints, unlike OpenAlex's arXiv records)?

One batch request per pool (all papers by arXiv id); requests (with S2_API_KEY from
.env if set) are paced, retried on 429, and cached under data/s2_cache.
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


_PAPERS = {}  # fields -> {paper id or "ARXIV:<id>": record}, from every cached response


def _usable(rec, fields):
    """A cached record can answer a request if it has every requested field
    and, for list fields such as citations.year, the requested subfields."""
    for f in fields.split(","):
        top, _, sub = f.partition(".")
        if top not in rec:
            return False
        if sub and isinstance(rec[top], list) and rec[top] and sub not in rec[top][0]:
            return False
    return True


def _paper_index(cache_dir, fields):
    if fields not in _PAPERS:
        idx = {}
        for path in glob.glob(os.path.join(cache_dir, "*.json")):
            try:
                with open(path) as f:
                    recs = json.load(f)
            except ValueError:
                continue
            for rec in recs if isinstance(recs, list) else []:
                if rec and rec.get("paperId") and _usable(rec, fields):
                    idx[rec["paperId"]] = rec
                    ax = (rec.get("externalIds") or {}).get("ArXiv")
                    if ax:
                        idx[f"ARXIV:{ax}"] = rec
        _PAPERS[fields] = idx
    return _PAPERS[fields]


def _api_key():
    """S2_API_KEY from the environment or the git-ignored .env (never logged)."""
    if os.environ.get("S2_API_KEY"):
        return os.environ["S2_API_KEY"]
    if os.path.isfile(".env"):
        with open(".env") as f:
            for line in f:
                k, _, v = line.strip().partition("=")
                if k == "S2_API_KEY" and v:
                    return v
    return None


def _fetch(ids, fields, max_tries):
    key = _api_key()
    headers = {"x-api-key": key} if key else {}
    delay, status = 5.0, None
    for _ in range(max_tries):
        try:
            r = requests.post(BATCH, params={"fields": fields}, json={"ids": ids},
                              headers=headers, timeout=120)
            status = r.status_code
        except requests.RequestException as e:
            r, status = None, type(e).__name__
        if r is not None and r.status_code == 200:
            return r.json()
        if status == 400:  # a malformed or unknown id: retrying won't help
            break
        print(f"S2 batch of {len(ids)}: {status}; retrying in {delay:.0f}s", file=sys.stderr, flush=True)
        time.sleep(delay)
        delay = min(delay * 2, 120)
    raise RuntimeError(f"S2 batch failed after {max_tries} tries: {status}")


def _fetch_split(ids, fields, max_tries):
    """Fetch, halving a batch that keeps failing: some batches (e.g. the citation
    lists of many papers) are refused as a whole but served in smaller parts.
    A single paper refused with 400 counts as unknown (None), like a paper
    Semantic Scholar does not have."""
    if len(ids) == 1:
        try:
            return _fetch(ids, fields, max_tries)
        except RuntimeError as e:
            if str(e).endswith(": 400"):
                return [None]
            raise
    try:
        return _fetch(ids, fields, min(max_tries, 6))
    except RuntimeError:
        h = len(ids) // 2
        return _fetch_split(ids[:h], fields, max_tries) + _fetch_split(ids[h:], fields, max_tries)


def s2_batch(ids, fields, cache_dir="data/s2_cache", max_tries=20):
    """Batch lookup, cached per request; papers already in any cached response
    are reused, so only papers never seen before are requested (overlapping
    pools, e.g. different search seeds, share most of their papers)."""
    key = hashlib.sha1(json.dumps([sorted(ids), fields]).encode()).hexdigest()
    path = os.path.join(cache_dir, key + ".json")
    if os.path.isfile(path):
        with open(path) as f:
            return json.load(f)
    idx = _paper_index(cache_dir, fields)
    missing = [i for i in ids if i not in idx]
    found = dict(zip(missing, _fetch_split(missing, fields, max_tries))) if missing else {}
    out = [idx.get(i, found.get(i)) for i in ids]
    for i, rec in found.items():
        if rec:
            idx[i] = idx[rec["paperId"]] = rec
    os.makedirs(cache_dir, exist_ok=True)
    with open(path, "w") as f:
        json.dump(out, f)
    return out


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
