# Judged evaluation: inputs, outputs and scripts, as run (Nov 2-6, 2026)

- `inputs/s{0,1,2}/<system>/<query>/` — the folders the DeepScholar-Bench judge read, one per
  held-out query (ids as in the frozen pools): `final_report.md`, `intro.md`, `paper.csv`,
  `stats.json`, written by the Qwen3-8B-AWQ writer (`scripts/run_writer.py`) from the selection
  list in `../selections/final/s<seed>/<system>.csv`. Systems: dspectra, cocite_rel,
  usvt_cocite_rel, qlink_rel, fixed_k, relevance_only, oracle, dsbase_rerun (DeepScholar-base's
  own papers, re-written by the same writer); seed 0 also has scocite_rel and the `_modes` variants.
  `inputs/dsbase_s0/` is DeepScholar-base's own output arranged for the judge (`scripts/to_judge_format.py`).
- `results/writer_s{0,1,2}/<system>/<metric>/` — the raw outputs of the local Llama-3.1-70B judge,
  per metric; `results/dsbase_s0/` the same for DeepScholar-base's own output.
- `deepscholar-bench-local-judge.patch` — our changes to the DeepScholar-Bench eval code (commit it
  was made against: see the `index` lines): longer timeouts for a local 70B, a string-decision
  fallback in the organization judge, and the parser change that counts a non-arXiv link when
  `paper.csv` lists it by URL (`eval/parsers/deepscholar_base.py`).
- `scripts/` — `run_judge.sh` (judge via a localhost relay, `relay.py`), `serve_judge.sh` /
  `serve_qwen.sh` / `setup_qwen.sh` (vLLM servers, localhost only), `run_writer.py` /
  `run_writer_all.sh` (writer), `judge_chain.sh` / `seeds12_chain.sh` (the runs as chained).
  Summaries: `../scripts/judged_eval.py` (seed 0) and `../scripts/judged_seeds.py` (seeds 0-2)
  -> `../results/judged`, `../results/judged_s12`.
