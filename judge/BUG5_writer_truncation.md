# Bug 5: the Nov 2-6 writer runs were capped at 512 generated tokens per LLM call

Found 2026-11-24 while replicating DeepScholar-base's filter stage (E24). Author of the bug: the
writer harness `judge/scripts/run_writer.py` (Eftychia's side), not Mateo's wrapper.

## What happened
`deepscholar_base.configs.Configs(lm=...)` derives its stage models (filter, search, taxonomize,
generation) from `lm` after removing `max_completion_tokens`, so each falls back to LOTUS's default
of 512 tokens. This is the upstream bug Mateo's wrapper fixes by passing every stage model
explicitly; `run_writer.py` built `Configs(lm=lm)` and re-introduced it. Every report in
`judge/inputs/s{0,1,2}` (all systems, all three seeds) was therefore written with each call cut at
512 tokens. Evidence: 280-360 "truncated by the max_tokens limit (512)" warnings per system log;
the judged `intro.md` files end mid-sentence; held-out introductions average 385-406 words against
520-546 after the fix (and 700-850 for Mateo's GPT-4.1-mini reports, which never had the cap).

## What it affects
- Every judged number that uses the Qwen-written reports: the three-seed Llama-judge table, its
  per-seed and paired-difference tables, and the "Qwen3-8B writer" columns of the GPT-4.1 rejudge.
  All systems were truncated alike, so comparisons between systems remain like for like, but the
  absolute scores are those of reports cut short by roughly a quarter to a third.
- The reading "the judge is not the limit; the 8B writer masks the gap" compares truncated Qwen
  reports with complete GPT-4.1-mini reports. Model strength and truncation are confounded there.
- Not affected: every retrieval result (recall, AUC, capacity experiments), the selection lists,
  DeepScholar-base's own reports and cost logs (Mateo's wrapper), the GPT-4.1-mini reports.
- The earlier note that our rerun of DeepScholar-base's lists scored lower claim coverage than
  Mateo's own reports (0.33 against 0.61, attributed to "a different writer version") is probably
  this bug.

## Fix and rerun
- `run_writer.py` now passes each stage model explicitly with max_tokens 10,000 and asserts it.
- Seed 0 rerun finished 2026-11-25 04:51: `judge/inputs_fix/s0/<system>/<row>/`, all 43 held-out
  queries for all eight systems, no truncation (two design queries failed: dsbase_rerun 004 on the
  context window, qlink_rel 019 on a timeout; neither is used by the tests).
- Queued: the same Llama-70B judge on the corrected held-out reports (`judge_fix_chain.sh`), plus
  document importance. For Mateo: the GPT-4.1 rejudge of `judge/inputs_fix/s0` replaces
  `results/qwen_writer_s0` as the "Qwen3-8B writer" column.
- Seeds 1 and 2 are not yet rerun.
