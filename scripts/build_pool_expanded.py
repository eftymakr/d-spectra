"""
The proposal's graph on DeepScholar-base's frozen pools: start from the
pool papers, add their references and their citing papers (published
before the query paper), and take citation edges among all of them.
Semantic Scholar supplies references and citations, since OpenAlex has
no reference lists for most of these arXiv preprints.

Pool papers are marked source="seed", so the pilot can select either
from the pool only or from the expanded pool. Output matches
build_graphs.py: data/graphs_ds/<arxiv_id>.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import os
import sys
import time
from collections import Counter

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from build_graphs import arxiv_core, is_query_version, norm_title, title_matcher  # noqa: E402
from pool_edges_s2 import s2_batch  # noqa: E402

META = "paperId,title,abstract,year,publicationDate,citationCount,externalIds,references.paperId"


def batch(ids, fields, chunk):
    out = []
    for k in range(0, len(ids), chunk):
        out.extend(s2_batch(ids[k:k + chunk], fields))
        time.sleep(1.5)
    return out


def before(p, cutoff: dt.date) -> bool:
    d = p.get("publicationDate")
    if d:
        try:
            return dt.date.fromisoformat(d[:10]) < cutoff
        except ValueError:
            pass
    y = p.get("year")
    return y is not None and int(y) < cutoff.year


def build(q, pool, cit_rows, imp_keys, args):
    t_q = dt.date.fromisoformat(str(q["published_date"])[:10])
    ax = list(dict.fromkeys(a for a in pool.arxiv_id_from_url.map(arxiv_core) if a))
    snippet = {arxiv_core(a): s for a, s in zip(pool.arxiv_id_from_url, pool.snippet)
               if isinstance(s, str) and arxiv_core(a)}
    seeds = [d for d in batch([f"ARXIV:{a}" for a in ax], META, 100) if d]
    seed_ids = [d["paperId"] for d in seeds]
    q_norm = norm_title(q["title"])

    ref_count = Counter(r["paperId"] for d in seeds for r in (d.get("references") or [])
                        if r.get("paperId"))
    cite_count = Counter()
    for d in batch(seed_ids, "citations.paperId,citations.publicationDate,citations.year", 20):
        for c in (d or {}).get("citations") or []:
            if c.get("paperId") and before(c, t_q):
                cite_count[c["paperId"]] += 1
    for s in seed_ids:
        ref_count.pop(s, None); cite_count.pop(s, None)

    extra = [p for p, _ in ref_count.most_common(args.n_refs)]
    extra += [p for p, _ in cite_count.most_common() if p not in extra][:args.n_citers]
    meta = {d["paperId"]: d for d in seeds}
    meta.update({d["paperId"]: d for d in batch(extra, META, 100) if d})

    nodes, index = [], {}
    for pid in seed_ids + extra:
        d = meta.get(pid)
        if d is None or pid in index or not d.get("title") or is_query_version(d["title"], q_norm):
            continue
        is_seed = pid in seed_ids
        if not is_seed and not before(d, t_q):
            continue
        a = arxiv_core((d.get("externalIds") or {}).get("ArXiv", ""))
        index[pid] = len(nodes)
        nodes.append({"s2_id": pid, "title": d["title"], "arxiv_id": a,
                      "abstract": d.get("abstract") or (snippet.get(a, "") if a else ""),
                      "publication_date": d.get("publicationDate"),
                      "cited_by_count": d.get("citationCount") or 0,
                      "source": "seed" if is_seed else ("ref" if pid in ref_count else "citer"),
                      "_refs": [r["paperId"] for r in (d.get("references") or []) if r.get("paperId")]})

    # pool papers Semantic Scholar does not know stay in as candidates without
    # citation links (text from the pool file), so the candidates are the whole pool
    present_ax = {nd["arxiv_id"] for nd in nodes if nd["arxiv_id"]}
    present_t = {norm_title(nd["title"]) for nd in nodes}
    n_unresolved = 0
    for _, row in pool.iterrows():
        a = arxiv_core(row.arxiv_id_from_url)
        title = row.title if isinstance(row.title, str) else ""
        if (not title or (a and a in present_ax) or norm_title(title) in present_t
                or is_query_version(title, q_norm)):
            continue
        present_t.add(norm_title(title))
        if a:
            present_ax.add(a)
        n_unresolved += 1
        nodes.append({"s2_id": None, "title": title, "arxiv_id": a,
                      "abstract": row.snippet if isinstance(row.snippet, str) else "",
                      "publication_date": str(row.date)[:10] if isinstance(row.date, str) else None,
                      "cited_by_count": 0, "source": "seed", "_refs": []})

    edges = sorted({(k, index[r]) for k, nd in enumerate(nodes) for r in nd.pop("_refs")
                    if r in index and index[r] != k})

    gt_ax = {arxiv_core(l): key for key, l in zip(cit_rows.citation_shorthand,
                                                   cit_rows.cited_paper_arxiv_link) if arxiv_core(l)}
    gt_titles = {norm_title(t): key for key, t in zip(cit_rows.citation_shorthand,
                                                      cit_rows.cited_paper_title)}
    match = title_matcher(gt_titles)
    node_keys = {}
    for k, nd in enumerate(nodes):
        key = gt_ax.get(nd["arxiv_id"]) if nd["arxiv_id"] else None
        if key is None:
            t = match(nd["title"])
            key = gt_titles[t] if t else None
        if key is not None:
            node_keys[k] = key
    in_pool = sorted(node_keys)
    return {
        "arxiv_id": arxiv_core(q["arxiv_id"]), "status": "ok",
        "query": {"title": q["title"], "abstract": q.get("abstract", ""),
                  "published_date": t_q.isoformat()},
        "nodes": nodes, "edges": edges,
        "gt": {"n_cited_in_related_work": int(cit_rows.citation_shorthand.nunique()),
               "n_important": len(imp_keys), "important_keys": sorted(imp_keys),
               "in_pool": in_pool,
               "important_in_pool": [k for k in in_pool if node_keys[k] in imp_keys],
               "node_keys": {str(k): v for k, v in node_keys.items()},
               "n_in_seed_pool": len({node_keys[k] for k in in_pool if nodes[k]["source"] == "seed"}),
               "n_in_pool": len(set(node_keys.values()))},
        "stats": {"n_nodes": len(nodes), "n_edges": len(edges),
                  "n_seeds": sum(nd["source"] == "seed" for nd in nodes),
                  "n_pool_without_s2": n_unresolved,
                  "n_refs": sum(nd["source"] == "ref" for nd in nodes),
                  "n_citers": sum(nd["source"] == "citer" for nd in nodes),
                  "frac_with_abstract": sum(bool(nd["abstract"]) for nd in nodes) / max(len(nodes), 1)},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pools", default="data/ds_pools_pilot/pools/qwen3-8b-awq_k50")
    ap.add_argument("--dataset_dir", default="data/deepscholar_bench")
    ap.add_argument("--out", default="data/graphs_ds")
    ap.add_argument("--n_refs", type=int, default=250)
    ap.add_argument("--n_citers", type=int, default=130)
    ap.add_argument("--passes", type=int, default=3)
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    papers = pd.read_csv(os.path.join(args.dataset_dir, "papers.csv"))
    abstracts = dict(zip(papers.arxiv_id, papers.abstract))
    cits = pd.read_csv(os.path.join(args.dataset_dir, "citations.csv"))
    imp = pd.read_csv(os.path.join(args.dataset_dir, "important_citations.csv"))
    # a query that fails (e.g. Semantic Scholar rate limits outlasting the
    # retries) is skipped and retried in the next pass
    for attempt in range(args.passes):
        failed = []
        for qdir in sorted(glob.glob(os.path.join(args.pools, "*/"))):
            with open(os.path.join(qdir, "query.json")) as f:
                q = json.load(f)
            q["abstract"] = abstracts.get(q["arxiv_id"], "")
            path = os.path.join(args.out, f"{arxiv_core(q['arxiv_id'])}.json")
            if os.path.isfile(path):
                continue
            # read IDs as text: as numbers, 2411.16260 would become 2411.1626
            pool = pd.read_csv(os.path.join(qdir, "pool_all.csv"), dtype={"arxiv_id_from_url": str})
            rows = cits[cits.parent_paper_arxiv_id == q["arxiv_id"]]
            imp_keys = set(imp[imp.parent_paper_arxiv_id == q["arxiv_id"]].citation_shorthand)
            try:
                g = build(q, pool, rows, imp_keys, args)
            except RuntimeError as e:
                failed.append(q["arxiv_id"])
                print(f"{q['arxiv_id']}: failed ({e}); will retry", flush=True)
                continue
            with open(path + ".tmp", "w") as f:  # rename so readers never see a partial file
                json.dump(g, f)
            os.replace(path + ".tmp", path)
            st, gt = g["stats"], g["gt"]
            print(f"{g['arxiv_id']}: {st['n_nodes']} nodes ({st['n_seeds']} pool, {st['n_refs']} refs, "
                  f"{st['n_citers']} citers), {st['n_edges']} edges, refs found "
                  f"{gt['n_in_seed_pool']} in pool / {gt['n_in_pool']} expanded of "
                  f"{gt['n_cited_in_related_work']}", flush=True)
        if not failed:
            break
        print(f"pass {attempt + 1}: {len(failed)} queries failed", flush=True)


if __name__ == "__main__":
    main()
