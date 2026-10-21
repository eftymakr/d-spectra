# D-SPECTRA: Direction-Aware Spectral Evidence Acquisition for Deep Research Agents

Course project by Eftychia Makri (em2388) and Mateo Bastidas (mib37).

D-SPECTRA decides which papers a deep-research agent passes to its (frozen) writer LLM. It builds a local directed citation graph around a query, fits a directed version of SPECTRA ([Nakis et al., 2026](https://arxiv.org/abs/2605.11142)), and selects papers that cover the graph's spectral modes instead of just the most relevant ones.

**Status (progress report 1):** this repo has the directed model, graph construction, selection, and the two LLM-free pilot experiments. The writer and judge integration (DeepScholar-base, step 1 of the plan) and closed-loop acquisition and stopping (step 4) are not implemented yet.

## What is implemented

| File | What it does |
|---|---|
| [dspectra/model.py](dspectra/model.py) | **Directed SPECTRA.** `P(i cites j) = σ(a_i + b_j + β K_ij)`, with `K = n·UΣVᵀ / ‖UΣVᵀ‖_*` and occupancy `p_k = σ_k / Σσ`, so `d_ev = exp(H(p))`. The objective is `NLL − η·log d_ev + R`, with bracket-and-bisect on η to hit a target `d_ev`. Also contains the original undirected SPECTRA (`SymmetricSpectra`) for the symmetrized ablation. Ported from the SPECTRA engine, keeping its SVD parameterisation, bounded β, centered factors and bias warm-up. Graphs have at most 500 nodes, so the loss uses every non-edge exactly instead of sampled negatives. |
| [dspectra/selection.py](dspectra/selection.py) | Greedy maximisation of the monotone submodular `F(S) = α Σ r_i/B + (1−α) Σ_k w_k (1 − e^{−γ z_k(S)})` with mode weights `w_k ∝ p_k Σ_i r_i V_ik²`. Also contains the set-level `d_ev(S)` and embedding diversity. `z_k` is normalised by each mode's relevant mass, which rescales γ per mode and keeps the `1 − 1/e` guarantee. |
| [dspectra/openalex.py](dspectra/openalex.py) | Cached, rate-limited OpenAlex client. The API key is read from `OPENALEX_API_KEY` or `.env` and is never cached or logged. |
| [scripts/synthetic_check.py](scripts/synthetic_check.py) | Planted directed graphs (50–500 nodes, 4 topic groups, popular "generic" papers). Checks η control, target hitting, offset behaviour, group recovery and held-out citation AUC against the symmetrized model, raw SVD, and the model without offsets. |
| [scripts/build_graphs.py](scripts/build_graphs.py) | For each of the 63 DeepScholar-Bench queries, builds the local graph from OpenAlex. Seeds come from search restricted to works published before the query paper; the pool adds the seeds' references and citing papers (also pre-dating the query), up to 500 nodes. Ground truth is the query's related-work citations, matched to pool papers by title. |
| [scripts/pilot_selection.py](scripts/pilot_selection.py) | Selection-only pilot with no LLM. Compares D-SPECTRA against relevance top-B, search-only, most-cited, η = 0 (no spectral term), symmetrized graph, raw SVD and semantic (embedding) modes at B ∈ {10, 20, 30, 45, 60}. Measures recall of human-cited references, `d_ev(S)` and diversity, with paired Wilcoxon tests. Relevance is the bge-m3 cosine to the query's title and abstract. |

## How to run

```bash
uv venv --python 3.11 .venv
uv pip install --python .venv/bin/python -r requirements.txt
# torch 2.5.1+cu121 was used (the driver here supports CUDA 12.2):
# uv pip install --python .venv/bin/python torch==2.5.1 --index-url https://download.pytorch.org/whl/cu121

# 1. synthetic sanity checks
.venv/bin/python scripts/synthetic_check.py --sizes 50 100 200 500 --out results/synthetic

# 2. per-query citation graphs (needs the DeepScholar-Bench dataset/ folder and an OpenAlex key in .env)
.venv/bin/python scripts/build_graphs.py --dataset_dir data/deepscholar_bench --out data/graphs

# 3. selection pilot: embed, fit and select (shardable), then aggregate
.venv/bin/python scripts/pilot_selection.py --embed
.venv/bin/python scripts/pilot_selection.py --shard 0/1
.venv/bin/python scripts/pilot_selection.py --aggregate
```

Results are written to `results/synthetic/` and `results/pilot/`. The tables and figures used in the progress report are committed there.

## Not yet implemented

- DeepScholar-base and fixed-k reproduction with a shared writer (planned: Qwen3-4B-Instruct-2507 served locally with vLLM; gpt-4o as the benchmark's released judge).
- Plugging D-SPECTRA's selected set into DeepScholar-base's writer and scoring with the released evaluation code.
- Closed-loop acquisition (refit, residual-driven expansion) and the ε stopping rule.
- ResearchQA and DeepResearch Bench II.
