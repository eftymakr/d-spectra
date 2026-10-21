"""
Build the local directed citation graph for each DeepScholar-Bench query
from OpenAlex.

For query paper q (published on date t_q, cutoff = t_q - 1 day):
  1. Seeds: OpenAlex relevance search restricted to works published by
     the cutoff, with up to five queries (the title, the title after an
     "Acronym:" prefix, and the most frequent two-word phrases of the
     title and abstract), results interleaved by rank. This is an
     LLM-free stand-in for DeepScholar-base's initial search; q itself
     is excluded.
  2. Expansion: references of the seeds ranked by how many seeds cite
     them, and works citing the top seeds by the cutoff, ranked the same
     way (ties broken by citation count).
  3. Edges: A_ij = 1 if pool work i cites pool work j. Duplicate records
     of one paper (e.g. arXiv and venue versions) are merged by title.
  4. Ground truth: references cited in q's related-work section
     (DeepScholar-Bench citations.csv). Each is resolved to OpenAlex by
     DOI or arXiv DOI where it has one (accepted only if the titles
     agree, since OpenAlex occasionally attaches a DOI to the wrong
     record) and matched to pool works by id/DOI first, by normalised
     title otherwise. Match rates are recorded; the benchmark's
     "important" subset is kept too.

Output: data/graphs/<arxiv_id>.json, one file per query.
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import os
import re
import sys
from collections import Counter

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from dspectra.openalex import OpenAlexClient, abstract_text, bare_doi, short_id  # noqa: E402


STOPWORDS = set("""a an the of for and or in on to with by from via at as is are be been
we our this that these those it its their can new novel using use used based toward towards
into over under than such while which when where how also both each more most between across
approach approaches method methods framework model models paper propose proposed show shows
results study task tasks work existing""".split())


def search_queries(title: str, abstract: str, n_phrases: int = 3):
    def bigrams(text):
        w = re.findall(r"[a-z][a-z0-9\-]+", str(text).lower())
        return [f"{a} {b}" for a, b in zip(w, w[1:])
                if a not in STOPWORDS and b not in STOPWORDS and len(a) > 2 and len(b) > 2]
    counts = Counter(bigrams(abstract))
    for bg in bigrams(title):
        counts[bg] += 2
    queries = [title]
    if ":" in title:
        queries.append(title.split(":", 1)[1].strip())
    queries += [bg for bg, _ in counts.most_common(n_phrases)]
    return list(dict.fromkeys(q for q in queries if q))


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(t).lower()).strip()


def arxiv_core(s) -> str:
    m = re.search(r"(\d{4}\.\d{4,5})", str(s))
    return m.group(1) if m else ""


def titles_agree(a: str, b: str, cutoff: float = 0.6) -> bool:
    return difflib.SequenceMatcher(None, norm_title(a), norm_title(b)).ratio() >= cutoff


def resolve_ground_truth(oa: OpenAlexClient, cit_rows):
    """Map each related-work citation to the DOIs and OpenAlex ids it is
    known by. A DOI counts only if the OpenAlex record behind it has an
    agreeing title."""
    wanted = {}
    for key, title, doi, link in zip(cit_rows.citation_shorthand, cit_rows.cited_paper_title,
                                     cit_rows.bib_paper_doi, cit_rows.cited_paper_arxiv_link):
        dois = [d for d in (bare_doi(doi),) if d]
        ax = arxiv_core(link)
        if ax:
            dois.append(f"10.48550/arxiv.{ax}")
        wanted[key] = (title, dois)
    records = {bare_doi(w.get("doi")): w for w in
               oa.by_dois([d for _, ds in wanted.values() for d in ds])}
    resolved = {}
    for key, (title, dois) in wanted.items():
        ids, good_dois = set(), set()
        for d in dois:
            w = records.get(d)
            if w is not None and titles_agree(w.get("title") or "", title):
                ids.add(short_id(w["id"]))
                good_dois.add(d)
        resolved[key] = {"title": title, "has_identifier": bool(dois),
                         "ids": ids, "dois": good_dois}
    return resolved


def title_matcher(gt_titles):
    keys = list(gt_titles)

    def match(title):
        t = norm_title(title)
        if not t:
            return None
        if t in gt_titles:
            return t
        close = difflib.get_close_matches(t, keys, n=1, cutoff=0.9)
        return close[0] if close else None
    return match


def build_one(oa: OpenAlexClient, q, cit_rows, imp_keys, args):
    aid = arxiv_core(q["arxiv_id"])
    t_q = dt.date.fromisoformat(str(q["published_date"])[:10])
    cutoff = (t_q - dt.timedelta(days=1)).isoformat()
    q_norm = norm_title(q["title"])

    def ok(w):
        return (w.get("title") and norm_title(w["title"]) != q_norm
                and (w.get("publication_date") or "9999") <= cutoff)

    queries = search_queries(q["title"], q["abstract"])
    result_lists = [[w for w in oa.search(s, cutoff, per_page=args.n_seeds) if ok(w)]
                    for s in queries]
    seeds, seen = [], set()
    for rank in range(args.n_seeds):
        for res in result_lists:
            if rank < len(res) and len(seeds) < args.n_seeds:
                wid = short_id(res[rank]["id"])
                if wid not in seen:
                    seen.add(wid)
                    seeds.append(res[rank])
    seed_ids = [short_id(w["id"]) for w in seeds]

    ref_count = Counter(short_id(r) for w in seeds for r in (w.get("referenced_works") or []))
    for s in seed_ids:
        ref_count.pop(s, None)
    ref_meta = {short_id(w["id"]): w for w in oa.works(list(ref_count)) if ok(w)}
    refs_ranked = sorted(ref_meta, key=lambda i: (-ref_count[i], -ref_meta[i]["cited_by_count"]))

    cite_count, cite_cc = Counter(), {}
    top_seeds = sorted(seeds, key=lambda w: -w["cited_by_count"])
    for w in top_seeds[:args.n_citing_seeds]:
        for c in oa.citing(w["id"], cutoff, select="id,publication_date,cited_by_count"):
            cid = short_id(c["id"])
            if cid not in seed_ids:
                cite_count[cid] += 1
                cite_cc[cid] = c.get("cited_by_count") or 0
    citers_ranked = sorted(cite_count, key=lambda i: (-cite_count[i], -cite_cc[i]))

    pool = list(seed_ids)
    pool += [i for i in refs_ranked if i not in pool][:args.n_refs]
    pool += [i for i in citers_ranked if i not in pool][:args.n_citers]
    pool = pool[:args.max_nodes]

    meta = {short_id(w["id"]): w for w in seeds}
    meta.update(ref_meta)
    missing = [i for i in pool if i not in meta]
    meta.update({short_id(w["id"]): w for w in oa.works(missing)})

    # merge duplicate records of the same paper by normalised title
    nodes, by_title, alias = [], {}, {}
    for pid in pool:
        w = meta.get(pid)
        if w is None or not ok(w):
            continue
        t = norm_title(w["title"])
        if t in by_title:
            k = by_title[t]
            alias[pid] = k
            nodes[k]["_refs"] |= {short_id(r) for r in (w.get("referenced_works") or [])}
            nodes[k]["openalex_ids"].append(pid)
            if bare_doi(w.get("doi")):
                nodes[k]["dois"].append(bare_doi(w.get("doi")))
            continue
        k = len(nodes)
        by_title[t] = k
        alias[pid] = k
        nodes.append({
            "openalex_id": pid, "openalex_ids": [pid], "title": w["title"],
            "dois": [bare_doi(w.get("doi"))] if bare_doi(w.get("doi")) else [],
            "abstract": abstract_text(w.get("abstract_inverted_index")),
            "publication_date": w.get("publication_date"),
            "cited_by_count": w.get("cited_by_count") or 0,
            "source": "seed" if pid in seed_ids else ("ref" if pid in ref_meta else "citer"),
            "_refs": {short_id(r) for r in (w.get("referenced_works") or [])},
        })
    edges = set()
    for k, nd in enumerate(nodes):
        refs = nd.pop("_refs")
        nd["n_refs_listed"] = len(refs)
        for r in refs:
            j = alias.get(r)
            if j is not None and j != k:
                edges.add((k, j))

    resolved = resolve_ground_truth(oa, cit_rows)
    id_to_key = {i: key for key, rv in resolved.items() for i in rv["ids"]}
    doi_to_key = {d: key for key, rv in resolved.items() for d in rv["dois"]}
    gt_titles = {norm_title(rv["title"]): key for key, rv in resolved.items()}
    match = title_matcher(gt_titles)
    node_keys, how = {}, {}
    for k, nd in enumerate(nodes):
        key = next((id_to_key[i] for i in nd["openalex_ids"] if i in id_to_key), None)
        if key is None:
            key = next((doi_to_key[d] for d in nd["dois"] if d in doi_to_key), None)
        if key is not None:
            node_keys[k], how[k] = key, "id"
            continue
        t = match(nd["title"])
        if t is not None:
            node_keys[k], how[k] = gt_titles[t], "title"
    keys_by_id = {node_keys[k] for k in node_keys if how[k] == "id"}
    keys_by_title = {node_keys[k] for k in node_keys if how[k] == "title"} - keys_by_id
    # how many id matches title matching alone would also have found
    title_also = {node_keys[k] for k in node_keys if how[k] == "id"
                  and gt_titles.get(match(nodes[k]["title"]) or "") == node_keys[k]}
    gt_in_pool = sorted(node_keys)
    imp_in_pool = [k for k in gt_in_pool if node_keys[k] in imp_keys]

    return {
        "arxiv_id": aid, "status": "ok",
        "query": {"title": q["title"], "abstract": q["abstract"],
                  "published_date": t_q.isoformat(), "search_queries": queries},
        "nodes": nodes, "edges": sorted(edges),
        "gt": {
            "n_cited_in_related_work": len(resolved),
            "n_important": int(len(imp_keys)),
            "important_keys": sorted(imp_keys),
            "in_pool": gt_in_pool, "important_in_pool": imp_in_pool,
            "node_keys": {str(k): v for k, v in node_keys.items()},
            "match": {
                "n_with_identifier": sum(rv["has_identifier"] for rv in resolved.values()),
                "n_resolved_by_id": sum(bool(rv["ids"]) for rv in resolved.values()),
                "n_in_pool": len(keys_by_id | keys_by_title),
                "n_in_pool_by_id": len(keys_by_id),
                "n_in_pool_by_title_only": len(keys_by_title),
                "n_id_matches_also_found_by_title": len(title_also),
            },
        },
        "stats": {
            "n_nodes": len(nodes), "n_edges": len(edges),
            "n_seeds": sum(nd["source"] == "seed" for nd in nodes),
            "n_refs": sum(nd["source"] == "ref" for nd in nodes),
            "n_citers": sum(nd["source"] == "citer" for nd in nodes),
            "frac_nodes_no_listed_refs": float(np.mean([nd["n_refs_listed"] == 0
                                                        for nd in nodes])) if nodes else 0.0,
            "frac_nodes_with_abstract": float(np.mean([bool(nd["abstract"])
                                                       for nd in nodes])) if nodes else 0.0,
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset_dir", default="data/deepscholar_bench",
                    help="DeepScholar-Bench dataset/ directory")
    ap.add_argument("--out", default="data/graphs")
    ap.add_argument("--limit", type=int, default=63)
    ap.add_argument("--order_seed", type=int, default=0)
    ap.add_argument("--n_seeds", type=int, default=50)
    ap.add_argument("--n_refs", type=int, default=300)
    ap.add_argument("--n_citers", type=int, default=150)
    ap.add_argument("--n_citing_seeds", type=int, default=20)
    ap.add_argument("--max_nodes", type=int, default=500)
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    papers = pd.read_csv(os.path.join(args.dataset_dir, "papers.csv"))
    cits = pd.read_csv(os.path.join(args.dataset_dir, "citations.csv"))
    imp = pd.read_csv(os.path.join(args.dataset_dir, "important_citations.csv"))
    order = np.random.default_rng(args.order_seed).permutation(len(papers))[:args.limit]

    oa = OpenAlexClient()
    for k, idx in enumerate(order):
        q = papers.iloc[idx]
        aid = arxiv_core(q["arxiv_id"])
        path = os.path.join(args.out, f"{aid}.json")
        if os.path.isfile(path):
            continue
        rows = cits[cits.parent_paper_arxiv_id == q["arxiv_id"]]
        imp_keys = set(imp[imp.parent_paper_arxiv_id == q["arxiv_id"]].citation_shorthand)
        try:
            g = build_one(oa, q, rows, imp_keys, args)
        except Exception as e:  # keep going; the failure is recorded
            g = {"arxiv_id": aid, "status": f"error: {e}"}
        with open(path, "w") as f:
            json.dump(g, f)
        st = g.get("stats", {}); gt = g.get("gt", {}); mt = gt.get("match", {})
        print(f"[{k + 1}/{len(order)}] {aid} {g['status']} nodes={st.get('n_nodes')} "
              f"edges={st.get('n_edges')} gt={gt.get('n_cited_in_related_work')} "
              f"resolved_by_id={mt.get('n_resolved_by_id')} in_pool={mt.get('n_in_pool')} "
              f"(id={mt.get('n_in_pool_by_id')}, title_only={mt.get('n_in_pool_by_title_only')}) "
              f"requests={oa.n_requests}", flush=True)


if __name__ == "__main__":
    main()
