# D-SPECTRA

Direction-aware spectral evidence acquisition for deep research agents. Course project by Eftychia Makri (em2388) and Mateo Bastidas (mib37).

D-SPECTRA chooses which papers a deep-research agent gives its writer LLM. It builds a directed citation graph around the query, fits a directed version of [SPECTRA](https://arxiv.org/abs/2605.11142), and picks papers that cover the graph's spectral modes, not just the most relevant ones.

## Current implementation (preliminary)

- `dspectra/model.py`: directed SPECTRA, `P(i cites j) = σ(a_i + b_j + β K_ij)` with `K = n·UΣVᵀ/‖UΣVᵀ‖_*` and `d_ev = exp(H(σ/Σσ))`, plus bisection on η to a target `d_ev`. Also the original undirected SPECTRA, used as an ablation.
- `dspectra/selection.py`: greedy submodular selection `F(S)` over the fitted modes, plus a Vendi-score baseline.
- `scripts/build_graphs.py`: a citation graph from OpenAlex for each of the 63 DeepScholar-Bench queries, using only papers published before the query paper.
- `scripts/synthetic_check.py`, `scripts/pilot_selection.py`, `scripts/convergence_check.py`: the LLM-free experiments (planted graphs, selection pilot, training-length check).

## Run

```bash
uv venv --python 3.11 .venv && uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python scripts/synthetic_check.py
.venv/bin/python scripts/build_graphs.py --dataset_dir <DeepScholar-Bench dataset/> --out data/graphs_v2   # needs OPENALEX_API_KEY in .env
.venv/bin/python scripts/pilot_selection.py --embed
.venv/bin/python scripts/pilot_selection.py --fit 0/1 --epochs 6000 --out results/pilot_v2
.venv/bin/python scripts/pilot_selection.py --evaluate --aggregate --out results/pilot_v2
```
