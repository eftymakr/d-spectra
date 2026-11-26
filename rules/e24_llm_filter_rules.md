# E24: DeepScholar-base's LLM filter on the same candidates as D-SPECTRA. Rules (2026-11-24, before any run)

Question. Every comparison with DeepScholar-base so far gives its LLM filter the search pool
(about 103 arXiv papers, 6% of the human-cited references) and the graph methods the expanded
graph (about 480 papers, 37%). The pool-only setting equalizes the candidates in one direction
(everyone restricted to the pool). E24 equalizes them in the other: the baseline's own filter,
unchanged, run over the expanded graph's papers. It answers whether D-SPECTRA selects better than
the LLM filter given the same documents, or only has more documents.

## Arms (search seed 0, the 63 queries; tests on the 43 held-out)
- filter_pool: deepscholar_base.filter.filter (sem_filter with chain-of-thought, then sem_topk to
  30; upstream prompts and defaults) over the graph's pool nodes (source = seed), with Qwen3-8B-AWQ
  and the sampling of the baseline runs (temperature 0.7, top_p 0.8, top_k 20, thinking off, seed 0,
  max_tokens 10,000). This replicates the baseline's filter stage with our harness; Mateo's wrapper
  is not on this machine. Replication check before the other arm is read: mean number kept within
  21.2 +/- 5 and held-out recall within 0.047 +/- 0.02 of DeepScholar-base's own kept lists (exact
  overlap is not expected: two baseline runs share only 19-46% of their papers).
- filter_expanded: the same call over all nodes of the graph (pool + references + citing papers),
  each with its title, abstract (as the snippet; empty when Semantic Scholar has none), URL, date.
- The topic is the query text of outputs/dsbase_final/s0/<query>/query.json, as in the baseline.
- Tokens of the filter stage (prompt + completion) are recorded per query.

## Statistic
- Recall of human-cited references at B = kept (the baseline's per-query count), as everywhere:
  the first B papers of the filter's ranked list (the whole list when it is shorter). Also the
  recall of the full list returned (up to 30) against every method re-selected at that size.
- Primary family, held-out, paired Wilcoxon, Holm over 5:
  F1 dspectra (d_ev = 8) - filter_expanded
  F2 qlink_rel - filter_expanded
  F3 usvt_cocite_rel - filter_expanded
  F4 filter_expanded - relevance_only (same graph)
  F5 filter_expanded - DeepScholar-base's own picks
- Descriptive: filter_expanded tokens per query against the baseline's filter (195,733) and
  against D-SPECTRA's zero; the share of filter_expanded's picks that are pool papers.

## Predictions
1. F5 > 0: the LLM filter also gains from the expanded candidates (recall at least 0.07).
2. F4 within +/- 0.02: an abstract-by-abstract relevance judgment behaves like relevance ranking.
3. F1 > 0 but small (under 0.03) and not significant after Holm; F2 and F3 > 0.05 and significant.
4. filter_expanded costs more than three times the baseline filter's tokens.

## Decision rule
- F1 significant and positive: "D-SPECTRA selects better than the LLM filter given the same
  candidates" may be stated. Otherwise the report says that against the LLM filter on equal
  candidates D-SPECTRA's advantage is cost (no LLM calls), and that the 2.6x recall gain over
  DeepScholar-base is due to the expanded candidates; the selection claim then rests on F2/F3
  (the query-anchored selectors) if those hold.
- One run per arm; no prompt, threshold or model change after results are seen. A failed
  replication check (filter_pool) stops the analysis until the harness is fixed, and that is reported.
