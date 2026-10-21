# DeepScholar-base outputs (final runs)

One folder per seed (s0, s1, s2), one subfolder per query (same names as the pools).
Settings: Qwen3-8B-AWQ, arXiv only, 2 rounds x 2 phrases, 50 results per phrase, temperature 0.7,
top_p 0.8, top_k 20, thinking off. Pools for the same seed: pools/final_r2_s<N>/.

- kept.csv: papers DeepScholar's LLM filter + top-k kept (up to 30), in rank order.
- references.csv: the report's reference list. DeepScholar's report lists every kept paper in
  per-category tables, so this is the same set as kept.csv, plus its category; cited_in_text marks
  the papers cited inline in the related-work paragraph.
- report.md: the generated report. query.json: target paper and cutoff.
- costs.csv (per seed): wall_seconds; llm_calls (completed LLM calls, counted from the run log);
  prompt/completion tokens per stage (search, filter, taxonomize, generation) and total;
  search_calls (rounds), search_phrases (= arXiv queries), arxiv_requests (incl. retries);
  empty_or_failed_searches; search_attempts (DeepScholar re-runs search if the filter keeps nothing);
  n_pool, n_kept, n_references, n_cited_in_text.
