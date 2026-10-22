# D-SPECTRA

Direction-aware spectral evidence acquisition for deep research agents. 

D-SPECTRA chooses which papers a deep-research agent gives its writer LLM. It builds a directed citation graph around the query, fits a directed version of [SPECTRA](https://arxiv.org/abs/2605.11142), and picks papers that cover the graph's spectral modes, not just the most relevant ones.

## Current implementation (preliminary)

- `dspectra/model.py`: directed SPECTRA, `P(i cites j) = σ(a_i + b_j + β K_ij)` with `K = n·UΣVᵀ/‖UΣVᵀ‖_*` and `d_ev = exp(H(σ/Σσ))`, plus bisection on η to a target `d_ev`. Also the original undirected SPECTRA, used as an ablation.
- `dspectra/selection.py`: greedy submodular selection `F(S)` over the fitted modes, plus a Vendi-score baseline.
- `scripts/build_graphs.py`: a citation graph from OpenAlex for each of the 63 DeepScholar-Bench queries, using only papers published before the query paper.
- `scripts/build_pool_expanded.py`: the same kind of graph starting from DeepScholar-base's frozen candidate pools, with citations from Semantic Scholar.
- `scripts/synthetic_check.py`, `scripts/pilot_selection.py`, `scripts/convergence_check.py`: the LLM-free experiments (planted graphs, selection pilot, training-length check).
- `scripts/fit_worker.py`, `scripts/fit_sensitivity.py`: parallel fitting, and extra `d_ev` targets for a subset of queries.
- `scripts/export_selections.py`: each method's selected papers, at DeepScholar's per-query budget, for the shared writer and judge.
- `scripts/pool_graphs.py`, `scripts/pool_edges_s2.py`: diagnostics of citations between pool papers (OpenAlex, Semantic Scholar).
- `results/`: fitted operators and per-query selections and recall for the runs below.

## Run

```bash
uv venv --python 3.11 .venv && uv pip install --python .venv/bin/python -r requirements.txt
# with an older NVIDIA driver, add: --extra-index-url https://download.pytorch.org/whl/cu121
.venv/bin/python scripts/synthetic_check.py
.venv/bin/python scripts/build_graphs.py --dataset_dir <DeepScholar-Bench dataset/> --out data/graphs_v2   # needs OPENALEX_API_KEY in .env
.venv/bin/python scripts/pilot_selection.py --embed
.venv/bin/python scripts/pilot_selection.py --fit 0/1 --epochs 6000 --out results/pilot_v2
.venv/bin/python scripts/pilot_selection.py --evaluate --aggregate --out results/pilot_v2
```

On DeepScholar-base's frozen pools (branch `pools-pilot`: `pools/final_r2_s0/` and `outputs/dsbase_final/s0/`):

```bash
P=<pools/final_r2_s0>; K=<outputs/dsbase_final/s0>
.venv/bin/python scripts/build_pool_expanded.py --pools $P --out data/graphs_dsf
.venv/bin/python scripts/fit_worker.py --pools $P --graphs data/graphs_dsf --worker 0/1 --out results/pilot_dsf
.venv/bin/python scripts/fit_sensitivity.py --ids_from <pilot pools> --graphs data/graphs_dsf --operators results/pilot_dsf/operators
.venv/bin/python scripts/pilot_selection.py --graphs data/graphs_dsf --emb_dir data/embeddings_dsf --embed
.venv/bin/python scripts/pilot_selection.py --graphs data/graphs_dsf --emb_dir data/embeddings_dsf --kept_dir $K \
    --evaluate --aggregate --out results/pilot_dsf                       # select from the whole graph
.venv/bin/python scripts/pilot_selection.py --graphs data/graphs_dsf --emb_dir data/embeddings_dsf --kept_dir $K \
    --evaluate --aggregate --select_from seeds --operators results/pilot_dsf/operators \
    --out results/pilot_dsf_strict                                       # select from the pool only
.venv/bin/python scripts/export_selections.py --pools $P --graphs data/graphs_dsf \
    --results expanded=results/pilot_dsf pool_only=results/pilot_dsf_strict --out selections/final_s0
```
