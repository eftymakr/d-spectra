"""
E24 (d-spectra/rules/e24_llm_filter_rules.md): DeepScholar-base's own filter stage (sem_filter +
sem_topk, upstream code and prompts) over a query's pool nodes or over all nodes of its expanded
citation graph, with the writer's backbone and sampling. Resumable: skips queries with a kept.csv.

  qwen-env/bin/python run_filter.py --arm pool|expanded --out <dir> [--only <folder> ...] [--rows 20 62]
Outputs <out>/<query folder>/kept.csv (rank, node, arxiv_id, s2_id, title, url, date, source) and stats.json.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import time

import pandas as pd

sys.path.insert(0, "/home/eftychia/Spectra/deepscholar-bench")
R = "/home/eftychia/Spectra/d-spectra"


def clean(s):
    return (s if isinstance(s, str) else "").replace("{", "(").replace("}", ")")


def url_of(arxiv_id, s2_id):
    if arxiv_id:
        return f"http://arxiv.org/abs/{arxiv_id}"
    return f"https://www.semanticscholar.org/paper/{s2_id}" if s2_id else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", choices=["pool", "expanded"], required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--outputs", default=f"{R}/outputs/dsbase_final/s0")
    ap.add_argument("--graphs", default=f"{R}/data/graphs_small")
    ap.add_argument("--api_base", default="http://127.0.0.1:18013/v1")
    ap.add_argument("--model", default="hosted_vllm/qwen3-8b-awq")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--rows", type=int, nargs=2, default=None, help="first and last query row (inclusive)")
    ap.add_argument("--only", nargs="*", default=None)
    args = ap.parse_args()
    from lotus.models import LM
    from deepscholar_base.configs import Configs
    from deepscholar_base.filter import filter as ds_filter

    for qdir in sorted(glob.glob(os.path.join(args.outputs, "*/"))):
        name = os.path.basename(os.path.normpath(qdir))
        row = int(name.split("_")[0])
        if (args.only and name not in args.only) or (args.rows and not args.rows[0] <= row <= args.rows[1]):
            continue
        out = os.path.join(args.out, name)
        if os.path.isfile(os.path.join(out, "kept.csv")):
            continue
        aid = re.search(r"(\d{4}\.\d{4,5})", name).group(1)
        gpath = f"{args.graphs}/{aid}.json"
        if not os.path.isfile(gpath):
            print(f"{name}: no graph", flush=True)
            continue
        g = json.load(open(gpath))
        topic = json.load(open(os.path.join(qdir, "query.json")))["query"]
        rows = []
        for k, nd in enumerate(g["nodes"]):
            if args.arm == "pool" and nd["source"] != "seed":
                continue
            ax, s2 = nd.get("arxiv_id") or "", nd.get("s2_id") or ""
            rows.append({"node": k, "arxiv_id": ax, "s2_id": s2, "title": clean(nd["title"]), "url": url_of(ax, s2),
                         "snippet": clean(nd.get("abstract") or ""), "date": nd.get("publication_date") or "",
                         "source": nd["source"]})
        docs = pd.DataFrame(rows)
        def stage_lm():  # explicit stage LMs: deriving them from `lm` caps every call at 512 tokens
            return LM(model=args.model, api_base=args.api_base, api_key="local", temperature=0.7, top_p=0.8,
                      max_tokens=10000, seed=args.seed, max_ctx_len=32768,
                      extra_body={"top_k": 20, "chat_template_kwargs": {"enable_thinking": False}})
        configs = Configs(lm=stage_lm(), filter_lm=stage_lm(), search_lm=stage_lm(), taxonomize_lm=stage_lm(),
                          generation_lm=stage_lm())
        assert configs.filter_lm.max_tokens == 10000, configs.filter_lm.max_tokens
        t0 = time.time()
        try:
            res = ds_filter(configs, docs, clean(topic))
        except Exception as e:  # noqa: BLE001
            print(f"{name}: FAILED {type(e).__name__}: {str(e)[:300]}", flush=True)
            continue
        st = configs.filter_lm.stats
        usage = {}
        for kind in ("physical_usage", "virtual_usage"):
            u = getattr(st, kind, None)
            usage[kind] = {a: getattr(u, a, None) for a in ("prompt_tokens", "completion_tokens", "total_tokens")} if u is not None else None
        os.makedirs(out, exist_ok=True)
        keep = res.reset_index(drop=True)
        keep.insert(0, "rank", range(1, len(keep) + 1))
        json.dump({"query": name, "arm": args.arm, "n_candidates": int(len(docs)), "n_kept": int(len(keep)),
                   "seconds": time.time() - t0, "usage": usage, "usage_str": str(st)[:600],
                   "columns": list(res.columns)}, open(os.path.join(out, "stats.json"), "w"), indent=1)
        keep[["rank", "node", "arxiv_id", "s2_id", "title", "url", "date", "source"]].to_csv(os.path.join(out, "kept.csv"), index=False)
        print(f"{name}: {len(docs)} candidates -> {len(keep)} kept, {time.time() - t0:.0f}s, {usage.get('physical_usage')}", flush=True)


if __name__ == "__main__":
    main()
