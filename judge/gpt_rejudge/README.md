# Rejudging with the paper's judges (Mateo)

These results rejudge the frozen selection lists with the judges used in the DeepScholar-Bench paper
(arXiv 2508.20033, App. A.2): GPT-4.1 for nugget coverage and GPT-4o for the other metrics. They
cover the 43 held-out queries (rows 20–62) for search seed 0.

## Contents
- `scripts/write_reports.py` runs DeepScholar's own intro writer (`generate_intro_section`) with
  any model on a fixed paper list. With `--papers-dir judge/inputs/s0/<system>` it uses exactly the
  papers in Efty's judge inputs, with the same topic text and search background as DeepScholar-base.
- `scripts/run_judge.py` judges many systems with DeepScholar-Bench's eval code. It runs two passes
  (nuggets, then the other metrics) and skips any pass that already has results. It writes
  `per_query.csv` and warns about failed judge calls (see the note below).
- `scripts/compare_judges.py` compares each system with `dsbase_rerun` using a paired Wilcoxon test,
  Holm-corrected. It also gives the per-query and system-level Spearman correlation against the
  Llama judge (`judge/results/writer_s0`).
- `results/qwen_writer_s0/`: Efty's Qwen-written reports (`judge/inputs/s0`), judged with GPT-4.1
  for nugget coverage and with reference coverage.
- `results/mini_writer_s0/`: the same paper lists, rewritten by GPT-4.1-mini and judged the same way.
- `inputs_mini_s0/<system>/<row>/`: the GPT-4.1-mini reports (`intro.md`, `paper.csv`, `meta.json`).

## Reproduce (from the folder that contains `deepscholar/` with the local-judge patch applied)
```
set -a; source deepscholar/.env; set +a          # OPENAI_API_KEY; never commit .env
python write_reports.py --run runs/final_qwen3-8b-awq_arxiv_k50_r2_s0 \
    --papers-dir d-spectra/judge/inputs/s0/<system> --model gpt-4.1-mini \
    --out eval_inputs/mini_s0/<system> --file-id $(seq 20 62)
python run_judge.py --systems-dir eval_inputs/mini_s0 --heldout \
    --other-evals reference_coverage --out eval_results/rejudge_mini_s0
python compare_judges.py --ours eval_results/rejudge_mini_s0/per_query.csv \
    --theirs d-spectra/judge/results/writer_s0 --metric nugget_coverage --heldout
```

## Note: failed judge calls are scored 0
When a judge call still fails after its retries (for example a rate limit or no API credit), the
eval code logs `Failed to assign nuggets: Reached max of 5 retries.`, scores that query 0 and
carries on. `run_judge.py` counts these lines and prints a warning. The results in this folder have
no failed calls.

## Cost
Nugget coverage (GPT-4.1) plus reference coverage costs about $0.25–0.30 per system for 43 queries.
Writing with GPT-4.1-mini costs a few cents per system.
