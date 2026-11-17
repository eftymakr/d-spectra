#!/usr/bin/env python3
"""
write_reports.py - run ONE writer over any selection, so every method is written (and judged) the same way.

For each query it takes:
  - the selection: DeepScholar's kept papers (final.csv, default) or a method's
    <selection-dir>/<query>/selected.csv (rows matched back to pool_all.csv by URL / arXiv ID)
  - the same search background DeepScholar's own writer got (stats.json, from that seed's run)
  - the same topic text (query.json, braces replaced as in the runner)
and runs DeepScholar's own intro writer (generate_intro_section) with the chosen model.

Output is the evaluator's layout: <out>/<dataset row>/intro.md + paper.csv (+ meta.json with
model, number of papers, LLM calls and tokens). Resumable: existing intro.md is kept unless --force.

Examples (from project/):
  # DeepScholar's selection, written by an API model (needs OPENAI_API_KEY loaded)
  python write_reports.py --run runs/final_qwen3-8b-awq_arxiv_k50_r2_s0 --model gpt-4.1-mini \
      --out eval_inputs/writer_gpt41mini/dsbase_s0 --file-id 0 1 2 3 4
  # same selection, written by local Qwen (vLLM must be running)
  python write_reports.py --run runs/final_qwen3-8b-awq_arxiv_k50_r2_s0 --model hosted_vllm/Qwen/Qwen3-8B-AWQ \
      --api-base http://localhost:8100/v1 --no-think --max-ctx 32768 --temperature 0.7 --top-p 0.8 --top-k 20 --seed 0 \
      --out eval_inputs/writer_qwen/dsbase_s0 --file-id 0 1 2 3 4
  # D-SPECTRA's selection, same writer
  python write_reports.py --run runs/final_qwen3-8b-awq_arxiv_k50_r2_s0 --selection-dir d-spectra/outputs/dspectra/s0 \
      --model gpt-4.1-mini --out eval_inputs/writer_gpt41mini/dspectra_s0
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
import time
from pathlib import Path

import pandas as pd

ID_RE = re.compile(r"(\d{4}\.\d{4,5})")


def parse_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--run", required=True, help="seed run folder, e.g. runs/final_..._s0")
    p.add_argument("--selection-dir", default=None,
                   help="DIR/<query>/selected.csv; omit to write DeepScholar's own selection (final.csv)")
    p.add_argument("--papers-dir", default=None,
                   help="DIR/<dataset row>/paper.csv (e.g. Efty's judge/inputs/s0/<system>): use exactly those papers")
    p.add_argument("--out", required=True)
    p.add_argument("--model", required=True, help="e.g. gpt-4.1-mini, or hosted_vllm/Qwen/Qwen3-8B-AWQ")
    p.add_argument("--api-base", default=None, help="vLLM URL for a local model")
    p.add_argument("--max-ctx", type=int, default=None, help="model context length (set 32768 for local Qwen)")
    p.add_argument("--max-tokens", type=int, default=10000)
    p.add_argument("--temperature", type=float, default=0.7)
    p.add_argument("--top-p", type=float, default=None)
    p.add_argument("--top-k", type=int, default=None)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--no-think", action="store_true")
    p.add_argument("--file-id", type=int, nargs="*", default=None, help="dataset rows to write (default all)")
    p.add_argument("--deepscholar-dir", default="deepscholar")
    p.add_argument("--dataset", default=None, help="default <deepscholar-dir>/dataset/papers_with_related_works.csv")
    p.add_argument("--force", action="store_true")
    p.add_argument("--dry-run", action="store_true", help="assemble inputs only, no LLM calls")
    return p.parse_args()


def pick_search_try(stats: dict) -> dict:
    tries = sorted((k for k in stats if k.startswith("search_try_")), key=lambda k: int(k.rsplit("_", 1)[1]))
    chosen = {}
    for k in tries:
        t = stats.get(k) or {}
        if t.get("post_filter_search_results"):
            chosen = t
    return chosen or (stats.get(tries[-1]) or {} if tries else {})


def ids_of(df: pd.DataFrame) -> pd.Series:
    src = df["arxiv_id_from_url"].astype(str) if "arxiv_id_from_url" in df.columns else df["url"].astype(str)
    return src.str.extract(ID_RE, expand=False)


def load_selection(qdir: Path, sel_dir: Path | None) -> tuple[pd.DataFrame, str]:
    if sel_dir is None:
        return pd.read_csv(qdir / "final.csv"), "deepscholar (final.csv)"
    sel = pd.read_csv(sel_dir / qdir.name / "selected.csv")
    pool = pd.read_csv(qdir / "pool_all.csv")
    pool_ids, sel_ids = ids_of(pool), ids_of(sel)
    rows, missing, outside = [], 0, 0
    for i in range(len(sel)):
        r = sel.iloc[i]
        url, aid = str(r.get("url", "")), sel_ids.iloc[i]
        hit = pool[pool["url"].astype(str) == url]
        if hit.empty and isinstance(aid, str):
            hit = pool[pool_ids == aid]
        if not hit.empty:                      # pool paper: same row DeepScholar's writer would see
            rows.append(hit.iloc[0])
        elif str(r.get("title", "")).strip() and str(r.get("snippet", "")).strip() not in ("", "nan"):
            rows.append(pd.Series({"title": r["title"], "url": url, "snippet": r["snippet"],
                                   "date": r.get("date", "")}))   # expanded-graph paper: its own fields
            outside += 1
        else:
            missing += 1
    if outside:
        print(f"  {qdir.name}: {outside} selected papers from outside the pool (own title/abstract used)")
    if missing:
        print(f"  {qdir.name}: {missing} selected papers with no pool match and no abstract (skipped)")
    return pd.DataFrame(rows).reset_index(drop=True), f"{sel_dir}"


async def main():
    args = parse_args()
    ds_dir = Path(args.deepscholar_dir).resolve()
    sys.path.insert(0, str(ds_dir))
    from lotus.models import LM
    from deepscholar_base.configs import Configs
    from deepscholar_base.final_generation import generate_intro_section

    dataset = pd.read_csv(args.dataset or ds_dir / "dataset" / "papers_with_related_works.csv")
    kw = {"temperature": args.temperature, "max_tokens": args.max_tokens}
    if args.api_base:
        kw["api_base"] = args.api_base
    if args.max_ctx:
        kw["max_ctx_len"] = args.max_ctx
    if args.top_p is not None:
        kw["top_p"] = args.top_p
    if args.seed is not None:
        kw["seed"] = args.seed
    body = {}
    if args.no_think:
        body["chat_template_kwargs"] = {"enable_thinking": False}
    if args.top_k is not None:
        body["top_k"] = args.top_k
    if body:
        kw["extra_body"] = body
    writer = LM(model=args.model, **kw)
    # Configs strips the token limit from the `lm` it is given, so pass it a separate object
    # and hand the writer in explicitly as the generation stage.
    configs = Configs(lm=LM(model=args.model, **kw), filter_lm=writer, search_lm=writer,
                      taxonomize_lm=writer, generation_lm=writer, use_agentic_search=False)

    out_root = Path(args.out)
    sel_dir = Path(args.selection_dir) if args.selection_dir else None
    n_done = 0
    for qdir in sorted(p for p in Path(args.run).iterdir() if p.is_dir()):
        m = re.match(r"(\d+)_(.+)$", qdir.name)
        if not m:
            continue
        idx, aid = int(m.group(1)), m.group(2)
        if args.file_id is not None and idx not in args.file_id:
            continue
        if str(dataset.iloc[idx]["arxiv_id"]) != aid:
            print(f"  SKIP {qdir.name}: dataset row {idx} is {dataset.iloc[idx]['arxiv_id']}")
            continue
        dest = out_root / str(idx)
        if (dest / "intro.md").exists() and not args.force:
            continue

        q = json.loads((qdir / "query.json").read_text())
        topic = str(q["query"]).replace("{", "(").replace("}", ")")
        stats = json.loads((qdir / "stats.json").read_text())
        background = pick_search_try(stats).get("search_background") or ""
        try:
            if args.papers_dir:
                pc = Path(args.papers_dir) / str(idx) / "paper.csv"
                docs, source = pd.read_csv(pc), str(pc.parent)
            else:
                docs, source = load_selection(qdir, sel_dir)
        except FileNotFoundError as e:
            print(f"  SKIP {qdir.name}: {e}")
            continue
        if docs.empty:
            print(f"  SKIP {qdir.name}: empty selection")
            continue
        docs = docs.fillna("")
        if "context" not in docs.columns or (docs["context"].astype(str) == "").any():
            docs["context"] = docs.apply(lambda r: f"{r.get('title', '')}[{r.get('url', '')}]: {r.get('snippet', '')}", axis=1)
        docs = docs.drop(columns=[c for c in docs.columns if c.startswith("_")], errors="ignore")

        dest.mkdir(parents=True, exist_ok=True)
        paper = docs.copy()
        paper["id"] = paper["url"].astype(str).str.extract(r"arxiv\.org/abs/([^)\s/]+)", expand=False)
        paper.to_csv(dest / "paper.csv", index=False)
        if args.dry_run:
            print(f"  [dry] {qdir.name}: {len(docs)} papers from {source}, background {len(background)} chars")
            continue

        writer.reset_stats()
        t0 = time.time()
        intro = await generate_intro_section(topic, docs, background, configs)
        (dest / "intro.md").write_text(intro or "")
        u = writer.stats.physical_usage
        (dest / "meta.json").write_text(json.dumps({
            "query": qdir.name, "selection": source, "n_papers": len(docs), "writer": args.model,
            "temperature": args.temperature, "top_p": args.top_p, "top_k": args.top_k, "seed": args.seed,
            "prompt_tokens": u.prompt_tokens, "completion_tokens": u.completion_tokens,
            "n_inline_citations": (intro or "").count("arxiv.org/abs"),
            "seconds": round(time.time() - t0, 1)}, indent=2))
        n_done += 1
        print(f"  [ok] {qdir.name}: {len(docs)} papers -> {(intro or '').count('arxiv.org/abs')} citations, "
              f"{len((intro or '').split())} words")
    print(f"Wrote {n_done} reports to {out_root}/<row>/")


if __name__ == "__main__":
    asyncio.run(main())
