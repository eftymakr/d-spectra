"""
LLM-free pilot of selection-only D-SPECTRA on DeepScholar-Bench graphs.

For each query graph (scripts/build_graphs.py), select B papers with each
method and measure how many of the references the human authors cited in
their related-work section the selection recovers (distinct references,
so duplicate records of one paper count once). No writer LLM or judge is
involved; this is a retrieval-side proxy for the proposal's gate.

Methods (all selecting from the same candidate pool):
  search_only      top-B by relevance among the initial-search seeds (no expansion)
  relevance_only   top-B by relevance over the expanded pool: F(S) with alpha = 1,
                   i.e. the proposal's main ablation (no coverage term), which on
                   the same pool is also the "citation expansion only" baseline
  most_cited       top-B by in-pool in-degree
  dspectra         greedy F(S) on directed SPECTRA modes, d_ev targeted to --target
  dspectra_eta0    same, fitted with eta = 0 (no capacity control)
  dspectra_d<k>    same, other d_ev targets (sensitivity)
  symmetrized      greedy F(S) on undirected SPECTRA fitted to A + A^T
  raw_svd          greedy F(S) on the SVD of A (no fitting)
  usvt             same, keeping only singular values above the universal
                   singular-value threshold
  semantic_modes   greedy F(S) on the SVD of the text-embedding matrix
                   (coverage of text modes, no citation structure)
  vendi            greedy relevance + Vendi score on text embeddings
                   (Vendi-RAG-style diversity, no citation structure)

Hyperparameters are fixed before looking at results: rank cap 32,
target d_ev 8 (sensitivity 4, 16), alpha 0.5, gamma 5.

Stages:
  --embed          bge-m3 embeddings for every graph (one process)
  --fit k/N        fit the model operators for every N-th graph from k (GPU)
  --evaluate       selections and metrics for every graph with saved operators
  --aggregate      tables, paired tests, premise check
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

BUDGETS = [10, 20, 30, 45, 60]
COMPARE = ["relevance_only", "dspectra_eta0", "symmetrized", "raw_svd", "usvt",
           "semantic_modes", "vendi", "search_only", "most_cited"]


def load_graph(path):
    with open(path) as f:
        g = json.load(f)
    if g.get("status") != "ok" or not g["nodes"]:
        return None
    n = len(g["nodes"])
    A = np.zeros((n, n), dtype=np.float32)
    for i, j in g["edges"]:
        A[i, j] = 1.0
    return g, A


def embed_all(graph_files, out_dir, device):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("BAAI/bge-m3", device=device)
    model.max_seq_length = 512
    os.makedirs(out_dir, exist_ok=True)
    for path in graph_files:
        aid = os.path.basename(path)[:-5]
        out = os.path.join(out_dir, f"{aid}.npz")
        if os.path.isfile(out):
            continue
        loaded = load_graph(path)
        if loaded is None:
            continue
        g, _ = loaded
        q = g["query"]["title"] + ". " + g["query"]["abstract"]
        docs = [nd["title"] + ". " + nd["abstract"] for nd in g["nodes"]]
        E = model.encode([q] + docs, batch_size=64, normalize_embeddings=True,
                         show_progress_bar=False)
        np.savez(out, query=E[0], nodes=E[1:])
        print(f"embedded {aid} ({len(docs)} nodes)", flush=True)


def relevance(Eq, En):
    """Cosine to the query rescaled to [0, 1] within the pool (relative to
    the pool, so not comparable across queries)."""
    cos = En @ Eq
    lo, hi = cos.min(), cos.max()
    return (cos - lo) / max(hi - lo, 1e-12)


def svd_modes(M, k, paper_axis, threshold=None):
    """Top-k singular vectors along the paper axis (0 = rows, 1 = columns)
    with occupancy sigma_k / sum(sigma); with `threshold`, only singular
    values above it are kept (at least one)."""
    U, s, Vt = np.linalg.svd(M, full_matrices=False)
    k = min(k, len(s))
    if threshold is not None:
        k = max(1, min(k, int((s > threshold).sum())))
    vecs = U[:, :k] if paper_axis == 0 else Vt[:k].T
    return vecs, s[:k] / s[:k].sum()


def usvt_threshold(A):
    """Universal singular-value threshold (Chatterjee, 2015) for an n x n
    matrix with entries in [0, 1]: (2 + 0.01) * sqrt(n * q), q the
    empirical Bernoulli variance."""
    n = A.shape[0]
    rho = A.sum() / (n * (n - 1))
    return 2.01 * np.sqrt(n * max(rho * (1 - rho), 1.0 / n))


def fit_query(path, args):
    from dspectra.model import FitConfig, diagnostics, fit, fit_to_target, modes
    g, A = load_graph(path)
    cfg = FitConfig(rank=args.rank, epochs=args.epochs, device=args.device)
    arrays, info = {}, {}
    t0 = time.time()

    def keep(name, model, extra):
        md = modes(model)
        arrays[f"{name}_V"], arrays[f"{name}_p"] = md["V"], md["p"]
        info[name] = dict(extra, d_ev=diagnostics(model)["d_ev"])

    res = fit_to_target(A, args.target, "directed", cfg, seed=args.seed)
    keep("dspectra", res.model, {"eta": res.eta, "probes": len(res.probes)})
    keep("dspectra_eta0", fit(A, "directed", 0.0, cfg, seed=args.seed), {"eta": 0.0})
    for t in args.sensitivity:
        rs = fit_to_target(A, t, "directed", cfg, seed=args.seed)
        keep(f"dspectra_d{t:g}", rs.model, {"eta": rs.eta, "probes": len(rs.probes)})
    rsym = fit_to_target(A, args.target, "symmetric", cfg, seed=args.seed)
    keep("symmetrized", rsym.model, {"eta": rsym.eta, "probes": len(rsym.probes)})
    info["_seconds"] = time.time() - t0
    info["_config"] = {"rank": args.rank, "epochs": args.epochs, "target": args.target,
                       "seed": args.seed}
    return arrays, info


def evaluate_query(path, args):
    from dspectra.selection import (embedding_diversity, greedy_select, greedy_vendi,
                                    set_d_ev, top_k)
    g, A = load_graph(path)
    aid = g["arxiv_id"]
    z = np.load(os.path.join(args.emb_dir, f"{aid}.npz"))
    En, Eq = z["nodes"], z["query"]
    n = A.shape[0]
    if En.shape[0] != n:
        raise ValueError(f"{aid}: embeddings have {En.shape[0]} rows but the graph has {n} "
                         f"nodes; recompute them with --embed for this --graphs directory")
    r = relevance(Eq, En)
    ops_dir = args.operators or f"{args.out}/operators"
    ops_npz = np.load(f"{ops_dir}/{aid}.npz")
    with open(f"{ops_dir}/{aid}.json") as f:
        fit_info = json.load(f)

    operators = {name: (ops_npz[f"{name}_V"], ops_npz[f"{name}_p"])
                 for name in fit_info if not name.startswith("_")}
    operators["raw_svd"] = svd_modes(A, args.rank, paper_axis=1)  # columns = cited papers
    operators["usvt"] = svd_modes(A, args.rank, paper_axis=1, threshold=usvt_threshold(A))
    operators["semantic_modes"] = svd_modes(En - En.mean(0), args.rank, paper_axis=0)
    yardstick = operators["dspectra"]

    node_key = {int(k): v for k, v in g["gt"]["node_keys"].items()}
    imp_keys = set(g["gt"]["important_keys"])
    keys_in_pool = set(node_key.values())
    seeds = np.array([k for k, nd in enumerate(g["nodes"]) if nd["source"] == "seed"])
    # --select_from seeds: every method picks only among the search pool (the
    # model is still fitted on the whole expanded graph)
    cand = seeds if args.select_from == "seeds" else None

    vendi_order = greedy_vendi(En, r, max(BUDGETS), args.alpha, candidates=cand)
    selections = {}
    for B in BUDGETS:
        selections[("search_only", B)] = top_k(r, B, candidates=seeds)
        selections[("relevance_only", B)] = top_k(r, B, candidates=cand)
        selections[("most_cited", B)] = top_k(A.sum(0) + 1e-6 * r, B, candidates=cand)
        selections[("vendi", B)] = vendi_order[:B]
        for name, (V, p) in operators.items():
            selections[(name, B)] = greedy_select(V, p, r, B, args.alpha, args.gamma,
                                                  candidates=cand)

    n_gt_all = g["gt"]["n_cited_in_related_work"]
    n_imp_all = g["gt"]["n_important"]
    rows = []
    for (method, B), S in selections.items():
        hit = {node_key[i] for i in S if i in node_key}
        rows.append({
            "arxiv_id": aid, "method": method, "B": B, "size": len(S),
            "hits": len(hit), "recall": len(hit) / max(n_gt_all, 1),
            "recall_reachable": len(hit) / len(keys_in_pool) if keys_in_pool else float("nan"),
            "recall_important": len(hit & imp_keys) / max(n_imp_all, 1),
            "d_ev_S": set_d_ev(*yardstick, r, S),
            "diversity": embedding_diversity(En, S),
            "mean_relevance": float(r[S].mean()) if S else 0.0,
        })

    # premise check: do the human-cited papers spread over more modes than a
    # relevance-ranked set of the same size? (one node per reference)
    premise = None
    first_node = {}
    for k, key in sorted(node_key.items()):
        first_node.setdefault(key, k)
    human = sorted(first_node.values())
    if len(human) >= 3:
        k = len(human)
        premise = {"k": k,
                   "d_ev_human": set_d_ev(*yardstick, r, human),
                   "d_ev_relevance": set_d_ev(*yardstick, r, top_k(r, k)),
                   "d_ev_random_mean": float(np.mean([
                       set_d_ev(*yardstick, r, np.random.default_rng(s).choice(n, k, replace=False))
                       for s in range(20)]))}
    return {"arxiv_id": aid, "n_nodes": n, "n_edges": int(A.sum()),
            "n_gt_in_pool": len(keys_in_pool), "n_gt_all": n_gt_all, "fit": fit_info,
            "premise": premise, "rows": rows,
            "selections": {f"{m}@{B}": [int(i) for i in S] for (m, B), S in selections.items()}}


def aggregate(out_dir):
    import pandas as pd
    from scipy.stats import spearmanr, wilcoxon
    per_q = [json.load(open(f)) for f in sorted(glob.glob(f"{out_dir}/per_query/*.json"))]
    df = pd.DataFrame([row for q in per_q for row in q["rows"]])
    reach_ids = [q["arxiv_id"] for q in per_q if q["n_gt_in_pool"] > 0]
    reach = df[df.arxiv_id.isin(reach_ids)]
    tables = {v: reach.pivot_table(index="method", columns="B", values=v, aggfunc="mean")
              for v in ["recall", "recall_important", "recall_reachable", "d_ev_S",
                        "diversity", "mean_relevance"]}
    tests = []
    for other in COMPARE:
        for B in BUDGETS:
            a = reach[(reach.method == "dspectra") & (reach.B == B)].set_index("arxiv_id").recall
            b = reach[(reach.method == other) & (reach.B == B)].set_index("arxiv_id").recall
            a, b = a.align(b, join="inner")
            diff = a - b
            p = wilcoxon(a, b).pvalue if (diff != 0).any() else 1.0
            tests.append({"vs": other, "B": B, "n": len(a), "mean_diff": diff.mean(),
                          "wins": int((diff > 0).sum()), "losses": int((diff < 0).sum()),
                          "p_wilcoxon": p})
    tests = pd.DataFrame(tests)

    prem = pd.DataFrame([q["premise"] for q in per_q if q["premise"]])
    prem_test = None
    if len(prem) >= 5:
        prem_test = {
            "n_queries": len(prem),
            "mean_d_ev_human": prem.d_ev_human.mean(),
            "mean_d_ev_relevance": prem.d_ev_relevance.mean(),
            "mean_d_ev_random": prem.d_ev_random_mean.mean(),
            "human_gt_relevance": int((prem.d_ev_human > prem.d_ev_relevance).sum()),
            "p_human_vs_relevance": wilcoxon(prem.d_ev_human, prem.d_ev_relevance).pvalue,
        }

    # does recall track the set's occupancy beyond its size? (within-query
    # Spearman over all method x budget cells)
    track = []
    for _, d in reach.groupby("arxiv_id"):
        if d.recall.nunique() > 1:
            track.append({"rho_d_ev": spearmanr(d.d_ev_S, d.recall)[0],
                          "rho_size": spearmanr(d["size"], d.recall)[0]})
    track = pd.DataFrame(track)

    fit_names = [k for k in per_q[0]["fit"] if not k.startswith("_")]
    summary = {
        "n_queries": len(per_q),
        "n_queries_with_gt_in_pool": len(reach_ids),
        "pool": {
            "mean_nodes": float(np.mean([q["n_nodes"] for q in per_q])),
            "mean_edges": float(np.mean([q["n_edges"] for q in per_q])),
            "pooled_gt_reachable_frac": float(sum(q["n_gt_in_pool"] for q in per_q)
                                              / sum(q["n_gt_all"] for q in per_q)),
        },
        "fit": {name: {"mean_d_ev": float(np.mean([q["fit"][name]["d_ev"] for q in per_q])),
                       "mean_eta": float(np.mean([q["fit"][name]["eta"] for q in per_q]))}
                for name in fit_names},
        "mean_fit_seconds": float(np.mean([q["fit"]["_seconds"] for q in per_q])),
        "premise": prem_test,
        "recall_tracks": {"mean_rho_d_ev": float(track.rho_d_ev.mean()),
                          "mean_rho_size": float(track.rho_size.mean()),
                          "n": len(track)} if len(track) else None,
    }
    for name, tab in tables.items():
        tab.round(4).to_csv(f"{out_dir}/{name}.csv")
    tests.round(4).to_csv(f"{out_dir}/tests_vs_dspectra.csv", index=False)
    df.to_csv(f"{out_dir}/all_rows.csv", index=False)
    with open(f"{out_dir}/summary.json", "w") as f:
        json.dump(summary, f, indent=2, default=float)
    pd.set_option("display.width", 200)
    print("recall of related-work citations (mean over queries):\n", tables["recall"].round(3))
    print("\nrecall of important citations:\n", tables["recall_important"].round(3))
    print("\nd_ev(S):\n", tables["d_ev_S"].round(2))
    print("\nD-SPECTRA vs others (paired Wilcoxon on recall):\n", tests.round(3).to_string())
    print(json.dumps(summary, indent=2, default=float))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graphs", default="data/graphs_v2")
    ap.add_argument("--emb_dir", default="data/embeddings_v2")
    ap.add_argument("--out", default="results/pilot")
    ap.add_argument("--embed", action="store_true")
    ap.add_argument("--fit", default=None, help="k/N shard of graphs to fit")
    ap.add_argument("--evaluate", action="store_true")
    ap.add_argument("--select_from", choices=["all", "seeds"], default="all",
                    help="select from the whole expanded graph or only the search pool")
    ap.add_argument("--operators", default=None,
                    help="directory of fitted operators (default: <out>/operators)")
    ap.add_argument("--aggregate", action="store_true")
    ap.add_argument("--rank", type=int, default=32)
    ap.add_argument("--epochs", type=int, default=1500)
    ap.add_argument("--target", type=float, default=8.0)
    ap.add_argument("--sensitivity", type=float, nargs="*", default=[4.0, 16.0])
    ap.add_argument("--alpha", type=float, default=0.5)
    ap.add_argument("--gamma", type=float, default=5.0)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--device", default="cuda")
    args = ap.parse_args()

    files = sorted(glob.glob(f"{args.graphs}/*.json"))
    if args.embed:
        embed_all(files, args.emb_dir, args.device)
    if args.fit:
        k, N = map(int, args.fit.split("/"))
        os.makedirs(f"{args.out}/operators", exist_ok=True)
        for path in files[k::N]:
            aid = os.path.basename(path)[:-5]
            out = f"{args.out}/operators/{aid}"
            if os.path.isfile(out + ".json") or load_graph(path) is None:
                continue
            arrays, info = fit_query(path, args)
            np.savez(out + ".npz", **arrays)
            with open(out + ".json", "w") as f:
                json.dump(info, f)
            print(f"{aid} fitted in {info['_seconds']:.0f}s  d_ev={info['dspectra']['d_ev']:.2f}",
                  flush=True)
    if args.evaluate:
        os.makedirs(f"{args.out}/per_query", exist_ok=True)
        for path in files:
            aid = os.path.basename(path)[:-5]
            if not os.path.isfile(f"{args.operators or args.out + '/operators'}/{aid}.json"):
                continue
            result = evaluate_query(path, args)
            with open(f"{args.out}/per_query/{aid}.json", "w") as f:
                json.dump(result, f)
    if args.aggregate:
        aggregate(args.out)


if __name__ == "__main__":
    main()
