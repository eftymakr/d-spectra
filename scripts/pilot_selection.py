"""
LLM-free pilot of selection-only D-SPECTRA on DeepScholar-Bench graphs.

For each query graph (scripts/build_graphs.py), select B papers with each
method and measure how many of the references the human authors cited in
their related-work section the selection recovers. No writer LLM or judge
is involved; this is a retrieval-side proxy for the proposal's gate.

Methods (all selecting from the same candidate pool):
  search_only      top-B by relevance among the initial-search seeds
  relevance        top-B by relevance over the expanded pool (fixed-k analogue)
  most_cited       top-B by in-pool in-degree
  dspectra         greedy F(S) on directed SPECTRA modes, d_ev targeted to --target
  dspectra_eta0    same, fitted with eta = 0 (no spectral term; main ablation)
  dspectra_d<k>    same, other d_ev targets (sensitivity)
  symmetrized      greedy F(S) on undirected SPECTRA fitted to A + A^T
  raw_svd          greedy F(S) on the SVD of A (no fitting)
  semantic         greedy F(S) on the SVD of the embedding matrix
                   (Vendi-style diversity, no citation structure)

Hyperparameters are fixed before looking at results: rank cap 32,
target d_ev 8 (sensitivity 4, 16), alpha 0.5, gamma 5.

Stages:
  --embed            compute bge-m3 embeddings for every graph (one process)
  --shard k/N        fit and select for every N-th graph starting at k
  --aggregate        combine per-query results into tables
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
    cos = En @ Eq
    lo, hi = cos.min(), cos.max()
    return (cos - lo) / max(hi - lo, 1e-12)


def svd_modes(M, k, paper_axis):
    """Top-k singular vectors along the paper axis (0 = rows, 1 = columns)
    with occupancy sigma_k / sum(sigma)."""
    U, s, Vt = np.linalg.svd(M, full_matrices=False)
    k = min(k, len(s))
    vecs = U[:, :k] if paper_axis == 0 else Vt[:k].T
    return vecs, s[:k] / s[:k].sum()


def run_query(path, emb_dir, args):
    from dspectra.model import FitConfig, diagnostics, fit, fit_to_target, modes
    from dspectra.selection import (embedding_diversity, greedy_select, set_d_ev, top_k)

    g, A = load_graph(path)
    aid = g["arxiv_id"]
    z = np.load(os.path.join(emb_dir, f"{aid}.npz"))
    En, Eq = z["nodes"], z["query"]
    r = relevance(Eq, En)
    n = A.shape[0]
    gt = set(g["gt"]["in_pool"]); imp = set(g["gt"]["important_in_pool"])
    seeds = np.array([k for k, nd in enumerate(g["nodes"]) if nd["source"] == "seed"])
    cfg = FitConfig(rank=args.rank, epochs=args.epochs, device=args.device)

    t0 = time.time()
    operators, fit_info = {}, {}
    res = fit_to_target(A, args.target, "directed", cfg, seed=args.seed)
    md = modes(res.model)
    operators["dspectra"] = (md["V"], md["p"])
    fit_info["dspectra"] = {"eta": res.eta, "d_ev": res.d_ev, "probes": len(res.probes)}
    yardstick = (md["V"], md["p"])

    m0 = fit(A, "directed", 0.0, cfg, seed=args.seed)
    m0d = modes(m0)
    operators["dspectra_eta0"] = (m0d["V"], m0d["p"])
    fit_info["dspectra_eta0"] = {"eta": 0.0, "d_ev": diagnostics(m0)["d_ev"]}

    for t in args.sensitivity:
        rs = fit_to_target(A, t, "directed", cfg, seed=args.seed)
        ms = modes(rs.model)
        operators[f"dspectra_d{t:g}"] = (ms["V"], ms["p"])
        fit_info[f"dspectra_d{t:g}"] = {"eta": rs.eta, "d_ev": rs.d_ev}

    rsym = fit_to_target(A, args.target, "symmetric", cfg, seed=args.seed)
    msym = modes(rsym.model)
    operators["symmetrized"] = (msym["V"], msym["p"])
    fit_info["symmetrized"] = {"eta": rsym.eta, "d_ev": rsym.d_ev}

    # columns of A are cited papers, so the cited-role factor is V of A's SVD
    operators["raw_svd"] = svd_modes(A, args.rank, paper_axis=1)
    operators["semantic"] = svd_modes(En - En.mean(0), args.rank, paper_axis=0)
    fit_seconds = time.time() - t0

    selections = {}
    for B in BUDGETS:
        selections[("search_only", B)] = top_k(r, B, candidates=seeds)
        selections[("relevance", B)] = top_k(r, B)
        selections[("most_cited", B)] = top_k(A.sum(0) + 1e-6 * r, B)
        for name, (V, p) in operators.items():
            selections[(name, B)] = greedy_select(V, p, r, B, args.alpha, args.gamma)

    rows = []
    n_gt_all = g["gt"]["n_cited_in_related_work"]; n_imp_all = g["gt"]["n_important"]
    for (method, B), S in selections.items():
        hit = gt & set(S); hit_imp = imp & set(S)
        rows.append({
            "arxiv_id": aid, "method": method, "B": B, "size": len(S),
            "hits": len(hit), "recall": len(hit) / max(n_gt_all, 1),
            "recall_reachable": len(hit) / len(gt) if gt else float("nan"),
            "recall_important": len(hit_imp) / max(n_imp_all, 1),
            "d_ev_S": set_d_ev(*yardstick, S),
            "diversity": embedding_diversity(En, S),
            "mean_relevance": float(r[S].mean()) if S else 0.0,
        })

    # premise check: do the human-cited papers spread over more modes than a
    # relevance-ranked set of the same size?
    premise = None
    if len(gt) >= 3:
        k = len(gt)
        premise = {"k": k,
                   "d_ev_human": set_d_ev(*yardstick, sorted(gt)),
                   "d_ev_relevance": set_d_ev(*yardstick, top_k(r, k)),
                   "d_ev_random_mean": float(np.mean([
                       set_d_ev(*yardstick, np.random.default_rng(s).choice(n, k, replace=False))
                       for s in range(20)]))}
    return {"arxiv_id": aid, "n_nodes": n, "n_edges": int(A.sum()),
            "n_gt_in_pool": len(gt), "n_gt_all": n_gt_all, "fit": fit_info,
            "fit_seconds": fit_seconds, "premise": premise, "rows": rows}


def aggregate(out_dir):
    import pandas as pd
    from scipy.stats import wilcoxon, spearmanr
    per_q = [json.load(open(f)) for f in sorted(glob.glob(f"{out_dir}/per_query/*.json"))]
    df = pd.DataFrame([row for q in per_q for row in q["rows"]])
    reach = df[df.arxiv_id.isin([q["arxiv_id"] for q in per_q if q["n_gt_in_pool"] > 0])]
    tab = reach.pivot_table(index="method", columns="B", values="recall", aggfunc="mean")
    tab_imp = reach.pivot_table(index="method", columns="B", values="recall_important",
                                aggfunc="mean")
    tab_reach = reach.pivot_table(index="method", columns="B", values="recall_reachable",
                                  aggfunc="mean")
    tests = []
    for other in ["relevance", "dspectra_eta0", "symmetrized", "raw_svd", "semantic",
                  "search_only", "most_cited"]:
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

    # does recall track the set's occupancy beyond its size? (within-query Spearman
    # over all method x budget cells)
    track = []
    for aid, d in reach.groupby("arxiv_id"):
        if d.recall.nunique() > 1:
            track.append({"rho_d_ev": spearmanr(d.d_ev_S, d.recall)[0],
                          "rho_size": spearmanr(d["size"], d.recall)[0]})
    track = pd.DataFrame(track)

    summary = {
        "n_queries": len(per_q),
        "n_queries_with_gt_in_pool": int(reach.arxiv_id.nunique()),
        "pool": {
            "mean_nodes": float(np.mean([q["n_nodes"] for q in per_q])),
            "mean_edges": float(np.mean([q["n_edges"] for q in per_q])),
            "mean_gt_reachable_frac": float(np.mean(
                [q["n_gt_in_pool"] / max(q["n_gt_all"], 1) for q in per_q])),
        },
        "fit": {name: {"mean_d_ev": float(np.mean([q["fit"][name]["d_ev"] for q in per_q]))}
                for name in per_q[0]["fit"]},
        "mean_fit_seconds": float(np.mean([q["fit_seconds"] for q in per_q])),
        "premise": prem_test,
        "recall_tracks": {"mean_rho_d_ev": float(track.rho_d_ev.mean()),
                          "mean_rho_size": float(track.rho_size.mean()),
                          "n": len(track)} if len(track) else None,
    }
    tab.round(4).to_csv(f"{out_dir}/recall.csv")
    tab_imp.round(4).to_csv(f"{out_dir}/recall_important.csv")
    tab_reach.round(4).to_csv(f"{out_dir}/recall_reachable.csv")
    tests.round(4).to_csv(f"{out_dir}/tests_vs_dspectra.csv", index=False)
    df.to_csv(f"{out_dir}/all_rows.csv", index=False)
    with open(f"{out_dir}/summary.json", "w") as f:
        json.dump(summary, f, indent=2, default=float)
    import pandas as _pd
    _pd.set_option("display.width", 200)
    print("recall of related-work citations (mean over queries):\n", tab.round(3))
    print("\nrecall of important citations:\n", tab_imp.round(3))
    print("\nD-SPECTRA vs others (paired Wilcoxon on recall):\n", tests.round(3).to_string())
    print(json.dumps(summary, indent=2, default=float))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graphs", default="data/graphs")
    ap.add_argument("--emb_dir", default="data/embeddings")
    ap.add_argument("--out", default="results/pilot")
    ap.add_argument("--embed", action="store_true")
    ap.add_argument("--shard", default=None, help="k/N")
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
    if args.shard:
        k, N = map(int, args.shard.split("/"))
        os.makedirs(f"{args.out}/per_query", exist_ok=True)
        for path in files[k::N]:
            aid = os.path.basename(path)[:-5]
            out = f"{args.out}/per_query/{aid}.json"
            if os.path.isfile(out) or load_graph(path) is None:
                continue
            if not os.path.isfile(os.path.join(args.emb_dir, f"{aid}.npz")):
                continue
            t0 = time.time()
            result = run_query(path, args.emb_dir, args)
            with open(out, "w") as f:
                json.dump(result, f)
            print(f"{aid} done in {time.time() - t0:.0f}s  d_ev={result['fit']['dspectra']['d_ev']:.2f} "
                  f"gt_in_pool={result['n_gt_in_pool']}", flush=True)
    if args.aggregate:
        aggregate(args.out)


if __name__ == "__main__":
    main()
