"""
DeepScholar-base's writer (intro -> taxonomize -> insights -> final report) on a
fixed list of papers per query, for every method's selection list, with the
same backbone, prompts, sampling and seed for all methods. Search and filter
are skipped: the list is what the filter would have passed.

Inputs: a selection list (export_final.py: query, rank, arxiv_id, s2_id, url,
title, abstract, date, in_pool, source) or DeepScholar-base's own kept lists
(outputs/<seed>/<query>/kept.csv). The task prompt is DeepScholar-base's own,
from outputs/<seed>/<query>/query.json, so every method answers the same query.
The search "background" DeepScholar-base feeds its intro is not stored, so it
is empty for every method, including the rerun of DeepScholar-base's own list.

Outputs, per method: <out>/<method>/<row>/final_report.md, intro.md (the
report up to "## Research papers", the judge's input), paper.csv (id, title,
url, snippet of the papers the report links to) and stats.json.
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import glob
import json
import os
import re
import sys
import time

import pandas as pd

sys.path.insert(0, "/home/eftychia/Spectra/deepscholar-bench")
LINK = re.compile(r"\[([^\]]+?)\]\((https?://[^\)]+)\)")


def clean(s):
    # Mateo's fix: LaTeX braces in abstracts crash LOTUS's prompt formatting
    return (s if isinstance(s, str) else "").replace("{", "(").replace("}", ")")


def debrace(df):
    """The same for every text column, including what the model wrote (intro,
    categories, insights): LOTUS reads {word} in any prompt as a column name."""
    for c in df.columns:
        if df[c].dtype == object:
            df[c] = df[c].map(lambda v: clean(v) if isinstance(v, str) else v)
    return df


def load_lists(args):
    """{query folder name: DataFrame(title, url, snippet, date)}"""
    lists = {}
    if args.selections:
        df = pd.read_csv(args.selections, dtype=str).fillna("")
        for name, g in df.groupby("query", sort=False):
            g = g.sort_values("rank", key=lambda s: s.astype(int))
            lists[name] = pd.DataFrame({"title": g.title.map(clean), "url": g.url,
                                        "snippet": g.abstract.map(clean), "date": g.date, "s2_id": g.s2_id})
    else:  # DeepScholar-base's own kept lists; abstracts from the frozen pool
        for qdir in sorted(glob.glob(os.path.join(args.outputs, "*/"))):
            name = os.path.basename(os.path.normpath(qdir))
            kept = pd.read_csv(qdir + "kept.csv", dtype=str).fillna("")
            pool = pd.read_csv(os.path.join(args.pools, name, "pool_all.csv"), dtype=str).fillna("")
            snip = dict(zip(pool.arxiv_id_from_url, pool.snippet))
            lists[name] = pd.DataFrame({"title": kept.title.map(clean), "url": kept.url,
                                        "snippet": kept.arxiv_id.map(lambda a: clean(snip.get(a, ""))),
                                        "date": kept.date})
    return lists


def mode_categories(name, docs, args, configs):
    """E18: categories from the fitted modes instead of the writer's own taxonomy.
    Each listed paper goes to its dominant cited-role mode, argmax_k p_k r_i V_ik^2
    on the eta = 0 fit (the per-mode quantity F(S) is built from); groups of one
    paper and papers outside the graph go to "Others". The LLM only names each
    group from its papers' titles. Returns the category of each row."""
    import numpy as np
    sys.path.insert(0, "/home/eftychia/Spectra/d-spectra/scripts")
    from build_graphs import arxiv_core
    from pilot_selection import relevance
    aid = re.search(r"(\d{4}\.\d{4,5})", name).group(1)
    g = json.load(open(os.path.join(args.graphs, f"{aid}.json")))
    z = np.load(os.path.join(args.emb_dir, f"{aid}.npz"))
    r = relevance(z["query"], z["nodes"])
    zf = np.load(os.path.join(args.operators, f"{aid}_full.npz"))
    V, p = zf["eta0_V"], zf["eta0_p"]
    by_ax = {nd["arxiv_id"]: k for k, nd in enumerate(g["nodes"]) if nd.get("arxiv_id")}
    by_s2 = {nd["s2_id"]: k for k, nd in enumerate(g["nodes"]) if nd.get("s2_id")}
    node = []
    for _, row in docs.iterrows():
        m = re.search(r"arxiv\.org/abs/([^)\s]+)", row["url"] or "")
        k = by_ax.get(arxiv_core(m.group(1))) if m else None
        if k is None and row.get("s2_id"):
            k = by_s2.get(row["s2_id"])
        node.append(k)
    mode = [int(np.argmax(p * r[k] * V[k] ** 2)) if k is not None else -1 for k in node]
    counts = {}
    for m in mode:
        counts[m] = counts.get(m, 0) + 1
    groups = sorted({m for m in mode if m >= 0 and counts[m] >= 2}, key=lambda m: -counts[m])
    names = {}
    for m in groups:
        titles = "\n".join(f"- {t}" for t, mm in zip(docs.title, mode) if mm == m)
        out = configs.taxonomize_lm.get_completion(
            "You name a group of related research papers. Reply with a short category title only (at most 8 words), no punctuation.",
            f"Papers:\n{titles}\n\nCategory title:")
        names[m] = clean(str(out).strip().split("\n")[0])[:80] or f"Group {m + 1}"
    return [names.get(m, "Others") for m in mode], {names[m]: int(counts[m]) for m in groups}


async def write_one(name, docs, args, configs):
    from deepscholar_base.final_generation import generate_final_report, generate_insights, generate_intro_section
    from deepscholar_base.taxonomize import categorize_references
    from deepscholar_base.utils.summary_generation import generate_category_summary_with_citations
    q = json.load(open(os.path.join(args.outputs, name, "query.json")))
    row = str(int(name.split("_")[0]))
    out = os.path.join(args.out, row)
    if os.path.isfile(os.path.join(out, "final_report.md")):
        return "skipped"
    docs = docs.copy()
    docs["query"] = ""
    docs["context"] = docs.apply(lambda r: f"{r['title']}[{r['url']}]: {r['snippet']}", axis=1)
    t0 = time.time()
    topic = clean(q["query"])
    intro = clean(await generate_intro_section(topic, docs, "", configs))
    groups = None
    if args.mode_taxonomy:
        docs["category"], groups = mode_categories(name, docs, args, configs)
        cats = await generate_category_summary_with_citations(docs, topic, configs.taxonomize_lm)
    else:
        docs, cats = await categorize_references(topic, intro, docs, configs)
    docs = debrace(docs)
    cats = debrace(cats) if cats is not None else None
    docs = debrace(await generate_insights(docs, configs))
    report = await generate_final_report(docs, cats, intro, configs)
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "final_report.md"), "w", encoding="utf-8").write(report)
    open(os.path.join(out, "intro.md"), "w", encoding="utf-8").write(report.split("\n## Research papers")[0].strip() + "\n")
    by_url = {u.strip(): (t, s) for t, u, s in zip(docs.title, docs.url, docs.snippet)}
    papers = {}
    for _, url in LINK.findall(report):
        u = url.strip()
        if u in by_url and u not in papers:
            m = re.search(r"arxiv\.org/abs/([^)\s]+)", u)
            papers[u] = {"id": m.group(1) if m else u, "title": by_url[u][0], "url": u, "snippet": by_url[u][1]}
    with open(os.path.join(out, "paper.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "title", "url", "snippet"])
        w.writeheader()
        w.writerows(papers.values())
    usage = {k: getattr(getattr(configs, k).stats, "virtual_usage", None) for k in ("taxonomize_lm", "generation_lm")}
    json.dump({"query": name, "n_papers": int(len(docs)), "n_linked": len(papers), "seconds": time.time() - t0,
               "usage": str(usage), "mode_groups": groups}, open(os.path.join(out, "stats.json"), "w"), indent=1)
    return f"{len(docs)} papers, {len(papers)} linked, {time.time() - t0:.0f}s"


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selections", default=None, help="a method's list (export_final.py); omit for DeepScholar-base's kept lists")
    ap.add_argument("--outputs", required=True, help="DeepScholar-base outputs for the seed (query.json, kept.csv)")
    ap.add_argument("--pools", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--api_base", default="http://127.0.0.1:18013/v1")
    ap.add_argument("--model", default="hosted_vllm/qwen3-8b-awq")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--only", nargs="*", default=None, help="query folder names to run")
    ap.add_argument("--mode_taxonomy", action="store_true", help="E18: categories from the fitted modes")
    ap.add_argument("--graphs", default="/home/eftychia/Spectra/d-spectra/data/graphs_small")
    ap.add_argument("--emb_dir", default="/home/eftychia/Spectra/d-spectra/data/embeddings_small")
    ap.add_argument("--operators", default="/home/eftychia/Spectra/d-spectra/results/e8_small/operators")
    args = ap.parse_args()
    from lotus.models import LM
    from deepscholar_base.configs import Configs
    def stage_lm():
        # every stage LM is built explicitly: Configs derives them from `lm` after dropping its
        # max_completion_tokens, which silently caps each call at LOTUS's default of 512 tokens
        # (the upstream bug Mateo's wrapper fixes; our Nov 2-6 writer runs had it, see bug 5)
        return LM(model=args.model, api_base=args.api_base, api_key="local", temperature=0.7, top_p=0.8,
                  max_tokens=10000, seed=args.seed, max_ctx_len=32768,
                  extra_body={"top_k": 20, "chat_template_kwargs": {"enable_thinking": False}})
    configs = Configs(lm=stage_lm(), filter_lm=stage_lm(), search_lm=stage_lm(), taxonomize_lm=stage_lm(),
                      generation_lm=stage_lm(), categorize_references=True, generate_category_summary=True,
                      generate_insights=True, use_structured_output=True)
    for k in ("filter_lm", "search_lm", "taxonomize_lm", "generation_lm"):
        assert getattr(configs, k).max_tokens == 10000, (k, getattr(configs, k).max_tokens)
    lists = load_lists(args)
    for name, docs in lists.items():
        if args.only and name not in args.only:
            continue
        try:
            msg = await write_one(name, docs, args, configs)
        except Exception as e:  # noqa: BLE001
            msg = f"FAILED: {type(e).__name__}: {str(e)[:200]}"
        print(f"{name}: {msg}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
