# Document importance for the seed-0 lists. Rules (2026-11-24, before the run)

The benchmark's document importance = min(1, median OpenAlex citation count of the documents a
report cites / median citation count of the query's important human-cited references that have
an arXiv link). It needs no judge model. Our Nov 2-6 runs returned 0 for 7 of 9 systems because
OpenAlex rate-limited the lookups (HTTP 429), so the metric was dropped. A two-query test on
11-24 returned valid values with no 429.

- Run: EVALS=document_importance judge/run_judge.sh on judge/writer/s0/<system> (the Qwen-written
  reports already judged), systems dsbase_rerun, fixed_k, relevance_only, dspectra, cocite_rel,
  usvt_cocite_rel, qlink_rel, oracle; all 63 queries; outputs judge/results/docimp_s0/<system>.
  A run with any 429 in its log is discarded and rerun, not patched.
- Statistic: per query score; the 43 held-out queries for the tests. Each system against
  dsbase_rerun, paired Wilcoxon, Holm over 7.
- Predictions: (1) every list drawn from the expanded graph (relevance_only, dspectra, cocite_rel,
  usvt_cocite_rel, qlink_rel) scores above dsbase_rerun, the co-citation and query-link lists by
  the most, because they favour well-cited papers; (2) fixed_k is within 0.05 of dsbase_rerun
  (both come from the same arXiv pool); (3) the metric is capped at 1 and counts are from today's
  OpenAlex, so it rewards popularity as such: a gain here supports "the pipeline retrieves more
  important documents", not the spectral term, and USVT co-citation is expected to gain as much
  as any SPECTRA-based list.
- The cited documents are those the 8B writer chose to cite, not the whole selection list, as
  for every other judged metric.

## Amendment (2026-11-24, same evening, before any valid result)
- The first full run was discarded as the rule requires: 55-589 log lines with HTTP 429 per system
  (the evaluator pauses 0.05 s between lookups, OpenAlex allows 10 per second). The lookup in our
  local patch of eval/utils.py now retries a 429 with exponential backoff; scores are unchanged.
- The reports of writer/s0 turned out to be truncated (judge/BUG5_writer_truncation.md), so the
  metric is run on the corrected reports instead (judge/inputs_fix/s0), held-out rows 20-62, inside
  judge_fix_chain.sh. A run is valid if it logs no failed lookup ("Error fetching citation count").
