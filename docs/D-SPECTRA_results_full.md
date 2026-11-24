# D-SPECTRA: what we did and what we found

*Eftychia Makri and Mateo Bastidas · state as of Nov 6, 2026. Every fitted result below was recomputed on Oct 29–30 after a bug in the model's optimizer was found and fixed (bug 4, section 4); only E3 and Appendix A were not rerun and still come from the buggy fits. E15–E22 (Oct 31–Nov 5) were run on the corrected code. The writer and judge have now been run on every frozen selection list for all three search seeds (Nov 2–6, sections 3.20–3.21). This document covers both halves of the project: Eftychia's side (directed SPECTRA, citation graphs, selection experiments) and Mateo's side (DeepScholar-base reproduction, frozen candidate pools). Every number in a table is generated directly from the result files listed in [section 6](#6-files-and-how-to-reproduce); nothing is typed in by hand. Text numbers were checked against those tables.*

## Contents

- [Summary](#summary)
- [1. The project and where we are in the plan](#1-the-project-and-where-we-are-in-the-plan)
- [2. What we did, experiment by experiment](#2-what-we-did-experiment-by-experiment)
- [3. Results](#3-results)
- [4. Bugs found and fixed](#4-bugs-found-and-fixed)
- [5. What it means](#5-what-it-means)
- [6. Files and how to reproduce](#6-files-and-how-to-reproduce)
- [7. Open items](#7-open-items)
- [Appendix A. Superseded: the 20 pilot pools](#appendix-a-superseded-the-20-pilot-pools)
- [Appendix B. Mateo's pilot report (verbatim)](#appendix-b-mateos-pilot-report-verbatim)

---

## Summary

**What D-SPECTRA does.** It chooses which papers a deep-research agent passes to its frozen writer LLM. For each query it builds a directed citation graph around the search results, fits a directed version of SPECTRA to it, and picks papers that cover the graph's spectral modes instead of only the most relevant ones.

**What we did** (details in section 2):

| # | Experiment | Data | Purpose |
|---|---|---|---|
| E1 | Synthetic check | Planted directed graphs, 50–500 nodes | Does the directed model work on small graphs? |
| E2 | Convergence check | 3 real graphs | Is the training budget enough? |
| E3 | OpenAlex pilot | All 63 DeepScholar-Bench queries, our own keyword search + citations | First comparison of selection methods, before Mateo's pools existed |
| E4 | DeepScholar-base reproduction (Mateo) | 20 pilot queries × 3 runs, then all 63 queries × 3 seeds | The baseline system, its candidate pools, its own picks and costs |
| E5 | Pool diagnostics | Mateo's 20 pilot pools | Do pool papers cite each other? How many human-cited papers do pools contain? |
| **E6** | **Main run: the proposal's version on the final pools** | **All 63 queries, Mateo's final seed-0 pools** | **D-SPECTRA vs DeepScholar-base's own picks and all baselines, at the matched budget, on 43 held-out queries** |
| E7 | Review checks | All of the above | Leakage, missing abstracts, a fair d_ev(S) test; found three bugs |
| E8 | Method variants and bigger graphs | All 63 queries, Mateo's final seed-0 pools | Three changes to D-SPECTRA and 2× larger graphs, chosen on the design queries, run once on the held-out queries |
| E9 | The remaining SPECTRA ingredients | Same as E8, current-size graphs | Spectral prefixes, rank caps 8–128, early-stopped η probes, three criteria for choosing η, three fit seeds and best-of-3 restarts |
| E10 | The rest of the plan's method work | Seed-0 pools, plus Mateo's search seeds 1 and 2 | α, γ and the link weight tuned on the design queries; a learning-rate schedule; the main comparison repeated on two more search seeds |
| E11 | What else helps the query link | Seed-0 pools, E8's fits | Model-free and USVT versions of the query link, coverage on top of the link score, fusion with USVT, the query's citing role predicted from its text |
| E12 | Final checks | All three search seeds; DeepScholar-base's judged reports | Frozen methods exported; the step-2 gate on judged coverage; seed-averaged, Holm-corrected tests; cost per query |
| E13 | Can the SPECTRA model itself win? | All three search seeds, existing fits | SPECTRA co-citation (the anchors' predicted citations), capacity as a denoising knob, and a learned ranker with and without SPECTRA features |
| E14 | SPECTRA's own capacity rule | All three search seeds | d_ev targeted to the graph baselines' effective ranks (USVT's, and the median of USVT and raw SVD), as the SPECTRA paper does, with no validation data |
| E15 | The query's citing role as the centre of selection | All three search seeds, existing fits | Mode coverage weighted by the modes the *query* cites, and pseudo-relevance feedback on the query link and on SPECTRA co-citation |
| E16 | The β ceiling | All three search seeds, refitted | β sits at its bound of 5 in every fit; every query refitted with β_max = 20 to see whether the bound costs recall or link prediction |
| — | The QR-fix refit | Everything from E1 on, except E3 and Appendix A | A sign bug in the optimizer (bug 4) was fixed and every fit redone; old results are kept in `results/pre_qrfix/` |
| E17 | A second hop of citations | Seed-0 pools, graphs six times larger | Does reaching more of the human-cited references (37% → 52%) help any method? |
| E19 | SPECTRA's own evaluation and the capacity frontier | All 63 graphs, the cv fits | Held-out link prediction against structural baselines; held-out AUC along the η grid |
| E20 | Rank caps 64 and 128 on the frontier | All 63 graphs, cv fits | Does held-out link prediction keep improving above the rank cap (SPECTRA's regime criterion)? |
| E21 | An inductive citing role for the query | All 63 graphs; 1,260 pseudo-queries, then the 43 real held-out queries | Can the query be placed in the fitted citing-role space from its text, instead of averaging anchors? |
| E22 | The sparsification frontier | All 63 graphs, the cv fits refitted with 50%, 25% and 10% of the citations | At what citation density would capacity control have mattered, and where do the benchmark's graphs sit relative to it? |
| **Judged** | **The writer and judge on every frozen list** | **Seed 0, 63 queries, 9 systems through the same writer and the same local judge; then seeds 1 and 2, 8 systems each** | **The endpoint the proxy stood in for: judged nugget coverage against DeepScholar-base's own picks, at a third of the tokens** |
| E18 | The fitted modes as the report's taxonomy | The three graph lists, same writer and judge | Does organising the report by the spectral modes help? (null by construction, 3.21) |

**Main results:**

Items 1–18 and 21–23 are on the proxy metric: recall of the references the human authors cited in the related-work section (E21 also uses the graph's own citations as ground truth; E22 is held-out citation prediction only). Items 19–20 are the judged evaluation: every frozen list through the same writer and the same local judge (sections 3.20–3.21).

1. **Main result (E6, 43 held-out queries, matched budget B = kept, about 21 papers).** D-SPECTRA recovers **0.120** of the human-cited references. DeepScholar-base's own picks recover **0.047** (+0.073, better on 29 queries and worse on 5, p < 0.001). Fixed-k gets **0.059** (p < 0.001), and relevance-only selection over the same expanded graph, the main ablation in its α = 1 reading, gets **0.090** (+0.030, 22 vs 5 queries, p = 0.006). D-SPECTRA also beats Vendi, semantic modes and symmetrized SPECTRA (p ≤ 0.038). Averaged over Mateo's three search seeds with a Holm correction over 16 comparisons (E12), D-SPECTRA (0.115) still beats relevance only (0.090, Holm p = 0.030), fixed-k and DeepScholar-base's picks (0.044).
2. **But it is not the best method.** It ties most-cited (0.096, p = 0.19). Plain spectral baselines do as well or better: USVT 0.138 (D-SPECTRA −0.018, p = 0.066; USVT ahead at B = 20, 30 and 45, p ≤ 0.036) and raw SVD 0.134 (−0.014, p = 0.087). Seed-averaged: D-SPECTRA vs USVT −0.020, Holm p = 0.28.
3. **Capacity control (η) makes no difference on the held-out queries.** D-SPECTRA (d_ev = 8) 0.120 vs η = 0 (d_ev ≈ 28) 0.122, p = 0.77; seed-averaged +0.001, p = 0.98. This is the other reading of the main ablation, "without the spectral term", and it is a tie. SPECTRA's own rule, targeting each query's d_ev to a baseline's effective rank (E14), gives 0.119 and 0.117: not different from d_ev = 8 or η = 0. On the 20 design queries more capacity is better (d_ev 4: 0.078, 8: 0.119, 16: 0.151, η = 0: 0.161), but that does not carry over to the held-out queries, where every setting from d_ev 4 to 28 gives 0.114–0.122.
4. **Most of the gain comes from following citations.** DeepScholar's pools contain only 6.1% of the human-cited references; the expanded graphs contain 37.1%. When every method may only pick from the pool, they all reach most of what the pool contains (85–96% on the held-out queries, except DeepScholar's own picks and Vendi), and D-SPECTRA's edge shrinks to +0.007 over fixed-k (p = 0.018). It still beats DeepScholar's own picks there (+0.019, p = 0.001).
5. **The premise behind "more capacity" is reversed on this data, though less sharply than before the fix.** The papers humans cited occupy *fewer* fitted modes than a relevance-ranked set of the same size (d_ev(S) 5.52 vs 6.29 on the held-out queries, higher in 10 of 36, p = 0.001; 5.67 vs 6.23 on all 63, p = 0.004; no difference on the design queries). At a fixed budget, methods whose picks have higher d_ev(S) have lower recall (Spearman −0.47 across methods at B = kept, held out; −0.05 to −0.47 across budgets). **The proposal's "strongest result" test fails:** within a query, recall tracks the number of papers (ρ = +0.55) far better than d_ev(S) (ρ = +0.17). This is on recall; on judged nugget coverage of DeepScholar-base's own reports the gate fails too (E12).
6. **Cost.** D-SPECTRA replaces only DeepScholar's LLM filter; the search and the writer stay the same.
   - The filter uses about 196,000 of DeepScholar-base's 284,000 tokens per query (69%). D-SPECTRA's selection uses no LLM calls.
   - Fitting: the d_ev = 8 search takes about 4 minutes per query on a free GPU (about 10 probe fits of 18 s each), plus graph building. DeepScholar-base takes 3.6 minutes end to end. The best method (item 11) needs no fit at all.
7. The earlier OpenAlex pilot (E3, our own search, **not rerun after the fix**) shows the same pattern: following citations doubles recall, D-SPECTRA ≈ relevance-only, and USVT is best at large budgets.
8. **E8: scoring the query as a new citing paper helps; the other changes and bigger graphs don't.**
   - **Query link + relevance** (its configuration chosen on the design queries: 5 anchors, η = 0 fit) recovers **0.167** at the matched budget on the 43 held-out queries:
     - better than D-SPECTRA (0.120; +0.047, 25 vs 7 queries, p < 0.001), relevance-only (p < 0.001), most-cited (p = 0.002) and USVT (0.138; +0.028, p = 0.027).
   - **No gain:** choosing η by held-out link prediction (held-out AUC is flat in η, 0.953–0.958, so the chosen η is close to arbitrary), and mode weights anchored on the pool.
   - **Bigger graphs** contain more of the references (41% vs 35%), but no method recalls more from them.
9. **E9: the rest of SPECTRA's machinery changes little.**
   - **Spectral prefixes:** keeping D-SPECTRA's top 4 modes gives +0.012 held out (p = 0.094, not significant). Prefixes don't change the query-link scores.
   - **Rank caps:** 64 and 128 change nothing (every difference within ±0.003). At η = 0 the fits stop growing at d_ev ≈ 43–45 under those caps.
   - **Choosing η:** early-stopped probes save about half the fitting but miss the target far more often (67% vs 97% within 5%) with the same recall. Held-out AUC and AP are flat in η; held-out NLL always picks the most negative η (d_ev ≈ 4.5) and is slightly worse (−0.018, p = 0.046).
   - **Fit seeds:** D-SPECTRA 0.117–0.120 and query link + relevance 0.165 in every seed; per-query sd across seeds ≤ 0.008. Best-of-3 restarts change nothing.
10. **E10: tuning helps the query link a little, not D-SPECTRA; the schedule no longer matters; search seeds agree.**
    - A 0.75 weight on the link score gives 0.177 held out (vs 0.165 at 0.5; +0.011, p = 0.16). D-SPECTRA's best α, γ give +0.007 (p = 0.34).
    - With the bug fixed, constant and cosine learning rates both converge (d_ev drift 0.0%, no loss rise) and give the same recall.
    - On search seeds 1 and 2, query link + relevance beats D-SPECTRA by +0.040 to +0.045 (p < 0.001) and is ahead of USVT by +0.019 to +0.027 in every seed.
11. **E11: the gain is in the idea, not in the model.**
    - A plain relevance-weighted count of how many of the 10 most relevant pool papers cite each paper, mixed with relevance, gets 0.172 held out against 0.177 for the tuned SPECTRA query link (p = 0.36).
    - The same idea on USVT's denoised citation matrix is the best method: **0.184**. It beats USVT (p = 0.001) and D-SPECTRA (p < 0.001); against the SPECTRA query link it is +0.007 (p = 0.27). Seed-averaged with Holm (E12): the three query-anchored methods (0.166–0.174) are indistinguishable from each other; the USVT version and the SPECTRA query link both beat USVT (Holm p = 0.041).
    - Coverage on top of the link score, fusion with USVT, and predicting the query's citing role from its text add nothing.
12. **E13: the fitted model matches, but does not beat, USVT denoising.**
    - **SPECTRA co-citation** (the anchors' mean predicted citation probability; chosen configuration: η = 0 fit, all 32 modes, 5 anchors) recovers 0.172 seed-averaged, the same as USVT co-citation (−0.002, Holm p = 1.0) and above D-SPECTRA (+0.057, Holm p = 0.003) and USVT (+0.037, uncorrected p = 0.041).
    - **Capacity:** fewer modes is worse here (2 modes −0.031, p = 0.051); 16 and 32 modes are the same.
    - **A learned ranker:** SPECTRA's features add +0.008 (Holm p = 0.29); the ranker does not beat the plain USVT co-citation score.
13. **E14: SPECTRA's own capacity rule changes nothing.** Targets taken from the baselines' effective ranks (USVT's, 14–30, median 22) are hit within 2% on every query. Recall is 0.119 (tmin) and 0.117 (tmed) held out, against 0.115 at d_ev = 8 and 0.114 at η = 0 (Holm p ≥ 0.067); still below USVT (0.135).
14. **E15: covering the modes the query cites adds nothing; feedback hurts.** Weighting F(S)'s modes by the query's own citing vector, with the query link + relevance score as the relevance term, gives 0.166 held out, seed-averaged: the same as the link score alone (−0.000, p = 0.48) and not different from USVT co-citation (−0.008, Holm p = 0.92). With text relevance as the term it is 0.149, below USVT co-citation (Holm p = 0.051). Re-estimating the query's citing role from the model's own top picks makes things worse: −0.008 for the query link (5/19, p = 0.028) and −0.015 for SPECTRA co-citation (7/18, p = 0.008). Every E15 method still beats D-SPECTRA (+0.034 to +0.050).
15. **E16: the β bound is a regulariser, not a limit.** With β_max = 20, β rises to 15 (η = 0) and 19 (d_ev = 8), training NLL falls from 0.103 to 0.006, and held-out citation AUC falls from 0.958 to 0.890 on 63 of 63 fits (held-out NLL 0.87 → 2.57): the looser model overfits. Held-out recall does not improve: D-SPECTRA +0.008 (Holm p = 0.42), η = 0 +0.010 (Holm p = 0.087), query link + relevance −0.002, SPECTRA co-citation +0.003. A +0.03 gain on the 20 design queries (seed 0) did not carry over. β_max = 5 stays.
16. **Bug 4 (section 4).** Householder QR flipped the sign of single columns of U or V during training, negating a whole mode in one step. Before the fix, η = 0 fits stopped at d_ev ≈ 8.5 instead of ≈ 28, the loss jumped, and d_ev drifted 4–12% over the last 1,000 epochs; after it, every fit converges. The refit raised D-SPECTRA by 0.007 and the query link by 0.012 (seed-averaged) and changed several borderline tests (before/after table in section 4), but no headline conclusion.
17. **E17: a second hop of citations hurts.** Graphs six times larger reach 52% of the human-cited references instead of 37%, but every graph method loses recall on them (most-cited by a third, Holm p = 0.002; the query-anchored scores by 0.010–0.015, not significant). Depth 1 stays.
18. **E19: the directed fit is the best citation model we have, and the frontier is flat.** Held-out AUC 0.959 against 0.935 for the best structural baseline and 0.846 for USVT, on all 63 graphs (Holm p < 0.001). Along the η grid, d_ev runs from 4 to 30 and held-out AUC stays within 0.001: every capacity is an equally good citation model, which is why no d_ev target or η rule ever changed a selection.
19. **Judged: the judge does not separate the methods, and the recall gain does not show up as nugget coverage.** With the same writer and judge on the 43 held-out queries, judged nugget coverage is 0.043 for DeepScholar-base's own picks, 0.036–0.070 for our seven methods and 0.089 for the oracle (the human-cited references themselves). No method differs from the baseline after Holm (the oracle's +0.046 has Holm p = 0.099); the query link + relevance list is nominally best (+0.027, 8 wins / 6 losses, p = 0.38) and USVT co-citation + relevance, the best method on recall, nominally worst (−0.007). What the proxy measured does transfer to the judge's **reference coverage** (every graph method above the baseline, query link + relevance +0.088, p < 0.001 uncorrected) and all our lists get a higher coverage-relevance grade (+0.13 to +0.28, p ≤ 0.02 uncorrected), at 89,000 tokens per query against 289,000. The judged endpoint is a tie at this sample size, not a win and not a loss: a 0–1 metric averaging 0.04–0.09 over 43 queries cannot resolve differences of 0.02. **Search seeds 1 and 2 through the same writer and judge (Nov 5–6) give the same answer:** seed-averaged nugget coverage 0.038–0.061 for our methods against 0.043 for the baseline (all Holm ≥ 0.26), the oracle +0.047 (Holm 0.079), reference coverage and coverage relevance above the baseline for every graph list in every seed.
20. **E18: organising the report by the fitted modes is a null by construction.** The judge scores the report's introduction, which DeepScholar-base's writer produces before it builds the taxonomy, so the mode-based taxonomy never reaches the judged text: 188 of 189 judged inputs are byte-identical to the writer's own taxonomy's. The experiment as designed could not have shown an effect.
21. **E20: rank cap 32 is binding by SPECTRA's criterion, by 0.002 AUC.** Held-out link prediction at η = 0 improves from 0.9585 to 0.9607 at cap 64 (59 wins / 4 losses) and 0.9611 at cap 128 (Holm p < 0.001 both), and is flat between 64 and 128, where d_ev stops at 44–46. E9 had shown recall unchanged at those caps; the extra modes improve the citation model by an amount selection cannot feel.
22. **E21: giving the query its own fitted citing role is the best selector against graph ground truth and changes nothing against the human one.** On 1,260 pseudo-queries (pool papers removed from their graph, their in-graph references as the target) a ridge map from text to the fitted citing factors recovers 0.303 at B = 15 (mixed with relevance) against 0.281 for SPECTRA co-citation and 0.244 for USVT co-citation + relevance, winning on 31–42 of 43 held-out graphs (Holm p < 0.001). On the 43 real queries, with the human-cited references as the target, it gets 0.165 against 0.175 and 0.168 (Holm p ≥ 0.64). By the rule written beforehand, the gap that remains is in the human reference lists, not in the predictor.
23. **E22: capacity control starts to matter at half the citations, and the benchmark's graphs sit just above that density.** Refitting the η grid with half of each graph's citations (2,370 instead of 4,704), the smallest model on the grid (d_ev ≈ 4) beats η = 0 (d_ev ≈ 30) on 52 of 63 graphs, by +0.011 held-out AUC (Holm p < 0.001 against the full graphs' −0.001), and the best η is −0.1 on 47 of 63 graphs. At a quarter and a tenth of the citations the frontier turns U-shaped: η = 0 is best again, the intermediate capacities are 0.02–0.13 AUC worse, and the smallest model loses outright at a tenth (−0.083, 59 of 63 graphs). The density at which SPECTRA's η would have changed our fits is a factor of two below DeepScholar-Bench's graphs, and only there; thinner graphs are not helped by the penalty either.

---

## 1. The project and where we are in the plan

For each query, D-SPECTRA builds a local **directed citation graph** (the search results plus their references and citing papers) and fits **directed SPECTRA**: `P(i cites j) = σ(a_i + b_j + β·K_ij)` with `K = n·UΣVᵀ / ‖UΣVᵀ‖_*`. It reads the graph's realized capacity as `d_ev = exp(H(p))` with `p_k = σ_k / Σσ`, controls it with one scalar η, and greedily selects papers that maximise the submodular coverage objective `F(S) = α·Σ r_i/B + (1−α)·Σ_k w_k (1 − e^{−γ z_k(S)})`. The benchmark is **DeepScholar-Bench**: 63 queries, each a real arXiv paper whose related-work section the system must write.

| Step in the proposal | Status | Who |
|---|---|---|
| 1. Reproduce DeepScholar-base and fixed-k with one backbone | **Done for seed 0.** DeepScholar-base runs end to end on all 63 queries × 3 seeds with saved pools, picks, reports and costs; its seed-0 picks and fixed-k's have been written and judged with the same writer and local judge as every other method (3.20). Since the published scores use GPT-4.1 or Llama-4 and the paper's judge is gpt-4o, "reproduced" means running end to end and stable across seeds, not matching their numbers. ResearchQA and DeepResearch Bench II not started | Mateo, Eftychia (judge) |
| 2. Per-query graphs, fit directed SPECTRA and raw SVD; gate: d_ev must correlate with judged coverage | **Done; the gate fails.** Graphs and fits for all 63 queries × 3 search seeds. On recall, higher d_ev(S) goes with lower recall; on the judge's nugget coverage of DeepScholar-base's reports, d_ev(S) does not track it (ρ = −0.07 and −0.03). It tracks claim coverage weakly (E12) | Eftychia |
| 3. Selection-only D-SPECTRA with core ablations | **Done on the proxy** (E6, E8–E17) **and judged on seed 0** (3.20): the judge does not separate D-SPECTRA from the baseline or from any other method. Selection lists for every frozen method and the oracle are exported for all three seeds (E12) | Eftychia |
| 4. Closed-loop acquisition and stopping | Not started; the "coverage lost by stopping early" diagnostic is therefore not done either | — |
| 5. Full runs, seeds, significance, judge spot-checks | **Partly.** Three search seeds and three fit seeds, Holm-corrected paired tests on recall (E12); writer and judge on every frozen list for seed 0 with Holm-corrected paired tests and the cost–coverage frontier (3.20). Not done: seeds 1–2 through the writer and judge, blinded judge spot-checks, a second backbone, the public release | — |

---

## 2. What we did, experiment by experiment

### E1. Synthetic check (planted directed graphs)

- **Input:** planted directed graphs with n = 50, 100, 200, 500 nodes, 4 topic groups and mean out-degree 8. Group g cites itself and group g+1, so direction matters. A few "generic" papers (2–4% of nodes) are cited by every group. 3 random seeds per size.
- **Steps:** hold out 10% of the citations; fit directed SPECTRA at fixed η ∈ {−0.5, −0.2, −0.1, 0, 0.05, 0.1, 0.2, 0.4}; bisect η to targets d_ev ∈ {2, 4, 8}; compare the directed model with the symmetrized model, raw SVD and the directed model without offsets.
- **Measured:** d_ev against η; how close bisection gets to the target; how much of the top mode's mass sits on generic papers; held-out citation AUC; recovery of the planted groups (NMI).
- **Settings:** rank cap 16, 6,000 epochs.
- **Script and output:** `scripts/synthetic_check.py` → `results/synthetic_6000/`.

### E2. Convergence check

- **Input:** 3 OpenAlex graphs from E3.
- **Steps:** fit directed SPECTRA for 6,000 epochs at η = 0 and at the η that hits d_ev = 8 after 1,500 epochs; log the loss and d_ev every 100 epochs.
- **Script and output:** `scripts/convergence_check.py` → `results/convergence/` (rerun after bug 4; the pre-fix run is in `results/pre_qrfix/convergence/`).

### E3. OpenAlex pilot (all 63 queries)

Built on Oct 20, before Mateo's pools existed, so it uses **our own search**, not DeepScholar-base's. **Its fits were not redone after bug 4** (section 4): its D-SPECTRA, η = 0 and symmetrized numbers come from the buggy optimizer and are kept only because the pattern (citations help, D-SPECTRA ≈ relevance only, USVT best) is the same as in E6.

- **Graphs:** for each query, an OpenAlex keyword search (the title, the title after any "Acronym:" prefix, and 3 frequent phrases) returns 50 seeds published before the query paper. We add the 300 references cited by the most seeds and the 150 papers citing the most top-20 seeds (also before the query date), merge duplicate records by title, and drop any work whose title is ≥ 90% similar to the query's. Citation edges come from OpenAlex. About 489 papers per graph.
- **Ground truth:** the references cited in the query's related-work section (`citations.csv`), matched to graph papers by DOI or arXiv ID (only if the titles agree) and by title otherwise; the benchmark's "important" subset is kept too.
- **Fits:** directed SPECTRA with d_ev targeted to 8 (and 4, 16 as sensitivity checks), η = 0, and the undirected model on A + Aᵀ; rank cap 32, 6,000 epochs.
- **Selection:** every method picks B ∈ {10, 20, 30, 45, 60} papers; we measure recall of the human-cited references.
- **Scripts and output:** `scripts/build_graphs.py` → `data/graphs_v2/`; `scripts/pilot_selection.py` → `results/pilot_v2/`.

### E4. DeepScholar-base reproduction (Mateo)

- **Pilot:** the first 20 queries, run three times on an RTX 3090 (twice arXiv-only, once arXiv + web), Qwen3-8B-AWQ through vLLM, thinking off, recursive search with 3 rounds × 2 queries × 50 results. Four bugs in DeepScholar fixed in a wrapper.
- **Final runs:** all 63 queries × seeds 0, 1, 2, arXiv only, 2 rounds × 2 queries × 50 results, temperature 0.7 / top_p 0.8 / top_k 20. Saved per query and seed: the frozen candidate pool (`pool_all.csv`), the papers DeepScholar's filter kept (`kept.csv`), the report's references, the report, and costs (`costs.csv`).
- **Where:** branch `pools-pilot` of the repo, `pools/` and `outputs/dsbase_final/`.

### E5. Pool diagnostics (Mateo's 20 pilot pools)

- **Steps:** look up every pool paper by arXiv ID in OpenAlex and in Semantic Scholar; count citations *between* pool papers; count how many human-cited references each pool contains.
- **Scripts and output:** `scripts/pool_graphs.py` (OpenAlex) → `data/pool_graphs/`; `scripts/pool_edges_s2.py` (Semantic Scholar) → `data/pool_graphs/s2_edges.csv`.
- **Caveat:** these numbers were affected by bug 3 (about 12% of pool papers missing; section 4).

### E6. Main run: the proposal's version on Mateo's 63 final pools

This is the main experiment. It follows the proposal: start from DeepScholar-base's frozen pool, add citations, fit directed SPECTRA, select.

- **Input:** Mateo's final seed-0 pools for all 63 queries (`pools/final_r2_s0/`, 103 papers per pool on average, 38–157) and DeepScholar-base's own picks for the same seed (`outputs/dsbase_final/s0/*/kept.csv`).
- **Graphs:** every pool paper is a candidate (bug-3 fix). Pool papers are looked up in Semantic Scholar by arXiv ID (OpenAlex lacks reference lists for most of these preprints). We then add (1) the **top 250 references**, ranked by how many pool papers cite them, and (2) the **top 130 citing papers** published before the query paper, ranked by how many pool papers they cite. Ties are broken by order of appearance. Anything whose title is ≥ 90% similar to the query's is removed. Pool papers Semantic Scholar does not know stay in without citation links. There is no hard cap: graphs end up at about pool size + 380 papers.
- **Fits:** directed SPECTRA with d_ev targeted to 8, η = 0, and the undirected model; rank cap 32, 6,000 epochs, learning rate 1e-2, cold-start bisection. For the 20 design queries only, also d_ev targets 4 and 16.
- **Two settings:** **expanded** (any paper in the graph may be picked; the proposal's version) and **pool-only** (only Mateo's pool papers may be picked; the model is still fitted on the whole graph).
- **Budgets:** B ∈ {10, 20, 30, 45, 60} and **B = kept**: exactly the number of DeepScholar's kept papers for that query, which is the fair comparison (the writer receives that many papers).
- **Baselines:** DeepScholar-base's own picks, fixed-k (top-B by relevance from the pool), relevance only over the expanded graph (the main ablation, α = 1), most-cited in the graph, Vendi, semantic modes, symmetrized SPECTRA, raw SVD, USVT, and D-SPECTRA with η = 0.
- **Split:** the 20 pilot queries are the **design** set (used for all decisions so far); the other **43 are held out** and are reported separately. This run is frozen as the held-out result: nothing is tuned on the 43.
- **Protocol notes:** one fit seed (0) and one search seed (Mateo's seed 0); the optimizer settings are kept as pre-registered even though they look unstable (E2), and any later learning-rate change will be reported separately.
- **Extra checks in the evaluation:** leakage (title look-alikes of the query, largest share of answers cited by one node), pool papers with no citation link, abstract coverage of each method's picks, the fixed-budget d_ev(S) test, and the premise check.
- **Scripts and output:** `scripts/build_pool_expanded.py` → `data/graphs_dsf/`, now superseded by `data/graphs_small/` (the same graphs with query 2506.00832 rebuilt from Mateo's updated pool), which every result below uses. Fits: `scripts/fit_variants.py --fits d8 eta0 cv` → `results/e8_small/operators/`, with the d_ev 4 and 16 targets (design queries) and the undirected model added by `scripts/fit_sensitivity.py`; the undirected fits were copied from the pre-fix run for the 62 byte-identical graphs (bug 4 cannot affect Q S² Qᵀ) and refitted for 2506.00832. Evaluation: `scripts/pilot_selection.py --operators results/e8_small/operators --kept_dir ...` → `results/pilot_dsf/` (expanded) and `results/pilot_dsf_strict/` (pool-only). The pre-fix run is in `results/pre_qrfix/pilot_dsf*/`. Selection lists: `scripts/export_final.py` → `selections/final/` (E12).

### E7. Review checks

Two rounds of review of the analysis led to: B = 20 and the matched budget reported next to B = 60, most-cited as a required baseline, a dev/test split, a fixed-budget version of the d_ev(S) test, leakage and abstract checks, and the fairness protocol. These checks uncovered **three bugs in my graph builders** (section 4). All were fixed and the affected results recomputed or replaced.

### E8. Method variants and bigger graphs

Started after E6, from a review of its results. It uses the same pools and evaluation as E6, with Mateo's updated pool for query 2506.00832 (the stale query in E6).

- **Bigger graphs:** the top 500 references and top 260 citing papers instead of 250 and 130, so about 860 papers instead of 480 (`data/graphs_big/`). The current-size graphs are E6's, with 2506.00832 rebuilt (`data/graphs_small/`).
- **η by held-out link prediction** (`dspectra_cv`). This is our addition, not SPECTRA's rule: the paper reports η = 0 or bisects η to d_ev targets taken from the baselines' effective ranks, never choosing on validation or test data (that rule is E14). Its link-prediction protocol removes 50% of the edges and keeps the training graph connected; ours holds out 10% uniformly.
  - hold out 10% of the citations and as many non-citations;
  - fit at η ∈ {−0.10, −0.06, −0.03, 0, 0.02, 0.04, 0.06};
  - keep the η with the highest held-out AUC and refit on the whole graph.
- **The query as a new citing node** (`qlink<m>_<fit>`):
  - the query's citing factor and offset are the relevance-weighted means of the m most relevant pool papers that have a reference list (m ∈ {5, 10, 20});
  - every paper is scored by the model's log-odds that the query cites it, a_q + b_j + β·K_qj. This uses the query's citing role against each paper's cited role, and brings popularity back in through b_j.
  - `qlinkrel<m>_<fit>` averages this score with relevance on a rank scale.
- **Mode weights anchored on the pool** (`poolU_<fit>`, `poolV_<fit>`):
  - w_k ∝ p_k · Σ_{i ∈ pool} r_i F_ik², with F the citing (U) or cited (V) factors, instead of the whole graph's relevance-weighted mass;
  - selection is otherwise as in D-SPECTRA.
- **Fits:** each variant runs on three fits: d_ev = 8 (`d8`), η by held-out links (`cv`) and η = 0 (`eta0`).
- **Selection rule, written down before any E8 result:**
  - There are three families: query link, query link + relevance, and pool-anchored weights.
  - In each family, the configuration with the highest mean recall at B = kept on the 20 design queries (expanded setting) is the one reported on the 43 held-out queries. This is decided separately for each graph size, and ties go to the higher recall at B = 20.
  - All other configurations are exploratory.
- **Settings:** as in E6 (rank cap 32, 6,000 epochs, α = 0.5, γ = 5, one fit seed), on GPU 1 only.
- **Scripts:** `scripts/build_pool_expanded.py --n_refs 500 --n_citers 260`, `scripts/fit_variants.py`, `scripts/pilot_selection.py --variants`.

### E9. The remaining SPECTRA ingredients

What the SPECTRA paper and code use that E1–E8 had not tried. Same pools, graphs (`data/graphs_small/`) and evaluation as E8; fits on GPU 1 only.

- **Spectral prefixes:**
  - SPECTRA's nested family: the fitted kernel truncated to its top k modes, k ∈ {4, 8, 16}, with the normalisation unchanged.
  - Applied to D-SPECTRA (the d_ev = 8 fit) and to E8's chosen query-link configurations, using E8's fits. No refitting.
- **Rank caps (overparameterisation, the paper's central claim):**
  - D-SPECTRA fitted with rank caps 64 and 128 at d_ev = 8, plus η = 0 at each;
  - a rank cap of 8 at η = 0, which is the paper's "rank cap only" baseline at the target capacity;
  - all compared with rank cap 32 (E8).
- **Early-stopped η probes:**
  - SPECTRA's cheap-probe protocol: each probe stops once d_ev is stable, then the chosen η is refitted for the full 6,000 epochs.
  - SPECTRA's defaults are used: checks every 100 epochs from epoch 500, the last 5 checks within 2% of their mean, 3 checks in a row.
- **Criteria for choosing η:** the E8 grid and held-out split, choosing by held-out AUC (as in E8), average precision, or the lowest held-out NLL.
- **Seeds and restarts:**
  - fit seeds 1 and 2 for the d_ev = 8 and η = 0 fits, to go with E8's seed 0;
  - "best of 3": per query and fit, the seed with the lowest training NLL, which is SPECTRA's restart selection.
- **Rules, written down before any E9 result:**
  - For prefixes, k ∈ {4, 8, 16, all 32} is chosen per family on the 20 design queries, by recall at B = kept (ties: B = 20, then all modes). The fit and the number of anchor papers are fixed to E8's choices.
  - Everything else is a fixed comparison, reported on the held-out queries with nothing chosen.
- **Scripts:** `scripts/fit_variants.py --fits es8 | --rank 8/64/128 | --fits cv cvap cvnll | --seed 1/2`; `scripts/pilot_selection.py --variants [--prefixes 4 8 16]`.

### E10. Selection hyperparameters, learning-rate schedule, search seeds

The plan's remaining method items (except the writer and judge).

- **Selection hyperparameters**, on E8's fits with no refitting:
  - D-SPECTRA's α (the weight on relevance) ∈ {0.25, 0.5, 0.75, 0.9} and γ (coverage saturation) ∈ {1, 2, 5, 10, 20};
  - for query link + relevance, the weight on the link score ∈ {0.25, 0.5, 0.75}.
- **Learning-rate schedule:**
  - cosine decay from 1e-2 to 1e-4 over the 6,000 epochs, for the d_ev = 8 and η = 0 fits;
  - against the constant 1e-2 of E1–E9, with an η = 0 refit at the constant rate that records the same convergence diagnostics;
  - diagnostics: d_ev drift over the last 1,000 epochs, and whether the loss ends above its minimum (the E2 instability).
- **Search seeds 1 and 2:**
  - graphs built from Mateo's seed-1 and seed-2 pools (same construction as E6);
  - d_ev = 8 and η = 0 fits;
  - every method evaluated against DeepScholar-base's own picks for that seed.
- **Rules, written down before any E10 result:**
  - α, γ and the link weight are chosen on the 20 design queries by recall at B = kept (ties: B = 20, then the defaults α = 0.5, γ = 5, weight 0.5).
  - The schedule and the search seeds are fixed comparisons using E8's chosen configurations.
- **Scripts:** `scripts/tune_selection.py`; `scripts/fit_variants.py --lr_schedule cosine`; `scripts/build_pool_expanded.py --pools pools/final_r2_s{1,2}`.

### E11. What else helps the query link

Evaluation only, on E8's fits (current-size graphs, seed 0). The anchors are the m most relevant pool papers with a reference list (m ∈ {5, 10, 20}), weighted by relevance. "+ relevance" means averaged with relevance on a rank scale, with weight 0.5 or 0.75 on the other score.

- **Co-citation, no model** (`cocite<m>`): the relevance-weighted number of anchors that cite each paper (bibliographic coupling). This tests whether the fitted model adds anything to "what do the most relevant pool papers cite".
- **The same on the USVT-denoised citation matrix** (`usvtlink<m>`): low-rank denoising without the directed model.
- **D-SPECTRA v2** (`v2_a<α>_g<γ>`): D-SPECTRA's F(S) with the tuned query link + relevance score in place of text relevance, so that mode coverage sits on top of the link prediction. α ∈ {0.25, 0.5, 0.75, 0.9}, γ ∈ {1, 2, 5, 10}.
- **Fusion with USVT** (`rrf<w>`): reciprocal-rank fusion (k = 60) of the tuned query link + relevance and USVT's selection, with weight w ∈ {0.25, 0.5, 0.75} on the query link.
- **The query's citing role from its own text** (`qtext<ridge>`):
  - per graph, a ridge regression (penalty 1, 10 or 100) from the text embeddings of papers with a reference list to their fitted citing factors and offsets, applied to the query's title and abstract;
  - this replaces the anchor average.
- **Rule, written down before any E11 result:** per family, the configuration with the highest mean recall at B = kept on the 20 design queries is the one reported on the 43 held-out queries (ties: B = 20).
- **Script:** `scripts/variants_e11.py`.

### E13. Can the fitted SPECTRA model itself win?

Evaluation only, on the existing d_ev = 8 and η = 0 fits of all three search seeds.

- **SPECTRA co-citation** (`scocite_<fit>_k<k>_m<m>[_obs]`):
  - each paper is scored by the relevance-weighted mean of the m most relevant pool papers' predicted citation probabilities P(i cites j), excluding self-citation;
  - this is the exact counterpart of E11's USVT co-citation, which averages the anchors' rows of the USVT-denoised matrix;
  - `_obs` adds the observed citations;
  - the kernel is truncated to its top k modes (k ∈ {2, 4, 8, 16, 32}), which tests capacity as a denoising knob;
  - m ∈ {5, 10}, the score is mixed with relevance at 0.75, and the fit is η = 0 or d_ev = 8.
- **Learned rankers:**
  - logistic regression with fixed settings (C = 1, balanced classes), trained on the design queries only;
  - features: relevance, co-citation, USVT co-citation, SPECTRA co-citation (fixed in advance as η = 0, all modes, 10 anchors), SPECTRA's popularity offset b_j, in-graph citations and paper type;
  - the same ranker without the two SPECTRA features, to see whether the model adds information.
- **Rule, written down before any E13 result:**
  - The SPECTRA co-citation configuration is chosen on seed 0's design queries and reported unchanged on the held-out queries and on seeds 1 and 2.
  - The capacity curve and the rankers are fixed comparisons.
- **Script:** `scripts/variants_e13.py`.

### E12. Final checks

- **Frozen methods exported** for the shared writer and judge: `scripts/export_final.py` → `selections/final/s{0,1,2}/`, one list per method per search seed, as many papers as DeepScholar-base kept for the query.
- **The step-2 gate on judged coverage:** DeepScholar-base's seed-0 reports scored by the local judge (section 3.11); d_ev(S) of the papers each report cites, and of all papers passed to the writer, correlated with each judged metric across queries, with and without controlling for |S| (`scripts/gate_judged.py`).
- **Seed-averaged, Holm-corrected tests:** per-query recall at B = kept averaged over search seeds 0–2, paired Wilcoxon on the 43 held-out queries, Holm over 16 pre-listed comparisons (`scripts/seed_tests.py`). The same for E13's 8 comparisons and E14's 8.
- **Cost per query:** tokens for each method and budget, from Mateo's per-stage token counts (the writer's tokens grow linearly with the number of papers passed).

### E14. SPECTRA's own capacity rule

What the SPECTRA paper actually does with η: fix d_ev targets from the baselines' realised effective ranks, with no validation or test data.

- **Targets, per query:** `tmin` = the smaller of USVT's and raw SVD's (rank 32) effective rank, in practice always USVT's (14–30 across our graphs, median 22); `tmed` = their median (about 25). Effective rank is measured as our d_ev is, exp(H(p)) with p ∝ singular values.
- **Fits:** bisection on η to each target; rank 32, 6,000 epochs, fit seed 0, all three search seeds (`scripts/fit_variants.py --fits tmin tmed`).
- **Selection:** D-SPECTRA's greedy F(S), α = 0.5, γ = 5.
- **Rules, written down before any result** (`e14.sh`): recall at B = kept, seed-averaged per query, 43 held-out queries, Wilcoxon with Holm over the 8 comparisons {tmin, tmed} × {relevance only, USVT, D-SPECTRA d_ev = 8, η = 0}; tmin is the primary setting.

### E15. The query's citing role as the centre of selection

Evaluation only, on the existing η = 0 and d_ev = 8 fits of all three search seeds (`scripts/variants_e15.py`). The premise check says the papers humans cite are *concentrated*, not spread, over the graph's modes, so E15 tries coverage of the modes the query itself cites, and lets the model refine its own picture of the query.

- **Query-anchored mode weights** (`qmodes_<fit>_m<m>_<score>_a<α>_g<γ>`): D-SPECTRA's greedy F(S) with w_k ∝ p_k (u_q,k σ_k)², where u_q is the relevance-weighted mean citing factor of the m most relevant pool papers with a reference list (m ∈ {5, 10}). This covers the modes the query cites, not the modes the graph has. The relevance term is either text relevance (`r`) or the tuned query link + relevance score (`ql`, weight 0.75 on the link). α ∈ {0.25, 0.5, 0.75}, γ ∈ {1, 2, 5}, fit η = 0 or d_ev = 8.
- **Pseudo-relevance feedback on the query link** (`prf<k>_r<rounds>[_keep]`): score with the 10 most relevant anchors, then re-estimate u_q and a_q from the top-k papers of the query link + relevance score, weighted by that score (k ∈ {5, 10, 20}, 1 or 2 rounds); `_keep` adds the feedback papers to the original anchors instead of replacing them. Fit η = 0.
- **The same on SPECTRA co-citation** (`sprf<k>_r<rounds>[_keep]`): the anchors' predicted citation probabilities (E13's chosen setting: η = 0, 5 anchors, all 32 modes), re-anchored on its own top-k picks.
- **Frozen comparison methods**, recomputed in the same script and checked against E11 and E13: USVT co-citation + relevance, co-citation + relevance, query link + relevance, SPECTRA co-citation + relevance.
- **Rules, written down before any result** (`e15.sh`): four families (query-anchored modes on text relevance, on the link score, feedback on the query link, feedback on SPECTRA co-citation). Per family, the configuration with the highest mean recall at B = kept on the 20 design queries of seed 0 is reported on the 43 held-out queries, seed-averaged (ties: B = 20, then the first in sorted order), with Holm over its 16 comparisons against USVT co-citation + relevance, SPECTRA co-citation + relevance, query link + relevance and D-SPECTRA.

### E16. The β ceiling

β is bounded by 5 (SPECTRA's own bound) and the audit found it at that bound in every fit, so the slope of the kernel was never free. A 20-query pilot (the design queries, seed 0, β_max = 20) showed +0.03 recall for D-SPECTRA and −0.05 for query link + relevance, so the full run was done.

- **Fits:** every query on all three search seeds refitted with β_max = 20 (fit seed 0, rank 32, 6,000 epochs): η = 0, d_ev = 8, and the held-out-link fit (`cv`, the E8 grid with 10% of citations held out), so held-out citation AUC can be compared with the β_max = 5 fits (`scripts/fit_variants.py --beta_max 20`).
- **Evaluations:** the same as for the β_max = 5 fits (`pilot_selection.py --variants`, `variants_e11.py`, `variants_e13.py`).
- **Rule, written down before any held-out result** (`e16_beta.sh`): a fixed comparison, β_max 20 vs 5, same method, 43 held-out queries, seed-averaged recall at B = kept, Holm over the four methods {D-SPECTRA, η = 0, query link + relevance, SPECTRA co-citation + relevance}. Held-out citation AUC is compared the same way.

### E17. A second hop of citations

The one untried change to the input after E16: our graphs (≈480 nodes) are far smaller than SPECTRA's and reach only 37% of the references humans cite.

- **Graphs:** search seed 0 only; the E8 build plus the 2,500 most-cited references of the first-hop papers (ranked by how many first-hop papers cite them, `build_pool_expanded.py --n_refs2 2500`). Second-hop papers were fetched without their own reference lists (Semantic Scholar's rate limits), so they have incoming edges only. Same embeddings model, same cutoff date.
- **Fits and evaluations:** η = 0 and d_ev = 8 at rank 32, the E8–E13 selection settings unchanged.
- **Rule, written down before results** (`e17_depth2.sh`): depth 2 vs depth 1, same method, held-out 43, recall at B = kept, paired Wilcoxon, Holm over six methods {USVT co-citation + relevance, SPECTRA co-citation + relevance, query link + relevance, USVT, relevance only, D-SPECTRA}. The table adds co-citation + relevance and most-cited and corrects over all eight, which is the more conservative choice.

### E19. SPECTRA's own evaluation, and the capacity frontier

What re-reading SPECTRA against our fits suggested (rules in `e19_e20_rules.md`, written first): SPECTRA's own test is held-out link prediction at matched parameters, which we had never reported; and our held-out AUC is flat in η, which in SPECTRA's terms is a flat capacity frontier.

- **E19a, link prediction:** all 63 depth-1 graphs, the cv fits' split (10% of citations held out plus as many non-citations, seed 0). The fit at η = 0 (SPECTRA's default; its AUC and AP recorded by the cv fit, trained without the held-out pairs) against baselines with no fitted parameters scored on the training citations: truncated SVD at rank 32, USVT, preferential attachment, in-degree, bibliographic-coupling paths. Paired Wilcoxon over the 63 graphs, Holm over the five baselines, AUC primary and AP secondary. No design/held-out split, since nothing is tuned.
- **E19b, frontier:** per query, held-out AUC against d_ev along the cv fits' η grid at rank cap 32 (descriptive, SPECTRA's Figure 2 on our graphs).
- **E20:** held-out AUC at rank caps 64 and 128 (cv fits only; E9 already has η = 0 and d_ev = 8 at those caps and the unchanged recall), to place the graphs in SPECTRA's "saturated" or "rank-cap-binding" regime by its own criterion. Rule (same file): AUC at η = 0 for caps 64 and 128 against cap 32, paired Wilcoxon over the 63 graphs, Holm over the two caps; the frontier redrawn with three caps, descriptive.

### E21. An inductive citing role for the query (cold start)

E19 showed the directed fit predicts citations far better than any structural baseline, yet as a selector it only ties USVT co-citation (E13). One reason suggested itself: every selector approximates the query by averaging a few anchor papers, because the query has no reference list and so no fitted citing role. E21 gives it one: a ridge map from the text embedding to the fitted citing factors U, learned on the graph's own nodes, applied to the query's abstract; the query is then scored by the model's own row, b_j + β·n·(u_q σ)·V_j / Σσ.

- **Rules, written before any result** (`scratchpad/e21_rules.md`). Primary: pseudo-queries. Per graph up to 20 pool papers with at least five in-graph references are removed entirely (no edges either way), the rest is fitted once at η = 0 (E8 settings), the ridge map (penalty by leave-one-out GCV) is trained on the fitted nodes with outgoing edges, and each pseudo-query is scored from its own text; ground truth is its in-graph references; recall at B = 15 (primary) and 30. Methods with the E10–E13 settings frozen: relevance only, USVT co-citation + relevance, SPECTRA co-citation + relevance, query link + relevance, the inductive role alone and mixed with relevance (0.75). Unit = graph (mean over its pseudo-queries), 43 held-out graphs, paired Wilcoxon, Holm over two comparisons (inductive + relevance vs USVT co-citation + relevance and vs SPECTRA co-citation + relevance). Secondary, read only if the primary wins: the same map on the full E8 fits applied to the 43 real held-out queries, recall of the human-cited references at B = kept, Holm over the same two.
- **Code:** `scripts/coldstart_e21.py` (stages fit, eval, real, tests) → `results/e21/`.

### E22. The sparsification frontier: when would capacity control have mattered?

E19 and E20 found the held-out capacity frontier flat: every d_ev from 4 to 45 predicts the held-out citations equally well, which is why no η rule or d_ev target ever changed a selection. That flatness may be a property of these graphs (4,700 citations each on average) rather than of the model. E22 removes citations at random and refits the η grid, to find the density at which the spectral penalty would have changed the fits and to place the benchmark's graphs relative to it.

- **Rules, written before any run** (`scratchpad/sparse_rules.md`). The 63 depth-1 graphs with all nodes kept and a random fraction keep ∈ {0.5, 0.25, 0.1} of the citations (one generator seed per graph, the same at every level); the cv fit as in E8 (`fit_variants.py --fits cv --edge_keep`: the 7-η grid from −0.1 to 0.06, rank 32, 6,000 epochs, β_max = 5, 10% of the remaining citations held out plus as many non-citations); keep = 1.0 is E8's cv fit. Per graph: gain = best held-out AUC on the grid − AUC at η = 0; low = AUC at η = −0.1 (d_ev ≈ 4) − AUC at η = 0; d_ev at η = 0 and at the best η. Primary: gain at each level against gain at 1.0, paired Wilcoxon over the 63 graphs, Holm over the three levels; secondary: low the same way; descriptive: the mean frontier per level. Predictions: (1) gain grows as keep falls and is significant at 0.1; (2) the best η moves negative; (3) at 0.1, low > 0; (4) if 1–3 hold, the benchmark's graphs are saturated by a factor of four or more. No selection reruns: the question is about the frontier.
- **Code:** `scripts/sparse_frontier.sh` (the fits, GPU 1, six workers, two hours per level) → `results/sparse_k{50,25,10}/operators/`; `scripts/sparse_frontier.py` → `results/sparse/` (`stats.csv`, `tests.csv`, `summary.md`, `frontier_sparse.png`).

### The judged evaluation: every frozen list through the same writer and judge

The endpoint the recall proxy stood in for. Search seed 0, all 63 queries.

- **Systems (nine):** DeepScholar-base's own kept lists, rerun through our writer so that the baseline and the methods share one writer version (`judge/run_writer.py`, Qwen3-8B-AWQ, localhost); fixed-k; relevance only; D-SPECTRA (d_ev = 8); co-citation + relevance; USVT co-citation + relevance; SPECTRA co-citation + relevance; query link + relevance; and the oracle (the human-cited references themselves, as many as the writer sees elsewhere). Each list has as many papers as DeepScholar-base kept for the query (21 on average). The writer is DeepScholar-base's own pipeline from the point after its filter (intro → taxonomy → insights → report), same prompts, model, sampling and seed for all; its search "background" is not stored, so it is empty for every system including the rerun.
- **Judge:** the local Llama-3.1-70B judge of 3.11, all seven metrics, one system at a time (three at once overloaded the 70B and timed out). One report could not be judged (the oracle's query 42: the writer linked no papers).
- **Rules, written down before the comparison was computed** (`scratchpad/judged_rules.md`): nugget coverage primary; unit = query; the 43 held-out queries; family 1 = each system vs the DeepScholar-base rerun, paired Wilcoxon, Holm over 8; family 2 = USVT co-citation + relevance (the frozen pick) vs D-SPECTRA and vs relevance only, Holm over 2; every other metric reported with uncorrected p and no claim; cost by the E12 token model; the frontier descriptive.
- **Two metrics are unusable from these runs** and are reported as such: organization is 0.5 on every report (the judge prefers whichever section it sees first, as in E12), and document importance looks every cited title up on OpenAlex, which answered "429 rate limit" during most judge runs, so it is 0 on every report of seven of the nine systems.

### E18. The fitted modes as the report's taxonomy

The one place the spectral modes could help the *report* rather than the *list*: DeepScholar-base's writer groups the papers into categories with an LLM taxonomy; E18 replaces that taxonomy with the fitted modes (each paper goes to its dominant cited-role mode on the η = 0 fit, singletons to "Others", and the LLM only names each group), on the three graph lists (D-SPECTRA, SPECTRA co-citation, USVT co-citation), same writer and judge.

- **Rule, written before any result** (`judge/e18_chain.sh`): paired per query, mode taxonomy vs the writer's own on the same list, 63 queries, Wilcoxon; primary metrics organization and nugget coverage, Holm over 3 lists × 2 metrics; the rest without a claim.
- **Design flaw, found when the scores came back identical:** DeepScholar-Bench's parser for this system scores `intro.md`, the report up to its "Research papers" section, and the writer generates that introduction *before* it builds the taxonomy. The taxonomy only shapes the paper listing the judge never reads. So the judged input is byte-identical between the two taxonomies on 188 of 189 reports, and E18 is a null by construction (3.21).

### Decisions and settings

| Topic | Decision | Why |
|---|---|---|
| Backbone | **Qwen3-8B-AWQ**, local via vLLM, thinking off, 32k context | Qwen3-4B passed only 2–3 papers per query through DeepScholar's filter; 8B keeps about 22 |
| Search corpus | **arXiv only**, recursive search (2 rounds × 2 queries) | Matches the DeepScholar paper; web search added no arXiv coverage, leaked ≈5 post-cutoff papers per query, and the model searched for the target paper by name |
| Sampling | Qwen's non-thinking settings (0.7 / 0.8 / 20), seeds 0–2 | Temperature 1.0 was the repo default for GPT-5-mini |
| Frozen pools | Every system selects from the same frozen pool per query and seed | Two identical search runs share only 46% of their papers |
| Citation source | **Semantic Scholar** for Mateo's pools; OpenAlex for the E3 pilot | OpenAlex has reference lists for few recent arXiv preprints |
| Graph for the pools | Fit on the pool **plus** references and citing papers; evaluate expanded and pool-only | Pool papers rarely cite each other; the proposal adds references and citing papers anyway |
| Date cutoff | Only works published before the query paper | Proposal's fairness rule |
| Other versions of the query paper | Excluded: titles ≥ 90% similar to the query's | Bug 1 (section 4) |
| Dev / test split | Design on the 20 pilot queries, claim on the other 43 | Only 63 queries; all were seen in the recall-only E3 pilot |
| Loss | Exact likelihood over all non-edges (balanced) | Graphs have ≤ ~530 nodes; SPECTRA samples 5 non-edges per edge |
| Training length | 6,000 epochs | SPECTRA's default. With bug 4 fixed, fits converge well before that (d_ev drift 0.0% over the last 1,000 epochs) |
| Main ablation | Both readings are reported: α = 1 (no coverage term, relevance only, which is the same method as "citation expansion only") and η = 0 (no capacity control) | The proposal's "without the spectral term" can mean either; the two give different answers (section 3.13) |
| How η is chosen | Bisection to a fixed d_ev = 8 (main), η = 0, SPECTRA's baseline-rank targets (E14), and our own held-out-AUC rule (E8) | SPECTRA itself uses η = 0 or baseline-rank targets, never validation data |
| F(S) scaling | z_k divided by each mode's relevant mass; relevance term divided by B | Puts both terms on one scale; still submodular |
| d_ev(S) | exp(entropy) of q_k ∝ p_k·Σ_{i∈S} r_i V_ik² | Same per-mode quantity the objective uses |
| Ground truth | References cited in the related-work section; also the "important" subset | Retrieval proxy until the judge runs |
| Reference matching | DOI or arXiv ID first (only if titles agree), title otherwise | OpenAlex sometimes attaches a DOI to the wrong record |
| Papers passed to the writer | As many as DeepScholar kept for that query ("B = kept") | Otherwise systems are not comparable |
| Judge | The released evaluation code with a **local Llama-3.1-70B-Instruct** (GPTQ 4-bit, vLLM), same for every system; see 3.11 | No paid key; scores are comparable between our systems but not with the paper's gpt-4o scores |
| Who runs the writer | Mateo runs every method's selection list through the same writer and judge | Same prompt, model, sampling and seeds for all methods |
| Closed loop (step 4) | Compared with a relevance-driven expansion at the same lookup budget | It grows the frozen pool |

| Setting | Value |
|---|---|
| Rank cap | 32 (16 in E1) |
| Training | 6,000 epochs, Adam, learning rate 1e-2, 200-epoch bias warm-up |
| Regularisation | λ = 1e-4 on β and offsets; β bounded by 5, initial β = 1. β reaches the bound in every fit; lifting it to 20 overfits the held-out links and does not raise recall (E16), so 5 is kept |
| η search | from η = 0, step 0.1, doubling, \|η\| ≤ 10, bisection to 2% tolerance, cold-start probes. With the fixed optimizer d_ev moves in discrete steps as a mode switches off, so the 2% tolerance is often not reachable: over the 3 search seeds the d_ev = 8 fits land within 2% on 54% of queries, within 5% on 97%, worst 8%, mean 8.00 |
| β | Bounded by 5 (SPECTRA's bound). It sits at the ceiling in every fit (mean 4.993–4.994), so the kernel's scale is capped; whether this confounds d_ev has not been tested |
| Target d_ev | 8 (4 and 16 as sensitivity checks: E3 all queries, E6 design queries) |
| Selection | α = 0.5, γ = 5 |
| Relevance r_i | bge-m3 cosine between the query (title + abstract) and the paper (title + abstract), rescaled to [0, 1] within each graph |

### Methods compared

| Method | What it selects |
|---|---|
| **DeepScholar-base's own picks** (`deepscholar_kept`) | The papers DeepScholar's LLM filter kept (E6 only, at B = kept) |
| **fixed-k (search only)** (`search_only`) | Top-B by relevance among the pool / search results only |
| **relevance only (main ablation)** (`relevance_only`) | Top-B by relevance from all candidates (α = 1); on the expanded graph, also "citation expansion only" |
| `most_cited` | Top-B by number of citations inside the graph |
| `vendi` | Greedy relevance + Vendi score on text embeddings |
| `semantic_modes` | F(S) on modes of the text-embedding matrix |
| `symmetrized` | F(S) on undirected SPECTRA fitted to A + Aᵀ |
| `raw_svd`, `usvt` | F(S) on the SVD of the citation matrix, without and with universal singular-value thresholding |
| `dspectra_eta0` | F(S) on directed SPECTRA fitted with η = 0 |
| **`dspectra`** | **D-SPECTRA**: F(S) on directed SPECTRA with d_ev targeted to 8 |
| `dspectra_d4`, `dspectra_d16` | D-SPECTRA with d_ev targeted to 4 and 16 |
| `dspectra_cv` (E8) | D-SPECTRA with η chosen by held-out link prediction |
| `qlink<m>_<fit>` (E8) | Top-B by the model's log-odds that the query cites the paper; the query's citing factor comes from the m most relevant pool papers |
| `qlinkrel<m>_<fit>` (E8) | The same score averaged with relevance on a rank scale |
| `poolU_<fit>`, `poolV_<fit>` (E8) | D-SPECTRA with mode weights anchored on the search pool (its citing or cited factors) |
| `dspectra_<fit>_k<k>`, `qlink*_k<k>` (E9) | The same with the kernel truncated to its top k modes |
| `dspectra_es`, `dspectra_cvap`, `dspectra_cvnll` (E9) | D-SPECTRA with early-stopped η probes; η chosen by held-out average precision or NLL |
| `qlinkrel10_eta0_l0.75` = `qlink_rel` (E10) | Query link + relevance with weight 0.75 on the link score (the frozen method) |
| `cocite<m>`, `cocite_rel` (E11) | Top-B by the relevance-weighted count of the m most relevant pool papers citing each paper (bibliographic coupling), alone or mixed with relevance (weight 0.75) |
| `usvtlink<m>`, `usvt_cocite_rel` (E11) | The same count on the USVT-denoised citation matrix |
| `v2_a<α>_g<γ>`, `rrf<w>`, `qtext<ridge>` (E11) | D-SPECTRA's F(S) on the link score; rank fusion with USVT; the query's citing role predicted from its text |
| `scocite_<fit>_k<k>_m<m>[_obs]` (E13) | The anchors' mean predicted citation probability under the fitted model, mixed with relevance |
| `learned`, `learned_nospectra` (E13) | Logistic-regression rankers trained on the design queries, with and without the SPECTRA features |
| `dspectra_tmin`, `dspectra_tmed` (E14) | D-SPECTRA with d_ev targeted to USVT's effective rank, or to the median of USVT's and raw SVD's |
| `qmodes_<fit>_m<m>_<r|ql>_a<α>_g<γ>` (E15) | D-SPECTRA's F(S) with mode weights w_k ∝ p_k (u_q,k σ_k)², the modes the query's citing vector loads on; relevance term = text relevance or the query link + relevance score |
| `prf<k>_r<rounds>[_keep]`, `sprf<k>_r<rounds>[_keep]` (E15) | Query link + relevance, or SPECTRA co-citation + relevance, with the query's citing role re-estimated from its own top-k picks (pseudo-relevance feedback) |
| β_max = 20 fits (E16) | The same methods on fits with the β bound raised from 5 to 20 |
| `oracle` (E12, exported only) | The benchmark's important human-cited references: the ideal-sources upper bound |

---

## 3. Results

### 3.1 Main run (E6): the proposal's version on the 63 final pools

**The graphs**

**Size, isolated pool papers and reference coverage**

|                                        | held-out (43)    | design (20)     | all (63)         |
|:---------------------------------------|:-----------------|:----------------|:-----------------|
| queries                                | 43               | 20              | 63               |
| nodes (mean)                           | 484              | 483             | 483              |
| edges (mean)                           | 4339             | 5487            | 4704             |
| pool papers (mean)                     | 105              | 104             | 104              |
| pool papers not in Semantic Scholar    | 3.7%             | 2.1%            | 3.2%             |
| pool papers with no citation link      | 23.3%            | 19.2%           | 22.0%            |
| human-cited refs in the pool           | 69/1120 = 6.2%   | 31/510 = 6.1%   | 100/1630 = 6.1%  |
| human-cited refs in the expanded graph | 392/1120 = 35.0% | 213/510 = 41.8% | 605/1630 = 37.1% |

Leakage check: graphs with a node title at least 80% similar to the query: 3 — 2506.01071 (0.82: Decoupled Contrastive Learning for Long-Tailed Recognition); 2505.21811 (0.81: Mixed Attention Network for Cross-domain Sequential Recommen); 2505.22458 (0.89: FDA: Fourier Domain Adaptation for Semantic Segmentation). Largest share of a query's reachable references cited by a single node: median 0.74, max 1.00 over 52 graphs; 8 graphs have a node citing all of them. Nodes dated on or after the query's date: 0 of 30444 (1876 undated).

**Held-out queries (43), expanded setting: the main result.** Recall of the references the human authors cited. "B = kept" is the matched budget. Blank cells are not missing runs: DeepScholar-base's own picks exist only at B = kept, because its filter decides how many papers to keep.

**Recall of related-work references (41 queries with a reference in the graph)**

| method                         | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks   | 0.047    |        |        |        |        |        |
| fixed-k (search only)          | 0.059    | 0.043  | 0.054  | 0.067  | 0.069  | 0.069  |
| relevance only (main ablation) | 0.090    | 0.053  | 0.089  | 0.119  | 0.146  | 0.173  |
| most_cited                     | 0.096    | 0.062  | 0.099  | 0.121  | 0.154  | 0.175  |
| vendi                          | 0.068    | 0.038  | 0.068  | 0.098  | 0.139  | 0.171  |
| semantic_modes                 | 0.091    | 0.055  | 0.084  | 0.120  | 0.150  | 0.164  |
| symmetrized                    | 0.094    | 0.063  | 0.101  | 0.124  | 0.153  | 0.185  |
| raw_svd                        | 0.134    | 0.073  | 0.126  | 0.161  | 0.203  | 0.231  |
| usvt                           | 0.138    | 0.079  | 0.134  | 0.165  | 0.204  | 0.230  |
| dspectra_eta0                  | 0.122    | 0.076  | 0.118  | 0.143  | 0.186  | 0.214  |
| dspectra                       | 0.120    | 0.080  | 0.117  | 0.142  | 0.182  | 0.214  |

**D-SPECTRA minus each method (wins/losses, paired Wilcoxon p)**

|                                | B=kept                  | B=10                    | B=20                    | B=30                    | B=45                    | B=60                    |
|:-------------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|
| DeepScholar-base's own picks   | +0.073 (29/5, p=<0.001) |                         |                         |                         |                         |                         |
| fixed-k (search only)          | +0.061 (29/6, p=<0.001) | +0.037 (26/4, p=<0.001) | +0.063 (29/5, p=<0.001) | +0.074 (32/7, p=<0.001) | +0.113 (33/5, p=<0.001) | +0.145 (34/4, p=<0.001) |
| relevance only (main ablation) | +0.030 (22/5, p=0.006)  | +0.027 (21/4, p=0.002)  | +0.028 (21/5, p=0.009)  | +0.023 (20/6, p=0.052)  | +0.036 (23/5, p=0.002)  | +0.041 (29/7, p=0.002)  |
| most_cited                     | +0.024 (19/15, p=0.194) | +0.018 (22/14, p=0.217) | +0.018 (19/17, p=0.375) | +0.021 (19/16, p=0.294) | +0.029 (19/13, p=0.094) | +0.039 (24/10, p=0.046) |
| vendi                          | +0.052 (25/2, p=<0.001) | +0.042 (21/3, p=<0.001) | +0.050 (23/2, p=<0.001) | +0.044 (26/4, p=0.001)  | +0.044 (27/4, p=<0.001) | +0.043 (25/6, p=<0.001) |
| semantic_modes                 | +0.029 (20/6, p=0.013)  | +0.025 (20/5, p=0.003)  | +0.033 (21/7, p=0.013)  | +0.022 (19/7, p=0.062)  | +0.032 (23/8, p=0.024)  | +0.050 (27/5, p=<0.001) |
| symmetrized                    | +0.026 (21/7, p=0.038)  | +0.017 (20/4, p=0.032)  | +0.016 (19/10, p=0.184) | +0.018 (19/8, p=0.136)  | +0.029 (21/5, p=0.005)  | +0.029 (23/5, p=0.004)  |
| raw_svd                        | -0.014 (9/16, p=0.087)  | +0.007 (15/11, p=0.374) | -0.009 (8/16, p=0.331)  | -0.019 (6/16, p=0.032)  | -0.021 (8/18, p=0.050)  | -0.017 (9/16, p=0.109)  |
| usvt                           | -0.018 (10/19, p=0.066) | +0.001 (14/12, p=0.790) | -0.017 (8/18, p=0.032)  | -0.023 (7/20, p=0.025)  | -0.022 (9/19, p=0.036)  | -0.016 (11/17, p=0.122) |
| dspectra_eta0                  | -0.002 (9/13, p=0.770)  | +0.004 (9/6, p=0.201)   | -0.000 (8/9, p=0.962)   | -0.002 (10/12, p=0.808) | -0.003 (7/10, p=0.478)  | +0.001 (10/9, p=0.952)  |

**Share of the reachable references recovered (pooled, 392 reachable)**

| method                         | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks   | 0.117    |        |        |        |        |        |
| fixed-k (search only)          | 0.151    | 0.110  | 0.135  | 0.168  | 0.173  | 0.173  |
| relevance only (main ablation) | 0.230    | 0.143  | 0.230  | 0.304  | 0.378  | 0.446  |
| most_cited                     | 0.255    | 0.161  | 0.255  | 0.314  | 0.395  | 0.446  |
| vendi                          | 0.179    | 0.110  | 0.179  | 0.253  | 0.355  | 0.436  |
| semantic_modes                 | 0.230    | 0.148  | 0.222  | 0.306  | 0.385  | 0.423  |
| symmetrized                    | 0.245    | 0.166  | 0.258  | 0.324  | 0.403  | 0.477  |
| raw_svd                        | 0.360    | 0.202  | 0.334  | 0.434  | 0.536  | 0.610  |
| usvt                           | 0.367    | 0.214  | 0.357  | 0.444  | 0.536  | 0.612  |
| dspectra_eta0                  | 0.327    | 0.202  | 0.306  | 0.383  | 0.497  | 0.574  |
| dspectra                       | 0.314    | 0.209  | 0.306  | 0.372  | 0.490  | 0.577  |

**Recall of important references (41 queries with a reference in the graph)**

| method                         | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks   | 0.066    |        |        |        |        |        |
| fixed-k (search only)          | 0.084    | 0.063  | 0.078  | 0.095  | 0.098  | 0.098  |
| relevance only (main ablation) | 0.123    | 0.077  | 0.122  | 0.158  | 0.195  | 0.227  |
| most_cited                     | 0.124    | 0.082  | 0.129  | 0.153  | 0.194  | 0.214  |
| vendi                          | 0.093    | 0.058  | 0.092  | 0.134  | 0.183  | 0.224  |
| semantic_modes                 | 0.124    | 0.080  | 0.118  | 0.160  | 0.199  | 0.214  |
| symmetrized                    | 0.127    | 0.089  | 0.135  | 0.164  | 0.200  | 0.241  |
| raw_svd                        | 0.180    | 0.099  | 0.169  | 0.216  | 0.271  | 0.306  |
| usvt                           | 0.181    | 0.107  | 0.180  | 0.223  | 0.272  | 0.304  |
| dspectra_eta0                  | 0.164    | 0.102  | 0.158  | 0.190  | 0.247  | 0.284  |
| dspectra                       | 0.160    | 0.109  | 0.155  | 0.187  | 0.240  | 0.285  |

**Held-out queries (43), pool-only setting** (every method picks only from Mateo's pool). Here fixed-k and relevance-only are the same method (top-B pool papers by relevance), so their rows are identical. DeepScholar-base's picks and fixed-k are also the same in both settings, since they only ever pick from the pool.

**Recall of related-work references (41 queries with a reference in the graph)**

| method                         | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks   | 0.047    |        |        |        |        |        |
| fixed-k (search only)          | 0.059    | 0.043  | 0.054  | 0.067  | 0.069  | 0.069  |
| relevance only (main ablation) | 0.059    | 0.043  | 0.054  | 0.067  | 0.069  | 0.069  |
| most_cited                     | 0.060    | 0.045  | 0.057  | 0.066  | 0.069  | 0.070  |
| vendi                          | 0.048    | 0.029  | 0.044  | 0.057  | 0.069  | 0.069  |
| semantic_modes                 | 0.060    | 0.042  | 0.053  | 0.065  | 0.069  | 0.069  |
| symmetrized                    | 0.063    | 0.047  | 0.060  | 0.069  | 0.069  | 0.069  |
| raw_svd                        | 0.065    | 0.053  | 0.063  | 0.069  | 0.070  | 0.070  |
| usvt                           | 0.065    | 0.055  | 0.063  | 0.069  | 0.070  | 0.070  |
| dspectra_eta0                  | 0.066    | 0.050  | 0.065  | 0.069  | 0.070  | 0.070  |
| dspectra                       | 0.067    | 0.049  | 0.067  | 0.068  | 0.070  | 0.070  |

**D-SPECTRA minus each method (wins/losses, paired Wilcoxon p)**

|                                | B=kept                 | B=10                   | B=20                    | B=30                  | B=45                  | B=60                  |
|:-------------------------------|:-----------------------|:-----------------------|:------------------------|:----------------------|:----------------------|:----------------------|
| DeepScholar-base's own picks   | +0.019 (15/1, p=0.001) |                        |                         |                       |                       |                       |
| fixed-k (search only)          | +0.007 (7/0, p=0.018)  | +0.006 (7/2, p=0.173)  | +0.013 (11/0, p=0.003)  | +0.000 (2/1, p=1.000) | +0.001 (1/0, p=0.317) | +0.001 (1/0, p=0.317) |
| relevance only (main ablation) | +0.007 (7/0, p=0.018)  | +0.006 (7/2, p=0.173)  | +0.013 (11/0, p=0.003)  | +0.000 (2/1, p=1.000) | +0.001 (1/0, p=0.317) | +0.001 (1/0, p=0.317) |
| most_cited                     | +0.007 (6/1, p=0.043)  | +0.004 (9/6, p=0.589)  | +0.009 (8/1, p=0.021)   | +0.002 (3/1, p=0.273) | +0.002 (1/0, p=0.317) | +0.000 (0/0, p=1.000) |
| vendi                          | +0.019 (13/0, p=0.001) | +0.021 (12/0, p=0.002) | +0.023 (15/0, p=<0.001) | +0.011 (8/0, p=0.012) | +0.002 (1/0, p=0.317) | +0.001 (1/0, p=0.317) |
| semantic_modes                 | +0.007 (7/0, p=0.018)  | +0.007 (7/2, p=0.110)  | +0.013 (11/0, p=0.003)  | +0.002 (3/0, p=0.109) | +0.002 (1/0, p=0.317) | +0.001 (1/0, p=0.317) |
| symmetrized                    | +0.004 (4/0, p=0.068)  | +0.002 (5/3, p=0.575)  | +0.007 (7/0, p=0.018)   | -0.001 (1/1, p=0.655) | +0.002 (1/0, p=0.317) | +0.001 (1/0, p=0.317) |
| raw_svd                        | +0.001 (2/1, p=0.593)  | -0.004 (2/5, p=0.176)  | +0.003 (3/1, p=0.144)   | -0.001 (0/1, p=0.317) | +0.000 (0/0, p=1.000) | +0.000 (0/0, p=1.000) |
| usvt                           | +0.001 (2/1, p=0.593)  | -0.005 (2/6, p=0.093)  | +0.003 (3/1, p=0.144)   | -0.001 (0/1, p=0.317) | +0.000 (0/0, p=1.000) | +0.000 (0/0, p=1.000) |
| dspectra_eta0                  | +0.000 (1/1, p=0.655)  | -0.001 (2/3, p=0.893)  | +0.002 (2/0, p=0.180)   | -0.001 (0/1, p=0.317) | +0.000 (0/0, p=1.000) | +0.000 (0/0, p=1.000) |

**Share of the reachable references recovered (pooled, 69 reachable)**

| method                         | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks   | 0.667    |        |        |        |        |        |
| fixed-k (search only)          | 0.855    | 0.623  | 0.768  | 0.957  | 0.986  | 0.986  |
| relevance only (main ablation) | 0.855    | 0.623  | 0.768  | 0.957  | 0.986  | 0.986  |
| most_cited                     | 0.855    | 0.652  | 0.826  | 0.942  | 0.986  | 1.000  |
| vendi                          | 0.681    | 0.420  | 0.638  | 0.812  | 0.971  | 0.986  |
| semantic_modes                 | 0.855    | 0.609  | 0.768  | 0.928  | 0.971  | 0.986  |
| symmetrized                    | 0.899    | 0.681  | 0.855  | 0.971  | 0.971  | 0.986  |
| raw_svd                        | 0.942    | 0.768  | 0.913  | 0.986  | 1.000  | 1.000  |
| usvt                           | 0.942    | 0.783  | 0.913  | 0.986  | 1.000  | 1.000  |
| dspectra_eta0                  | 0.957    | 0.725  | 0.928  | 0.986  | 1.000  | 1.000  |
| dspectra                       | 0.957    | 0.710  | 0.957  | 0.971  | 1.000  | 1.000  |

**Design queries (20), expanded setting** (including d_ev targets 4 and 16)

**Recall of related-work references (17 queries with a reference in the graph)**

| method                         | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks   | 0.040    |        |        |        |        |        |
| fixed-k (search only)          | 0.041    | 0.022  | 0.036  | 0.045  | 0.060  | 0.062  |
| relevance only (main ablation) | 0.076    | 0.040  | 0.065  | 0.083  | 0.114  | 0.144  |
| most_cited                     | 0.186    | 0.110  | 0.163  | 0.200  | 0.227  | 0.264  |
| vendi                          | 0.076    | 0.027  | 0.065  | 0.097  | 0.118  | 0.149  |
| semantic_modes                 | 0.085    | 0.039  | 0.064  | 0.094  | 0.131  | 0.157  |
| symmetrized                    | 0.085    | 0.039  | 0.070  | 0.104  | 0.150  | 0.188  |
| raw_svd                        | 0.209    | 0.116  | 0.168  | 0.226  | 0.274  | 0.291  |
| usvt                           | 0.205    | 0.114  | 0.180  | 0.227  | 0.265  | 0.289  |
| dspectra_eta0                  | 0.161    | 0.071  | 0.129  | 0.176  | 0.227  | 0.265  |
| dspectra_d4                    | 0.078    | 0.030  | 0.066  | 0.087  | 0.178  | 0.222  |
| dspectra                       | 0.119    | 0.054  | 0.095  | 0.138  | 0.187  | 0.237  |
| dspectra_d16                   | 0.151    | 0.066  | 0.122  | 0.166  | 0.225  | 0.256  |

**D-SPECTRA minus each method (wins/losses, paired Wilcoxon p)**

|                                | B=kept                 | B=10                   | B=20                   | B=30                    | B=45                    | B=60                    |
|:-------------------------------|:-----------------------|:-----------------------|:-----------------------|:------------------------|:------------------------|:------------------------|
| DeepScholar-base's own picks   | +0.079 (13/1, p=0.002) |                        |                        |                         |                         |                         |
| fixed-k (search only)          | +0.078 (13/0, p=0.001) | +0.031 (10/0, p=0.005) | +0.059 (10/2, p=0.005) | +0.093 (15/0, p=<0.001) | +0.128 (15/0, p=<0.001) | +0.175 (15/0, p=<0.001) |
| relevance only (main ablation) | +0.043 (9/1, p=0.017)  | +0.014 (6/0, p=0.028)  | +0.029 (8/2, p=0.074)  | +0.055 (11/0, p=0.003)  | +0.074 (13/0, p=0.001)  | +0.093 (13/0, p=0.001)  |
| most_cited                     | -0.067 (5/9, p=0.090)  | -0.056 (4/7, p=0.131)  | -0.069 (5/8, p=0.263)  | -0.062 (4/10, p=0.187)  | -0.040 (6/9, p=0.211)   | -0.028 (6/8, p=0.397)   |
| vendi                          | +0.043 (8/1, p=0.011)  | +0.027 (9/1, p=0.013)  | +0.029 (6/2, p=0.035)  | +0.041 (9/0, p=0.008)   | +0.069 (11/1, p=0.005)  | +0.088 (13/0, p=0.001)  |
| semantic_modes                 | +0.034 (10/2, p=0.041) | +0.015 (6/1, p=0.063)  | +0.030 (8/2, p=0.047)  | +0.044 (12/1, p=0.023)  | +0.056 (11/1, p=0.003)  | +0.080 (13/1, p=0.001)  |
| symmetrized                    | +0.034 (10/1, p=0.013) | +0.015 (5/0, p=0.043)  | +0.024 (9/2, p=0.109)  | +0.034 (10/1, p=0.008)  | +0.037 (9/2, p=0.018)   | +0.048 (10/2, p=0.005)  |
| raw_svd                        | -0.090 (1/10, p=0.004) | -0.062 (0/10, p=0.005) | -0.074 (3/10, p=0.006) | -0.088 (1/10, p=0.008)  | -0.087 (1/11, p=0.004)  | -0.054 (0/10, p=0.005)  |
| usvt                           | -0.086 (2/9, p=0.010)  | -0.060 (1/9, p=0.007)  | -0.086 (2/10, p=0.005) | -0.089 (1/10, p=0.008)  | -0.077 (1/12, p=0.002)  | -0.053 (0/10, p=0.005)  |
| dspectra_eta0                  | -0.042 (0/8, p=0.012)  | -0.017 (0/7, p=0.018)  | -0.035 (1/10, p=0.013) | -0.038 (1/7, p=0.036)   | -0.039 (2/7, p=0.066)   | -0.028 (1/9, p=0.047)   |
| dspectra_d4                    | +0.041 (7/0, p=0.018)  | +0.024 (7/0, p=0.018)  | +0.028 (10/3, p=0.152) | +0.051 (11/0, p=0.003)  | +0.009 (7/3, p=0.575)   | +0.014 (7/3, p=0.285)   |
| dspectra_d16                   | -0.032 (0/8, p=0.012)  | -0.012 (0/6, p=0.028)  | -0.028 (1/9, p=0.022)  | -0.027 (1/8, p=0.051)   | -0.038 (0/6, p=0.028)   | -0.020 (2/9, p=0.110)   |

**All 63 queries, expanded setting**

**Recall of related-work references (58 queries with a reference in the graph)**

| method                         | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks   | 0.045    |        |        |        |        |        |
| fixed-k (search only)          | 0.054    | 0.037  | 0.049  | 0.061  | 0.067  | 0.067  |
| relevance only (main ablation) | 0.086    | 0.049  | 0.082  | 0.108  | 0.137  | 0.165  |
| most_cited                     | 0.122    | 0.076  | 0.118  | 0.144  | 0.175  | 0.201  |
| vendi                          | 0.071    | 0.035  | 0.067  | 0.098  | 0.133  | 0.165  |
| semantic_modes                 | 0.089    | 0.051  | 0.078  | 0.112  | 0.145  | 0.162  |
| symmetrized                    | 0.091    | 0.056  | 0.092  | 0.118  | 0.152  | 0.186  |
| raw_svd                        | 0.156    | 0.085  | 0.139  | 0.180  | 0.224  | 0.249  |
| usvt                           | 0.158    | 0.089  | 0.148  | 0.183  | 0.222  | 0.248  |
| dspectra_eta0                  | 0.133    | 0.074  | 0.121  | 0.153  | 0.198  | 0.229  |
| dspectra                       | 0.120    | 0.072  | 0.111  | 0.141  | 0.184  | 0.221  |

**D-SPECTRA minus each method (wins/losses, paired Wilcoxon p)**

|                                | B=kept                  | B=10                    | B=20                     | B=30                    | B=45                     | B=60                    |
|:-------------------------------|:------------------------|:------------------------|:-------------------------|:------------------------|:-------------------------|:------------------------|
| DeepScholar-base's own picks   | +0.075 (42/6, p=<0.001) |                         |                          |                         |                          |                         |
| fixed-k (search only)          | +0.066 (42/6, p=<0.001) | +0.035 (36/4, p=<0.001) | +0.062 (39/7, p=<0.001)  | +0.080 (47/7, p=<0.001) | +0.117 (48/5, p=<0.001)  | +0.154 (49/4, p=<0.001) |
| relevance only (main ablation) | +0.034 (31/6, p=<0.001) | +0.023 (27/4, p=<0.001) | +0.028 (29/7, p=0.002)   | +0.032 (31/6, p=0.001)  | +0.047 (36/5, p=<0.001)  | +0.056 (42/7, p=<0.001) |
| most_cited                     | -0.002 (24/24, p=0.862) | -0.003 (26/21, p=0.828) | -0.007 (24/25, p=0.905)  | -0.003 (23/26, p=0.877) | +0.009 (25/22, p=0.415)  | +0.020 (30/18, p=0.186) |
| vendi                          | +0.049 (33/3, p=<0.001) | +0.038 (30/4, p=<0.001) | +0.044 (29/4, p=<0.001)  | +0.043 (35/4, p=<0.001) | +0.051 (38/5, p=<0.001)  | +0.056 (38/6, p=<0.001) |
| semantic_modes                 | +0.031 (30/8, p=0.001)  | +0.022 (26/6, p=<0.001) | +0.032 (29/9, p=0.002)   | +0.029 (31/8, p=0.006)  | +0.039 (34/9, p=<0.001)  | +0.059 (40/6, p=<0.001) |
| symmetrized                    | +0.029 (31/8, p=0.002)  | +0.016 (25/4, p=0.006)  | +0.019 (28/12, p=0.053)  | +0.023 (29/9, p=0.012)  | +0.032 (30/7, p=<0.001)  | +0.035 (33/7, p=<0.001) |
| raw_svd                        | -0.036 (10/26, p=0.001) | -0.013 (15/21, p=0.223) | -0.028 (11/26, p=0.005)  | -0.039 (7/26, p=<0.001) | -0.040 (9/29, p=<0.001)  | -0.028 (9/26, p=0.002)  |
| usvt                           | -0.038 (12/28, p=0.002) | -0.017 (15/21, p=0.096) | -0.037 (10/28, p=<0.001) | -0.042 (8/30, p=<0.001) | -0.038 (10/31, p=<0.001) | -0.027 (11/27, p=0.003) |
| dspectra_eta0                  | -0.013 (9/21, p=0.069)  | -0.002 (9/13, p=0.770)  | -0.010 (9/19, p=0.083)   | -0.012 (11/19, p=0.106) | -0.014 (9/17, p=0.075)   | -0.008 (11/18, p=0.210) |

**Premise check and the fixed-budget d_ev(S) test**

**Premise check (human-cited set vs same-size relevance-ranked set)**

|               | queries   | d_ev(S) human-cited   | d_ev(S) relevance-ranked   | d_ev(S) random   | human higher   | p (Wilcoxon)   |
|:--------------|:----------|:----------------------|:---------------------------|:-----------------|:---------------|:---------------|
| held-out (43) | 36        | 5.52                  | 6.29                       | 6.90             | 10/36          | 0.001          |
| design (20)   | 16        | 6.01                  | 6.10                       | 7.04             | 7/16           | 0.632          |
| all (63)      | 52        | 5.67                  | 6.23                       | 6.95             | 17/52          | 0.004          |

DeepScholar's kept papers found in the graphs: 1342 of 1355 (99.0%); matched budget per query: mean 21.3 (min 3, max 30).

*Expanded setting:*

**Spearman of d_ev(S) with recall at a fixed budget, across methods**

|                                      | B=kept       | B=10         | B=20         | B=30         | B=45         | B=60         |
|:-------------------------------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|
| held-out (43): rho of method means   | -0.47        | -0.46        | -0.35        | -0.05        | -0.06        | -0.16        |
| held-out (43): within-query mean rho | -0.19 (n=39) | -0.15 (n=38) | -0.12 (n=39) | -0.13 (n=41) | -0.13 (n=41) | -0.15 (n=41) |
| design (20): rho of method means     | -0.53        | -0.14        | -0.63        | -0.41        | -0.57        | -0.34        |
| design (20): within-query mean rho   | -0.11 (n=15) | -0.13 (n=15) | -0.10 (n=15) | -0.02 (n=16) | -0.10 (n=16) | -0.06 (n=16) |
| all (63): rho of method means        | -0.59        | -0.69        | -0.61        | -0.38        | -0.39        | -0.39        |
| all (63): within-query mean rho      | -0.19 (n=54) | -0.15 (n=53) | -0.13 (n=54) | -0.12 (n=57) | -0.13 (n=57) | -0.14 (n=57) |

*Pool-only setting* (n counts the queries where the methods' recall differs at all; few do at large budgets, where every method gets everything in the pool):

**Spearman of d_ev(S) with recall at a fixed budget, across methods**

|                                      | B=kept       | B=10         | B=20         | B=30         | B=45        | B=60        |
|:-------------------------------------|:-------------|:-------------|:-------------|:-------------|:------------|:------------|
| held-out (43): rho of method means   | +0.75        | +0.38        | +0.80        | +0.45        | +0.49       | +0.64       |
| held-out (43): within-query mean rho | +0.03 (n=21) | -0.11 (n=22) | +0.03 (n=19) | +0.08 (n=11) | -0.23 (n=2) | +0.88 (n=1) |
| design (20): rho of method means     | +0.37        | -0.07        | +0.58        | +0.78        | +0.52       | +0.23       |
| design (20): within-query mean rho   | +0.28 (n=10) | +0.02 (n=9)  | +0.12 (n=9)  | +0.00 (n=7)  | -0.00 (n=5) | -0.17 (n=4) |
| all (63): rho of method means        | +0.72        | +0.17        | +0.86        | +0.77        | +0.50       | +0.42       |
| all (63): within-query mean rho      | +0.10 (n=31) | -0.07 (n=31) | +0.05 (n=27) | +0.02 (n=18) | -0.09 (n=7) | +0.02 (n=5) |

**Abstract coverage and costs**

**Share of selected papers (B=kept) that have an abstract**

|                                | with abstract   |
|:-------------------------------|:----------------|
| DeepScholar-base's own picks   | 1.00            |
| fixed-k (search only)          | 1.00            |
| relevance only (main ablation) | 1.00            |
| most_cited                     | 0.80            |
| vendi                          | 0.97            |
| semantic_modes                 | 0.98            |
| symmetrized                    | 1.00            |
| raw_svd                        | 0.96            |
| usvt                           | 0.97            |
| dspectra_eta0                  | 0.98            |
| dspectra_d4                    | 0.98            |
| dspectra                       | 0.99            |
| dspectra_d16                   | 1.00            |

**Costs per query**

|                                                 | DeepScholar-base (Mateo, seed 0)       | D-SPECTRA pipeline (DeepScholar's search, our selection, the same writer)                                                            |
|:------------------------------------------------|:---------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| wall time per query                             | 3.6 min (search + filter + writer)     | search and writer as DeepScholar, plus 29.2 min of fitting (3 fits, shared GPUs, 12 jobs in parallel) and graph building (not timed) |
| LLM calls per query                             | 215 (all stages; not logged per stage) | 0 for selection; search and writer calls unchanged                                                                                   |
| tokens: search stage                            | 43,761                                 | same                                                                                                                                 |
| tokens: filter stage                            | 195,733 (69%)                          | 0 (replaced by the fit)                                                                                                              |
| tokens: writer stages (taxonomize + generation) | 45,002                                 | about the same (same number of papers; not run yet)                                                                                  |
| tokens: total                                   | 284,496                                | ≈88,763 (estimate)                                                                                                                   |
| arXiv requests per query                        | 5.0                                    | same, plus ≈12 Semantic Scholar batch requests                                                                                       |
| pool / kept papers                              | 103 / 21.2                             | same pool; same number of papers at B=kept                                                                                           |

**Takeaways (E6).**

- **The graphs.** There are 483 papers and 4,704 citations per graph on average, and 104 of the papers are pool papers. DeepScholar's pool holds 6.1% of the human-cited references; adding references and citing papers raises that to 37.1%. 3.2% of pool papers are unknown to Semantic Scholar, and 22.0% have no citation link in the graph. All of them stay in as candidates.
- **Held-out, expanded, B = kept (the main comparison).**
  - D-SPECTRA (0.120) beats:
    - DeepScholar-base's own picks (0.047, p < 0.001)
    - fixed-k (0.059, p < 0.001)
    - relevance-only over the same graph (0.090, p = 0.006)
    - Vendi (0.068, p < 0.001)
    - semantic modes (0.091, p = 0.013)
    - symmetrized SPECTRA (0.094, p = 0.038)
  - The gains over relevance-only (+0.023 to +0.041) hold at every budget (p ≤ 0.009 except B = 30, p = 0.052), and over fixed-k everywhere (p < 0.001).
  - In pooled terms, D-SPECTRA recovers 31.4% of the reachable references at B = kept, against 11.7% for DeepScholar's picks.
  - The important-reference subset shows the same ordering (0.160 vs 0.066 for DeepScholar).
- **Where it loses.**
  - Most-cited ties on the held-out queries (0.096, p = 0.19) and is ahead on the design queries (0.186 vs 0.119, p = 0.09).
  - USVT and raw SVD are the best methods overall: on the held-out queries USVT beats D-SPECTRA at B = 20, 30 and 45 (p ≤ 0.036) and is ahead at B = kept (0.138, p = 0.066); raw SVD is ahead at B = 30 (p = 0.032).
  - On all 63 queries, both beat D-SPECTRA at the matched budget (p ≤ 0.002). Their picks are more concentrated on the dominant, heavily cited modes.
- **η, the proposal's capacity control.**
  - Held out: target 8 (0.120) and η = 0 (0.122, d_ev ≈ 28) differ by at most 0.004 at any budget, with no significant difference.
  - Design queries: *more* capacity is better. η = 0 (0.161) beats target 8 (0.119) at every budget (0 wins / 8 losses at B = kept, p = 0.012), target 16 (0.151) beats it (p = 0.012), and target 4 (0.078) is worse (p = 0.018).
  - That ordering does not appear on the held-out queries, where every capacity setting gives 0.114–0.122 (E14 adds targets 14–30: 0.117–0.119). Capacity control has no reliable effect.
- **Pool-only setting.**
  - The pool holds only 69 reachable references across the 43 held-out queries. Every method gets most of them: 85–96% at B = kept, except DeepScholar's own picks (67%) and Vendi (68%).
  - D-SPECTRA beats DeepScholar's picks (+0.019, p = 0.001), fixed-k (+0.007, p = 0.018) and Vendi. It ties raw SVD, USVT and η = 0.
  - Fixed-k and relevance-only are identical here by construction: both take the top-B pool papers by relevance.
- **Premise and the fixed-budget d_ev(S) test.**
  - On 36 held-out queries, the human-cited set has d_ev(S) 5.52, the same-size relevance-ranked set 6.29 and a random set 6.90. The human set is higher in only 10 of the 36 (p = 0.001). On all 63: 5.67 vs 6.23 (p = 0.004). On the 16 design queries the two are the same (6.01 vs 6.10, p = 0.63).
  - At a fixed budget, d_ev(S) of a method's picks is negatively related to its recall: Spearman of method means −0.47 at B = kept on the held-out queries (−0.05 to −0.47 across budgets), and the within-query mean is −0.12 to −0.19. Before bug 4 was fixed these were −0.77 to −0.88; the relation is weaker now but never positive in the expanded setting.
  - In the pool-only setting the method means correlate positively (+0.38 to +0.80), but every method there gets nearly everything the pool holds, the within-query correlations are about zero, and few queries differ at all, so this says little.
  - **The proposal's own success test** ("scores track achieved d_ev(S) better than |S|, sweeping B"): within a query, over every method × budget cell, recall correlates with |S| at ρ = +0.55 and with d_ev(S) at ρ = +0.17 (57 queries). The test fails on recall. On the judge's scores it fails too (E12, section 3.13).
  - The proposal's gate, "d_ev must correlate with coverage", is therefore not passed on recall or on judged nugget coverage.
- **Abstracts.** 99% of D-SPECTRA's picks have an abstract. Most-cited is the exception (80%): heavily cited older papers often lack one in Semantic Scholar, which matters once the writer has to read them.
- **Costs.**
  - D-SPECTRA replaces only DeepScholar's filter stage, which uses 195,733 of its 284,496 tokens per query (69%). The search (43,761 tokens) and the writer (45,002) are unchanged.
  - D-SPECTRA's selection makes no LLM calls, but it is slower in wall time. The cost table's 29 minutes is for three fits (the d_ev = 8 search, η = 0 and the held-out-AUC search) with 12 jobs sharing one GPU; on a free GPU one 6,000-epoch fit takes about 18 s and the d_ev = 8 search (about 10 probes) about 4 minutes, plus graph building, which we did not time. DeepScholar-base takes 3.6 minutes end to end.
  - The proposal promises matched per-query budgets, so the final report has to give wall time as well as LLM calls; citation lookups (about 12 Semantic Scholar batch requests per query) are reported but not yet charged against a matched budget.
  - DeepScholar's kept papers were found in our graphs for 1,342 of 1,355 picks (99%), so the matched-budget comparison is on the same papers.

### 3.2 E1: synthetic check

**Mean d_ev by graph size n (rows) and eta (columns)**

| n   | -0.5   | -0.2   | -0.1   | 0.0   | 0.05   | 0.1   | 0.2   | 0.4   |
|:----|:-------|:-------|:-------|:------|:-------|:------|:------|:------|
| 50  | 1.00   | 3.92   | 7.32   | 13.80 | 14.45  | 14.82 | 15.22 | 15.59 |
| 100 | 1.00   | 3.86   | 9.02   | 15.00 | 15.29  | 15.47 | 15.67 | 15.83 |
| 200 | 1.00   | 3.88   | 10.46  | 15.48 | 15.65  | 15.75 | 15.85 | 15.93 |
| 500 | 1.00   | 3.62   | 11.89  | 15.74 | 15.83  | 15.88 | 15.93 | 15.97 |

**Bisection to a target d_ev (mean over 3 seeds)**

|            | achieved   | max_rel_err   | probes   | seconds   |
|:-----------|:-----------|:--------------|:---------|:----------|
| (50, 2.0)  | 2.010      | 0.017         | 9.667    | 1265.710  |
| (50, 4.0)  | 3.924      | 0.090         | 14.667   | 1866.276  |
| (50, 8.0)  | 8.089      | 0.022         | 7.667    | 974.755   |
| (100, 2.0) | 2.005      | 0.014         | 11.333   | 1477.407  |
| (100, 4.0) | 3.820      | 0.095         | 13.000   | 1654.779  |
| (100, 8.0) | 8.091      | 0.046         | 14.000   | 1776.023  |
| (200, 2.0) | 2.014      | 0.011         | 8.667    | 1138.762  |
| (200, 4.0) | 3.899      | 0.034         | 12.333   | 1568.787  |
| (200, 8.0) | 7.716      | 0.040         | 14.000   | 1779.615  |
| (500, 2.0) | 1.984      | 0.011         | 8.667    | 1138.731  |
| (500, 4.0) | 3.910      | 0.031         | 11.333   | 1441.477  |
| (500, 8.0) | 7.813      | 0.027         | 13.333   | 1695.054  |

Targets hit within 5%: 31/36; within 10%: 36/36.

**Share of the top mode's mass on generic popular papers (lower is better)**

| variant             | 50    | 100   | 200   | 500   |
|:--------------------|:------|:------|:------|:------|
| directed            | 0.034 | 0.013 | 0.011 | 0.024 |
| directed_no_offsets | 0.157 | 0.154 | 0.175 | 0.185 |
| raw_svd             | 0.349 | 0.333 | 0.650 | 0.763 |
| symmetrized         | 0.028 | 0.020 | 0.013 | 0.023 |

**Held-out citation AUC**

| variant             | 50    | 100   | 200   | 500   |
|:--------------------|:------|:------|:------|:------|
| directed            | 0.752 | 0.720 | 0.718 | 0.739 |
| directed_no_offsets | 0.662 | 0.682 | 0.685 | 0.679 |
| symmetrized         | 0.596 | 0.607 | 0.663 | 0.663 |

Generic papers are [0.02, 0.02, 0.02, 0.04] of nodes for n = 50, 100, 200, 500.

**Planted-group recovery (NMI, higher is better)**

| variant                 | 50    | 100   | 200   | 500   |
|:------------------------|:------|:------|:------|:------|
| directed                | 0.510 | 0.424 | 0.536 | 0.404 |
| directed_citing_role(U) | 0.587 | 0.543 | 0.484 | 0.593 |
| directed_no_offsets     | 0.521 | 0.433 | 0.465 | 0.373 |
| raw_svd                 | 0.551 | 0.427 | 0.521 | 0.310 |
| symmetrized             | 0.474 | 0.470 | 0.499 | 0.390 |

**Mean held-out citation AUC by n and eta**

| n   | -0.5   | -0.2   | -0.1   | 0.0   | 0.05   | 0.1   | 0.2   | 0.4   |
|:----|:-------|:-------|:-------|:------|:-------|:------|:------|:------|
| 50  | 0.725  | 0.753  | 0.724  | 0.713 | 0.703  | 0.696 | 0.680 | 0.659 |
| 100 | 0.692  | 0.718  | 0.700  | 0.671 | 0.661  | 0.653 | 0.643 | 0.630 |
| 200 | 0.698  | 0.721  | 0.698  | 0.684 | 0.675  | 0.669 | 0.661 | 0.654 |
| 500 | 0.705  | 0.739  | 0.723  | 0.708 | 0.710  | 0.707 | 0.701 | 0.697 |

**Takeaways** (rerun after bug 4)**.** η controls d_ev monotonically at every size (Spearman between η and d_ev = 1.0 on every graph), and bisection hits targets within 5% in 31 of 36 runs and within 10% in all 36. The offsets keep popular papers out of the main mode (1–3% of its mass, against 15–19% without offsets and 33–76% for raw SVD). Keeping direction improves held-out citation prediction (0.72–0.75 against 0.60–0.66 symmetrized). Group recovery is weak for every variant at this sparsity, so it does not separate them.

### 3.3 E2: convergence check

**Convergence check (directed SPECTRA, 3 real graphs, at eta=0 and at the eta hitting d_ev=8 in 1,500 epochs)**

| query      | eta    | d_ev@1500   | d_ev@3000   | d_ev@5000   | d_ev@6000   | change 1500->6000   | nll@1500   | nll@6000   | d_ev range over last 1000   |
|:-----------|:-------|:------------|:------------|:------------|:------------|:--------------------|:-----------|:-----------|:----------------------------|
| 2504.06211 | 0.000  | 27.149      | 27.347      | 27.401      | 27.408      | 0.010               | 0.159      | 0.152      | 27.40-27.41                 |
| 2504.06211 | -0.059 | 8.018       | 8.238       | 8.187       | 8.182       | 0.020               | 0.206      | 0.195      | 8.18-8.19                   |
| 2504.06975 | 0.000  | 29.033      | 29.193      | 29.276      | 29.286      | 0.009               | 0.064      | 0.057      | 29.28-29.29                 |
| 2504.06975 | -0.039 | 8.035       | 7.716       | 7.671       | 7.663       | -0.046              | 0.095      | 0.090      | 7.66-7.67                   |
| 2504.09307 | 0.000  | 29.785      | 29.824      | 29.877      | 29.888      | 0.003               | 0.055      | 0.048      | 29.88-29.89                 |
| 2504.09307 | -0.045 | 7.970       | 7.642       | 7.556       | 7.546       | -0.053              | 0.089      | 0.083      | 7.55-7.56                   |

**Takeaways** (rerun after bug 4)**.** With the fixed optimizer the fits are settled well before 6,000 epochs: d_ev changes by 5% or less between 1,500 and 6,000, moves by about 0.01 over the last 1,000 epochs, and the loss falls monotonically. The pre-fix run of this check showed d_ev drifting 6–18% over the last 1,000 epochs and the loss *rising* in 2 of 6 runs; we attributed that to a learning rate that is too high, but it was bug 4 (sign flips of single modes), which no schedule could fix (E10). All results use 6,000 epochs, SPECTRA's own budget, which is now more than enough.

### 3.4 E3: OpenAlex pilot (63 queries, our own search)

**OpenAlex pilot graphs (data/graphs_v2)**

|                                                             | value            |
|:------------------------------------------------------------|:-----------------|
| queries                                                     | 63               |
| nodes per graph, mean (min-max)                             | 489 (474-499)    |
| directed edges per graph, mean (min-max)                    | 3933 (872-11133) |
| density                                                     | 0.0165           |
| fraction of nodes with no listed references                 | 0.108            |
| fraction of nodes with an abstract                          | 0.771            |
| related-work references (all queries)                       | 1630             |
| references with a DOI or arXiv ID                           | 1078 (66.1%)     |
| references resolved by identifier with agreeing title       | 606              |
| references in the pools                                     | 480 (29.4%)      |
| in pool: matched by identifier / by title only              | 138 / 342        |
| identifier matches also found by title matching             | 135/138 (97.8%)  |
| pool nodes matching a reference that came from search seeds | 127/489 (26.0%)  |
| queries with at least one reference in the pool             | 53               |

> **Not rerun after bug 4.** The D-SPECTRA, η = 0 and symmetrized rows below come from the buggy optimizer (the fit-free baselines are unaffected). The pattern matches E6, which was rerun, so we did not spend the GPU time on this superseded pilot.

Means over the 53 queries with at least one human-cited reference in the graph; the best any method can do is 0.294.

**Recall of related-work references**

| method                         | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:-------|:-------|:-------|:-------|:-------|
| fixed-k (search only)          | 0.057  | 0.076  | 0.088  | 0.093  | 0.093  |
| relevance only (main ablation) | 0.066  | 0.105  | 0.133  | 0.169  | 0.191  |
| most_cited                     | 0.037  | 0.059  | 0.081  | 0.111  | 0.128  |
| vendi                          | 0.045  | 0.096  | 0.117  | 0.148  | 0.173  |
| semantic_modes                 | 0.066  | 0.105  | 0.130  | 0.170  | 0.183  |
| symmetrized                    | 0.066  | 0.100  | 0.130  | 0.160  | 0.187  |
| raw_svd                        | 0.069  | 0.110  | 0.151  | 0.188  | 0.215  |
| usvt                           | 0.074  | 0.118  | 0.151  | 0.192  | 0.219  |
| dspectra_eta0                  | 0.075  | 0.112  | 0.136  | 0.156  | 0.181  |
| dspectra_d4                    | 0.074  | 0.113  | 0.136  | 0.169  | 0.186  |
| dspectra                       | 0.072  | 0.110  | 0.134  | 0.163  | 0.181  |
| dspectra_d16                   | 0.068  | 0.106  | 0.135  | 0.161  | 0.184  |

**Share of the reachable references recovered (pooled over 53 queries; 480 references reachable)**

| method                         | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:-------|:-------|:-------|:-------|:-------|
| fixed-k (search only)          | 0.154  | 0.208  | 0.244  | 0.265  | 0.265  |
| relevance only (main ablation) | 0.181  | 0.292  | 0.375  | 0.477  | 0.542  |
| most_cited                     | 0.096  | 0.154  | 0.217  | 0.302  | 0.352  |
| vendi                          | 0.117  | 0.260  | 0.327  | 0.419  | 0.496  |
| semantic_modes                 | 0.181  | 0.290  | 0.367  | 0.483  | 0.523  |
| symmetrized                    | 0.179  | 0.290  | 0.375  | 0.463  | 0.542  |
| raw_svd                        | 0.185  | 0.294  | 0.415  | 0.525  | 0.604  |
| usvt                           | 0.198  | 0.319  | 0.419  | 0.535  | 0.613  |
| dspectra_eta0                  | 0.210  | 0.310  | 0.390  | 0.450  | 0.523  |
| dspectra_d4                    | 0.210  | 0.319  | 0.383  | 0.475  | 0.535  |
| dspectra                       | 0.204  | 0.310  | 0.392  | 0.471  | 0.527  |
| dspectra_d16                   | 0.185  | 0.298  | 0.381  | 0.460  | 0.527  |

**D-SPECTRA minus each method (wins/losses over queries, paired Wilcoxon p)**

|                                | B=10                    | B=20                    | B=30                    | B=45                    | B=60                    |
|:-------------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|
| fixed-k (search only)          | +0.015 (21/7, p=0.009)  | +0.034 (28/9, p=0.003)  | +0.046 (32/9, p=0.001)  | +0.069 (34/7, p=<0.001) | +0.087 (37/6, p=<0.001) |
| relevance only (main ablation) | +0.007 (17/11, p=0.223) | +0.005 (15/13, p=0.600) | +0.001 (19/15, p=0.837) | -0.006 (14/19, p=0.532) | -0.010 (14/18, p=0.364) |
| most_cited                     | +0.036 (30/11, p=0.010) | +0.051 (35/13, p=0.011) | +0.054 (32/13, p=0.004) | +0.051 (32/12, p=0.011) | +0.052 (31/12, p=0.008) |
| vendi                          | +0.027 (26/5, p=<0.001) | +0.014 (21/11, p=0.130) | +0.017 (25/12, p=0.113) | +0.015 (27/15, p=0.056) | +0.008 (21/17, p=0.320) |
| semantic_modes                 | +0.006 (15/10, p=0.288) | +0.005 (17/15, p=0.627) | +0.005 (19/16, p=0.774) | -0.007 (15/23, p=0.519) | -0.003 (15/17, p=0.688) |
| symmetrized                    | +0.006 (16/7, p=0.140)  | +0.010 (17/13, p=0.440) | +0.005 (16/14, p=0.789) | +0.003 (16/14, p=0.758) | -0.006 (13/17, p=0.254) |
| raw_svd                        | +0.003 (17/11, p=0.673) | -0.000 (20/14, p=0.752) | -0.016 (12/18, p=0.131) | -0.026 (10/22, p=0.006) | -0.034 (8/20, p=0.009)  |
| usvt                           | -0.002 (14/14, p=0.864) | -0.008 (15/17, p=0.460) | -0.016 (12/19, p=0.170) | -0.029 (9/22, p=0.002)  | -0.038 (9/23, p=0.002)  |
| dspectra_eta0                  | -0.003 (6/9, p=0.363)   | -0.002 (6/6, p=0.308)   | -0.002 (8/8, p=0.552)   | +0.007 (13/5, p=0.043)  | -0.001 (11/7, p=0.913)  |
| dspectra_d4                    | -0.002 (9/11, p=0.455)  | -0.003 (11/11, p=0.721) | -0.001 (17/13, p=0.943) | -0.006 (13/15, p=0.362) | -0.005 (12/14, p=0.469) |
| dspectra_d16                   | +0.005 (13/4, p=0.102)  | +0.004 (12/8, p=0.360)  | -0.001 (16/9, p=0.989)  | +0.001 (12/9, p=0.794)  | -0.003 (12/12, p=0.898) |

**Recall of the benchmark's important references**

| method                         | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:-------|:-------|:-------|:-------|:-------|
| fixed-k (search only)          | 0.079  | 0.102  | 0.117  | 0.122  | 0.122  |
| relevance only (main ablation) | 0.089  | 0.136  | 0.170  | 0.216  | 0.244  |
| most_cited                     | 0.046  | 0.072  | 0.096  | 0.135  | 0.156  |
| vendi                          | 0.059  | 0.122  | 0.150  | 0.190  | 0.222  |
| semantic_modes                 | 0.090  | 0.139  | 0.169  | 0.217  | 0.234  |
| symmetrized                    | 0.088  | 0.131  | 0.172  | 0.207  | 0.239  |
| raw_svd                        | 0.090  | 0.140  | 0.191  | 0.239  | 0.271  |
| usvt                           | 0.097  | 0.149  | 0.196  | 0.245  | 0.277  |
| dspectra_eta0                  | 0.100  | 0.147  | 0.176  | 0.198  | 0.230  |
| dspectra_d4                    | 0.097  | 0.141  | 0.169  | 0.216  | 0.237  |
| dspectra                       | 0.095  | 0.144  | 0.172  | 0.208  | 0.234  |
| dspectra_d16                   | 0.090  | 0.138  | 0.173  | 0.207  | 0.235  |

**D_ev(S) of the selected set**

| method                         | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:-------|:-------|:-------|:-------|:-------|
| fixed-k (search only)          | 6.93   | 7.25   | 7.61   | 7.89   | 7.91   |
| relevance only (main ablation) | 6.95   | 7.25   | 7.35   | 7.46   | 7.55   |
| most_cited                     | 4.86   | 5.36   | 5.60   | 5.90   | 6.12   |
| vendi                          | 7.39   | 7.72   | 7.76   | 7.74   | 7.72   |
| semantic_modes                 | 6.92   | 7.34   | 7.44   | 7.59   | 7.70   |
| symmetrized                    | 6.50   | 6.93   | 7.09   | 7.24   | 7.33   |
| raw_svd                        | 5.56   | 6.00   | 6.23   | 6.54   | 6.76   |
| usvt                           | 5.52   | 5.99   | 6.25   | 6.53   | 6.75   |
| dspectra_eta0                  | 6.34   | 6.58   | 6.78   | 6.94   | 7.06   |
| dspectra_d4                    | 6.24   | 6.45   | 6.63   | 6.79   | 6.93   |
| dspectra                       | 6.44   | 6.73   | 6.93   | 7.08   | 7.18   |
| dspectra_d16                   | 6.41   | 6.72   | 6.90   | 7.05   | 7.15   |

**Embedding diversity of the selected set**

| method                         | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:-------|:-------|:-------|:-------|:-------|
| fixed-k (search only)          | 0.336  | 0.374  | 0.406  | 0.455  | 0.468  |
| relevance only (main ablation) | 0.308  | 0.328  | 0.343  | 0.357  | 0.370  |
| most_cited                     | 0.426  | 0.440  | 0.446  | 0.453  | 0.458  |
| vendi                          | 0.395  | 0.389  | 0.388  | 0.391  | 0.393  |
| semantic_modes                 | 0.315  | 0.342  | 0.362  | 0.377  | 0.389  |
| symmetrized                    | 0.319  | 0.343  | 0.357  | 0.371  | 0.381  |
| raw_svd                        | 0.364  | 0.383  | 0.389  | 0.394  | 0.397  |
| usvt                           | 0.367  | 0.385  | 0.390  | 0.395  | 0.398  |
| dspectra_eta0                  | 0.325  | 0.354  | 0.369  | 0.383  | 0.390  |
| dspectra_d4                    | 0.327  | 0.359  | 0.374  | 0.386  | 0.394  |
| dspectra                       | 0.321  | 0.352  | 0.369  | 0.380  | 0.388  |
| dspectra_d16                   | 0.322  | 0.350  | 0.365  | 0.377  | 0.385  |

**Premise check** (47 queries): human-cited sets occupy fewer fitted modes than relevance-ranked sets of the same size: d_ev(S) 5.66 vs 6.75 (random 7.12); the human set is higher in 13 of 47 queries (p = 0.002).

**Takeaways.** Following citations doubles recall (relevance-only 0.191 vs fixed-k 0.093 at B = 60); 74% of the human-cited references the graphs contain were reached only through citations. D-SPECTRA does not beat relevance-only selection (+0.005 at B = 20, −0.010 at B = 60, both p > 0.2). USVT is best at B ≥ 30 and beats D-SPECTRA at B = 45 and 60 (p = 0.002). Capacity control makes no measurable difference (targets 4, 8, 16 and η = 0 alike).

### 3.5 E4: DeepScholar-base reproduction (Mateo)

*Tables copied from Mateo's pilot report (`D-SPECTRA_pilot_report.md`).*

| Setting | DeepScholar paper | Repo default | Our pilot | Final runs |
| --- | --- | --- | --- | --- |
| Search mode | recursive | agentic | recursive | recursive |
| Rounds × queries per round | 2 × 2 | 3 × 2 | 3 × 2 | 2 × 2 |
| Results kept per query | 50 | 10 | 50 | 50 |
| Papers passed to the writer | up to 30 | up to 30 | up to 30 | up to 30 |
| Corpus | arXiv only | arXiv + web | arXiv (+ one web run) | arXiv only |
| Model | GPT-4.1 or Llama-4-Scout | GPT-5-mini | Qwen3-8B-AWQ | Qwen3-8B-AWQ |
| Sampling | not stated | temperature 1.0 | temperature 1.0 | 0.7 / top_p 0.8 / top_k 20, seeds 0–2 |

| Pilot run | Papers in pool (mean) | Papers DeepScholar kept (mean) | Minutes per query |
| --- | --- | --- | --- |
| arXiv A | 125.9 | 22.1 | 3.8 |
| arXiv B | 123.1 | 21.4 | 2.6 |
| arXiv + web | 176.3 | 27.2 | 4.1 |

- **Search is noisy:** runs A and B share only 46% of their arXiv papers (14–86%), so every system must select from the same frozen pool.
- **Web search adds no arXiv coverage** (overlap 41% vs 46% noise, p = 0.39) **and leaks** about 5 post-cutoff papers per query; the model also searched for the target paper by name.
- **Backbone:** Qwen3-4B kept only 2–3 papers per query; the 8B keeps about 22.

| Bug fixed in DeepScholar (in a wrapper) | Fix |
| --- | --- |
| Every LLM call silently capped at 512 tokens; the filter rejected almost everything | pass the 10k limit to each stage |
| Only the last search round is kept | save all rounds as `pool_all.csv` |
| Model writes 5–10 search queries instead of 2, overflowing the context | keep the first 2 |
| LaTeX braces in an abstract crash the filter | replace `{ }` with `( )` |

**From the DeepScholar paper (arXiv 2508.20033, Table 3; checked in the paper).** DeepScholar-ref with GPT-4.1 and Claude; "Oracle" gives the system the important references the human authors cited.

| Retrieval | Organization | Nugget coverage | Relevance rate | Reference coverage | Document importance | Citation precision | Claim coverage | Overall |
|---|---|---|---|---|---|---|---|---|
| arxiv.org | .698 | .307 | .610 | .152 | .009 | .944 | .895 | .286 |
| parallel.ai | .865 | .444 | .675 | .160 | .017 | .846 | .781 | .334 |
| tavily.com | .929 | .327 | .550 | .070 | .015 | .711 | .578 | .258 |
| Oracle (arxiv.org) | .782 | .487 | .686 | 1.000 | 1.000 | .955 | .899 | .808 |
| Oracle (all) | .778 | .528 | .680 | 1.000 | .822 | .941 | .828 | .782 |

**Retrieval is the bottleneck:** with the true references the overall score goes from .286 to .808 (with Llama-4: .195 → .590–.600).

**Final runs** (Oct 21): pools, kept papers, references, reports and costs for all 63 queries × seeds 0–2 (seed 2 covers 54 of 63 so far). The tables below are computed directly from Mateo's files: `costs.csv` for costs and sizes, and the pools and `kept.csv` lists matched to the human-cited references by arXiv ID, then by title, with no citation graph involved.

**Costs and sizes per seed**

|                                           | seed 0           | seed 1           | seed 2           |
|:------------------------------------------|:-----------------|:-----------------|:-----------------|
| queries                                   | 63               | 63               | 54               |
| wall time per query (min)                 | 3.6              | 3.2              | 4.0              |
| LLM calls per query                       | 215              | 239              | 232              |
| prompt / completion tokens per query      | 245,705 / 38,791 | 259,927 / 36,746 | 258,004 / 41,808 |
| of which filter stage (prompt)            | 166,555          | 179,214          | 175,378          |
| arXiv search phrases / requests per query | 4.0 / 5.0        | 4.1 / 4.4        | 4.0 / 4.9        |
| queries with empty or failed searches     | 0                | 0                | 0                |
| queries where search was re-run           | 0                | 1                | 0                |
| pool papers per query, mean (min-max)     | 103 (38-157)     | 103 (39-155)     | 105 (51-164)     |
| kept papers per query, mean (min-max)     | 21.2 (3-30)      | 21.8 (5-30)      | 22.9 (11-30)     |
| references cited inline in the report     | 11.3 of 21.2     | 12.2 of 21.8     | 13.0 of 22.9     |

**How much the pools and kept papers agree across seeds**

|                                                | seed 0 vs 1                  | seed 0 vs 2                  | seed 1 vs 2                  |
|:-----------------------------------------------|:-----------------------------|:-----------------------------|:-----------------------------|
| pool: overlap (Jaccard), mean (min-max)        | 0.58 (0.12-1.00), 63 queries | 0.55 (0.21-0.97), 54 queries | 0.59 (0.19-1.00), 54 queries |
| kept papers: overlap (Jaccard), mean (min-max) | 0.19 (0.00-0.58), 63 queries | 0.19 (0.00-0.54), 54 queries | 0.19 (0.00-0.50), 54 queries |

**Human-cited references in DeepScholar-base's pool and kept papers**

|                                                          | seed 0             | seed 1             | seed 2             |
|:---------------------------------------------------------|:-------------------|:-------------------|:-------------------|
| held-out (43): refs in pool (pooled)                     | 66/1120 = 5.9%     | 73/1120 = 6.5%     | 50/862 = 5.8%      |
| held-out (43): refs in kept papers (pooled)              | 44/1120 = 3.9%     | 40/1120 = 3.6%     | 33/862 = 3.8%      |
| held-out (43): recall of kept papers (mean over queries) | 0.044 (43 queries) | 0.037 (43 queries) | 0.042 (34 queries) |
| design (20): refs in pool (pooled)                       | 30/510 = 5.9%      | 37/510 = 7.3%      | 33/510 = 6.5%      |
| design (20): refs in kept papers (pooled)                | 17/510 = 3.3%      | 23/510 = 4.5%      | 20/510 = 3.9%      |
| design (20): recall of kept papers (mean over queries)   | 0.034 (20 queries) | 0.045 (20 queries) | 0.036 (20 queries) |
| all: refs in pool (pooled)                               | 96/1630 = 5.9%     | 110/1630 = 6.7%    | 83/1372 = 6.0%     |
| all: refs in kept papers (pooled)                        | 61/1630 = 3.7%     | 63/1630 = 3.9%     | 53/1372 = 3.9%     |
| all: recall of kept papers (mean over queries)           | 0.041 (63 queries) | 0.039 (63 queries) | 0.040 (54 queries) |

**Takeaways.**
- **Cost:** 3.2–4.0 minutes, 215–239 LLM calls and about 285,000–300,000 tokens per query; the LLM filter alone uses about two-thirds of the prompt tokens. No search failed; one query (seed 1) re-ran its search.
- **Seeds matter a lot for what reaches the writer.** The pools of two seeds overlap 55–59% (Jaccard), but the papers DeepScholar keeps overlap only 19%. Reporting three seeds, and freezing the pool per seed so every system selects from the same one, is essential.
- **DeepScholar-base finds few of the papers the human authors cited:** its pool contains about 6–7% of them and its kept papers about 4% (recall 0.039–0.041 per query), stable across seeds and similar on the design and held-out queries. Its filter keeps roughly two-thirds of the human-cited papers that are in its pool.

### 3.6 E5: pool diagnostics (20 pilot pools; affected by bug 3)

> These numbers come from reading Mateo's pilot pools with bug 3, so about 12% of each pool's papers were missing. The direction of the findings holds; the exact shares are understated. The E6 graph table above has the corrected numbers for the final pools.

**Citations between pool papers, OpenAlex vs Semantic Scholar (means over 20 queries)**

| pool     | papers (mean)   | OpenAlex: resolved   | OpenAlex: with refs   | OpenAlex: within-pool citations   | S2: resolved   | S2: within-pool citations   | S2: per paper   | S2: isolated   |
|:---------|:----------------|:---------------------|:----------------------|:----------------------------------|:---------------|:----------------------------|:----------------|:---------------|
| 3 rounds | 121.500         | 0.400                | 0.141                 | 0.650                             | 0.910          | 50.800                      | 0.430           | 0.692          |
| 2 rounds | 105.450         | 0.396                | 0.136                 | 0.550                             | 0.906          | 43.950                      | 0.403           | 0.711          |

Semantic Scholar: 87.8% of pool papers have a reference list.

**Related-work references contained in the pool, same 20 queries**

| pool     | DeepScholar pool   | our OpenAlex expanded pool   |
|:---------|:-------------------|:-----------------------------|
| 3 rounds | 41/510 = 8.0%      | 167/510 = 32.7%              |
| 2 rounds | 35/510 = 6.9%      | 167/510 = 32.7%              |

**Takeaways.** OpenAlex cannot supply citation links for these recent arXiv preprints; Semantic Scholar can, but pool papers rarely cite each other, so the model has to be fitted on the pool plus its citation neighbourhood. DeepScholar's pools contain only a small share of the human-cited references; adding citations raises it several-fold.

### 3.7 Graph sizes compared with SPECTRA's

| Graph | Nodes | Edges | Avg. degree |
|---|---|---|---|
| SPECTRA: socfb-Amherst41 | 2,235 | 90,954 | 81 |
| SPECTRA: inf-openflights | 2,939 | 15,677 | 11 |
| SPECTRA: bio-grid-worm | 3,507 | 6,531 | 3.7 |
| SPECTRA: inf-power | 4,941 | 6,594 | 2.7 |
| SPECTRA: socfb-American75 | 6,386 | 217,662 | 68 |
| SPECTRA: bio-grid-human | 9,436 | 31,182 | 6.6 |
| Ours: E3 OpenAlex graphs | 489 | 3,933 (directed) | 16 |
| Ours: E6 final-pool graphs | 482 | 4,673 (directed) | 19 |

Our graphs are 5–20× smaller than SPECTRA's (it was never tested below about 2,000 nodes); small graphs are exactly the extension the proposal claims.

### 3.8 E8: method variants and bigger graphs

**The graphs.** The current graphs are E6's, with query 2506.00832 rebuilt from Mateo's updated pool. The bigger graphs add twice as many references and citing papers.

**Size and human-cited references they contain**

|                               | small, design (20)   | small, held-out (43)   | big, design (20)   | big, held-out (43)   |
|:------------------------------|:---------------------|:-----------------------|:-------------------|:---------------------|
| nodes (mean)                  | 483                  | 484                    | 860                | 861                  |
| edges (mean)                  | 5487                 | 4339                   | 10357              | 7972                 |
| human-cited refs in the graph | 213/510 = 41.8%      | 392/1120 = 35.0%       | 239/510 = 46.9%    | 459/1120 = 41.0%     |

**η chosen by held-out link prediction** (mean held-out AUC and d_ev at each η, and how many queries chose each η)

*Current graphs:*

**Held-out link prediction over eta (63 queries)**

|       | auc   | d_ev   | queries choosing it   |
|:------|:------|:-------|:----------------------|
| -0.10 | 0.958 | 3.562  | 16                    |
| -0.06 | 0.958 | 7.537  | 12                    |
| -0.03 | 0.958 | 15.665 | 19                    |
| +0.00 | 0.958 | 28.226 | 14                    |
| +0.02 | 0.956 | 29.256 | 2                     |
| +0.04 | 0.954 | 29.832 | 0                     |
| +0.06 | 0.953 | 30.219 | 0                     |

*Bigger graphs:*

**Held-out link prediction over eta (63 queries)**

|       | auc   | d_ev   | queries choosing it   |
|:------|:------|:-------|:----------------------|
| -0.10 | 0.964 | 3.139  | 5                     |
| -0.06 | 0.967 | 6.872  | 25                    |
| -0.03 | 0.967 | 15.714 | 24                    |
| +0.00 | 0.967 | 29.177 | 8                     |
| +0.02 | 0.965 | 30.032 | 0                     |
| +0.04 | 0.964 | 30.486 | 1                     |
| +0.06 | 0.963 | 30.782 | 0                     |

**The selection rule on the design queries.** Every configuration, at the matched budget and B = 20. "chosen" marks the configuration reported on the held-out queries.

*Current graphs:*

**Every configuration (recall, expanded)**

| family                     | config          | B=kept   | B=20   | chosen   |
|:---------------------------|:----------------|:---------|:-------|:---------|
| query link (model only)    | qlink10_cv      | 0.234    | 0.218  |          |
| query link (model only)    | qlink10_d8      | 0.238    | 0.215  |          |
| query link (model only)    | qlink10_eta0    | 0.231    | 0.227  |          |
| query link (model only)    | qlink20_cv      | 0.234    | 0.208  |          |
| query link (model only)    | qlink20_d8      | 0.226    | 0.195  |          |
| query link (model only)    | qlink20_eta0    | 0.230    | 0.216  |          |
| query link (model only)    | qlink5_cv       | 0.245    | 0.229  |          |
| query link (model only)    | qlink5_d8       | 0.244    | 0.210  |          |
| query link (model only)    | qlink5_eta0     | 0.253    | 0.242  | yes      |
| query link + relevance     | qlinkrel10_cv   | 0.216    | 0.170  |          |
| query link + relevance     | qlinkrel10_d8   | 0.210    | 0.189  |          |
| query link + relevance     | qlinkrel10_eta0 | 0.231    | 0.181  |          |
| query link + relevance     | qlinkrel20_cv   | 0.202    | 0.172  |          |
| query link + relevance     | qlinkrel20_d8   | 0.207    | 0.169  |          |
| query link + relevance     | qlinkrel20_eta0 | 0.214    | 0.164  |          |
| query link + relevance     | qlinkrel5_cv    | 0.216    | 0.175  |          |
| query link + relevance     | qlinkrel5_d8    | 0.202    | 0.182  |          |
| query link + relevance     | qlinkrel5_eta0  | 0.244    | 0.190  | yes      |
| pool-anchored mode weights | poolU_cv        | 0.137    | 0.108  |          |
| pool-anchored mode weights | poolU_d8        | 0.112    | 0.099  |          |
| pool-anchored mode weights | poolU_eta0      | 0.149    | 0.128  |          |
| pool-anchored mode weights | poolV_cv        | 0.142    | 0.112  |          |
| pool-anchored mode weights | poolV_d8        | 0.130    | 0.107  |          |
| pool-anchored mode weights | poolV_eta0      | 0.159    | 0.130  | yes      |

*Bigger graphs:*

**Every configuration (recall, expanded)**

| family                     | config          | B=kept   | B=20   | chosen   |
|:---------------------------|:----------------|:---------|:-------|:---------|
| query link (model only)    | qlink10_cv      | 0.222    | 0.217  |          |
| query link (model only)    | qlink10_d8      | 0.215    | 0.195  |          |
| query link (model only)    | qlink10_eta0    | 0.220    | 0.215  |          |
| query link (model only)    | qlink20_cv      | 0.225    | 0.191  |          |
| query link (model only)    | qlink20_d8      | 0.212    | 0.194  |          |
| query link (model only)    | qlink20_eta0    | 0.224    | 0.201  |          |
| query link (model only)    | qlink5_cv       | 0.230    | 0.202  |          |
| query link (model only)    | qlink5_d8       | 0.226    | 0.203  |          |
| query link (model only)    | qlink5_eta0     | 0.243    | 0.228  | yes      |
| query link + relevance     | qlinkrel10_cv   | 0.186    | 0.161  |          |
| query link + relevance     | qlinkrel10_d8   | 0.174    | 0.158  |          |
| query link + relevance     | qlinkrel10_eta0 | 0.190    | 0.148  | yes      |
| query link + relevance     | qlinkrel20_cv   | 0.172    | 0.141  |          |
| query link + relevance     | qlinkrel20_d8   | 0.170    | 0.142  |          |
| query link + relevance     | qlinkrel20_eta0 | 0.170    | 0.151  |          |
| query link + relevance     | qlinkrel5_cv    | 0.164    | 0.137  |          |
| query link + relevance     | qlinkrel5_d8    | 0.169    | 0.143  |          |
| query link + relevance     | qlinkrel5_eta0  | 0.174    | 0.153  |          |
| pool-anchored mode weights | poolU_cv        | 0.119    | 0.094  |          |
| pool-anchored mode weights | poolU_d8        | 0.112    | 0.080  |          |
| pool-anchored mode weights | poolU_eta0      | 0.128    | 0.125  |          |
| pool-anchored mode weights | poolV_cv        | 0.141    | 0.101  |          |
| pool-anchored mode weights | poolV_d8        | 0.129    | 0.078  |          |
| pool-anchored mode weights | poolV_eta0      | 0.155    | 0.133  | yes      |

**Held-out queries (43), current graphs: the main E8 result.** Expanded setting. The new rows are the chosen configurations: `qlink5_eta0` (query link, model only), `qlinkrel5_eta0` (query link + relevance) and `poolV_eta0` (pool-anchored weights).

**Recall, expanded (41 queries with a reference in the graph)**

|                                  | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:---------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks     | 0.047    |        |        |        |        |        |
| fixed-k (search only)            | 0.059    | 0.043  | 0.054  | 0.067  | 0.069  | 0.069  |
| relevance only                   | 0.090    | 0.053  | 0.089  | 0.119  | 0.146  | 0.173  |
| most_cited                       | 0.096    | 0.062  | 0.099  | 0.121  | 0.154  | 0.175  |
| usvt                             | 0.138    | 0.079  | 0.134  | 0.165  | 0.204  | 0.230  |
| raw_svd                          | 0.134    | 0.073  | 0.126  | 0.161  | 0.203  | 0.231  |
| D-SPECTRA, eta = 0               | 0.122    | 0.076  | 0.118  | 0.143  | 0.186  | 0.214  |
| D-SPECTRA (d_ev = 8)             | 0.120    | 0.080  | 0.117  | 0.142  | 0.182  | 0.214  |
| D-SPECTRA, eta by held-out links | 0.111    | 0.072  | 0.102  | 0.138  | 0.176  | 0.207  |
| qlink5_eta0                      | 0.166    | 0.103  | 0.171  | 0.202  | 0.231  | 0.257  |
| qlinkrel5_eta0                   | 0.167    | 0.096  | 0.159  | 0.204  | 0.233  | 0.253  |
| poolV_eta0                       | 0.122    | 0.071  | 0.118  | 0.144  | 0.185  | 0.207  |

**New variants vs D-SPECTRA and baselines at B=kept (mean difference, wins/losses, paired Wilcoxon p)**

|                                  | vs D-SPECTRA (d_ev = 8)   | vs relevance only       | vs most_cited           | vs usvt                 |
|:---------------------------------|:--------------------------|:------------------------|:------------------------|:------------------------|
| D-SPECTRA, eta by held-out links | -0.009 (9/15, p=0.265)    | +0.020 (19/8, p=0.042)  | +0.015 (21/17, p=0.464) | -0.028 (10/23, p=0.017) |
| qlink5_eta0                      | +0.046 (18/9, p=0.058)    | +0.075 (22/5, p=<0.001) | +0.070 (24/7, p=0.001)  | +0.027 (13/11, p=0.568) |
| qlinkrel5_eta0                   | +0.047 (25/7, p=<0.001)   | +0.077 (31/4, p=<0.001) | +0.071 (26/10, p=0.002) | +0.028 (17/10, p=0.027) |
| poolV_eta0                       | +0.001 (11/8, p=0.763)    | +0.031 (23/5, p=0.006)  | +0.026 (21/14, p=0.154) | -0.017 (10/19, p=0.082) |

**Share of picks at B=kept with an abstract (all evaluated queries)**

|                                  | with abstract   |
|:---------------------------------|:----------------|
| DeepScholar-base's own picks     | 1.00            |
| fixed-k (search only)            | 1.00            |
| relevance only                   | 1.00            |
| most_cited                       | 0.80            |
| usvt                             | 0.97            |
| raw_svd                          | 0.96            |
| D-SPECTRA, eta = 0               | 0.98            |
| D-SPECTRA (d_ev = 8)             | 0.99            |
| D-SPECTRA, eta by held-out links | 0.98            |
| qlink5_eta0                      | 0.79            |
| qlinkrel5_eta0                   | 0.97            |
| poolV_eta0                       | 0.98            |

*Pool-only setting:*

**Recall, pool only (41 queries)**

|                                  | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:---------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks     | 0.047    |        |        |        |        |        |
| fixed-k (search only)            | 0.059    | 0.043  | 0.054  | 0.067  | 0.069  | 0.069  |
| relevance only                   | 0.059    | 0.043  | 0.054  | 0.067  | 0.069  | 0.069  |
| most_cited                       | 0.060    | 0.045  | 0.057  | 0.066  | 0.069  | 0.070  |
| usvt                             | 0.065    | 0.055  | 0.063  | 0.069  | 0.070  | 0.070  |
| raw_svd                          | 0.065    | 0.053  | 0.063  | 0.069  | 0.070  | 0.070  |
| D-SPECTRA, eta = 0               | 0.066    | 0.050  | 0.065  | 0.069  | 0.070  | 0.070  |
| D-SPECTRA (d_ev = 8)             | 0.067    | 0.049  | 0.067  | 0.068  | 0.070  | 0.070  |
| D-SPECTRA, eta by held-out links | 0.069    | 0.051  | 0.064  | 0.069  | 0.070  | 0.070  |
| qlink5_eta0                      | 0.059    | 0.055  | 0.060  | 0.065  | 0.068  | 0.069  |
| qlinkrel5_eta0                   | 0.067    | 0.057  | 0.065  | 0.068  | 0.070  | 0.070  |
| poolV_eta0                       | 0.066    | 0.050  | 0.065  | 0.069  | 0.069  | 0.070  |

**Held-out queries (43), bigger graphs.** The chosen configurations are `qlink5_eta0`, `qlinkrel10_eta0` and `poolV_eta0`.

**Recall, expanded (41 queries with a reference in the graph)**

|                                  | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:---------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks     | 0.047    |        |        |        |        |        |
| fixed-k (search only)            | 0.059    | 0.043  | 0.054  | 0.067  | 0.069  | 0.069  |
| relevance only                   | 0.086    | 0.057  | 0.085  | 0.116  | 0.141  | 0.160  |
| most_cited                       | 0.091    | 0.056  | 0.089  | 0.111  | 0.131  | 0.159  |
| usvt                             | 0.130    | 0.072  | 0.120  | 0.158  | 0.201  | 0.223  |
| raw_svd                          | 0.130    | 0.072  | 0.120  | 0.158  | 0.201  | 0.223  |
| D-SPECTRA, eta = 0               | 0.118    | 0.078  | 0.114  | 0.142  | 0.169  | 0.192  |
| D-SPECTRA (d_ev = 8)             | 0.118    | 0.066  | 0.117  | 0.143  | 0.164  | 0.196  |
| D-SPECTRA, eta by held-out links | 0.118    | 0.062  | 0.112  | 0.148  | 0.175  | 0.197  |
| qlink5_eta0                      | 0.166    | 0.108  | 0.161  | 0.206  | 0.232  | 0.252  |
| qlinkrel10_eta0                  | 0.159    | 0.100  | 0.152  | 0.190  | 0.233  | 0.258  |
| poolV_eta0                       | 0.119    | 0.074  | 0.114  | 0.137  | 0.171  | 0.199  |

**New variants vs D-SPECTRA and baselines at B=kept (mean difference, wins/losses, paired Wilcoxon p)**

|                                  | vs D-SPECTRA (d_ev = 8)   | vs relevance only       | vs most_cited           | vs usvt                 |
|:---------------------------------|:--------------------------|:------------------------|:------------------------|:------------------------|
| D-SPECTRA, eta by held-out links | +0.000 (8/8, p=0.918)     | +0.032 (23/7, p=0.004)  | +0.027 (17/12, p=0.187) | -0.012 (9/15, p=0.153)  |
| qlink5_eta0                      | +0.048 (18/10, p=0.067)   | +0.080 (24/7, p=<0.001) | +0.075 (24/7, p=0.001)  | +0.036 (17/10, p=0.102) |
| qlinkrel10_eta0                  | +0.041 (22/5, p=0.001)    | +0.073 (31/2, p=<0.001) | +0.068 (23/10, p=0.008) | +0.029 (15/12, p=0.086) |
| poolV_eta0                       | +0.001 (11/9, p=0.513)    | +0.033 (23/6, p=0.008)  | +0.028 (20/11, p=0.196) | -0.011 (8/12, p=0.240)  |

**Share of picks at B=kept with an abstract (all evaluated queries)**

|                                  | with abstract   |
|:---------------------------------|:----------------|
| DeepScholar-base's own picks     | 1.00            |
| fixed-k (search only)            | 1.00            |
| relevance only                   | 0.99            |
| most_cited                       | 0.81            |
| usvt                             | 0.96            |
| raw_svd                          | 0.96            |
| D-SPECTRA, eta = 0               | 0.99            |
| D-SPECTRA (d_ev = 8)             | 0.99            |
| D-SPECTRA, eta by held-out links | 0.99            |
| qlink5_eta0                      | 0.79            |
| qlinkrel10_eta0                  | 0.97            |
| poolV_eta0                       | 0.99            |

*Pool-only setting:*

**Recall, pool only (41 queries)**

|                                  | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:---------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks     | 0.047    |        |        |        |        |        |
| fixed-k (search only)            | 0.059    | 0.043  | 0.054  | 0.067  | 0.069  | 0.069  |
| relevance only                   | 0.059    | 0.043  | 0.054  | 0.067  | 0.069  | 0.069  |
| most_cited                       | 0.055    | 0.040  | 0.054  | 0.066  | 0.069  | 0.070  |
| usvt                             | 0.064    | 0.053  | 0.062  | 0.069  | 0.070  | 0.070  |
| raw_svd                          | 0.064    | 0.053  | 0.062  | 0.069  | 0.070  | 0.070  |
| D-SPECTRA, eta = 0               | 0.065    | 0.049  | 0.064  | 0.069  | 0.070  | 0.070  |
| D-SPECTRA (d_ev = 8)             | 0.066    | 0.049  | 0.065  | 0.068  | 0.070  | 0.070  |
| D-SPECTRA, eta by held-out links | 0.064    | 0.050  | 0.062  | 0.069  | 0.070  | 0.070  |
| qlink5_eta0                      | 0.060    | 0.055  | 0.060  | 0.062  | 0.068  | 0.069  |
| qlinkrel10_eta0                  | 0.066    | 0.057  | 0.064  | 0.068  | 0.070  | 0.070  |
| poolV_eta0                       | 0.065    | 0.051  | 0.065  | 0.068  | 0.070  | 0.070  |

**Design queries (20)**, for comparison with the held-out results.

*Current graphs:*

**Recall, expanded (17 queries with a reference in the graph)**

|                                  | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:---------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks     | 0.040    |        |        |        |        |        |
| fixed-k (search only)            | 0.041    | 0.022  | 0.036  | 0.045  | 0.060  | 0.062  |
| relevance only                   | 0.076    | 0.040  | 0.065  | 0.083  | 0.114  | 0.144  |
| most_cited                       | 0.186    | 0.110  | 0.163  | 0.200  | 0.227  | 0.264  |
| usvt                             | 0.205    | 0.114  | 0.180  | 0.227  | 0.265  | 0.289  |
| raw_svd                          | 0.209    | 0.116  | 0.168  | 0.226  | 0.274  | 0.291  |
| D-SPECTRA, eta = 0               | 0.161    | 0.071  | 0.129  | 0.176  | 0.227  | 0.265  |
| D-SPECTRA (d_ev = 8)             | 0.119    | 0.054  | 0.095  | 0.138  | 0.187  | 0.237  |
| D-SPECTRA, eta by held-out links | 0.144    | 0.062  | 0.115  | 0.159  | 0.207  | 0.253  |
| qlink5_eta0                      | 0.253    | 0.145  | 0.242  | 0.270  | 0.307  | 0.345  |
| qlinkrel5_eta0                   | 0.244    | 0.093  | 0.190  | 0.260  | 0.311  | 0.340  |
| poolV_eta0                       | 0.159    | 0.071  | 0.130  | 0.175  | 0.228  | 0.258  |

**New variants vs D-SPECTRA and baselines at B=kept (mean difference, wins/losses, paired Wilcoxon p)**

|                                  | vs D-SPECTRA (d_ev = 8)   | vs relevance only       | vs most_cited          | vs usvt                |
|:---------------------------------|:--------------------------|:------------------------|:-----------------------|:-----------------------|
| D-SPECTRA, eta by held-out links | +0.025 (6/1, p=0.028)     | +0.068 (11/1, p=0.008)  | -0.042 (4/7, p=0.424)  | -0.062 (2/8, p=0.013)  |
| qlink5_eta0                      | +0.134 (15/1, p=<0.001)   | +0.178 (15/0, p=<0.001) | +0.068 (11/1, p=0.005) | +0.048 (10/3, p=0.033) |
| qlinkrel5_eta0                   | +0.125 (14/0, p=<0.001)   | +0.168 (14/0, p=<0.001) | +0.058 (10/3, p=0.023) | +0.039 (8/2, p=0.074)  |
| poolV_eta0                       | +0.040 (7/0, p=0.018)     | +0.083 (12/1, p=0.006)  | -0.027 (6/7, p=0.727)  | -0.046 (2/8, p=0.028)  |

*Bigger graphs:*

**Recall, expanded (18 queries with a reference in the graph)**

|                                  | B=kept   | B=10   | B=20   | B=30   | B=45   | B=60   |
|:---------------------------------|:---------|:-------|:-------|:-------|:-------|:-------|
| DeepScholar-base's own picks     | 0.038    |        |        |        |        |        |
| fixed-k (search only)            | 0.039    | 0.021  | 0.034  | 0.043  | 0.057  | 0.059  |
| relevance only                   | 0.069    | 0.037  | 0.057  | 0.079  | 0.117  | 0.135  |
| most_cited                       | 0.174    | 0.102  | 0.150  | 0.193  | 0.227  | 0.257  |
| usvt                             | 0.198    | 0.113  | 0.178  | 0.216  | 0.254  | 0.290  |
| raw_svd                          | 0.198    | 0.113  | 0.178  | 0.216  | 0.254  | 0.290  |
| D-SPECTRA, eta = 0               | 0.149    | 0.077  | 0.124  | 0.165  | 0.219  | 0.259  |
| D-SPECTRA (d_ev = 8)             | 0.119    | 0.053  | 0.085  | 0.139  | 0.187  | 0.227  |
| D-SPECTRA, eta by held-out links | 0.130    | 0.063  | 0.095  | 0.143  | 0.196  | 0.240  |
| qlink5_eta0                      | 0.243    | 0.143  | 0.228  | 0.259  | 0.298  | 0.311  |
| qlinkrel10_eta0                  | 0.190    | 0.077  | 0.148  | 0.213  | 0.271  | 0.317  |
| poolV_eta0                       | 0.155    | 0.075  | 0.133  | 0.170  | 0.218  | 0.249  |

**New variants vs D-SPECTRA and baselines at B=kept (mean difference, wins/losses, paired Wilcoxon p)**

|                                  | vs D-SPECTRA (d_ev = 8)   | vs relevance only      | vs most_cited          | vs usvt                |
|:---------------------------------|:--------------------------|:-----------------------|:-----------------------|:-----------------------|
| D-SPECTRA, eta by held-out links | +0.010 (5/2, p=0.398)     | +0.060 (9/2, p=0.026)  | -0.044 (3/9, p=0.117)  | -0.069 (1/11, p=0.006) |
| qlink5_eta0                      | +0.123 (14/1, p=0.003)    | +0.174 (15/1, p=0.001) | +0.069 (12/2, p=0.011) | +0.045 (11/3, p=0.041) |
| qlinkrel10_eta0                  | +0.070 (11/0, p=0.003)    | +0.120 (13/1, p=0.001) | +0.016 (9/4, p=0.311)  | -0.008 (3/7, p=0.475)  |
| poolV_eta0                       | +0.035 (9/2, p=0.041)     | +0.085 (13/1, p=0.001) | -0.020 (5/6, p=1.000)  | -0.044 (2/11, p=0.046) |

**Bigger vs current graphs, same method**

**Bigger graphs minus current graphs, same method (recall, expanded; all queries, recall 0 where nothing is reachable)**

|                                  | design, B=kept                  | design, B=20                    | held-out, B=kept                | held-out, B=20                  |
|:---------------------------------|:--------------------------------|:--------------------------------|:--------------------------------|:--------------------------------|
| fixed-k (search only)            | 0.035 → 0.035 (+0.000, p=1.000) | 0.030 → 0.030 (+0.000, p=1.000) | 0.057 → 0.057 (+0.000, p=1.000) | 0.052 → 0.052 (+0.000, p=1.000) |
| relevance only                   | 0.064 → 0.062 (-0.002, p=0.674) | 0.055 → 0.051 (-0.004, p=0.345) | 0.086 → 0.082 (-0.004, p=0.397) | 0.085 → 0.081 (-0.005, p=0.346) |
| most_cited                       | 0.158 → 0.157 (-0.001, p=0.953) | 0.139 → 0.135 (-0.004, p=0.575) | 0.091 → 0.087 (-0.005, p=0.386) | 0.094 → 0.085 (-0.009, p=0.096) |
| usvt                             | 0.174 → 0.178 (+0.004, p=0.575) | 0.153 → 0.161 (+0.008, p=0.397) | 0.132 → 0.124 (-0.008, p=0.273) | 0.128 → 0.114 (-0.013, p=0.122) |
| raw_svd                          | 0.177 → 0.178 (+0.001, p=0.779) | 0.143 → 0.161 (+0.017, p=0.059) | 0.128 → 0.124 (-0.004, p=0.513) | 0.120 → 0.114 (-0.006, p=0.533) |
| D-SPECTRA, eta = 0               | 0.137 → 0.134 (-0.003, p=0.965) | 0.110 → 0.111 (+0.002, p=0.779) | 0.116 → 0.112 (-0.004, p=0.413) | 0.112 → 0.109 (-0.003, p=0.523) |
| D-SPECTRA (d_ev = 8)             | 0.101 → 0.107 (+0.006, p=0.657) | 0.080 → 0.077 (-0.003, p=0.767) | 0.115 → 0.113 (-0.002, p=0.873) | 0.112 → 0.112 (+0.000, p=0.808) |
| D-SPECTRA, eta by held-out links | 0.122 → 0.117 (-0.005, p=0.779) | 0.098 → 0.085 (-0.012, p=0.433) | 0.106 → 0.113 (+0.007, p=0.280) | 0.097 → 0.107 (+0.010, p=0.296) |
| query link (model only)          | 0.215 → 0.219 (+0.003, p=0.514) | 0.206 → 0.205 (-0.001, p=0.674) | 0.158 → 0.158 (-0.000, p=0.975) | 0.163 → 0.154 (-0.009, p=0.267) |
| query link + relevance           | 0.207 → 0.171 (-0.036, p=0.023) | 0.162 → 0.133 (-0.029, p=0.004) | 0.159 → 0.152 (-0.008, p=0.411) | 0.151 → 0.145 (-0.007, p=0.444) |
| pool-anchored mode weights       | 0.135 → 0.139 (+0.004, p=0.563) | 0.111 → 0.119 (+0.008, p=0.374) | 0.116 → 0.113 (-0.002, p=0.470) | 0.112 → 0.109 (-0.004, p=0.522) |

**Takeaways (E8).**

- **Query link + relevance is the best method on the held-out queries.** On the current graphs at the matched budget it recovers 0.167, compared with:
  - D-SPECTRA 0.120: +0.047, better on 25 queries and worse on 7, p < 0.001;
  - relevance-only 0.090: +0.077, p < 0.001;
  - most-cited 0.096: +0.071, p = 0.002;
  - USVT 0.138: +0.028, better on 17 and worse on 10, p = 0.027;
  - DeepScholar-base's own picks 0.047: 3.6×.

  It is ahead of D-SPECTRA at every budget (0.096 vs 0.080 at B = 10, 0.253 vs 0.214 at B = 60), and 97% of its picks have an abstract.
- **The model-only query link** (`qlink5_eta0`) is as strong (0.166), but not significantly better than D-SPECTRA (p = 0.058). Like most-cited, 21% of its picks have no abstract.
- **The design set overstated the gains.** Over D-SPECTRA they were +0.134 (model only) and +0.125 (with relevance) on the design queries, against +0.046 and +0.047 on the held-out ones. Picking the best of 9 configurations per family on 20 queries inflates the design numbers, which is why the claim rests on the 43 held-out queries.
- **Anchors.** On the fixed fits the design queries choose 5 anchors for query link + relevance, where the pre-fix fits chose 10. The frozen method of E10–E12 keeps 10 anchors (it was frozen before the fix); with 5 anchors it would be +0.005 held out, seed-averaged (16 wins / 15 losses, p = 0.36; table in 3.10).
- **η by held-out link prediction makes no difference.**
  - Held-out AUC is almost flat over η: 0.953–0.958 on the current graphs, 0.963–0.967 on the bigger ones, so the chosen η is close to arbitrary and spreads over the whole grid.
  - The resulting fit is no better than d_ev = 8: 0.111 vs 0.120 on the current graphs (p = 0.27) and 0.118 vs 0.118 on the bigger ones.
  - This rule is ours, not SPECTRA's (E14 tests SPECTRA's). Either way, capacity control has no reliable effect.
- **Pool-anchored mode weights give no gain:** 0.122 vs 0.120 on the current graphs, 0.119 vs 0.118 on the bigger ones, both n.s.
- **Bigger graphs don't help.**
  - With 861 instead of 484 papers, they contain more of the human-cited references: 41.0% vs 35.0% on the held-out queries, 46.9% vs 41.8% on the design ones.
  - But no method recalls more. Over all 43 held-out queries at the matched budget, every same-method difference is within ±0.01 and none is significant (D-SPECTRA 0.115 → 0.113, USVT 0.132 → 0.124, query link + relevance 0.159 → 0.152).
  - With about 21 papers to pick, the budget, not the graph, is the limit.
- **Pool-only setting:** no variant gains; every method recovers 0.047–0.069. The pool contains too few of the references.

### 3.9 E9: the remaining SPECTRA ingredients

All on the current-size graphs, at the matched budget (B = kept) unless stated.

**Spectral prefixes** (the kernel truncated to its top k modes; k chosen on the design queries)

**Recall by number of modes kept**

| family                  | modes kept   | design B=kept   | design B=20   | chosen   |
|:------------------------|:-------------|:----------------|:--------------|:---------|
| D-SPECTRA (d_ev = 8)    | all 32       | 0.119           | 0.095         |          |
| D-SPECTRA (d_ev = 8)    | 4            | 0.138           | 0.107         | yes      |
| D-SPECTRA (d_ev = 8)    | 8            | 0.135           | 0.095         |          |
| D-SPECTRA (d_ev = 8)    | 16           | 0.119           | 0.095         |          |
| query link (model only) | all 32       | 0.253           | 0.242         | yes      |
| query link (model only) | 4            | 0.244           | 0.212         |          |
| query link (model only) | 8            | 0.250           | 0.230         |          |
| query link (model only) | 16           | 0.248           | 0.218         |          |
| query link + relevance  | all 32       | 0.231           | 0.181         | yes      |
| query link + relevance  | 4            | 0.212           | 0.167         |          |
| query link + relevance  | 8            | 0.213           | 0.171         |          |
| query link + relevance  | 16           | 0.214           | 0.180         |          |

**The chosen number of modes vs all 32**

|                         | chosen          | held-out B=kept   | all modes, held-out B=kept   | chosen minus all modes   |
|:------------------------|:----------------|:------------------|:-----------------------------|:-------------------------|
| D-SPECTRA (d_ev = 8)    | dspectra_d8_k4  | 0.133             | 0.120                        | +0.012 (16/6, p=0.094)   |
| query link (model only) | qlink5_eta0     | 0.166             | 0.166                        | (same)                   |
| query link + relevance  | qlinkrel10_eta0 | 0.165             | 0.165                        | (same)                   |

**Early-stopped η probes** (SPECTRA's cheap probes plus a full refit, against E8's full-length probes)

**E9 early-stopped probes (63 queries)**

|                                         | full probes (E8)   | early-stopped probes + full refit   |
|:----------------------------------------|:-------------------|:------------------------------------|
| probes per query                        | 9.6                | 8.9                                 |
| probe epochs per query                  | 57,333             | 22,089 (+6,000 refit)               |
| d_ev within 5% of 8 after the final fit | 97%                | 67%                                 |

Same eta as the full-probe search on 19% of queries; mean relative d_ev error after the final fit 3.8% (full probes 2.2%).

*Recall:*

**Recall at B=kept**

|                          | design                | held-out              |
|:-------------------------|:----------------------|:----------------------|
| full probes (E8)         | 0.119                 | 0.120                 |
| early-stopped probes     | 0.117                 | 0.116                 |
| early-stopped minus full | -0.002 (1/3, p=0.713) | -0.004 (3/7, p=0.139) |

**Rank caps** (8 at η = 0 is the paper's "rank cap only" baseline; 32 is E8)

*Design queries:*

**Recall at B=kept**

|              | d_ev (d_ev = 8 fit / eta = 0 fit)   | D-SPECTRA (d_ev = 8)   | D-SPECTRA, eta = 0   | query link (model only)   | query link + relevance   | query link (model only), d_ev = 8 fit   | query link + relevance, d_ev = 8 fit   |
|:-------------|:------------------------------------|:-----------------------|:---------------------|:--------------------------|:-------------------------|:----------------------------------------|:---------------------------------------|
| rank cap 8   | – / 7.8                             | –                      | 0.121                | 0.238                     | 0.210                    | –                                       | –                                      |
| rank cap 32  | 8.0 / 28.0                          | 0.119                  | 0.161                | 0.253                     | 0.231                    | 0.244                                   | 0.210                                  |
| rank cap 64  | 8.0 / 43.3                          | 0.136                  | 0.173                | 0.250                     | 0.231                    | 0.247                                   | 0.210                                  |
| rank cap 128 | 8.0 / 44.7                          | 0.124                  | 0.170                | 0.250                     | 0.231                    | 0.243                                   | 0.210                                  |

*Held-out queries:*

**Recall at B=kept**

|              | d_ev (d_ev = 8 fit / eta = 0 fit)   | D-SPECTRA (d_ev = 8)   | D-SPECTRA, eta = 0   | query link (model only)   | query link + relevance   | query link (model only), d_ev = 8 fit   | query link + relevance, d_ev = 8 fit   |
|:-------------|:------------------------------------|:-----------------------|:---------------------|:--------------------------|:-------------------------|:----------------------------------------|:---------------------------------------|
| rank cap 8   | – / 7.8                             | –                      | 0.116                | 0.153                     | 0.155                    | –                                       | –                                      |
| rank cap 32  | 8.0 / 28.0                          | 0.120                  | 0.122                | 0.166                     | 0.165                    | 0.152                                   | 0.153                                  |
| rank cap 64  | 8.0 / 43.3                          | 0.121                  | 0.122                | 0.165                     | 0.163                    | 0.149                                   | 0.153                                  |
| rank cap 128 | 8.0 / 44.7                          | 0.120                  | 0.123                | 0.165                     | 0.163                    | 0.152                                   | 0.152                                  |

**Difference from rank cap 32, same method (B=kept)**

|                       | D-SPECTRA, eta = 0     | query link (model only)   | query link + relevance   | D-SPECTRA (d_ev = 8)   | query link (model only), d_ev = 8 fit   | query link + relevance, d_ev = 8 fit   |
|:----------------------|:-----------------------|:--------------------------|:-------------------------|:-----------------------|:----------------------------------------|:---------------------------------------|
| rank cap 8 minus 32   | -0.005 (8/13, p=0.520) | -0.013 (6/15, p=0.052)    | -0.011 (2/12, p=0.003)   | –                      | –                                       | –                                      |
| rank cap 64 minus 32  | +0.000 (3/2, p=0.786)  | -0.000 (3/4, p=0.866)     | -0.002 (2/4, p=0.345)    | +0.000 (2/2, p=1.000)  | -0.003 (2/6, p=0.401)                   | +0.000 (5/5, p=0.959)                  |
| rank cap 128 minus 32 | +0.001 (3/3, p=0.674)  | -0.001 (3/5, p=0.779)     | -0.002 (2/4, p=0.345)    | -0.000 (6/6, p=0.906)  | +0.000 (6/6, p=0.875)                   | -0.001 (4/5, p=0.767)                  |

**Three criteria for choosing η** (same grid and held-out split as E8)

**E9 eta chosen by held-out link prediction, three criteria (B=kept)**

|              | eta chosen (median, range)   | d_ev (mean)   | D-SPECTRA, design   | D-SPECTRA, held-out   | query link + relevance, held-out   | D-SPECTRA vs d_ev = 8, held-out   |
|:-------------|:-----------------------------|:--------------|:--------------------|:----------------------|:-----------------------------------|:----------------------------------|
| held-out AUC | -0.03 (-0.10 to +0.02)       | 14.7          | 0.144               | 0.111                 | 0.154                              | -0.009 (9/15, p=0.265)            |
| held-out AP  | -0.03 (-0.10 to +0.00)       | 16.5          | 0.144               | 0.120                 | 0.154                              | -0.001 (11/11, p=0.974)           |
| held-out NLL | -0.10 (-0.10 to -0.03)       | 4.5           | 0.084               | 0.103                 | 0.136                              | -0.018 (7/20, p=0.046)            |

**E9 held-out link prediction over eta (mean over 63 queries)**

| eta   | auc   | ap    | nll   | d_ev   |
|:------|:------|:------|:------|:-------|
| -0.10 | 0.958 | 0.956 | 0.748 | 3.562  |
| -0.06 | 0.958 | 0.957 | 0.792 | 7.537  |
| -0.03 | 0.958 | 0.958 | 0.843 | 15.665 |
| +0.00 | 0.958 | 0.959 | 0.873 | 28.226 |
| +0.02 | 0.956 | 0.956 | 0.908 | 29.256 |
| +0.04 | 0.954 | 0.955 | 0.928 | 29.832 |
| +0.06 | 0.953 | 0.953 | 0.945 | 30.219 |

**Fit seeds 0–2 and best-of-3 restarts** (seed 0 is E8; USVT and the other fit-free baselines don't depend on the fit seed)

**E9 seeds 0-2 and best-of-3 restarts (recall at B=kept)**

|                         | design: mean of 3 seeds (range)   | design: per-query sd across seeds   | design: best-of-3 by training NLL   | held-out: mean of 3 seeds (range)   | held-out: per-query sd across seeds   | held-out: best-of-3 by training NLL   |
|:------------------------|:----------------------------------|:------------------------------------|:------------------------------------|:------------------------------------|:--------------------------------------|:--------------------------------------|
| D-SPECTRA (d_ev = 8)    | 0.126 (0.119–0.130)               | 0.007                               | 0.123                               | 0.119 (0.117–0.120)                 | 0.008                                 | 0.119                                 |
| D-SPECTRA, eta = 0      | 0.161 (0.161–0.161)               | 0.000                               | 0.161                               | 0.121 (0.121–0.122)                 | 0.003                                 | 0.120                                 |
| query link (model only) | 0.253 (0.253–0.253)               | 0.000                               | 0.253                               | 0.165 (0.165–0.166)                 | 0.002                                 | 0.165                                 |
| query link + relevance  | 0.231 (0.231–0.231)               | 0.000                               | 0.231                               | 0.165 (0.165–0.165)                 | 0.002                                 | 0.165                                 |

**The E8 comparisons repeated per fit seed (held-out, B=kept)**

|        | query link + relevance vs D-SPECTRA   | query link + relevance vs USVT   | query link (model only) vs D-SPECTRA   |
|:-------|:--------------------------------------|:---------------------------------|:---------------------------------------|
| seed 0 | +0.045 (23/5, p=<0.001)               | +0.027 (17/7, p=0.013)           | +0.046 (18/9, p=0.058)                 |
| seed 1 | +0.048 (25/5, p=<0.001)               | +0.027 (15/7, p=0.013)           | +0.049 (18/10, p=0.035)                |
| seed 2 | +0.045 (23/5, p=<0.001)               | +0.027 (15/7, p=0.013)           | +0.045 (18/10, p=0.060)                |

**Takeaways (E9).**

- **Spectral prefixes: a small, non-significant gain for D-SPECTRA; nothing for the query link.**
  - Keeping D-SPECTRA's top 4 modes (chosen on the design queries) gives 0.133 held out against 0.120 with all 32 (+0.012, better on 16 queries and worse on 6, p = 0.094). That's still below query link + relevance and USVT (0.138).
  - For the query-link scores the design queries choose all 32 modes, so nothing changes.
- **Early-stopped η probes don't pay off.**
  - They save about half the fitting: 22,089 probe epochs plus the 6,000-epoch refit per query, against 57,333.
  - But the final fit lands within 5% of d_ev = 8 on only 67% of queries, against 97% with full probes (mean error 3.8% vs 2.2%), because a probe stopped early still moves afterwards. Recall is the same (held-out 0.116 vs 0.120, p = 0.14).
- **Overparameterisation (rank caps):**
  - The d_ev = 8 fits reach 8.0 at every cap. At η = 0 the fits spread as the cap grows and then stop: d_ev 7.8, 28.0, 43.3 and 44.7 at caps 8, 32, 64 and 128, so the graphs' realised capacity saturates at about 45 modes.
  - Nothing changes in recall: D-SPECTRA 0.120, 0.121, 0.120 at caps 32, 64, 128, query link + relevance 0.165, 0.163, 0.163, every difference within ±0.003 and none significant.
  - The "rank cap only" baseline at cap 8 is slightly worse for query link + relevance (−0.011, p = 0.003) and no different for the others.
  - Before the fix, larger caps seemed to help the query link by about 0.01; that was an artefact of the broken fits.
- **The criterion for choosing η doesn't matter, because held-out link prediction barely depends on η.**
  - Held-out AUC (0.953–0.958) and AP (0.953–0.959) are flat for η ≤ 0 and fall slightly for η > 0; held-out NLL rises monotonically with η (0.748 at −0.10 to 0.945 at +0.06), so it always picks the most negative η (d_ev ≈ 4.5).
  - D-SPECTRA on the chosen fit is no better than at d_ev = 8: AUC 0.111 (p = 0.27), AP 0.120 (p = 0.97), NLL 0.103 (−0.018, p = 0.046).
  - The query-link score is unaffected (0.154, 0.154, 0.136).
- **Fit seeds: everything is stable.**
  - Over three fit seeds, held-out recall is 0.117–0.120 for D-SPECTRA, 0.121–0.122 for η = 0, 0.165–0.166 for the query link (both versions); per query, recall varies by 0.002–0.008 (sd) across seeds.
  - Query link + relevance beats D-SPECTRA by +0.045 to +0.048 (p < 0.001) and USVT by +0.027 (p = 0.013) in every seed.
  - Best-of-3 restarts by training NLL give the same numbers, so restarts add nothing.

### 3.10 E10: selection hyperparameters and learning-rate schedule

**Selection hyperparameters** (on E8's fits; chosen on the design queries)

**Every configuration (recall)**

| family                               | config                | design B=kept   | design B=20   | held-out B=kept   |         |
|:-------------------------------------|:----------------------|:----------------|:--------------|:------------------|:--------|
| D-SPECTRA (alpha, gamma)             | dspectra_a0.25_g1     | 0.135           | 0.100         | 0.134             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.25_g10    | 0.102           | 0.074         | 0.102             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.25_g2     | 0.143           | 0.102         | 0.127             | chosen  |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.25_g20    | 0.095           | 0.080         | 0.094             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.25_g5     | 0.116           | 0.090         | 0.110             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.5_g1      | 0.114           | 0.083         | 0.118             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.5_g10     | 0.109           | 0.087         | 0.114             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.5_g2      | 0.119           | 0.086         | 0.119             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.5_g20     | 0.098           | 0.087         | 0.102             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.5_g5      | 0.119           | 0.095         | 0.120             | default |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.75_g1     | 0.092           | 0.069         | 0.097             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.75_g10    | 0.103           | 0.090         | 0.108             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.75_g2     | 0.109           | 0.076         | 0.103             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.75_g20    | 0.095           | 0.086         | 0.100             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.75_g5     | 0.106           | 0.083         | 0.113             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.9_g1      | 0.084           | 0.067         | 0.094             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.9_g10     | 0.097           | 0.076         | 0.102             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.9_g2      | 0.092           | 0.067         | 0.094             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.9_g20     | 0.095           | 0.076         | 0.100             |         |
| D-SPECTRA (alpha, gamma)             | dspectra_a0.9_g5      | 0.093           | 0.072         | 0.099             |         |
| query link + relevance (link weight) | qlinkrel10_eta0_l0.25 | 0.179           | 0.146         | 0.149             |         |
| query link + relevance (link weight) | qlinkrel10_eta0_l0.5  | 0.231           | 0.181         | 0.165             | default |
| query link + relevance (link weight) | qlinkrel10_eta0_l0.75 | 0.250           | 0.230         | 0.177             | chosen  |

Held-out values are shown for completeness; the choice uses the design columns only.

**Chosen vs default**

|                                      | chosen                | held-out B=kept   | default, held-out B=kept   | chosen minus default    |
|:-------------------------------------|:----------------------|:------------------|:---------------------------|:------------------------|
| D-SPECTRA (alpha, gamma)             | dspectra_a0.25_g2     | 0.127             | 0.120                      | +0.007 (13/10, p=0.338) |
| query link + relevance (link weight) | qlinkrel10_eta0_l0.75 | 0.177             | 0.165                      | +0.011 (15/10, p=0.158) |

**E10 tuned query link + relevance (qlinkrel10_eta0_l0.75) vs the other methods, held-out (B=kept)**

|                                 | difference               |
|:--------------------------------|:-------------------------|
| vs D-SPECTRA (d_ev = 8)         | +0.056 (25/11, p=<0.001) |
| vs USVT                         | +0.038 (20/14, p=0.005)  |
| vs raw SVD                      | +0.042 (20/14, p=0.003)  |
| vs most-cited                   | +0.081 (27/8, p=<0.001)  |
| vs relevance only               | +0.086 (32/3, p=<0.001)  |
| vs query link (model only)      | +0.011 (22/14, p=0.109)  |
| vs DeepScholar-base's own picks | +0.129 (36/2, p=<0.001)  |

**Learning-rate schedule** (cosine decay from 1e-2 to 1e-4 against the constant 1e-2)

**Convergence of the eta = 0 fits (63 queries)**

|                                                     | constant 1e-2   | cosine 1e-2 to 1e-4   |
|:----------------------------------------------------|:----------------|:----------------------|
| d_ev (eta = 0, mean)                                | 28.00           | 27.94                 |
| d_ev drift over the last 1,000 epochs (median, max) | 0.0%, 0.1%      | 0.0%, 0.0%            |
| loss rise from its minimum to the end (median, max) | 0.00%, 0.0%     | 0.00%, 0.0%           |
| fits whose loss ends more than 1% above its minimum | 0%              | 0%                    |
| training NLL (mean)                                 | 0.1035          | 0.1048                |

**Hitting d_ev = 8**

|                  | constant (E8)   | cosine   |
|:-----------------|:----------------|:---------|
| probes per query | 9.6             | 9.1      |
| within 5% of 8   | 97%             | 100%     |

**Recall at B=kept**

|                         | design: constant (E8)   | design: cosine   | held-out: constant (E8)   | held-out: cosine   | held-out: cosine minus constant   |
|:------------------------|:------------------------|:-----------------|:--------------------------|:-------------------|:----------------------------------|
| D-SPECTRA (d_ev = 8)    | 0.119                   | 0.126            | 0.120                     | 0.120              | +0.000 (4/3, p=0.735)             |
| D-SPECTRA, eta = 0      | 0.161                   | 0.161            | 0.122                     | 0.122              | +0.000 (2/2, p=0.715)             |
| query link (model only) | 0.253                   | 0.253            | 0.166                     | 0.166              | +0.001 (1/1, p=0.655)             |
| query link + relevance  | 0.231                   | 0.231            | 0.165                     | 0.166              | +0.001 (1/0, p=0.317)             |

**Search seeds 1 and 2** (graphs built from Mateo's seed-1 and seed-2 pools; E8's chosen configurations, nothing re-chosen)

**Graphs**

|                               | search seed 0   | search seed 1   | search seed 2   |
|:------------------------------|:----------------|:----------------|:----------------|
| queries                       | 63              | 63              | 63              |
| nodes (mean)                  | 483             | 482             | 484             |
| human-cited refs in the pool  | 6.1%            | 6.9%            | 6.5%            |
| human-cited refs in the graph | 37.1%           | 39.9%           | 38.2%           |

**Recall at B=kept (queries with a reference in the graph: seed 0 41, seed 1 40, seed 2 40)**

|               | DeepScholar-base's own picks   | fixed-k (search only)   | relevance only   | most-cited   | USVT   | raw SVD   | D-SPECTRA, eta = 0   | D-SPECTRA (d_ev = 8)   | query link (model only)   | query link + relevance   |
|:--------------|:-------------------------------|:------------------------|:-----------------|:-------------|:-------|:----------|:---------------------|:-----------------------|:--------------------------|:-------------------------|
| search seed 0 | 0.047                          | 0.059                   | 0.090            | 0.096        | 0.138  | 0.134     | 0.122                | 0.120                  | 0.166                     | 0.165                    |
| search seed 1 | 0.040                          | 0.063                   | 0.102            | 0.104        | 0.152  | 0.148     | 0.126                | 0.127                  | 0.186                     | 0.172                    |
| search seed 2 | 0.054                          | 0.063                   | 0.097            | 0.097        | 0.142  | 0.130     | 0.118                | 0.122                  | 0.174                     | 0.162                    |

**Query link + relevance vs each method (B=kept)**

|               | vs D-SPECTRA (d_ev = 8)   | vs USVT                 | vs most-cited           | vs relevance only       | vs DeepScholar-base's own picks   |
|:--------------|:--------------------------|:------------------------|:------------------------|:------------------------|:----------------------------------|
| search seed 0 | +0.045 (23/5, p=<0.001)   | +0.027 (17/7, p=0.013)  | +0.070 (25/9, p=0.001)  | +0.075 (31/4, p=<0.001) | +0.118 (33/2, p=<0.001)           |
| search seed 1 | +0.045 (22/3, p=<0.001)   | +0.019 (15/9, p=0.063)  | +0.068 (24/9, p=0.002)  | +0.070 (30/3, p=<0.001) | +0.131 (36/0, p=<0.001)           |
| search seed 2 | +0.040 (20/6, p=<0.001)   | +0.019 (14/11, p=0.109) | +0.065 (23/11, p=0.007) | +0.065 (27/3, p=<0.001) | +0.108 (33/1, p=<0.001)           |

**Recall at B=kept (queries with a reference in the graph: seed 0 17, seed 1 17, seed 2 17)**

|               | DeepScholar-base's own picks   | fixed-k (search only)   | relevance only   | most-cited   | USVT   | raw SVD   | D-SPECTRA, eta = 0   | D-SPECTRA (d_ev = 8)   | query link (model only)   | query link + relevance   |
|:--------------|:-------------------------------|:------------------------|:-----------------|:-------------|:-------|:----------|:---------------------|:-----------------------|:--------------------------|:-------------------------|
| search seed 0 | 0.040                          | 0.041                   | 0.076            | 0.186        | 0.205  | 0.209     | 0.161                | 0.119                  | 0.253                     | 0.231                    |
| search seed 1 | 0.053                          | 0.056                   | 0.071            | 0.187        | 0.201  | 0.211     | 0.148                | 0.141                  | 0.252                     | 0.219                    |
| search seed 2 | 0.042                          | 0.049                   | 0.089            | 0.187        | 0.218  | 0.213     | 0.168                | 0.151                  | 0.255                     | 0.220                    |

**Anchor sensitivity** (not pre-registered; added after the refit because the design queries now choose 5 anchors in E8 while the frozen method keeps 10)

**Query link + relevance with anchors re-chosen on the fixed fits (B=kept, all queries)**

|                              | design, seed 0   | held-out, seed 0   | held-out, mean of 3 seeds   |
|:-----------------------------|:-----------------|:-------------------|:----------------------------|
| 5 anchors, link weight 0.25  | 0.148            | 0.143              | 0.142                       |
| 5 anchors, link weight 0.5   | 0.207            | 0.159              | 0.161                       |
| 5 anchors, link weight 0.75  | 0.228            | 0.164              | 0.171                       |
| 10 anchors, link weight 0.25 | 0.152            | 0.142              | 0.141                       |
| 10 anchors, link weight 0.5  | 0.196            | 0.158              | 0.156                       |
| 10 anchors, link weight 0.75 | 0.212            | 0.168              | 0.166                       |

5 vs 10 anchors at link weight 0.75, held-out, mean of 3 seeds: +0.005 (16/15, p=0.357).

**Takeaways (E10).**

- **Tuning helps the query link a little, not D-SPECTRA.**
  - D-SPECTRA's best α and γ on the design queries (α = 0.25, γ = 2) give 0.127 held out, against 0.120 at the defaults (+0.007, p = 0.34).
  - For query link + relevance, a 0.75 weight on the link score gives 0.177, against 0.165 at 0.5 (+0.011, better on 15 queries and worse on 10, p = 0.16). That beats D-SPECTRA (+0.056, p < 0.001), USVT (+0.038, 20 vs 14, p = 0.005), most-cited (+0.081, p < 0.001) and DeepScholar's own picks (+0.129).
  - Five anchors instead of ten would add +0.005 seed-averaged (p = 0.36). The frozen method keeps ten.
- **The learning-rate schedule no longer matters.** With bug 4 fixed, the constant rate already converges: d_ev drifts 0.0% over the last 1,000 epochs (max 0.1%) and no fit's loss ends above its minimum; the cosine schedule gives the same (training NLL 0.1048 vs 0.1035, recall identical, every p ≥ 0.3). The pre-fix version of this experiment found that the schedule removed the drift but not the loss rise; that rise was the bug.
- **Search seeds agree.** On seeds 1 and 2 the graphs contain 39.9% and 38.2% of the human-cited references (seed 0: 37.1%). Held out, query link + relevance beats D-SPECTRA by +0.045 and +0.040 (p < 0.001), relevance only by +0.070 and +0.065, and is ahead of USVT by +0.019 in both (p = 0.063 and 0.11; seed 0: +0.027, p = 0.013). The seed-averaged, corrected version is in 3.13.

### 3.11 The judge: setup and DeepScholar-base's scores

We cloned DeepScholar-Bench (`/home/eftychia/Spectra/deepscholar-bench`, commit c95413b) and run its released evaluation code (`eval/`) with a **local judge**: Llama-3.1-70B-Instruct (GPTQ 4-bit) served by vLLM 0.6.3 on GPU 1, localhost only. The paper's judge is gpt-4o.

**Why the scores can't be compared with the paper's.** The judge model differs, and the paper's full system outputs aren't published: the repository has only 2–3 sample reports per system. On top of that, its shipped judge scores pair those samples with the wrong benchmark rows, so they can't be used to calibrate a different judge either. Comparisons under this judge (DeepScholar-base against our methods, through the same writer) are valid.

**Changes needed to run it locally** (all in `judge/deepscholar-bench-local-judge.patch` and `judge/relay.py`):
- a longer timeout per judge call;
- OpenAlex lookups with our key, without printing URLs;
- the organization metric reading the judge's decision when LOTUS returns it as plain text;
- a localhost relay that renames `max_completion_tokens`, caps replies at 2,048 tokens, and passes the JSON format to vLLM as `guided_json`, which vLLM 0.6.3 enforces;
- a one-line vLLM fix so the server binds to localhost only.

**DeepScholar-base, Mateo's seed-0 reports (63 queries, Qwen3-8B writer):**

| Metric | Score |
|---|---|
| Nugget coverage | 0.09 |
| Reference coverage | 0.09 |
| Document importance | 0.11 |
| Citation precision | 0.09 |
| Claim coverage | 0.33 |
| Coverage relevance (0–2) | 1.43 |
| Organization | 0.50 on every report: uninformative with this judge |

- **Organization:** the judge always prefers whichever related-work section it is shown first, so both orderings cancel out on every report.
- **Citation precision and claim coverage:** these count every sentence of 50 characters or more, and a sentence without a citation scores 0. Mateo's reports cite only about half their papers inline (11.3 of 21.2), so the writer's citation habits pull these scores down. That affects every method equally, since they all go through the same writer.
- **Cost:** the judge took about 2.4 hours for 63 reports (all 7 metrics) on GPU 1.
- **These numbers are not the baseline for our methods.** Mateo's reports come from an earlier version of the writer run; rerunning DeepScholar-base's *same kept lists* through the writer we use for every method (3.20) gives nugget coverage 0.070, reference coverage 0.090, citation precision 0.444, claim coverage 0.613 and coverage relevance 1.62 on the same 63 queries: the rerun's reports cite far more inline, which moves the citation-based metrics by a factor of 2–5. Every comparison in 3.20 is against that rerun, so the baseline and the methods share one writer.
- **Document importance** is not usable from any of our judge runs: the metric looks each cited title up on OpenAlex, which rate-limited the lookups (HTTP 429) during most runs, so most systems score exactly 0 on every report. It can be recomputed without the judge model (`EVALS=document_importance run_judge.sh`) once the OpenAlex quota allows.

### 3.12 E11: what else helps the query link

**The chosen configuration of each family at B=kept (differences: mean, wins/losses, paired Wilcoxon p)**

|                                            | config                | design B=kept   | held-out B=kept   | vs tuned query link + relevance   | vs USVT                 | vs D-SPECTRA             |
|:-------------------------------------------|:----------------------|:----------------|:------------------|:----------------------------------|:------------------------|:-------------------------|
| query link + relevance, tuned (E10)        | qlinkrel10_eta0_l0.75 | 0.250           | 0.177             |                                   | +0.038 (20/14, p=0.005) | +0.056 (25/11, p=<0.001) |
| query link, model only (E8)                | qlink5_eta0           | 0.253           | 0.166             | -0.011 (14/22, p=0.109)           | +0.027 (13/11, p=0.568) | +0.046 (18/9, p=0.058)   |
| co-citation by the anchors (no model)      | cocite10              | 0.256           | 0.168             | -0.009 (9/20, p=0.222)            | +0.030 (13/16, p=0.538) | +0.048 (19/16, p=0.047)  |
| co-citation + relevance (no model)         | cocite10_l0.75        | 0.257           | 0.172             | -0.005 (7/13, p=0.360)            | +0.033 (17/17, p=0.064) | +0.051 (24/12, p=0.001)  |
| query link on the USVT-denoised matrix     | usvtlink5             | 0.253           | 0.167             | -0.010 (7/23, p=0.033)            | +0.028 (13/18, p=0.543) | +0.046 (19/15, p=0.074)  |
| USVT query link + relevance                | usvtlink5_l0.75       | 0.258           | 0.184             | +0.007 (15/9, p=0.265)            | +0.046 (20/11, p=0.001) | +0.064 (25/9, p=<0.001)  |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.75_g1           | 0.248           | 0.173             | -0.004 (3/7, p=0.333)             | +0.034 (20/13, p=0.009) | +0.052 (25/11, p=<0.001) |
| fusion of query link + relevance with USVT | rrf0.75               | 0.242           | 0.165             | -0.012 (5/14, p=0.080)            | +0.026 (16/16, p=0.041) | +0.045 (25/11, p=<0.001) |
| query link from the query's own text       | qtext1                | 0.244           | 0.150             | -0.027 (9/22, p=0.050)            | +0.011 (15/17, p=0.874) | +0.029 (20/14, p=0.225)  |
| query link from text + relevance           | qtext1_l0.75          | 0.239           | 0.174             | -0.003 (10/13, p=0.976)           | +0.035 (20/13, p=0.003) | +0.053 (24/12, p=<0.001) |

**Does the fitted directed model beat simpler versions of the same idea? (B=kept)**

|                                                                              | difference              | budgets 10 / 20 / 60     |
|:-----------------------------------------------------------------------------|:------------------------|:-------------------------|
| model only: query link (E8) vs co-citation (no model)                        | -0.002 (19/11, p=0.789) | +0.000 / +0.010 / -0.010 |
| with relevance: tuned query link (E10) vs co-citation + relevance (no model) | +0.005 (13/7, p=0.360)  | +0.004 / -0.007 / +0.006 |
| with relevance: tuned query link (E10) vs USVT query link + relevance        | -0.007 (9/15, p=0.265)  | -0.001 / -0.011 / +0.005 |

*Every configuration on the design queries (the selection rule):*

**Every configuration (recall)**

| family                                     | config           | design B=kept   | design B=20   | chosen   |
|:-------------------------------------------|:-----------------|:----------------|:--------------|:---------|
| co-citation by the anchors (no model)      | cocite10         | 0.256           | 0.225         | yes      |
| co-citation by the anchors (no model)      | cocite20         | 0.244           | 0.232         |          |
| co-citation by the anchors (no model)      | cocite5          | 0.235           | 0.202         |          |
| co-citation + relevance (no model)         | cocite10_l0.5    | 0.189           | 0.173         |          |
| co-citation + relevance (no model)         | cocite10_l0.75   | 0.257           | 0.231         | yes      |
| co-citation + relevance (no model)         | cocite20_l0.5    | 0.185           | 0.174         |          |
| co-citation + relevance (no model)         | cocite20_l0.75   | 0.255           | 0.231         |          |
| co-citation + relevance (no model)         | cocite5_l0.5     | 0.156           | 0.133         |          |
| co-citation + relevance (no model)         | cocite5_l0.75    | 0.223           | 0.203         |          |
| query link on the USVT-denoised matrix     | usvtlink10       | 0.250           | 0.228         |          |
| query link on the USVT-denoised matrix     | usvtlink20       | 0.244           | 0.220         |          |
| query link on the USVT-denoised matrix     | usvtlink5        | 0.253           | 0.223         | yes      |
| USVT query link + relevance                | usvtlink10_l0.5  | 0.210           | 0.179         |          |
| USVT query link + relevance                | usvtlink10_l0.75 | 0.252           | 0.238         |          |
| USVT query link + relevance                | usvtlink20_l0.5  | 0.203           | 0.170         |          |
| USVT query link + relevance                | usvtlink20_l0.75 | 0.226           | 0.224         |          |
| USVT query link + relevance                | usvtlink5_l0.5   | 0.225           | 0.186         |          |
| USVT query link + relevance                | usvtlink5_l0.75  | 0.258           | 0.236         | yes      |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.25_g1      | 0.211           | 0.174         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.25_g10     | 0.155           | 0.137         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.25_g2      | 0.189           | 0.158         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.25_g5      | 0.160           | 0.135         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.5_g1       | 0.242           | 0.228         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.5_g10      | 0.196           | 0.163         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.5_g2       | 0.211           | 0.203         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.5_g5       | 0.204           | 0.168         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.75_g1      | 0.248           | 0.230         | yes      |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.75_g10     | 0.232           | 0.205         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.75_g2      | 0.244           | 0.222         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.75_g5      | 0.241           | 0.218         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.9_g1       | 0.247           | 0.226         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.9_g10      | 0.244           | 0.220         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.9_g2       | 0.247           | 0.226         |          |
| D-SPECTRA v2 (coverage on the link score)  | v2_a0.9_g5       | 0.245           | 0.228         |          |
| fusion of query link + relevance with USVT | rrf0.25          | 0.205           | 0.180         |          |
| fusion of query link + relevance with USVT | rrf0.5           | 0.202           | 0.177         |          |
| fusion of query link + relevance with USVT | rrf0.75          | 0.242           | 0.208         | yes      |
| query link from the query's own text       | qtext1           | 0.244           | 0.224         | yes      |
| query link from the query's own text       | qtext10          | 0.207           | 0.185         |          |
| query link from the query's own text       | qtext100         | 0.175           | 0.160         |          |
| query link from text + relevance           | qtext100_l0.5    | 0.211           | 0.164         |          |
| query link from text + relevance           | qtext100_l0.75   | 0.207           | 0.181         |          |
| query link from text + relevance           | qtext10_l0.5     | 0.208           | 0.163         |          |
| query link from text + relevance           | qtext10_l0.75    | 0.211           | 0.194         |          |
| query link from text + relevance           | qtext1_l0.5      | 0.222           | 0.174         |          |
| query link from text + relevance           | qtext1_l0.75     | 0.239           | 0.219         | yes      |

**Takeaways (E11).**

- **The fitted directed model is not what makes the query link work.** A model-free count recovers as much on the held-out queries at the matched budget. It scores each paper by how many of the 10 most relevant pool papers cite it, weighted by relevance:
  - count only: 0.168, against 0.166 for the model-only query link (−0.002, p = 0.79);
  - with relevance: 0.172, against 0.177 for the tuned query link + relevance (−0.005, p = 0.36).
- **The best method is the same idea on USVT's denoised citation matrix, plus relevance** (`usvtlink5_l0.75`): **0.184** held out. That beats:
  - USVT: +0.046, better on 20 queries and worse on 11, p = 0.001;
  - D-SPECTRA: +0.064, p < 0.001;
  - DeepScholar-base's own picks: 0.047, so 3.9×.
  - Against the tuned SPECTRA query link + relevance it is +0.007 (15 vs 9, p = 0.27): not a significant difference. Before the fix it was +0.020 (p = 0.009); the refit closed that gap.
- **Coverage on top of the link score adds nothing.** D-SPECTRA v2 chose α = 0.75, γ = 1 and gets 0.173 against 0.177 for the link score alone (p = 0.33).
- **Fusion with USVT adds nothing** (0.165).
- **Predicting the query's citing role from its text is worse than using the anchors:** 0.150 model only (−0.027, p = 0.050), and 0.174 with relevance, the same as the anchors.
- **So the gain comes from the query-as-citing-node idea itself:** "what do the papers most like the query cite?", with text relevance mixed in. Directed SPECTRA, a plain count and USVT denoising of the same citations give the same recall (0.172–0.184, no pair significantly different after correction; 3.13).
- **These comparisons are the last that should use the 43 held-out queries as a test.** Every round from E8 on tuned something on the design queries and then reported on the held-out ones, and the E11 and E13 methods were designed after earlier held-out results had been seen. The frozen methods are checked on Mateo's search seeds 1 and 2 (E10, E12), but new queries would be the clean test.

### 3.13 E12: final checks

**Frozen methods and selection lists** (`scripts/export_final.py` → `selections/final/s{0,1,2}/`, 63 queries per seed, as many papers as DeepScholar-base kept):
- `fixed_k`, `relevance_only` and `dspectra` (as proposed);
- `qlink_rel`: query link + relevance, 10 anchors, link weight 0.75 (E10);
- `cocite_rel` and `usvt_cocite_rel`: co-citation + relevance, plain and USVT-denoised (E11);
- `oracle`: the benchmark's important human-cited references, up to 30 with abstracts first. This is the proposal's ideal-sources upper bound. It is exported but has not been run through the writer.

The lists were regenerated after bug 4 and reproduce the held-out recall of the tables exactly (seed 0: 0.059, 0.090, 0.120, 0.177, 0.172, 0.184 over the 41 queries with a reachable reference; seeds 1 and 2 likewise). Each paper has a `url`: arXiv if there is one, otherwise Semantic Scholar. 16–25% of the expanded methods' picks are not on arXiv.

**The judge must see non-arXiv papers.** DeepScholar-Bench's parser only resolved arXiv links, so citations of those papers would have been dropped. That would have lowered citation precision and claim coverage for the expanded methods but not for DeepScholar-base. The parser now also accepts the URLs listed in `paper.csv`, and DeepScholar-base's reports parse exactly as before.

**The step-2 gate on judged coverage** (`scripts/gate_judged.py`, DeepScholar-base seed 0, 63 queries, local judge). S is the set of papers each report cites (11.3 on average) or all papers passed to the writer (21); d_ev(S) is on the d_ev = 8 fit. The last two columns show the pre-fix fits.

**E12 the step-2 gate on judged coverage (DeepScholar-base, seed 0, 63 queries)**

| set S                           | judged metric           | rho of d_ev(S)   | rho of |S|       | rho of d_ev(S) given |S|   | before the fix: rho of d_ev(S)   | before the fix: given |S|   |
|:--------------------------------|:------------------------|:-----------------|:-----------------|:---------------------------|:---------------------------------|:----------------------------|
| papers the report cites         | nugget_coverage         | -0.07 (p=0.584)  | +0.01 (p=0.937)  | -0.11 (p=0.378)            | +0.07                            | +0.02 (p=0.905)             |
| papers the report cites         | reference_coverage      | +0.22 (p=0.090)  | +0.14 (p=0.267)  | +0.13 (p=0.323)            | -0.10                            | -0.20 (p=0.121)             |
| papers the report cites         | document_importance     | +0.07 (p=0.599)  | +0.12 (p=0.359)  | -0.04 (p=0.741)            | +0.03                            | -0.04 (p=0.749)             |
| papers the report cites         | cite_p                  | +0.22 (p=0.077)  | +0.27 (p=0.034)  | +0.12 (p=0.349)            | -0.02                            | -0.12 (p=0.364)             |
| papers the report cites         | claim_coverage          | +0.28 (p=0.025)  | +0.38 (p=0.002)  | +0.14 (p=0.269)            | +0.21                            | +0.05 (p=0.717)             |
| papers the report cites         | coverage_relevance_rate | -0.04 (p=0.745)  | -0.12 (p=0.336)  | +0.03 (p=0.816)            | -0.16                            | -0.14 (p=0.269)             |
| all papers passed to the writer | nugget_coverage         | -0.03 (p=0.833)  | -0.04 (p=0.740)  | -0.01 (p=0.915)            | +0.12                            | +0.16 (p=0.222)             |
| all papers passed to the writer | reference_coverage      | +0.10 (p=0.432)  | +0.18 (p=0.166)  | +0.04 (p=0.762)            | -0.08                            | -0.11 (p=0.401)             |
| all papers passed to the writer | document_importance     | -0.05 (p=0.703)  | +0.15 (p=0.256)  | -0.08 (p=0.553)            | -0.01                            | -0.06 (p=0.666)             |
| all papers passed to the writer | cite_p                  | +0.27 (p=0.029)  | +0.17 (p=0.178)  | +0.24 (p=0.054)            | +0.06                            | +0.05 (p=0.704)             |
| all papers passed to the writer | claim_coverage          | +0.36 (p=0.004)  | +0.02 (p=0.886)  | +0.35 (p=0.005)            | +0.27                            | +0.27 (p=0.034)             |
| all papers passed to the writer | coverage_relevance_rate | +0.02 (p=0.879)  | +0.51 (p=<0.001) | -0.05 (p=0.674)            | -0.15                            | -0.20 (p=0.108)             |

- **d_ev of the baseline's citation sets does not track judged nugget coverage**, the primary endpoint (ρ = −0.07 and −0.03), so the gate fails on judged coverage as well as on recall.
- d_ev(S) of all papers passed does track **claim coverage** (ρ = +0.36, p = 0.004; +0.35 given |S|, p = 0.005), the one cell of 12 that would survive a Holm correction, and it was the same cell before the fix (+0.27, p = 0.034). Claim coverage counts sentences with a supporting citation, so a more spread-out set of sources may give the writer more to cite. That is a lead for the judged runs, not a passed gate.

**Seed-averaged, corrected comparisons** (`scripts/seed_tests.py`). Per-query recall at B = kept, averaged over search seeds 0–2. All 43 held-out queries are included, with recall 0 where nothing is reachable, so the values are slightly below the 41-query means elsewhere. Holm correction over all 16 comparisons:

**E12 seed-averaged recall at B=kept (43 held-out and 20 design queries, recall 0 where nothing is reachable)**

|                              | design, mean of 3 seeds   | design, per-seed range   | held-out, mean of 3 seeds   | held-out, per-seed range   |
|:-----------------------------|:--------------------------|:-------------------------|:----------------------------|:---------------------------|
| USVT co-citation + relevance | 0.221                     | 0.218–0.224              | 0.174                       | 0.171–0.175                |
| co-citation + relevance      | 0.219                     | 0.215–0.224              | 0.168                       | 0.164–0.174                |
| query link + relevance       | 0.218                     | 0.212–0.227              | 0.166                       | 0.162–0.168                |
| USVT                         | 0.177                     | 0.170–0.185              | 0.135                       | 0.132–0.142                |
| D-SPECTRA                    | 0.117                     | 0.101–0.128              | 0.115                       | 0.113–0.118                |
| most-cited                   | 0.159                     | 0.158–0.159              | 0.093                       | 0.090–0.097                |
| relevance only               | 0.067                     | 0.060–0.075              | 0.090                       | 0.086–0.095                |
| fixed-k                      | 0.041                     | 0.035–0.047              | 0.058                       | 0.057–0.059                |
| DeepScholar-base's own picks | 0.038                     | 0.034–0.045              | 0.044                       | 0.038–0.050                |

**E12 seed-averaged comparisons, held-out (all 16, Holm-corrected)**

| comparison                                                   | difference   | wins/losses   | p      | Holm p   |
|:-------------------------------------------------------------|:-------------|:--------------|:-------|:---------|
| D-SPECTRA vs DeepScholar-base's own picks                    | +0.071       | 33/4          | <0.001 | <0.001   |
| D-SPECTRA vs fixed-k                                         | +0.057       | 31/6          | <0.001 | 0.002    |
| D-SPECTRA vs relevance only                                  | +0.025       | 27/7          | 0.003  | 0.030    |
| D-SPECTRA vs USVT                                            | -0.020       | 11/22         | 0.046  | 0.278    |
| D-SPECTRA vs most-cited                                      | +0.023       | 23/14         | 0.152  | 0.607    |
| query link + relevance vs D-SPECTRA                          | +0.050       | 27/9          | <0.001 | <0.001   |
| query link + relevance vs USVT                               | +0.030       | 22/13         | 0.005  | 0.041    |
| query link + relevance vs relevance only                     | +0.075       | 33/5          | <0.001 | <0.001   |
| query link + relevance vs co-citation + relevance            | -0.003       | 17/14         | 0.860  | 0.860    |
| co-citation + relevance vs D-SPECTRA                         | +0.053       | 27/9          | <0.001 | 0.002    |
| co-citation + relevance vs USVT                              | +0.033       | 20/16         | 0.050  | 0.278    |
| USVT co-citation + relevance vs D-SPECTRA                    | +0.058       | 26/9          | <0.001 | 0.002    |
| USVT co-citation + relevance vs USVT                         | +0.038       | 22/10         | 0.005  | 0.041    |
| USVT co-citation + relevance vs query link + relevance       | +0.008       | 20/13         | 0.253  | 0.758    |
| USVT co-citation + relevance vs co-citation + relevance      | +0.005       | 18/13         | 0.367  | 0.758    |
| USVT co-citation + relevance vs DeepScholar-base's own picks | +0.130       | 36/1          | <0.001 | <0.001   |

**The main ablation, both readings.** The proposal's "D-SPECTRA without the spectral term" can mean dropping the coverage term (α = 1, which is relevance only over the expanded graph and therefore also the proposal's "citation expansion only" baseline; they are one method here) or dropping capacity control (η = 0). The two give different answers:

**E12 the main ablation, both readings (held-out, mean of 3 search seeds, B=kept)**

|                                                                              | comparison value   | D-SPECTRA   | difference   | wins/losses   | p     | Holm p                  |
|:-----------------------------------------------------------------------------|:-------------------|:------------|:-------------|:--------------|:------|:------------------------|
| alpha = 1: no coverage term (relevance only; also 'citation expansion only') | 0.090              | 0.115       | +0.025       | 27/7          | 0.003 | 0.030                   |
| eta = 0: no capacity control                                                 | 0.114              | 0.115       | +0.001       | 14/14         | 0.982 | not in the family of 16 |

- **D-SPECTRA beats relevance only after correction** (+0.025, Holm p = 0.030; before the fix this was Holm p = 0.057). It still beats DeepScholar-base's picks and fixed-k (Holm p ≤ 0.002), and it does not beat USVT (−0.020, Holm p = 0.28) or most-cited.
- **D-SPECTRA ties η = 0** (+0.001, 14 wins / 14 losses, p = 0.98). So the coverage term helps over plain relevance; capacity control does not help over no capacity control.
- **All three query-anchored methods beat D-SPECTRA** (Holm p ≤ 0.002) and are indistinguishable from each other (+0.003 to +0.008, Holm p ≥ 0.76). The USVT co-citation version and the SPECTRA query link also beat USVT (Holm p = 0.041 each); the plain count does not quite (Holm p = 0.28).

**Cost per query** (held-out recall at each budget, seed 0, all 43 queries):

**E12 cost per query (held-out recall at each budget, seed 0, all 43 queries)**

|                              | B = 10      | B = 20      | B = kept     | B = 60       | Semantic Scholar requests   | GPU fitting                            |
|:-----------------------------|:------------|:------------|:-------------|:-------------|:----------------------------|:---------------------------------------|
| DeepScholar-base's own picks |             |             | 0.045 @ 289k |              | –                           | –                                      |
| fixed-k                      | 0.041 @ 71k | 0.052 @ 87k | 0.057 @ 89k  | 0.066 @ 152k | 0                           | –                                      |
| relevance only               | 0.051 @ 71k | 0.085 @ 87k | 0.086 @ 89k  | 0.165 @ 152k | ≈ 12                        | –                                      |
| D-SPECTRA                    | 0.076 @ 71k | 0.112 @ 87k | 0.115 @ 89k  | 0.204 @ 152k | ≈ 12                        | d_ev = 8 search, ≈ 4 min on a free GPU |
| USVT                         | 0.075 @ 71k | 0.128 @ 87k | 0.132 @ 89k  | 0.220 @ 152k | ≈ 12                        | SVD, < 1 s                             |
| query link + relevance       | 0.113 @ 71k | 0.157 @ 87k | 0.168 @ 89k  | 0.261 @ 152k | ≈ 12                        | one eta = 0 fit, ≈ 18 s on a free GPU  |
| co-citation + relevance      | 0.109 @ 71k | 0.164 @ 87k | 0.164 @ 89k  | 0.255 @ 152k | ≈ 12                        | none                                   |
| USVT co-citation + relevance | 0.114 @ 71k | 0.167 @ 87k | 0.175 @ 89k  | 0.255 @ 152k | ≈ 12                        | SVD, < 1 s                             |

LLM tokens: DeepScholar-base's search (43,885) + its filter (199,785, DeepScholar-base only) + the writer, which grows by 1,626 tokens per paper from 10,502 (r = 0.93 over 62 queries).

- **The best methods are also nearly free.** USVT co-citation + relevance needs no model fitting, only the citation graph (about 12 Semantic Scholar requests); the SPECTRA query link needs one 18-second fit.
- At about 89,000 tokens per query, USVT co-citation + relevance recovers 3.9× DeepScholar-base's picks, which cost about 289,000.
- Even at 10 papers (71,000 tokens), it recovers more than double DeepScholar-base's picks (0.114 vs 0.045).
- Not done: cost–coverage frontiers over tokens on the judged metrics, and charging citation lookups against a matched budget.

### 3.14 E13: can the fitted SPECTRA model itself win?

**Recall at B=kept (queries with a reference in the graph: seed 0 41, seed 1 40, seed 2 40)**

|                                                       | seed 0   | seed 1   | seed 2   | mean of seeds   |
|:------------------------------------------------------|:---------|:---------|:---------|:----------------|
| SPECTRA co-citation + relevance (scocite_eta0_k32_m5) | 0.177    | 0.186    | 0.188    | 0.184           |
| learned ranker (all features)                         | 0.176    | 0.188    | 0.169    | 0.177           |
| learned ranker without SPECTRA features               | 0.167    | 0.179    | 0.161    | 0.169           |
| USVT co-citation + relevance (E11)                    | 0.184    | 0.188    | 0.184    | 0.185           |
| co-citation + relevance (E11)                         | 0.172    | 0.187    | 0.180    | 0.180           |
| query link + relevance (E10)                          | 0.177    | 0.179    | 0.174    | 0.177           |
| USVT                                                  | 0.138    | 0.152    | 0.142    | 0.144           |
| D-SPECTRA                                             | 0.120    | 0.127    | 0.122    | 0.123           |
| DeepScholar-base's own picks                          | 0.047    | 0.040    | 0.054    | 0.047           |

**Paired comparisons at B=kept (mean difference, wins/losses, Wilcoxon p)**

|                                                                                             | seed 0                  | seed 1                  | seed 2                  |
|:--------------------------------------------------------------------------------------------|:------------------------|:------------------------|:------------------------|
| SPECTRA co-citation + relevance (scocite_eta0_k32_m5) vs USVT co-citation + relevance (E11) | -0.007 (9/13, p=0.230)  | -0.002 (9/9, p=0.616)   | +0.004 (12/9, p=0.664)  |
| SPECTRA co-citation + relevance (scocite_eta0_k32_m5) vs co-citation + relevance (E11)      | +0.005 (15/8, p=0.648)  | -0.001 (13/11, p=0.966) | +0.008 (16/9, p=0.360)  |
| SPECTRA co-citation + relevance (scocite_eta0_k32_m5) vs query link + relevance (E10)       | -0.000 (9/12, p=0.781)  | +0.007 (12/10, p=0.516) | +0.014 (14/6, p=0.054)  |
| SPECTRA co-citation + relevance (scocite_eta0_k32_m5) vs USVT                               | +0.038 (19/15, p=0.033) | +0.034 (17/15, p=0.068) | +0.046 (20/14, p=0.008) |
| SPECTRA co-citation + relevance (scocite_eta0_k32_m5) vs D-SPECTRA                          | +0.056 (24/13, p=0.002) | +0.059 (25/10, p=0.001) | +0.067 (26/8, p=<0.001) |
| learned ranker (all features) vs USVT co-citation + relevance (E11)                         | -0.008 (9/11, p=0.198)  | +0.000 (13/12, p=0.893) | -0.015 (10/16, p=0.115) |
| learned ranker (all features) vs learned ranker without SPECTRA features                    | +0.009 (10/4, p=0.084)  | +0.009 (10/1, p=0.045)  | +0.007 (7/5, p=0.239)   |
| learned ranker without SPECTRA features vs USVT co-citation + relevance (E11)               | -0.017 (10/15, p=0.031) | -0.009 (10/14, p=0.236) | -0.023 (9/15, p=0.084)  |

*Seed-averaged, Holm-corrected (43 held-out queries, recall 0 where nothing is reachable):*

**E13 seed-averaged recall at B=kept (43 held-out queries, recall 0 where nothing is reachable)**

|                                         | held-out, mean of 3 seeds   |
|:----------------------------------------|:----------------------------|
| USVT co-citation + relevance            | 0.174                       |
| SPECTRA co-citation + relevance         | 0.172                       |
| co-citation + relevance                 | 0.168                       |
| learned ranker (all features)           | 0.166                       |
| query link + relevance                  | 0.166                       |
| learned ranker without SPECTRA features | 0.159                       |
| USVT                                    | 0.135                       |
| D-SPECTRA (d_ev = 8)                    | 0.115                       |

**E13 seed-averaged comparisons, held-out (8 comparisons, Holm-corrected)**

|                                                                          | difference   | wins/losses   | p      | Holm p   |
|:-------------------------------------------------------------------------|:-------------|:--------------|:-------|:---------|
| SPECTRA co-citation + relevance vs USVT co-citation + relevance          | -0.002       | 14/14         | 0.699  | 1.000    |
| SPECTRA co-citation + relevance vs co-citation + relevance               | +0.004       | 18/13         | 0.327  | 1.000    |
| SPECTRA co-citation + relevance vs query link + relevance                | +0.006       | 18/13         | 0.410  | 1.000    |
| SPECTRA co-citation + relevance vs USVT                                  | +0.037       | 20/15         | 0.041  | 0.284    |
| SPECTRA co-citation + relevance vs D-SPECTRA (d_ev = 8)                  | +0.057       | 26/10         | <0.001 | 0.003    |
| learned ranker (all features) vs USVT co-citation + relevance            | -0.007       | 14/14         | 0.362  | 1.000    |
| learned ranker (all features) vs learned ranker without SPECTRA features | +0.008       | 15/7          | 0.048  | 0.286    |
| learned ranker without SPECTRA features vs USVT co-citation + relevance  | -0.015       | 14/17         | 0.100  | 0.499    |

**Scocite_eta0_k*_m5 by number of modes kept (recall at B=kept)**

|              | seed 0   | seed 1   | seed 2   | vs all 32 modes (seed 0)   |
|:-------------|:---------|:---------|:---------|:---------------------------|
| top 2 modes  | 0.146    | 0.154    | 0.142    | -0.031 (8/17, p=0.051)     |
| top 4 modes  | 0.159    | 0.164    | 0.166    | -0.017 (7/14, p=0.054)     |
| top 8 modes  | 0.167    | 0.181    | 0.186    | -0.010 (8/12, p=0.135)     |
| top 16 modes | 0.176    | 0.190    | 0.190    | -0.001 (6/8, p=0.851)      |
| all 32 modes | 0.177    | 0.186    | 0.188    |                            |

*Design queries, and every SPECTRA co-citation configuration (the selection rule):*

**Recall at B=kept (queries with a reference in the graph: seed 0 17, seed 1 17, seed 2 17)**

|                                                       | seed 0   | seed 1   | seed 2   | mean of seeds   |
|:------------------------------------------------------|:---------|:---------|:---------|:----------------|
| SPECTRA co-citation + relevance (scocite_eta0_k32_m5) | 0.265    | 0.264    | 0.262    | 0.264           |
| learned ranker (all features)                         | 0.251    | 0.259    | 0.256    | 0.255           |
| learned ranker without SPECTRA features               | 0.243    | 0.244    | 0.242    | 0.243           |
| USVT co-citation + relevance (E11)                    | 0.258    | 0.264    | 0.257    | 0.260           |
| co-citation + relevance (E11)                         | 0.257    | 0.264    | 0.253    | 0.258           |
| query link + relevance (E10)                          | 0.250    | 0.252    | 0.267    | 0.256           |
| USVT                                                  | 0.205    | 0.201    | 0.218    | 0.208           |
| D-SPECTRA                                             | 0.119    | 0.141    | 0.151    | 0.137           |
| DeepScholar-base's own picks                          | 0.040    | 0.053    | 0.042    | 0.045           |

**Every configuration (recall)**

| config                   | design B=kept   | design B=20   | chosen   |
|:-------------------------|:----------------|:--------------|:---------|
| scocite_d8_k16_m10       | 0.248           | 0.225         |          |
| scocite_d8_k16_m10_obs   | 0.258           | 0.243         |          |
| scocite_d8_k16_m5        | 0.260           | 0.238         |          |
| scocite_d8_k16_m5_obs    | 0.256           | 0.244         |          |
| scocite_d8_k2_m10        | 0.220           | 0.206         |          |
| scocite_d8_k2_m10_obs    | 0.235           | 0.226         |          |
| scocite_d8_k2_m5         | 0.226           | 0.200         |          |
| scocite_d8_k2_m5_obs     | 0.242           | 0.242         |          |
| scocite_d8_k32_m10       | 0.248           | 0.225         |          |
| scocite_d8_k32_m10_obs   | 0.258           | 0.243         |          |
| scocite_d8_k32_m5        | 0.260           | 0.238         |          |
| scocite_d8_k32_m5_obs    | 0.256           | 0.244         |          |
| scocite_d8_k4_m10        | 0.232           | 0.211         |          |
| scocite_d8_k4_m10_obs    | 0.252           | 0.230         |          |
| scocite_d8_k4_m5         | 0.241           | 0.217         |          |
| scocite_d8_k4_m5_obs     | 0.251           | 0.231         |          |
| scocite_d8_k8_m10        | 0.242           | 0.221         |          |
| scocite_d8_k8_m10_obs    | 0.257           | 0.238         |          |
| scocite_d8_k8_m5         | 0.258           | 0.237         |          |
| scocite_d8_k8_m5_obs     | 0.255           | 0.240         |          |
| scocite_eta0_k16_m10     | 0.251           | 0.227         |          |
| scocite_eta0_k16_m10_obs | 0.261           | 0.235         |          |
| scocite_eta0_k16_m5      | 0.253           | 0.243         |          |
| scocite_eta0_k16_m5_obs  | 0.262           | 0.248         |          |
| scocite_eta0_k2_m10      | 0.219           | 0.206         |          |
| scocite_eta0_k2_m10_obs  | 0.248           | 0.230         |          |
| scocite_eta0_k2_m5       | 0.234           | 0.206         |          |
| scocite_eta0_k2_m5_obs   | 0.252           | 0.233         |          |
| scocite_eta0_k32_m10     | 0.251           | 0.236         |          |
| scocite_eta0_k32_m10_obs | 0.261           | 0.243         |          |
| scocite_eta0_k32_m5      | 0.265           | 0.247         | yes      |
| scocite_eta0_k32_m5_obs  | 0.258           | 0.240         |          |
| scocite_eta0_k4_m10      | 0.232           | 0.216         |          |
| scocite_eta0_k4_m10_obs  | 0.245           | 0.236         |          |
| scocite_eta0_k4_m5       | 0.233           | 0.205         |          |
| scocite_eta0_k4_m5_obs   | 0.253           | 0.242         |          |
| scocite_eta0_k8_m10      | 0.236           | 0.226         |          |
| scocite_eta0_k8_m10_obs  | 0.252           | 0.238         |          |
| scocite_eta0_k8_m5       | 0.248           | 0.229         |          |
| scocite_eta0_k8_m5_obs   | 0.262           | 0.237         |          |

**Takeaways (E13).**

- **SPECTRA co-citation is the best use of the fitted model, and it now matches the USVT version.**
  - Chosen on the design queries (η = 0 fit, all 32 modes, 5 anchors, predictions only; before the fix the choice was 16 modes, 10 anchors, with observed citations), it recovers 0.177, 0.186 and 0.188 held out across the three search seeds, 0.172 seed-averaged over all 43.
  - Against USVT co-citation + relevance: −0.002 (14 wins / 14 losses, Holm p = 1.0); before the fix it was behind by 0.014.
  - It beats D-SPECTRA (+0.057, Holm p = 0.003) and is ahead of USVT (+0.037, p = 0.041 uncorrected, Holm p = 0.28).
  - It is level with plain co-citation (+0.004) and the SPECTRA query link (+0.006).
- **Capacity matters a little for this score, in the direction of more.**
  - 2 modes: 0.146 (−0.031 vs all 32, p = 0.051); 4: 0.159; 8: 0.167; 16 and 32: 0.176–0.177.
  - Before the fix, 4 to 32 modes were flat; the fixed fits spread their information over more modes (d_ev ≈ 28 at η = 0 instead of 8.5), so truncating them costs more.
- **SPECTRA's features carry a little information beyond the simple scores, but not enough to win.**
  - The learned ranker with SPECTRA features recovers 0.166 seed-averaged, against 0.159 without them (+0.008, 15 vs 7, Holm p = 0.29).
  - Neither ranker beats the plain USVT co-citation score (−0.007 and −0.015, n.s.).
- **On recall, nothing makes the fitted directed model better than USVT denoising of the same citations.** The remaining chance for D-SPECTRA is the judged evaluation, where claim coverage may reward a spread of sources (3.13). That is why D-SPECTRA v2 (coverage on top of the link score) is worth including in the writer runs.

### 3.15 E14: SPECTRA's own capacity rule

**E14 fits (63 queries x 3 search seeds)**

| fit                                          | target d_ev (mean; min-max)   | achieved d_ev (mean)   | eta (mean)   | beta (mean)   | within 2% of target   |
|:---------------------------------------------|:------------------------------|:-----------------------|:-------------|:--------------|:----------------------|
| D-SPECTRA, tmed (median of USVT and raw SVD) | 25.4; 20.5-30.5               | 25.5                   | -0.014       | 4.994         | 100%                  |
| D-SPECTRA, tmin (USVT's effective rank)      | 22.0; 13.6-30.5               | 22.0                   | -0.020       | 4.994         | 100%                  |

**E14 seed-averaged recall at B=kept**

|                                              | design (20)   | held-out (43)   |
|:---------------------------------------------|:--------------|:----------------|
| D-SPECTRA, tmin (USVT's effective rank)      | 0.139         | 0.119           |
| D-SPECTRA, tmed (median of USVT and raw SVD) | 0.137         | 0.117           |
| D-SPECTRA (d_ev = 8)                         | 0.117         | 0.115           |
| D-SPECTRA, eta = 0                           | 0.135         | 0.114           |
| USVT                                         | 0.177         | 0.135           |
| relevance only                               | 0.067         | 0.090           |

**E14 seed-averaged comparisons, held-out (8 comparisons, Holm-corrected)**

|                                                                      | difference   | wins/losses   | p     | Holm p   |
|:---------------------------------------------------------------------|:-------------|:--------------|:------|:---------|
| D-SPECTRA, tmin (USVT's effective rank) vs relevance only            | +0.028       | 27/7          | 0.002 | 0.014    |
| D-SPECTRA, tmin (USVT's effective rank) vs USVT                      | -0.016       | 13/21         | 0.057 | 0.226    |
| D-SPECTRA, tmin (USVT's effective rank) vs D-SPECTRA (d_ev = 8)      | +0.003       | 12/10         | 0.140 | 0.419    |
| D-SPECTRA, tmin (USVT's effective rank) vs D-SPECTRA, eta = 0        | +0.004       | 13/7          | 0.011 | 0.067    |
| D-SPECTRA, tmed (median of USVT and raw SVD) vs relevance only       | +0.026       | 26/8          | 0.003 | 0.022    |
| D-SPECTRA, tmed (median of USVT and raw SVD) vs USVT                 | -0.019       | 11/20         | 0.024 | 0.121    |
| D-SPECTRA, tmed (median of USVT and raw SVD) vs D-SPECTRA (d_ev = 8) | +0.001       | 11/14         | 0.609 | 0.609    |
| D-SPECTRA, tmed (median of USVT and raw SVD) vs D-SPECTRA, eta = 0   | +0.002       | 10/6          | 0.215 | 0.429    |

**Takeaways (E14).**

- **The targets are reachable.** USVT's effective rank is 13.6–30.5 across the graphs (mean 22.0); the median of USVT and raw SVD is 20.5–30.5 (mean 25.4). Bisection hits every one within 2%, with η between −0.05 and 0 (mean −0.020 and −0.014).
- **Recall doesn't move.** Held out, seed-averaged: tmin 0.119, tmed 0.117, d_ev = 8 0.115, η = 0 0.114 (tmin vs d_ev = 8 +0.003, p = 0.14; tmin vs η = 0 +0.004, Holm p = 0.067). Both beat relevance only (Holm p ≤ 0.022) and neither beats USVT (−0.016 and −0.019, Holm p ≥ 0.12).
- **Together with E6, E8, E9 and E13:** d_ev targets of 4, 8, 14–30 and about 28 (η = 0), and η chosen by three held-out criteria, all give held-out recall within 0.114–0.122 for D-SPECTRA. On the design queries higher capacity looks better (0.139 and 0.137 here, 0.161 at η = 0, 0.119 at d_ev = 8), but that is where the 20-query noise is, and it does not transfer. There is no capacity setting at which D-SPECTRA's mode coverage beats USVT or the query-anchored scores.

### 3.16 E15: the query's citing role as the centre of selection

**The selection rule on the design queries** (seed 0, queries with a reachable reference; every configuration):

**Every configuration (recall)**

| family                                                        | config                      | design B=kept   | design B=20   | chosen   |
|:--------------------------------------------------------------|:----------------------------|:----------------|:--------------|:---------|
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m10_r_a0.25_g1    | 0.153           | 0.133         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m10_r_a0.25_g2    | 0.144           | 0.134         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m10_r_a0.25_g5    | 0.147           | 0.135         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m10_r_a0.5_g1     | 0.162           | 0.117         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m10_r_a0.5_g2     | 0.173           | 0.129         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m10_r_a0.5_g5     | 0.170           | 0.131         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m10_r_a0.75_g1    | 0.116           | 0.072         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m10_r_a0.75_g2    | 0.135           | 0.099         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m10_r_a0.75_g5    | 0.146           | 0.116         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m5_r_a0.25_g1     | 0.158           | 0.141         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m5_r_a0.25_g2     | 0.150           | 0.129         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m5_r_a0.25_g5     | 0.148           | 0.136         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m5_r_a0.5_g1      | 0.154           | 0.120         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m5_r_a0.5_g2      | 0.168           | 0.123         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m5_r_a0.5_g5      | 0.151           | 0.120         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m5_r_a0.75_g1     | 0.116           | 0.069         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m5_r_a0.75_g2     | 0.142           | 0.095         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_d8_m5_r_a0.75_g5     | 0.149           | 0.114         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m10_r_a0.25_g1  | 0.215           | 0.185         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m10_r_a0.25_g2  | 0.213           | 0.186         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m10_r_a0.25_g5  | 0.220           | 0.193         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m10_r_a0.5_g1   | 0.202           | 0.169         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m10_r_a0.5_g2   | 0.215           | 0.198         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m10_r_a0.5_g5   | 0.220           | 0.205         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m10_r_a0.75_g1  | 0.136           | 0.113         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m10_r_a0.75_g2  | 0.173           | 0.127         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m10_r_a0.75_g5  | 0.177           | 0.149         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m5_r_a0.25_g1   | 0.222           | 0.190         | yes      |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m5_r_a0.25_g2   | 0.212           | 0.183         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m5_r_a0.25_g5   | 0.215           | 0.186         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m5_r_a0.5_g1    | 0.202           | 0.170         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m5_r_a0.5_g2    | 0.212           | 0.187         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m5_r_a0.5_g5    | 0.206           | 0.186         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m5_r_a0.75_g1   | 0.134           | 0.095         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m5_r_a0.75_g2   | 0.159           | 0.122         |          |
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m5_r_a0.75_g5   | 0.170           | 0.149         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m10_ql_a0.25_g1   | 0.206           | 0.184         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m10_ql_a0.25_g2   | 0.192           | 0.171         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m10_ql_a0.25_g5   | 0.197           | 0.165         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m10_ql_a0.5_g1    | 0.232           | 0.205         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m10_ql_a0.5_g2    | 0.227           | 0.194         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m10_ql_a0.5_g5    | 0.225           | 0.186         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m10_ql_a0.75_g1   | 0.252           | 0.226         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m10_ql_a0.75_g2   | 0.253           | 0.212         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m10_ql_a0.75_g5   | 0.242           | 0.212         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m5_ql_a0.25_g1    | 0.213           | 0.184         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m5_ql_a0.25_g2    | 0.197           | 0.167         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m5_ql_a0.25_g5    | 0.199           | 0.161         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m5_ql_a0.5_g1     | 0.231           | 0.208         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m5_ql_a0.5_g2     | 0.225           | 0.202         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m5_ql_a0.5_g5     | 0.224           | 0.187         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m5_ql_a0.75_g1    | 0.252           | 0.220         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m5_ql_a0.75_g2    | 0.255           | 0.218         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_d8_m5_ql_a0.75_g5    | 0.249           | 0.208         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m10_ql_a0.25_g1 | 0.235           | 0.200         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m10_ql_a0.25_g2 | 0.229           | 0.196         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m10_ql_a0.25_g5 | 0.226           | 0.196         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m10_ql_a0.5_g1  | 0.247           | 0.218         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m10_ql_a0.5_g2  | 0.245           | 0.209         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m10_ql_a0.5_g5  | 0.235           | 0.206         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m10_ql_a0.75_g1 | 0.258           | 0.232         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m10_ql_a0.75_g2 | 0.252           | 0.230         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m10_ql_a0.75_g5 | 0.255           | 0.227         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m5_ql_a0.25_g1  | 0.228           | 0.203         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m5_ql_a0.25_g2  | 0.227           | 0.197         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m5_ql_a0.25_g5  | 0.220           | 0.198         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m5_ql_a0.5_g1   | 0.249           | 0.221         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m5_ql_a0.5_g2   | 0.240           | 0.214         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m5_ql_a0.5_g5   | 0.231           | 0.210         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m5_ql_a0.75_g1  | 0.259           | 0.244         | yes      |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m5_ql_a0.75_g2  | 0.252           | 0.243         |          |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m5_ql_a0.75_g5  | 0.248           | 0.236         |          |
| feedback on the query link                                    | prf10_r1                    | 0.198           | 0.166         |          |
| feedback on the query link                                    | prf10_r1_keep               | 0.224           | 0.196         |          |
| feedback on the query link                                    | prf10_r2                    | 0.165           | 0.134         |          |
| feedback on the query link                                    | prf10_r2_keep               | 0.215           | 0.191         |          |
| feedback on the query link                                    | prf20_r1                    | 0.207           | 0.184         |          |
| feedback on the query link                                    | prf20_r1_keep               | 0.209           | 0.185         |          |
| feedback on the query link                                    | prf20_r2                    | 0.182           | 0.139         |          |
| feedback on the query link                                    | prf20_r2_keep               | 0.203           | 0.179         |          |
| feedback on the query link                                    | prf5_r1                     | 0.192           | 0.163         |          |
| feedback on the query link                                    | prf5_r1_keep                | 0.237           | 0.214         | yes      |
| feedback on the query link                                    | prf5_r2                     | 0.152           | 0.134         |          |
| feedback on the query link                                    | prf5_r2_keep                | 0.231           | 0.213         |          |
| feedback on SPECTRA co-citation                               | sprf10_r1                   | 0.193           | 0.167         |          |
| feedback on SPECTRA co-citation                               | sprf10_r1_keep              | 0.218           | 0.198         |          |
| feedback on SPECTRA co-citation                               | sprf10_r2                   | 0.154           | 0.136         |          |
| feedback on SPECTRA co-citation                               | sprf10_r2_keep              | 0.219           | 0.188         |          |
| feedback on SPECTRA co-citation                               | sprf20_r1                   | 0.199           | 0.169         |          |
| feedback on SPECTRA co-citation                               | sprf20_r1_keep              | 0.217           | 0.189         |          |
| feedback on SPECTRA co-citation                               | sprf20_r2                   | 0.169           | 0.142         |          |
| feedback on SPECTRA co-citation                               | sprf20_r2_keep              | 0.204           | 0.160         |          |
| feedback on SPECTRA co-citation                               | sprf5_r1                    | 0.179           | 0.151         |          |
| feedback on SPECTRA co-citation                               | sprf5_r1_keep               | 0.237           | 0.207         | yes      |
| feedback on SPECTRA co-citation                               | sprf5_r2                    | 0.140           | 0.120         |          |
| feedback on SPECTRA co-citation                               | sprf5_r2_keep               | 0.231           | 0.205         |          |

Held-out values are not shown here; the choice uses the design columns only.

**Held-out queries (43), seed-averaged**

**The chosen configuration of each family and the frozen methods**

|                                                               | chosen                     | design (20)   | held-out (43)   | family range, held-out   |
|:--------------------------------------------------------------|:---------------------------|:--------------|:----------------|:-------------------------|
| query-anchored modes, relevance term = text relevance         | qmodes_eta0_m5_r_a0.25_g1  | 0.181         | 0.149           | 0.102–0.153              |
| query-anchored modes, relevance term = query link + relevance | qmodes_eta0_m5_ql_a0.75_g1 | 0.219         | 0.166           | 0.111–0.166              |
| feedback on the query link                                    | prf5_r1_keep               | 0.207         | 0.158           | 0.107–0.158              |
| feedback on SPECTRA co-citation                               | sprf5_r1_keep              | 0.204         | 0.157           | 0.097–0.157              |
| USVT co-citation + relevance (E11)                            | (frozen)                   | 0.221         | 0.174           |                          |
| SPECTRA co-citation + relevance (E13)                         | (frozen)                   | 0.224         | 0.172           |                          |
| query link + relevance (E10)                                  | (frozen)                   | 0.218         | 0.166           |                          |
| co-citation + relevance (E11)                                 | (frozen)                   | 0.219         | 0.168           |                          |
| USVT                                                          | (frozen)                   | 0.177         | 0.135           |                          |
| D-SPECTRA (d_ev = 8)                                          | (frozen)                   | 0.117         | 0.115           |                          |

Means over search seeds 0–2 per query; all queries count, recall 0 where nothing is reachable.

**The chosen configuration of each family vs the frozen methods (seed-averaged, B=kept, Holm over 16)**

|                                                                                            | vs USVT co-citation + relevance (E11)   | vs SPECTRA co-citation + relevance (E13)   | vs query link + relevance (E10)     | vs D-SPECTRA (d_ev = 8)             |
|:-------------------------------------------------------------------------------------------|:----------------------------------------|:-------------------------------------------|:------------------------------------|:------------------------------------|
| query-anchored modes, relevance term = text relevance (qmodes_eta0_m5_r_a0.25_g1)          | -0.025 (8/27, p=0.004, Holm 0.051)      | -0.023 (9/26, p=0.014, Holm 0.131)         | -0.017 (7/23, p=0.014, Holm 0.131)  | +0.034 (22/12, p=0.012, Holm 0.131) |
| query-anchored modes, relevance term = query link + relevance (qmodes_eta0_m5_ql_a0.75_g1) | -0.008 (15/21, p=0.307, Holm 0.921)     | -0.007 (15/17, p=0.495, Holm 0.968)        | -0.000 (9/14, p=0.484, Holm 0.968)  | +0.050 (27/9, p=<0.001, Holm 0.003) |
| feedback on the query link (prf5_r1_keep)                                                  | -0.016 (13/21, p=0.021, Holm 0.147)     | -0.014 (13/20, p=0.031, Holm 0.167)        | -0.008 (5/19, p=0.028, Holm 0.167)  | +0.043 (27/8, p=<0.001, Holm 0.007) |
| feedback on SPECTRA co-citation (sprf5_r1_keep)                                            | -0.017 (10/21, p=0.012, Holm 0.131)     | -0.015 (7/18, p=0.008, Holm 0.095)         | -0.009 (12/20, p=0.108, Holm 0.431) | +0.042 (26/10, p=0.002, Holm 0.035) |

**Does the new step help the score it is built on? (seed-averaged, B=kept)**

|                                                                                                  | difference (wins/losses, Wilcoxon p)   |
|:-------------------------------------------------------------------------------------------------|:---------------------------------------|
| feedback on the query link (prf5_r1_keep) vs no feedback (query link + relevance)                | -0.008 (5/19, p=0.028)                 |
| feedback on SPECTRA co-citation (sprf5_r1_keep) vs no feedback (SPECTRA co-citation + relevance) | -0.015 (7/18, p=0.008)                 |
| query-anchored modes on the link score vs the link score alone                                   | -0.000 (9/14, p=0.484)                 |

**Takeaways (E15).**

- **Query-anchored mode coverage adds nothing to the link score.** With the query link + relevance score as the relevance term, the chosen configuration (η = 0 fit, 5 anchors, α = 0.75, γ = 1) gets 0.166 held out: identical to the link score alone (−0.000, 9 wins / 14 losses, p = 0.48) and not different from USVT co-citation + relevance (−0.008, Holm p = 0.92) or SPECTRA co-citation (−0.007). The best α on the design queries is the one that puts most weight on the link score, and the family's held-out range is 0.111–0.166: the coverage term can only hurt.
- **With text relevance as the term it is worse:** 0.149, below USVT co-citation (−0.025, 8/27, Holm p = 0.051) and the query link (−0.017), though still above D-SPECTRA (+0.034). Weighting the modes by the query instead of by the whole graph (E8's pool-anchored weights gave 0.122, D-SPECTRA 0.120 on the same fits) helps D-SPECTRA's own objective by about 0.03, but not enough to reach the ranking scores.
- **Feedback hurts.** Re-estimating the query's citing role from the model's own top picks lowers the query link by 0.008 (5 wins / 19 losses, p = 0.028) and SPECTRA co-citation by 0.015 (7/18, p = 0.008); two rounds and larger k are worse still (family ranges 0.107–0.158 and 0.097–0.157). The model's picture of the query is best taken from the text-nearest pool papers once; its own picks drift away from the answer.
- **Every E15 method beats D-SPECTRA** (+0.034 to +0.050, Holm p ≤ 0.131, three of four ≤ 0.038), which repeats E8–E13: the query's citing role is the useful quantity, mode coverage is not.

### 3.17 E16: the β ceiling

**Beta_max 20 vs 5**

|                                          | β_max = 5   | β_max = 20   |
|:-----------------------------------------|:------------|:-------------|
| β after fitting, η = 0 (mean)            | 4.99        | 14.77        |
| β after fitting, d_ev = 8 (mean)         | 4.99        | 19.05        |
| d_ev at η = 0 (mean)                     | 28.0        | 30.3         |
| training NLL, η = 0 (mean)               | 0.103       | 0.006        |
| training NLL, d_ev = 8 (mean)            | 0.146       | 0.029        |
| held-out citation AUC at η = 0 (mean)    | 0.958       | 0.890        |
| held-out AP at η = 0 (mean)              | 0.959       | 0.914        |
| held-out NLL at η = 0 (mean)             | 0.87        | 2.57         |
| best held-out AUC over the η grid (mean) | 0.961       | 0.946        |

Held-out AUC at η = 0, β_max 20 minus 5: -0.068 on 63 fits, higher on 0 and lower on 63 (Wilcoxon p=<0.001). Held-out links: 10% of the citations and as many non-citations, the same split as E8's η-by-held-out fits.

**Beta_max 20 vs 5, same method (held-out 43, design 20; Holm over 4)**

|                                 | design, β_max 5   | design, β_max 20   | held-out, β_max 5   | held-out, β_max 20   | held-out: 20 minus 5                |
|:--------------------------------|:------------------|:-------------------|:--------------------|:---------------------|:------------------------------------|
| D-SPECTRA (d_ev = 8)            | 0.117             | 0.132              | 0.115               | 0.124                | +0.008 (21/9, p=0.141, Holm 0.424)  |
| D-SPECTRA, eta = 0              | 0.135             | 0.165              | 0.114               | 0.124                | +0.010 (17/10, p=0.022, Holm 0.087) |
| query link + relevance          | 0.218             | 0.220              | 0.166               | 0.163                | -0.002 (10/13, p=0.503, Holm 1.000) |
| SPECTRA co-citation + relevance | 0.224             | 0.216              | 0.172               | 0.175                | +0.003 (12/14, p=0.790, Holm 1.000) |

**The 20 design queries, seed 0 only, that motivated the full run (recall at B=kept)**

|                                     | β_max 5   | β_max 20   | 20 minus 5            |
|:------------------------------------|:----------|:-----------|:----------------------|
| D-SPECTRA (d_ev = 8)                | 0.101     | 0.130      | +0.029 (8/2, p=0.022) |
| D-SPECTRA, η = 0                    | 0.137     | 0.168      | +0.030 (9/1, p=0.007) |
| query link (model only)             | 0.215     | 0.213      | -0.002 (3/4, p=0.735) |
| query link + relevance (weight 0.5) | 0.196     | 0.150      | -0.046 (1/9, p=0.017) |

Queries with a reachable reference only, as the per-query evaluation files report them.

**Takeaways (E16).**

- **The bound was binding.** Freed to 20, β settles at 14.8 (η = 0) and 19.0 (d_ev = 8) on average, and the training NLL falls from 0.103 to 0.006 (η = 0) and from 0.146 to 0.029 (d_ev = 8). d_ev at η = 0 rises slightly (28.0 → 30.3).
- **The looser model overfits.** Held-out citation AUC at η = 0 falls from 0.958 to 0.890, lower on every one of the 63 fits (p < 0.001); average precision 0.959 → 0.914; held-out NLL 0.87 → 2.57. Even the best η on the grid reaches only 0.946 against 0.961. With exact all-pairs likelihood on a 480-node graph, the bound on the kernel's slope is doing the regularising that SPECTRA's sampled negatives and larger graphs do elsewhere.
- **Recall does not improve.** Held out, seed-averaged: D-SPECTRA 0.115 → 0.124 (+0.008, 21/9, Holm p = 0.42), η = 0 0.114 → 0.124 (+0.010, 17/10, Holm p = 0.087), query link + relevance 0.166 → 0.163 (−0.002), SPECTRA co-citation 0.172 → 0.175 (+0.003). The sharper probabilities help the coverage objective a little and the ranking scores not at all.
- **The pilot was the design set talking.** On the 20 design queries (seed 0) the gains were +0.029 (8/2, p = 0.022) and +0.030 (9/1, p = 0.007) for D-SPECTRA, and −0.046 (1/9, p = 0.017) for query link + relevance at link weight 0.5; seed-averaged on the same queries they shrink to +0.015 and +0.030, and held out to +0.008 and +0.010. The same pattern as E8: 20-query differences at p ≈ 0.01–0.02 do not transfer.
- **Decision:** β_max = 5 stays. It is SPECTRA's bound, it predicts held-out citations better, and no method's held-out recall is significantly different without it.

---

### 3.18 E17: a second hop of citations

**One hop (250 references + 130 citing papers per pool) vs two hops (plus 2,500 references of the first hop)**

|                            | graphs   | nodes (mean)   | edges (mean)   | second-hop nodes (mean)   | human-cited refs reachable   | nodes with abstract   |
|:---------------------------|:---------|:---------------|:---------------|:--------------------------|:-----------------------------|:----------------------|
| depth 1 (E8), held-out 43  | 43       | 484            | 4,339          | 0                         | 36.7%                        | 81%                   |
| depth 1 (E8), all 63       | 63       | 483            | 4,704          | 0                         | 38.0%                        | 83%                   |
| depth 2 (E17), held-out 43 | 43       | 2960           | 28,647         | 2477                      | 51.5%                        | 67%                   |
| depth 2 (E17), all 63      | 63       | 2961           | 30,983         | 2478                      | 52.2%                        | 69%                   |

Second-hop nodes carry only the edges pointing at them (their own reference lists were not fetched).

**Depth 2 vs depth 1, same method (held-out 43; Holm over 8)**

|                                       | depth 1   | depth 2   | depth 2 minus depth 1               |
|:--------------------------------------|:----------|:----------|:------------------------------------|
| USVT co-citation + relevance (E11)    | 0.175     | 0.164     | -0.012 (7/17, p=0.081, Holm 0.407)  |
| SPECTRA co-citation + relevance (E13) | 0.168     | 0.154     | -0.015 (7/17, p=0.034, Holm 0.209)  |
| query link + relevance (E10)          | 0.168     | 0.154     | -0.015 (7/19, p=0.030, Holm 0.209)  |
| co-citation + relevance (E11)         | 0.164     | 0.153     | -0.010 (7/16, p=0.117, Holm 0.469)  |
| USVT                                  | 0.132     | 0.118     | -0.014 (6/15, p=0.126, Holm 0.469)  |
| relevance only                        | 0.086     | 0.091     | +0.005 (12/8, p=0.765, Holm 0.765)  |
| most cited                            | 0.091     | 0.055     | -0.036 (0/18, p=<0.001, Holm 0.002) |
| D-SPECTRA (d_ev = 8)                  | 0.115     | 0.107     | -0.008 (11/15, p=0.258, Holm 0.517) |

Each method re-tuned nothing: the E8–E13 settings were applied unchanged to the larger graphs (fits: eta = 0 and d_ev = 8 at rank 32).

**Takeaways (E17).**

- **The graphs grow six-fold and reach many more of the human-cited references** (37% → 52%), so the ceiling for every method rises.
- **No method gets closer to it.** Every graph method loses recall on the larger graphs: the four query-anchored scores by 0.010–0.015 (7 wins against 16–19 losses each; p = 0.03–0.12, none significant after Holm), USVT by 0.014, D-SPECTRA by 0.008 (11/15, p = 0.26). Most-cited falls by a third (0.091 → 0.055, 0/18, Holm p = 0.002): the second hop is where the field's most-cited papers live, and they are not what this query cites. Relevance-only is the only method unchanged (+0.005).
- **Why:** the 2,500 added papers are references of references, chosen by citation count among the first hop. They dilute the structural scores (more candidates share the anchors' citations, and the fitted modes now describe the wider field rather than the query's neighbourhood) without adding papers the query's own neighbourhood points at. The reachable references the second hop adds are mostly ones the scores cannot find.
- **Decision:** depth 1 stays. E17 is a negative result on the input side, as E9–E16 were on the model side.

### 3.19 E19: SPECTRA's own evaluation, and the capacity frontier

**The directed fit against structural baselines (10% of citations held out, as many non-citations; Holm over 5 per metric)**

|                                                  | AUC   | fit minus baseline (AUC)   | AP    | fit minus baseline (AP)    |
|:-------------------------------------------------|:------|:---------------------------|:------|:---------------------------|
| directed SPECTRA fit, eta = 0 (rank cap 32)      | 0.958 |                            | 0.959 |                            |
| truncated SVD, rank 32 (rank cap only)           | 0.824 | +0.135 (63/0, Holm <0.001) | 0.879 | +0.080 (63/0, Holm <0.001) |
| USVT                                             | 0.846 | +0.113 (63/0, Holm <0.001) | 0.892 | +0.066 (63/0, Holm <0.001) |
| preferential attachment (out-degree x in-degree) | 0.904 | +0.055 (63/0, Holm <0.001) | 0.892 | +0.067 (63/0, Holm <0.001) |
| in-degree (popularity)                           | 0.833 | +0.125 (63/0, Holm <0.001) | 0.810 | +0.149 (63/0, Holm <0.001) |
| bibliographic-coupling paths (A Aᵀ A)            | 0.934 | +0.024 (63/0, Holm <0.001) | 0.929 | +0.030 (63/0, Holm <0.001) |

Median 421 held-out citations per graph. The fit's AUC over the whole eta grid: 0.952–0.961; per query the grid moves AUC by 0.007 (median).

**Realized dimension and held-out AUC along the eta grid (63 graphs, cv fits)**

|           | d_ev (mean)   | held-out AUC (mean)   | sd over queries   |
|:----------|:--------------|:----------------------|:------------------|
| η = -0.1  | 3.6           | 0.9576                | 0.015             |
| η = -0.06 | 7.5           | 0.9584                | 0.013             |
| η = -0.03 | 15.7          | 0.9580                | 0.014             |
| η = 0     | 28.2          | 0.9585                | 0.011             |
| η = 0.02  | 29.3          | 0.9557                | 0.013             |
| η = 0.04  | 29.8          | 0.9542                | 0.013             |
| η = 0.06  | 30.2          | 0.9531                | 0.012             |

![Capacity frontiers of the 63 per-query citation graphs at rank cap 32](d-spectra/results/e19_linkpred/frontier_r32.png)

**Takeaways (E19).**

- **As a citation model, the directed fit is clearly the best thing we have.** Held-out AUC 0.959 against 0.935 for the best structural baseline (bibliographic-coupling paths), 0.904 for preferential attachment, 0.846 for USVT and 0.824 for a rank-32 SVD; it wins on all 63 graphs against every baseline on both AUC and average precision (Holm p < 0.001 throughout). This is SPECTRA's own kind of result, and it holds on our graphs.
- **But a better citation model is not a better selector.** The same fit, used as a link predictor for selection (SPECTRA co-citation, E13), ties USVT co-citation (0.172 vs 0.174), whose underlying predictor is 0.11 AUC worse. Selection at B ≈ 15 papers depends on the top of one ranking anchored on a handful of papers, where every reasonable predictor agrees; the fit's advantage is spread over the 200,000 pairs the selection never looks at.
- **The frontier is flat.** Along the η grid d_ev runs from 3.6 to 30.2 and held-out AUC stays within 0.9576–0.9585 for η ≤ 0, dropping to 0.953 at η = 0.06 (the paper's own observation that positive η spreads mass onto noise modes). Per query the whole grid moves AUC by 0.007 (median). In SPECTRA's terms, on these graphs every realized dimension between 4 and 30 is an equally good citation model, which is why no d_ev target, η rule or criterion (E6, E9, E14) ever changed the selections: they were choosing between models the data cannot tell apart. E22 (3.23) asks at what density that stops being true.
- **E20: the cap is binding by SPECTRA's criterion, but only just.** Held-out AUC at η = 0 rises from 0.9585 at cap 32 to 0.9607 at cap 64 (59 wins / 4 losses) and 0.9611 at cap 128 (60 / 3), both Holm p < 0.001; the step from 64 to 128 is 0.0004. So the graphs sit in SPECTRA's "rank-cap-binding" regime at r = 32 and are saturated by r = 64, where d_ev at η = 0 stops at 44–46 modes (as E9 found). The best point of the frontier moves little (d_ev 15 → 26 → 28 across caps) and the whole gain is 0.002 AUC. E9 had already shown that recall does not change at these caps; E20 says why: the extra modes improve the citation model by an amount selection cannot feel.

**E20 held-out citation AUC at rank caps 32, 64 and 128 (cv fits, eta = 0, 63 graphs, paired Wilcoxon, Holm over 2)**

|              | graphs   | held-out AUC at eta = 0   | d_ev at eta = 0   | best AUC on the eta grid   | d_ev at the best AUC   | AUC vs cap 32 (eta = 0)   | wins / losses   | p      | Holm p (2)   |
|:-------------|:---------|:--------------------------|:------------------|:---------------------------|:-----------------------|:--------------------------|:----------------|:-------|:-------------|
| rank cap 32  | 63       | 0.9585                    | 28.2              | 0.9610                     | 14.7                   | –                         | –               | –      | –            |
| rank cap 64  | 63       | 0.9607                    | 44.1              | 0.9625                     | 25.8                   | +0.0022                   | 59 / 4          | <0.001 | <0.001       |
| rank cap 128 | 63       | 0.9611                    | 45.7              | 0.9627                     | 28.1                   | +0.0026                   | 60 / 3          | <0.001 | <0.001       |

Means over the 63 graphs; d_ev is the realized dimension of the cv fit (10% of citations held out) at eta = 0, and at the eta with the best held-out AUC.

![Capacity frontiers at three rank caps](d-spectra/results/e19_linkpred/frontier_caps.png)

### 3.20 The judged evaluation of the selection lists

Nine systems, search seed 0, the same writer and the same local judge for all (rules and set-up in section 2). The baseline is DeepScholar-base's own kept lists rerun through that writer, not Mateo's judged reports (3.11).

**Judged scores, held-out 43 queries (seed 0, same writer and judge)**

|                                      | n judged   | papers   | tokens / query   | nugget coverage   | reference coverage   | citation precision   | claim coverage   | coverage relevance (0-2)   | organization   |
|:-------------------------------------|:-----------|:---------|:-----------------|:------------------|:---------------------|:---------------------|:-----------------|:---------------------------|:---------------|
| DeepScholar-base's own picks (rerun) | 43         | 21.3     | 289k             | 0.043             | 0.113                | 0.423                | 0.609            | 1.57                       | 0.500          |
| fixed-k                              | 43         | 21.1     | 89k              | 0.065             | 0.149                | 0.429                | 0.581            | 1.70                       | 0.500          |
| relevance only                       | 43         | 21.1     | 89k              | 0.061             | 0.131                | 0.420                | 0.577            | 1.86                       | 0.500          |
| D-SPECTRA (d_ev = 8)                 | 43         | 21.1     | 89k              | 0.048             | 0.172                | 0.418                | 0.558            | 1.74                       | 0.500          |
| co-citation + relevance              | 43         | 21.1     | 89k              | 0.051             | 0.161                | 0.455                | 0.580            | 1.77                       | 0.500          |
| USVT co-citation + relevance         | 43         | 21.1     | 89k              | 0.036             | 0.177                | 0.407                | 0.537            | 1.75                       | 0.500          |
| SPECTRA co-citation + relevance      | 43         | 21.1     | 89k              | 0.042             | 0.141                | 0.447                | 0.583            | 1.76                       | 0.500          |
| query link + relevance               | 43         | 21.1     | 89k              | 0.070             | 0.201                | 0.459                | 0.576            | 1.76                       | 0.500          |
| oracle (human-cited refs)            | 42         | 17.7     | 83k              | 0.089             | 0.702                | 0.466                | 0.589            | 1.95                       | 0.500          |

Tokens per query by the E12 model (search 43,885 + filter 199,785 for DeepScholar-base only + writer 10,502 + 1,626 per paper). Document importance is omitted: it looks every cited title up on OpenAlex, which answered 429 (rate limit) during most judge runs, so it is 0 on every report of 7 of the 9 systems (kept in rows.csv). oracle (human-cited refs): report [42] not judged (the writer linked no papers), means over the rest

**Judged scores, all 63 queries (seed 0, same writer and judge)**

|                                      | n judged   | papers   | tokens / query   | nugget coverage   | reference coverage   | citation precision   | claim coverage   | coverage relevance (0-2)   | organization   |
|:-------------------------------------|:-----------|:---------|:-----------------|:------------------|:---------------------|:---------------------|:-----------------|:---------------------------|:---------------|
| DeepScholar-base's own picks (rerun) | 63         | 21.5     | 289k             | 0.070             | 0.090                | 0.444                | 0.613            | 1.62                       | 0.500          |
| fixed-k                              | 63         | 21.3     | 89k              | 0.075             | 0.114                | 0.455                | 0.596            | 1.73                       | 0.500          |
| relevance only                       | 63         | 21.3     | 89k              | 0.079             | 0.115                | 0.417                | 0.571            | 1.87                       | 0.500          |
| D-SPECTRA (d_ev = 8)                 | 63         | 21.3     | 89k              | 0.061             | 0.139                | 0.437                | 0.566            | 1.72                       | 0.500          |
| co-citation + relevance              | 63         | 21.3     | 89k              | 0.078             | 0.159                | 0.487                | 0.611            | 1.79                       | 0.500          |
| USVT co-citation + relevance         | 63         | 21.3     | 89k              | 0.058             | 0.173                | 0.435                | 0.547            | 1.75                       | 0.500          |
| SPECTRA co-citation + relevance      | 63         | 21.3     | 89k              | 0.075             | 0.151                | 0.423                | 0.558            | 1.77                       | 0.500          |
| query link + relevance               | 63         | 21.3     | 89k              | 0.085             | 0.187                | 0.461                | 0.570            | 1.79                       | 0.500          |
| oracle (human-cited refs)            | 62         | 17.8     | 83k              | 0.117             | 0.683                | 0.461                | 0.581            | 1.95                       | 0.500          |

Tokens per query by the E12 model (search 43,885 + filter 199,785 for DeepScholar-base only + writer 10,502 + 1,626 per paper). Document importance is omitted: it looks every cited title up on OpenAlex, which answered 429 (rate limit) during most judge runs, so it is 0 on every report of 7 of the 9 systems (kept in rows.csv). oracle (human-cited refs): report [42] not judged (the writer linked no papers), means over the rest

**The pre-registered tests** (nugget coverage, held-out 43, paired Wilcoxon):

**Each method vs DeepScholar-base's own picks on nugget coverage (held-out 43, paired Wilcoxon, Holm over 8)**

|                                 | n   | method   | DS-base rerun   | diff   | wins / losses   | p     | Holm p (8)   |
|:--------------------------------|:----|:---------|:----------------|:-------|:----------------|:------|:-------------|
| fixed-k                         | 43  | 0.065    | 0.043           | +0.022 | 8 / 5           | 0.235 | 1.000        |
| relevance only                  | 43  | 0.061    | 0.043           | +0.018 | 9 / 3           | 0.091 | 0.640        |
| D-SPECTRA (d_ev = 8)            | 43  | 0.048    | 0.043           | +0.005 | 7 / 5           | 0.695 | 1.000        |
| co-citation + relevance         | 43  | 0.051    | 0.043           | +0.009 | 5 / 6           | 0.929 | 1.000        |
| USVT co-citation + relevance    | 43  | 0.036    | 0.043           | -0.007 | 4 / 8           | 0.327 | 1.000        |
| SPECTRA co-citation + relevance | 43  | 0.042    | 0.043           | -0.000 | 6 / 6           | 0.906 | 1.000        |
| query link + relevance          | 43  | 0.070    | 0.043           | +0.027 | 8 / 6           | 0.379 | 1.000        |
| oracle (human-cited refs)       | 42  | 0.089    | 0.044           | +0.046 | 12 / 3          | 0.012 | 0.099        |

**USVT co-citation + relevance vs D-SPECTRA and vs relevance only on nugget coverage (held-out 43, Holm over 2)**

|                      | n   | USVT co-citation + relevance   | other   | diff   | wins / losses   | p     | Holm p (2)   |
|:---------------------|:----|:-------------------------------|:--------|:-------|:----------------|:------|:-------------|
| D-SPECTRA (d_ev = 8) | 43  | 0.036                          | 0.048   | -0.012 | 4 / 6           | 0.359 | 0.359        |
| relevance only       | 43  | 0.036                          | 0.061   | -0.025 | 2 / 10          | 0.050 | 0.100        |

**The other metrics**, uncorrected and without a claim:

**The other metrics vs DeepScholar-base's own picks (held-out 43; difference and uncorrected p, no claim)**

|                                 | nugget coverage   | reference coverage   | citation precision   | claim coverage   | coverage relevance (0-2)   |
|:--------------------------------|:------------------|:---------------------|:---------------------|:-----------------|:---------------------------|
| fixed-k                         | +0.022 (0.235)    | +0.036 (0.092)       | +0.007 (0.995)       | -0.028 (0.228)   | +0.130 (0.020)             |
| relevance only                  | +0.018 (0.091)    | +0.018 (0.972)       | -0.003 (0.837)       | -0.032 (0.583)   | +0.280 (<0.001)            |
| D-SPECTRA (d_ev = 8)            | +0.005 (0.695)    | +0.059 (0.052)       | -0.005 (0.930)       | -0.051 (0.165)   | +0.161 (0.008)             |
| co-citation + relevance         | +0.009 (0.929)    | +0.047 (0.017)       | +0.033 (0.499)       | -0.028 (0.562)   | +0.199 (0.005)             |
| USVT co-citation + relevance    | -0.007 (0.327)    | +0.064 (0.003)       | -0.015 (0.875)       | -0.072 (0.091)   | +0.178 (0.006)             |
| SPECTRA co-citation + relevance | -0.000 (0.906)    | +0.028 (0.068)       | +0.024 (0.722)       | -0.025 (0.359)   | +0.186 (0.011)             |
| query link + relevance          | +0.027 (0.379)    | +0.088 (<0.001)      | +0.037 (0.233)       | -0.033 (0.308)   | +0.182 (0.016)             |
| oracle (human-cited refs)       | +0.046 (0.012)    | +0.587 (<0.001)      | +0.042 (0.241)       | -0.023 (0.791)   | +0.360 (<0.001)            |

Organization is 0.5 on every report (the judge prefers whichever section it sees first), so it is omitted.

![Cost and judged coverage of the selection lists](d-spectra/results/judged/frontier.png)

**Takeaways (judged).**

- **On the primary metric nothing separates from the baseline.** Judged nugget coverage on the held-out queries is 0.043 for DeepScholar-base's own picks, between 0.036 (USVT co-citation + relevance) and 0.070 (query link + relevance) for our seven methods, and 0.089 for the oracle. Only the oracle's +0.046 (12 wins / 3 losses, p = 0.012) is nominally significant and it does not survive Holm (0.099). The method that is best on recall is nominally the worst here, and the ordering among our methods (query link > fixed-k > relevance only > co-citation > D-SPECTRA > SPECTRA co-citation > USVT co-citation) has no relation to their recall ordering.
- **The judge's reference coverage says what the proxy said.** It measures the overlap of the report's citations with the human-cited references, so it is the recall proxy applied to what the writer actually cites: every graph method is above the baseline (query link + relevance +0.088, p < 0.001; USVT co-citation + relevance +0.064, p = 0.003; D-SPECTRA +0.059, p = 0.052; uncorrected) and the oracle is at 0.70. The selection gain survives the writer; it just does not turn into nuggets.
- **Coverage relevance rises for every one of our lists** (+0.13 to +0.36 on the 0–2 scale, p ≤ 0.02 uncorrected, the oracle highest at 1.95): the judge finds the related-work sections written from the expanded graphs more on-topic than those from DeepScholar-base's filter. Claim coverage is 0.02–0.07 lower for all of them (none significant) and citation precision is unchanged.
- **Why the primary metric cannot resolve this.** Nugget coverage is a 0–1 fraction averaging 0.04–0.09, with most reports at 0 and the oracle, which has the actual human-cited papers, at only 0.089. With 43 queries the only difference the paired test picks up is the oracle's 0.046, and that only before correction; the 0.01–0.03 gaps between methods are far below it. The step-2 gate (E12) had already shown that this judge's nugget coverage does not track d_ev(S) on the baseline's reports; the full run shows it does not track recall either.
- **Cost.** All our lists cost 89,000 tokens per query against 289,000 for DeepScholar-base's filter, for the same or better judged scores on every usable metric. That is the one judged claim that is clean: the filter can be replaced by graph selection at a third of the tokens with no loss the judge can detect.
- **What this is not.** One writer, one judge model, and a judge whose organization metric is blind and whose document-importance metric failed on the network. Search seeds 1 and 2 are below.

**Seeds 1 and 2 through the same writer and judge** (rules written first, `scratchpad/seeds12_rules.md`: the same two families, each query's score averaged over its three seeds, Holm over 7 in family 1 since SPECTRA co-citation was exported for seed 0 only; analysis `scripts/judged_seeds.py` → `results/judged_s12/`).

**Per-seed means on the held-out queries (same writer and judge for every seed)**

|                                      | nugget coverage, s0   | nugget coverage, s1   | nugget coverage, s2   | reference coverage, s0   | reference coverage, s1   | reference coverage, s2   | coverage relevance (0-2), s0   | coverage relevance (0-2), s1   | coverage relevance (0-2), s2   |
|:-------------------------------------|:----------------------|:----------------------|:----------------------|:-------------------------|:-------------------------|:-------------------------|:-------------------------------|:-------------------------------|:-------------------------------|
| DeepScholar-base's own picks (rerun) | 0.043                 | 0.059                 | 0.029                 | 0.113                    | 0.111                    | 0.127                    | 1.57                           | 1.59                           | 1.56                           |
| fixed-k                              | 0.065                 | 0.049                 | 0.049                 | 0.149                    | 0.151                    | 0.132                    | 1.70                           | 1.72                           | 1.71                           |
| relevance only                       | 0.061                 | 0.059                 | 0.063                 | 0.131                    | 0.132                    | 0.134                    | 1.86                           | 1.89                           | 1.82                           |
| D-SPECTRA (d_ev = 8)                 | 0.048                 | 0.040                 | 0.045                 | 0.172                    | 0.162                    | 0.152                    | 1.74                           | 1.74                           | 1.71                           |
| co-citation + relevance              | 0.051                 | 0.051                 | 0.054                 | 0.161                    | 0.145                    | 0.151                    | 1.77                           | 1.81                           | 1.75                           |
| USVT co-citation + relevance         | 0.036                 | 0.046                 | 0.034                 | 0.177                    | 0.199                    | 0.183                    | 1.75                           | 1.77                           | 1.73                           |
| query link + relevance               | 0.070                 | 0.060                 | 0.046                 | 0.201                    | 0.178                    | 0.152                    | 1.76                           | 1.79                           | 1.75                           |
| oracle (human-cited refs)            | 0.089                 | 0.092                 | 0.092                 | 0.702                    | 0.702                    | 0.702                    | 1.95                           | 1.95                           | 1.95                           |

Held-out 43 queries per seed. seed 0 oracle (human-cited refs): report [42] not judged; seed 1 oracle (human-cited refs): report [42] not judged; seed 2 oracle (human-cited refs): report [42] not judged

**Seed-averaged scores, held-out 43 queries (each query's score is its mean over the seeds that have it)**

|                                      | queries   | seeds / query   | papers   | tokens / query   | nugget coverage   | reference coverage   | citation precision   | claim coverage   | coverage relevance (0-2)   |
|:-------------------------------------|:----------|:----------------|:---------|:-----------------|:------------------|:---------------------|:---------------------|:-----------------|:---------------------------|
| DeepScholar-base's own picks (rerun) | 43        | 3.00            | 21.8     | 290k             | 0.043             | 0.117                | 0.413                | 0.576            | 1.57                       |
| fixed-k                              | 43        | 3.00            | 21.5     | 89k              | 0.054             | 0.144                | 0.419                | 0.562            | 1.71                       |
| relevance only                       | 43        | 3.00            | 21.5     | 89k              | 0.061             | 0.133                | 0.446                | 0.584            | 1.85                       |
| D-SPECTRA (d_ev = 8)                 | 43        | 3.00            | 21.5     | 89k              | 0.044             | 0.162                | 0.444                | 0.583            | 1.73                       |
| co-citation + relevance              | 43        | 3.00            | 21.5     | 89k              | 0.052             | 0.152                | 0.466                | 0.587            | 1.78                       |
| USVT co-citation + relevance         | 43        | 3.00            | 21.5     | 89k              | 0.038             | 0.186                | 0.402                | 0.533            | 1.75                       |
| query link + relevance               | 43        | 3.00            | 21.5     | 89k              | 0.059             | 0.177                | 0.439                | 0.561            | 1.77                       |
| oracle (human-cited refs)            | 42        | 3.00            | 17.7     | 83k              | 0.091             | 0.702                | 0.466                | 0.589            | 1.95                       |

Organization (0.5 on every report) and document importance (OpenAlex rate limit) are unusable and omitted; kept in rows.csv.

**Each method vs DeepScholar-base's own picks on nugget coverage (seed-averaged, held-out 43, paired Wilcoxon, Holm over 7)**

|                              | n   | method   | DS-base rerun   | diff   | wins / losses   | p     | Holm p (7)   |
|:-----------------------------|:----|:---------|:----------------|:-------|:----------------|:------|:-------------|
| fixed-k                      | 43  | 0.054    | 0.043           | +0.011 | 12 / 4          | 0.056 | 0.278        |
| relevance only               | 43  | 0.061    | 0.043           | +0.018 | 12 / 4          | 0.044 | 0.262        |
| D-SPECTRA (d_ev = 8)         | 43  | 0.044    | 0.043           | +0.001 | 7 / 6           | 0.807 | 1.000        |
| co-citation + relevance      | 43  | 0.052    | 0.043           | +0.008 | 7 / 7           | 0.551 | 1.000        |
| USVT co-citation + relevance | 43  | 0.038    | 0.043           | -0.005 | 8 / 8           | 0.469 | 1.000        |
| query link + relevance       | 43  | 0.059    | 0.043           | +0.015 | 10 / 5          | 0.182 | 0.728        |
| oracle (human-cited refs)    | 42  | 0.091    | 0.044           | +0.047 | 12 / 4          | 0.011 | 0.079        |

**USVT co-citation + relevance vs D-SPECTRA and vs relevance only on nugget coverage (seed-averaged, held-out 43, Holm over 2)**

|                      | n   | USVT co-citation + relevance   | other   | diff   | wins / losses   | p     | Holm p (2)   |
|:---------------------|:----|:-------------------------------|:--------|:-------|:----------------|:------|:-------------|
| D-SPECTRA (d_ev = 8) | 43  | 0.038                          | 0.044   | -0.006 | 5 / 8           | 0.600 | 0.600        |
| relevance only       | 43  | 0.038                          | 0.061   | -0.023 | 5 / 10          | 0.047 | 0.094        |

**The other metrics vs DeepScholar-base's own picks (seed-averaged, held-out 43; difference and uncorrected p, no claim)**

|                              | nugget coverage   | reference coverage   | citation precision   | claim coverage   | coverage relevance (0-2)   |
|:-----------------------------|:------------------|:---------------------|:---------------------|:-----------------|:---------------------------|
| fixed-k                      | +0.011 (0.056)    | +0.027 (0.068)       | +0.006 (0.948)       | -0.014 (0.305)   | +0.139 (<0.001)            |
| relevance only               | +0.018 (0.044)    | +0.015 (0.364)       | +0.033 (0.157)       | +0.008 (0.724)   | +0.279 (<0.001)            |
| D-SPECTRA (d_ev = 8)         | +0.001 (0.807)    | +0.045 (0.005)       | +0.031 (0.247)       | +0.007 (0.628)   | +0.157 (<0.001)            |
| co-citation + relevance      | +0.008 (0.551)    | +0.035 (0.005)       | +0.053 (0.057)       | +0.011 (0.554)   | +0.204 (<0.001)            |
| USVT co-citation + relevance | -0.005 (0.469)    | +0.069 (0.001)       | -0.011 (0.689)       | -0.044 (0.097)   | +0.176 (0.002)             |
| query link + relevance       | +0.015 (0.182)    | +0.060 (0.001)       | +0.026 (0.372)       | -0.016 (0.562)   | +0.194 (<0.001)            |
| oracle (human-cited refs)    | +0.047 (0.011)    | +0.583 (<0.001)      | +0.052 (0.148)       | +0.010 (0.528)   | +0.355 (<0.001)            |

**Takeaways (seeds 0–2), scored against the rules.**

- **Prediction 1 (the oracle separates from the baseline after Holm) fails, narrowly.** Seed-averaged nugget coverage is 0.091 for the oracle against 0.044 for the baseline (+0.047, 12 wins / 4 losses, p = 0.011), Holm p = 0.079 over 7. The seed-0 numbers were +0.046 and Holm 0.099; averaging over seeds did not change the oracle's margin, it reduced the per-query noise by less than the rule assumed, because the per-query score is still a 0–1 fraction that is 0 on most queries in every seed.
- **Prediction 2 (no other method separates; every difference within ±0.03) holds.** The seven methods are at 0.038–0.061 against 0.043, all differences within +0.018, none below Holm 0.26. The ordering is stable across seeds only at the ends: relevance only is nominally the best of our lists in every seed (0.059–0.063) and USVT co-citation + relevance the worst (0.034–0.046); query link + relevance, best in seed 0, is 0.046 in seed 2.
- **Prediction 3 (reference coverage and coverage relevance keep their direction) holds.** Every graph method is above the baseline on reference coverage (+0.027 to +0.069, uncorrected p ≤ 0.005 for the four citation-scored lists) and on coverage relevance (+0.14 to +0.28, p ≤ 0.002 for all seven), in each seed separately.
- **Prediction 4 (D-SPECTRA and USVT co-citation + relevance do not differ) holds** (−0.006, Holm 0.60). USVT co-citation + relevance is nominally below relevance only (−0.023, p = 0.047, Holm 0.094): the list with the highest recall and the highest reference coverage has the lowest nugget coverage, on three seeds.
- **The judged conclusion with three seeds is the seed-0 conclusion.** Graph selection at 89,000 tokens matches DeepScholar-base's filter at 290,000 on nugget coverage and beats it on reference coverage and coverage relevance; no selection method is separable from any other on nugget coverage; and the judge's nugget metric does not track the recall proxy. Averaging seeds did not resolve the 0.02 gaps, which puts the limit at the metric rather than at the sample.

### 3.21 E18: the fitted modes as the report's taxonomy

**Primary metrics (63 queries, paired Wilcoxon, Holm over 3 lists x 2 metrics)**

|                                                  | n   | modes   | writer's taxonomy   | diff   | wins / losses   | p     | Holm p (6)   |
|:-------------------------------------------------|:----|:--------|:--------------------|:-------|:----------------|:------|:-------------|
| D-SPECTRA (d_ev = 8), organization               | 63  | 0.500   | 0.500               | +0.000 | 0 / 0           | 1.000 | 1.000        |
| D-SPECTRA (d_ev = 8), nugget coverage            | 63  | 0.061   | 0.061               | +0.000 | 0 / 0           | 1.000 | 1.000        |
| SPECTRA co-citation + relevance, organization    | 63  | 0.500   | 0.500               | +0.000 | 0 / 0           | 1.000 | 1.000        |
| SPECTRA co-citation + relevance, nugget coverage | 63  | 0.075   | 0.075               | +0.000 | 0 / 0           | 1.000 | 1.000        |
| USVT co-citation + relevance, organization       | 63  | 0.500   | 0.500               | +0.000 | 0 / 0           | 1.000 | 1.000        |
| USVT co-citation + relevance, nugget coverage    | 63  | 0.058   | 0.058               | +0.000 | 0 / 0           | 1.000 | 1.000        |

**E18 the other judged metrics, modes minus writer's taxonomy (63 queries; uncorrected p, no claim)**

|                                 | reference coverage   | citation precision   | claim coverage   | coverage relevance (0-2)   |
|:--------------------------------|:---------------------|:---------------------|:-----------------|:---------------------------|
| D-SPECTRA (d_ev = 8)            | +0.000 (1.000)       | +0.004 (0.317)       | +0.002 (0.317)   | +0.001 (0.715)             |
| SPECTRA co-citation + relevance | +0.000 (1.000)       | +0.000 (1.000)       | +0.000 (1.000)   | +0.010 (0.451)             |
| USVT co-citation + relevance    | +0.000 (1.000)       | +0.000 (1.000)       | +0.000 (1.000)   | -0.004 (0.317)             |

**Takeaways (E18).**

- **A null by construction, not a result about the modes.** The judge's input (`intro.md`) is produced before the taxonomy exists, so it is identical between the two conditions on 188 of 189 reports and every primary comparison is 0 wins / 0 losses. The small differences in citation precision and coverage relevance come from the one report whose introduction differed and from the paper lists (`paper.csv`), which do differ in 59–60 of 63 reports per list because the linked papers change with the taxonomy.
- **What would test the idea:** judging the full report (DeepScholar-Bench's own parser does not, and its scores for this system are defined on the introduction), or feeding the mode groups into the introduction's generation. Neither is in the proposal; noted as an open item, not pursued.

### 3.22 E21: an inductive citing role for the query

**Recall of each pseudo-query's in-graph references (mean over graphs of the per-graph mean)**

|                                 | held-out, B = 15   | held-out, B = 30   | design, B = 15   | design, B = 30   |
|:--------------------------------|:-------------------|:-------------------|:-----------------|:-----------------|
| relevance only                  | 0.179              | 0.270              | 0.173            | 0.266            |
| USVT co-citation + relevance    | 0.244              | 0.375              | 0.259            | 0.399            |
| SPECTRA co-citation + relevance | 0.281              | 0.420              | 0.290            | 0.446            |
| query link + relevance          | 0.257              | 0.390              | 0.261            | 0.418            |
| inductive role alone            | 0.316              | 0.466              | 0.330            | 0.489            |
| inductive role + relevance      | 0.303              | 0.456              | 0.309            | 0.464            |

Pseudo-queries: 860 on the 43 held-out graphs, 400 on the 20 design graphs; each removed from its graph before the fit. Methods use the E10-E13 settings unchanged.

**The pre-registered tests (unit = graph, 43 held-out graphs, paired Wilcoxon, Holm over 2 per budget)**

|                                                 | n graphs   | inductive + relevance   | other   | diff   | wins / losses   | p      | Holm p (2)   |
|:------------------------------------------------|:-----------|:------------------------|:--------|:-------|:----------------|:-------|:-------------|
| pseudo B=15: vs USVT co-citation + relevance    | 43         | 0.303                   | 0.244   | +0.059 | 39/4            | <0.001 | <0.001       |
| pseudo B=15: vs SPECTRA co-citation + relevance | 43         | 0.303                   | 0.281   | +0.021 | 31/12           | <0.001 | <0.001       |
| pseudo B=30: vs USVT co-citation + relevance    | 43         | 0.456                   | 0.375   | +0.082 | 42/1            | <0.001 | <0.001       |
| pseudo B=30: vs SPECTRA co-citation + relevance | 43         | 0.456                   | 0.420   | +0.037 | 38/5            | <0.001 | <0.001       |

B = 15 is the primary budget; B = 30 is reported the same way.

**Recall of the human-cited references at B = kept (43 held-out queries, search seed 0, Holm over 2)**

|                                    | n queries   | inductive + relevance   | other   | diff   | wins / losses   | p     | Holm p (2)   |
|:-----------------------------------|:------------|:------------------------|:--------|:-------|:----------------|:------|:-------------|
| vs USVT co-citation + relevance    | 43          | 0.165                   | 0.175   | -0.010 | 12/16           | 0.322 | 0.644        |
| vs SPECTRA co-citation + relevance | 43          | 0.165                   | 0.168   | -0.003 | 14/14           | 0.665 | 0.665        |

Read by the rule only because the pseudo-query test won; the ridge map is trained on the full graph's fitted nodes.

**Every method at B = kept (43 held-out queries, search seed 0)**

|                                 | held-out 43, recall at B = kept   |
|:--------------------------------|:----------------------------------|
| relevance only                  | 0.086                             |
| USVT co-citation + relevance    | 0.175                             |
| SPECTRA co-citation + relevance | 0.168                             |
| query link + relevance          | 0.168                             |
| inductive role alone            | 0.143                             |
| inductive role + relevance      | 0.165                             |

**Takeaways (E21).**

- **On pseudo-queries the inductive role is the best selector we have built, by a wide margin.** With the pseudo-query's own in-graph references as ground truth, the role predicted from its text alone recovers 0.316 at B = 15 and, mixed with relevance, 0.303, against 0.281 for SPECTRA co-citation + relevance, 0.257 for the query link, 0.244 for USVT co-citation + relevance and 0.179 for relevance only. Both pre-registered comparisons win on 31–42 of the 43 held-out graphs at both budgets (Holm p < 0.001). The design graphs agree. This is the first place the fitted model beats USVT denoising as a selector, and it does so through the thing only the fit has: a citing-role space a new node can be placed in.
- **On the real queries it changes nothing.** Applied to the 43 benchmark queries with the human-cited references as ground truth, inductive + relevance recovers 0.165 against 0.175 for USVT co-citation + relevance (−0.010, 12 wins / 16 losses, Holm p = 0.64) and 0.168 for SPECTRA co-citation (Holm p = 0.67); the role alone gets 0.143.
- **What the split says, by the rule written beforehand:** "a win on pseudo-queries without one on real queries means the remaining gap is the human reference lists, not the predictor". The predictor is right about what a paper in this graph would cite. The benchmark's ground truth is what the human authors chose to cite in a related-work section, of which the graph reaches 37%, and which E6 showed is more concentrated in the dominant modes than any ranking we produce. Every method is at 0.165–0.175 on that target, and the better citation model cannot move it, for the same reason E19's better AUC could not: the target is not the graph's citation process.
- **For the report:** the fitted citing-role space is a real, transferable capability (E19 for links, E21 for cold-start selection against graph ground truth), and the benchmark's human reference lists are where every method's recall is capped, not the predictor. Not pursued further: tuning the mixing weight or the ridge for the real queries (the rule froze them; any gain would be within the 0.01 noise of the other methods).

### 3.23 E22: the sparsification frontier

**E22 sparsification frontier per keep level (63 graphs, cv fits, rank cap 32, the same eta grid; means over graphs)**

|           | citations per graph (mean)   | held out (mean)   | AUC at eta = 0   | best AUC on the grid   | gain   | low     | low > 0   | best eta (median)   | d_ev at eta = 0   | d_ev at the best eta   | d_ev at eta = -0.1   |
|:----------|:-----------------------------|:------------------|:-----------------|:-----------------------|:-------|:--------|:----------|:--------------------|:------------------|:-----------------------|:---------------------|
| keep 1    | 4,704                        | 470               | 0.9585           | 0.9610                 | 0.0025 | -0.0009 | 29 / 63   | -0.03               | 28.2              | 14.7                   | 3.6                  |
| keep 0.5  | 2,370                        | 237               | 0.9057           | 0.9216                 | 0.0160 | +0.0108 | 52 / 63   | -0.1                | 30.5              | 7.1                    | 3.7                  |
| keep 0.25 | 1,194                        | 119               | 0.8470           | 0.8673                 | 0.0203 | -0.0045 | 35 / 63   | -0.03               | 31.5              | 17.5                   | 3.1                  |
| keep 0.1  | 492                          | 49                | 0.7912           | 0.8118                 | 0.0207 | -0.0826 | 2 / 63    | 0.02                | 31.8              | 30.5                   | 1.8                  |

gain = best held-out AUC on the eta grid minus AUC at eta = 0; low = AUC at eta = -0.1 (the most negative eta) minus AUC at eta = 0. keep = 1.0 is E8's cv fit. Held out = 10% of the citations that remain after thinning, plus as many non-citations.

**E22 gain and low at each keep level against keep = 1.0 (paired Wilcoxon over the 63 graphs, Holm over the three levels per statistic)**

|                        | mean at the level   | mean at keep 1.0   | diff    | wins / losses   | p      | Holm p (3)   |
|:-----------------------|:--------------------|:-------------------|:--------|:----------------|:-------|:-------------|
| gain, keep 0.5 vs 1.0  | +0.0160             | +0.0025            | +0.0135 | 56 / 6          | <0.001 | <0.001       |
| gain, keep 0.25 vs 1.0 | +0.0203             | +0.0025            | +0.0178 | 47 / 15         | <0.001 | <0.001       |
| gain, keep 0.1 vs 1.0  | +0.0207             | +0.0025            | +0.0182 | 43 / 17         | <0.001 | <0.001       |
| low, keep 0.5 vs 1.0   | +0.0108             | -0.0009            | +0.0117 | 53 / 10         | <0.001 | <0.001       |
| low, keep 0.25 vs 1.0  | -0.0045             | -0.0009            | -0.0037 | 34 / 29         | 0.984  | 0.984        |
| low, keep 0.1 vs 1.0   | -0.0826             | -0.0009            | -0.0817 | 4 / 59          | <0.001 | <0.001       |

**E22 which eta gives the best held-out AUC, per keep level (graphs per eta, 63 per row)**

|           | eta -0.1   | eta -0.06   | eta -0.03   | eta 0   | eta 0.02   | eta 0.04   | eta 0.06   |
|:----------|:-----------|:------------|:------------|:--------|:-----------|:-----------|:-----------|
| keep 1    | 16         | 12          | 19          | 14      | 2          | 0          | 0          |
| keep 0.5  | 47         | 10          | 0           | 4       | 2          | 0          | 0          |
| keep 0.25 | 27         | 4           | 2           | 11      | 11         | 5          | 3          |
| keep 0.1  | 1          | 2           | 0           | 20      | 15         | 14         | 11         |

**Held-out AUC (d_ev) at each eta of the cv grid**

|           | eta -0.1     | eta -0.06    | eta -0.03     | eta 0         | eta 0.02      | eta 0.04      | eta 0.06      |
|:----------|:-------------|:-------------|:--------------|:--------------|:--------------|:--------------|:--------------|
| keep 1    | 0.9576 (3.6) | 0.9584 (7.5) | 0.9580 (15.7) | 0.9585 (28.2) | 0.9557 (29.3) | 0.9542 (29.8) | 0.9531 (30.2) |
| keep 0.5  | 0.9165 (3.7) | 0.9080 (7.4) | 0.8969 (16.0) | 0.9057 (30.5) | 0.9007 (31.1) | 0.8984 (31.3) | 0.8959 (31.5) |
| keep 0.25 | 0.8425 (3.1) | 0.8238 (6.0) | 0.8042 (12.1) | 0.8470 (31.5) | 0.8457 (31.8) | 0.8434 (31.9) | 0.8410 (31.9) |
| keep 0.1  | 0.7086 (1.8) | 0.6969 (3.5) | 0.6616 (6.6)  | 0.7912 (31.8) | 0.7865 (32.0) | 0.7856 (32.0) | 0.7820 (32.0) |

![Capacity frontier as citations are removed](d-spectra/results/sparse/frontier_sparse.png)

**Takeaways (E22), scored against the rules.**

- **Prediction 1 (gain grows, significant at a tenth) holds, with a caveat.** What the best η buys over η = 0 rises from 0.002 AUC on the full graphs to 0.016 at half the citations, 0.020 at a quarter and 0.021 at a tenth, each above the full graphs' value on 43–56 of 63 graphs (Holm p < 0.001 at every level). The caveat is that gain is the best of seven noisy numbers, and the held-out set shrinks from 470 citations to 237, 119 and 49: at a quarter and a tenth the best η scatters over the whole grid (at a tenth, 20 graphs at η = 0 and 40 at η > 0) and part of the gain is selection noise. At half the citations it is not: the best η is −0.1 on 47 of 63 graphs.
- **Prediction 2 (the best η moves negative) holds at half the citations and fails below.** The mean d_ev at the best η is 14.7 on the full graphs, 7.1 at half, 17.5 at a quarter and 30.5 at a tenth, where the median best η is +0.02.
- **Prediction 3 (at a tenth, the smallest model beats η = 0 outright) fails; it holds at half instead.** At half the citations the η = −0.1 fit (d_ev 3.7) is +0.011 AUC above η = 0 (d_ev 30.5), on 52 of 63 graphs (Holm p < 0.001 against the full graphs, where it is −0.001 on 29 of 63). At a quarter it is −0.005 (35 of 63, p = 0.98) and at a tenth −0.083 (2 of 63). This is the one fixed-η statistic, free of selection, and it is the result of the experiment.
- **The frontier is not monotone below half density.** At a quarter and a tenth of the citations the mean AUC along the grid is U-shaped: 0.843 (d_ev 3) → 0.824 (6) → 0.804 (12) → 0.847 (η = 0, d_ev 31.5) at a quarter, and 0.709 → 0.697 → 0.662 → 0.791 at a tenth. The intermediate capacities are the worst, and η = 0, where the realized dimension sits at the rank cap, is the best. So below half density the penalty is not a clean capacity knob: it does not only remove modes, it concentrates the fit's full β on the surviving ones, and on 100–500 training citations those overfit faster than the diffuse η = 0 fit does. An interpretation, not a tested claim.
- **Prediction 4, the placement.** Items 1–3 do not all hold, so the rule's "saturated by a factor of four or more" is not the reading. The reading is narrower: SPECTRA's capacity control would have changed our fits, and changed them for the better, at about half the benchmark's citation density, and nowhere else on the grid. DeepScholar-Bench's graphs, at 4,700 citations, are about a factor of two above that window; the absolute citation model also degrades steadily as citations are removed (AUC at η = 0 0.959 → 0.906 → 0.847 → 0.791). Whether a +0.011 AUC gain at half density would have changed a selection was not tested (the rule excluded selection reruns), and E19–E20 suggest it would not: selection could not feel a 0.002 gain at cap 64, and the gap between the fit and USVT (0.11 AUC) never reached the selections either.

---

## 4. Bugs found and fixed

Bugs 1–3 were in my graph builders, found by the review checks (E7); old outputs are kept in `data/_backup/`. Bug 4 was in the model's optimizer, found by an audit of the code against the SPECTRA paper and engine on Oct 29; old results are kept in `results/pre_qrfix/` and the old selection lists in `selections/pre_qrfix/`.

| # | Bug | Effect | Fix | Results affected |
|---|---|---|---|---|
| 1 | The query paper was excluded only by exact title match | An earlier venue record of query 2504.21282 ("Birdie…", title 98% identical, dated before the arXiv version) stayed in its own graph and brought 3 of its 12 reachable references with it | Exclude any work whose title is ≥ 90% similar to the query's | E3 (one query rebuilt, refitted and re-evaluated; results moved by at most 0.002) |
| 2 | In the pilot-pool graphs, papers without an arXiv ID inherited one pool row's abstract | 1,274 of 9,763 nodes (13%) had a wrong abstract, so wrong relevance scores | Only use pool abstracts for pool papers | Appendix A (graphs rebuilt, embeddings and evaluations redone) |
| 3 | Mateo's arXiv IDs were read as numbers | IDs ending in 0 lost the zero (2411.16260 → 2411.1626), so 1,033 of 8,821 pool rows (11.7%) were looked up wrongly and dropped | Read IDs as text; keep pool papers Semantic Scholar does not know as candidates without links | E5 and Appendix A (not rerun; replaced by E6, which has the fix) |
| 4 | **Sign flips in the QR orthonormalisation.** U and V are each orthonormalised by a Householder QR. When a pivot crosses zero, one column of Q flips sign. SPECTRA's symmetric kernel Q S² Qᵀ is blind to that; our directed kernel U S Vᵀ is not: a flip in U but not in V negates mode k in a single step | Checked on three graphs at η = 0: 907–1,296 of 3,000 epochs had an unpaired flip; the loss jumped by up to +0.34 to +0.84 at those steps against at most +0.006 elsewhere; the final training NLL was 29–68% higher than with the fix; η = 0 fits stopped at d_ev 8–9 instead of 27–30; d_ev drifted 4–12% over the last 1,000 epochs instead of about 0%. This is the "instability" E2 saw and the learning-rate schedule (E10) could not cure | Multiply each column of Q by the sign of the corresponding diagonal entry of R (`dspectra/model.py`, `_orthonormal`) | **Every fitted result**: E1, E2, E6, E8–E13 were refitted and re-evaluated on Oct 29–30, and E14 was run on the fixed code. Not rerun: E3 and Appendix A (superseded pilots). The undirected (symmetrized) fits are unaffected and were copied for the 62 unchanged graphs; query 2506.00832 was refitted |

**What bug 4 changed.** Numbers moved by about 0.01 and a few borderline tests crossed 0.05 in either direction; no headline conclusion changed.

**Before and after the QR fix**

|                                                                | before   | after   |
|:---------------------------------------------------------------|:---------|:--------|
| D-SPECTRA: held-out recall, mean of 3 seeds                    | 0.108    | 0.115   |
| query link + relevance: held-out recall, mean of 3 seeds       | 0.154    | 0.166   |
| D-SPECTRA vs relevance only: Holm p                            | 0.057    | 0.030   |
| D-SPECTRA vs USVT: Holm p                                      | 0.053    | 0.278   |
| query link + relevance vs USVT: Holm p                         | 0.420    | 0.041   |
| USVT co-citation + relevance vs query link + relevance: Holm p | 0.057    | 0.758   |
| USVT co-citation + relevance vs D-SPECTRA: Holm p              | <0.001   | 0.002   |
| mean d_ev at eta = 0 (seed 0)                                  | 8.5      | 28.0    |
| mean eta for d_ev = 8 (seed 0)                                 | -0.007   | -0.056  |
| within-query rho, recall vs d_ev(S)                            | -0.07    | +0.17   |
| within-query rho, recall vs |S|                                | +0.54    | +0.55   |

Before the fix, held-out AUC was flat in η and the chosen η spread over the grid; after it, the same. Before, E13's 4–32 modes were flat; after, 2–8 modes are worse. Before, the design queries showed target 8 ahead of η = 0; after, η = 0 is ahead there (and the two tie held out, as before).

**Leakage check after the fixes:** in the E3 graphs, three other title look-alikes (similarity 0.81–0.89) are genuinely different papers. In the E6 graphs, the closest look-alikes (similarity 0.81–0.89, in 3 graphs) are also different papers on the same topic, for example "FDA: Fourier Domain Adaptation for Semantic Segmentation" in the graph for "Universal Domain Adaptation for Semantic Segmentation". A single node citing most of a query's answers is common (median 64–71% of reachable references in E3, 74% in E6) and legitimate: surveys and closely related earlier work.

In 8 E6 graphs, one paper cites *all* of the query's reachable references. That happens only where there are 4–11 of them, and we checked each paper by hand. They are surveys and earlier related work, all dated before the query, for example "Diffusion Model Quantization: A Review" for Q-VDiT and "Federated Unlearning: A Survey…" for the federated-unlearning query. Three of them are papers from DeepScholar's own pool. No node in any E6 graph is dated on or after its query's date; 6% of nodes have no date.

**Status of the review points**

| Point | Status |
|---|---|
| The headline win was at B = 60, but the writer gets ≈22 papers | Fixed: the matched budget (B = kept) and B = 20 are reported |
| Most-cited beats D-SPECTRA | Confirmed; most-cited is a required baseline |
| No clean test set | Fixed: 20 design / 43 held-out queries; E6 is frozen as the held-out result |
| η not really tested on Mateo's pools | d_ev targets 4 and 16 run on the 20 design queries |
| The \|S\| vs d_ev(S) test is confounded | Redone at a fixed budget |
| The optimizer looks unstable | It was bug 4, fixed; the fits now converge (E2, E10 rerun) |
| Leakage through duplicate papers | One real leak found and fixed (bug 1); E6 checked |
| Expanded papers may lack text | Abstract coverage reported; bug 2 found and fixed |
| The proxy may favour concentrated, popular picks | Plan: run the judge on a subset early |
| DeepScholar's own picks and a matched budget | Added in E6 |

**Corrections to the submitted progress report (Oct 21).** Checked line by line against the submitted PDF:

| In the report | Correction |
|---|---|
| "the judge (gpt-4o, released evaluation code)" | We run the released evaluation code with a **local Llama-3.1-70B-Instruct** judge (3.11); no gpt-4o key was used. Scores are comparable between our systems, not with the paper's |
| "its 250 most-cited references" | They are the 250 references **cited by the most pool papers** (and the 130 citing papers that cite the most pool papers), not the most-cited papers globally; the top 250 is taken before the date filter, which can drop a few undated ones |
| "added most-cited, USVT, greedy Vendi and η = 0 baselines" | USVT and Vendi-style diversity are **in the proposal**; only most-cited and η = 0 were added |
| "6,000 epochs (1,500 had not converged)" | 6,000 had not converged either: the drift and loss rise were bug 4. With the fix, fits converge well within 6,000 |
| "adds ≈9 min of GPU fitting per query" | That was three fits sharing a GPU with 12 jobs. One 6,000-epoch fit takes about 18 s on a free GPU and the d_ev = 8 search about 4 min |
| "22 on average, 3–30" kept papers | Seed 0: mean 21.5, range 3–30; seeds 1 and 2: 21.8 (5–30) and 22.6 (6–30) |
| "+.026, p=.004" over top-k by relevance "at every budget"; "trails USVT (−.022, p=.044)"; Table 1 | Single seed, pre-fix fits, uncorrected. Now: +0.030 (p = 0.006) on seed 0 and +0.025 with Holm p = 0.030 seed-averaged; vs USVT −0.018 (p = 0.066) and −0.020 (Holm p = 0.28). Table 1's D-SPECTRA rows are 0.120 and 0.122 after the fix (the fit-free rows are unchanged) |
| "dev targets hit within 5% in 32/36 runs; … AUC .688–.756 vs .596–.663" | After the fix: 31/36 (36/36 within 10%); 0.718–0.752 vs 0.596–0.663 |
| "dev(S) 5.48 vs 6.73, p<.001" and "ρ = −.88" | After the fix: 5.52 vs 6.29 (p = 0.001) on the held-out queries; ρ = −0.47 at B = kept |
| "Code repository: github.com/eftymakr/d-spectra" | The repository is private, and E8–E16 are not yet pushed |

---

## 5. What it means

1. **The proposal's pipeline works and beats the baseline system on the proxy.** At the same number of papers, D-SPECTRA's picks contain about 2.6× as many of the human-cited references as DeepScholar-base's LLM-filtered picks (0.120 vs 0.047 on the held-out queries; 0.115 vs 0.044 seed-averaged), with no LLM calls for selection.
2. **Most of that gain comes from following citations, not from the spectral model.**
   - DeepScholar's pools hold only about 6% of the references humans cite; adding references and citing papers raises that to 37%.
   - Relevance-only selection over the expanded graph already gets most of the gain (0.090).
   - D-SPECTRA's own contribution over relevance-only is real but modest: +0.025 seed-averaged (Holm p = 0.030), and it comes from the coverage term, not from capacity control (η = 0 ties it).
3. **The specific claims about directed capacity control are not supported.**
   - Raw SVD and USVT do as well or better.
   - Changing the target d_ev (4, 8, 14–30, η = 0), choosing η by held-out AUC, AP or NLL, SPECTRA's own baseline-rank targets (E14), prefixes, rank caps, early-stopped probes and restarts: none moves D-SPECTRA's held-out recall out of 0.114–0.133, and most not out of 0.114–0.122.
   - The papers humans cite are *more* concentrated in the graph's dominant modes than a relevance ranking is, not less, and at a fixed budget higher d_ev(S) goes with lower recall. Within a query, recall tracks |S| (ρ = +0.55), not d_ev(S) (ρ = +0.17). On this proxy, "more spectral diversity" is the wrong direction, and the proposal's strongest-result test fails.
   - β sits at its bound of 5 in every fit. Lifting the bound to 20 (E16) lets the model fit the training citations almost perfectly but lowers held-out citation AUC on every graph (0.958 → 0.890) and leaves held-out recall unchanged after correction; the bound is a regulariser, not a confound.
   - **The model-side levers are exhausted.** Capacity (targets 4 to 30, η = 0), SPECTRA's own η rule, η by three held-out criteria, spectral prefixes, rank caps 8–128, early-stopped probes, restarts, the learning-rate schedule, the β bound, mode weights anchored on the pool or on the query, coverage on top of the link score, and feedback from the model's own picks: none moves D-SPECTRA's held-out recall above 0.133, and none moves the query-anchored scores at all. The input-side lever is exhausted too: a second hop of citations (E17) raises reachability from 37% to 52% and lowers every graph method's recall. What is left to test is the endpoint (the writer and judge).
   - **E19 says why the model levers were inert.** The held-out capacity frontier is flat: every realized dimension from 4 to 30 predicts held-out citations equally well (AUC 0.958 ± 0.001), so the d_ev targets, η rules and criteria were choosing among models the data cannot distinguish. E20 adds that the rank cap of 32 is binding by SPECTRA's own criterion, but by 0.002 AUC, saturating at cap 64; the modes above 32 are real and useless for selection.
   - **E22 says where the flatness ends.** With half of each graph's citations removed, the smallest model on the η grid beats η = 0 by 0.011 AUC on 52 of 63 graphs, so the penalty is a real capacity control at that density; the benchmark's graphs are a factor of two above it. Below a quarter of the citations the penalised fits are worse than η = 0, not better. The regime in which SPECTRA's η would have mattered is a window around half the benchmark's density, not everything below it.
4. **The judged evaluation is done, and it does not change the conclusion; it also cannot confirm it (3.20).**
   - Recall of human-cited references rewards popular, well-connected papers, which is what most-cited, raw SVD and USVT pick. On DeepScholar-base's own reports, d_ev of the cited set does not track the judge's nugget coverage (ρ ≈ 0, E12).
   - With every frozen list through the same writer and judge, nugget coverage is a tie: 0.043 for the baseline, 0.036–0.070 for our methods, 0.089 for the oracle, nothing significant after Holm. The 3.5–4× recall gain shows up in the judge's reference coverage (+0.06 to +0.09, uncorrected p ≤ 0.05 for the query-anchored methods) and in a higher coverage-relevance grade for every list, at a third of the tokens, but not as nuggets. D-SPECTRA is in the middle of the pack on every metric.
   - The judge is the limit, not the methods: a metric averaging 0.04–0.09 over 43 queries, with the oracle itself at 0.09, cannot resolve differences of 0.02. Seeds 1 and 2 through the same writer and judge did not change a single conclusion (oracle Holm 0.079, every method within +0.018 of the baseline), so the limit is the metric, not the sample. Organization is blind with this judge and document importance failed on the network; a stronger judge model is the one thing left to try.
   - E18, the one attempt to use the modes in the report rather than in the list, was a null by construction (3.21).
5. **The useful part of the model is directed link prediction, not mode coverage (E8).**
   - As a citation model it is the best we have (E19): held-out AUC 0.959 against 0.935 for the best model-free baseline and 0.846 for USVT, on all 63 graphs. That is SPECTRA's kind of result and it transfers to directed citation graphs; it just does not transfer to selection, where the fit ties USVT co-citation.
   - Scoring the query as a new citing node puts the query's citing role against each paper's cited role and brings popularity back in through b_j. It beats D-SPECTRA by +0.050 and USVT by +0.030 seed-averaged (Holm p ≤ 0.041).
   - Covering the fitted modes with F(S) doesn't improve, whatever η or mode weights we use, including weights taken from the query's own citing vector (E15); coverage on top of the link score adds nothing either (E11, E15), and refining the query's citing role from the model's own picks makes it worse (E15).
   - **E21 shows what the fit can do that USVT cannot, and where it stops mattering.** Placed in the fitted citing-role space from its text alone, a held-out paper's references are recovered far better than by any anchor-based score (0.303 vs 0.244 for USVT co-citation + relevance, 39 of 43 graphs). Against the benchmark's human reference lists the same map ties everything else (0.165 vs 0.175). The citing-role space is the model's genuine contribution; the benchmark's target is where it cannot be used.
   - **E11, E13 and E14 qualify it:** the fitted model isn't needed for the gain.
     - A model-free count of how many of the most relevant pool papers cite each paper does as well as the SPECTRA query link.
     - The same count on USVT's denoised citation matrix (0.184) and the anchors' predicted citations under the fitted model (0.172–0.184) are the same within noise.
     - What works is treating the query as a new citing paper, through the papers most like it, and mixing in relevance. Directed SPECTRA matches USVT denoising of the same citations and does not add to it on this proxy.
   - **For the report:** query-anchored citation scoring beats DeepScholar-base's filter by about 3.5–4× on recall at a third of the tokens and with no fitting; directed spectral capacity control does not help, tested every way SPECTRA allows plus three of our own. Through the writer and judge, the gain survives as reference coverage and coverage relevance, and no system is separable from any other on nugget coverage (3.20).
6. **Caveats.**
   - Every selection result in 3.1–3.19 is on a retrieval proxy (recall of human-cited references). The judged evaluation (3.20) is one search seed, one writer and one judge model, with two of seven metrics unusable (organization, document importance).
   - The held-out queries are not fully clean. E6 was frozen before anyone looked at them, but the E8–E10 methods were chosen on the design queries after E6's held-out results were known, and the E11 and E13 methods were designed after the E8–E10 held-out results had been seen. The search-seed replication (E10, E12) checks stability, not independence; only new queries would.
   - Three search seeds and three fit seeds; the tests in 3.13–3.17 are Holm-corrected, the per-experiment tables in 3.1–3.12 are not. There are hundreds of uncorrected comparisons in this document; isolated p ≈ 0.02–0.05 results should be read as weak.
   - 41 of the 43 held-out queries have a reachable reference; seed-averaged tables count all 43.
   - E3, Appendix A and the E5 diagnostics were seen during design and were not rerun after bug 4.
   - F(S) deviates from the proposal in two documented ways (relevance term divided by B, z_k normalised by each mode's relevant mass) and the per-mode occupancy is σ/Σσ rather than SPECTRA's σ²/Σσ², as proposed.
   - Not done from the proposal: the closed loop (step 4) and its "coverage lost by stopping early" diagnostic; ResearchQA and DeepResearch Bench II; a second backbone; blinded judge spot-checks; citation lookups charged against a matched budget. The writer and judge on search seeds 1 and 2 are running (section 7).

---

## 6. Files and how to reproduce

Everything is under `/home/eftychia/Spectra/d-spectra/` (GitHub: `eftymakr/d-spectra`, private). `main` holds the code and results up to E6 as of Oct 22; the bug-4 fix, E8–E16 and the refitted results are local and not yet pushed. `data/` and the superseded results are not in git. Every fitted result directory listed below was regenerated on Oct 29–30; the pre-fix versions are in `results/pre_qrfix/<same name>/`.

| What | Where |
|---|---|
| Directed SPECTRA, fitting, bisection | `dspectra/model.py` |
| Selection, Vendi selector, d_ev(S) | `dspectra/selection.py` |
| OpenAlex client (key in the git-ignored `.env`) | `dspectra/openalex.py` |
| E1 synthetic check | `scripts/synthetic_check.py` → `results/synthetic_6000/` |
| E2 convergence check | `scripts/convergence_check.py` → `results/convergence/` |
| E3 OpenAlex graphs and pilot | `scripts/build_graphs.py` → `data/graphs_v2/`; `scripts/pilot_selection.py` → `results/pilot_v2/` |
| E5 pool diagnostics | `scripts/pool_graphs.py`, `scripts/pool_edges_s2.py` → `data/pool_graphs/` |
| E6 graphs | `scripts/build_pool_expanded.py` → `data/graphs_dsf/`, superseded by `data/graphs_small/` (2506.00832 rebuilt) |
| E6 fits | `scripts/fit_variants.py --fits d8 eta0 cv` and `scripts/fit_sensitivity.py` (targets 4, 16; `--kind symmetric`) → `results/e8_small/operators/` |
| E6 evaluation | `scripts/pilot_selection.py --operators results/e8_small/operators --kept_dir …` → `results/pilot_dsf/` (expanded), `results/pilot_dsf_strict/` (pool-only) |
| Selection lists for Mateo's writer | `scripts/export_final.py` → `selections/final/s{0,1,2}/` (the old `selections/final_s0/` is in `selections/pre_qrfix/`) |
| E8 graphs | `data/graphs_small/` (E6's, with 2506.00832 rebuilt), `data/graphs_big/` (`build_pool_expanded.py --n_refs 500 --n_citers 260`) |
| E8 fits | `scripts/fit_variants.py` → `results/e8_small/operators/`, `results/e8_big/operators/` (with `*_full.npz`: every fitted quantity) |
| E8 evaluation | `scripts/pilot_selection.py --variants` → `results/e8_{small,big}/` (expanded), `results/e8_{small,big}_strict/` (pool-only) |
| E9 | `scripts/fit_variants.py` → `results/e9_{es,r8,r64,r128,crit,seed1,seed2}/`; prefixes from E8's fits → `results/e9_prefix/` |
| E10 | `scripts/tune_selection.py` → `results/e10_tune/`; `fit_variants.py --lr_schedule cosine` → `results/e10_lr/`, `results/e10_lrconst/`; seeds 1–2: `data/graphs_s{1,2}/`, `results/e10_s{1,2}/` |
| E11 | `scripts/variants_e11.py` → `results/e11{,_s1,_s2}/rows.csv` |
| E12 | `scripts/export_final.py` → `selections/final/`; `scripts/gate_judged.py` → `results/gate_judged_s0/`; `scripts/seed_tests.py` → `results/seed_tests/`; `scripts/to_judge_format.py` for the judge's input format |
| E13 | `scripts/variants_e13.py` → `results/e13_s{0,1,2}/rows.csv`; seed-averaged tests → `results/e13_tests/` |
| E14 | `scripts/fit_variants.py --fits tmin tmed` → `results/e14_s{0,1,2}/`; tests → `results/e14_tests/` |
| E15 | `scripts/variants_e15.py` → `results/e15_s{0,1,2}/rows.csv`; tests → `results/e15_tests/` |
| E16 | `scripts/fit_variants.py --fits d8 eta0 cv --beta_max 20` → `results/e16_beta20_s{0,1,2}/` (operators, `per_query/`, `e11/`, `e13/`); the 20-query pilot → `results/e15_beta20/`; tests → `results/e16_tests/` |
| The judge | `/home/eftychia/Spectra/judge/` (`serve_judge.sh`, `relay.py`, `run_judge.sh`, `deepscholar-bench-local-judge.patch`), results in `judge/results/dsbase_s0/`; the benchmark clone at `/home/eftychia/Spectra/deepscholar-bench` |
| E17 | `scripts/build_pool_expanded.py --n_refs2 2500` → `data/graphs_d2/`; fits → `results/e17_d2/`, `results/e17_d2_d8/`; tests → `results/e17_tests/` |
| E19 | `scripts/linkpred_e19.py` → `results/e19_linkpred/` (`per_graph.csv`, `tests.csv`); `scripts/frontier_e19.py` → `frontier_r32.png` |
| E20 | `scripts/fit_variants.py --rank 64/128 --fits cv` → `results/e20_r64/`, `results/e20_r128/`; tests and per-graph AUC → `results/e20_r64/e20_tests.csv`, `e20_per_graph.csv`; `scripts/frontier_e20.py` → `results/e19_linkpred/frontier_caps.png` |
| E21 | `scripts/coldstart_e21.py` → `results/e21/` (`fits/`, `pseudo_rows.csv`, `real_rows.csv`, `tests.csv`); rules `scratchpad/e21_rules.md` |
| E22 | `scripts/sparse_frontier.sh` (`fit_variants.py --fits cv --edge_keep 0.5/0.25/0.1`) → `results/sparse_k{50,25,10}/operators/`; `scripts/sparse_frontier.py` → `results/sparse/` (`stats.csv`, `tests.csv`, `summary.md`, `frontier_sparse.png`); rules `scratchpad/sparse_rules.md` |
| The writer on every list | `judge/run_writer.py`, `judge/serve_qwen.sh`, `judge/run_writer_all.sh` → `judge/writer/s0/<system>/<row>/` (`final_report.md`, `intro.md`, `paper.csv`, `stats.json`); E18 with `--mode_taxonomy` → `judge/writer/s0/<system>_modes/` |
| The judge on every list | `judge/judge_chain2.sh`, `judge/chain3.sh`, `judge/chain4_repair.sh` → `judge/results/writer_s0/<system>/<metric>/`; analysis `scripts/judged_eval.py` → `results/judged/` (`rows.csv`, `tests.csv`, `frontier.png`); rules `scratchpad/judged_rules.md` |
| Seeds 1 and 2 through the writer and judge | `judge/seeds12_chain.sh` → `judge/writer/s{1,2}/<system>/`, `judge/results/writer_s{1,2}/<system>/<metric>/`; analysis `scripts/judged_seeds.py` → `results/judged_s12/` (`rows.csv`, `avg.csv`, `tests.csv`); rules `scratchpad/seeds12_rules.md` |
| Pre-fix results | `results/pre_qrfix/`, `selections/pre_qrfix/` |
| Mateo's pools and outputs | `data/ds_pools_final/`, `data/ds_outputs_final/` (from branch `pools-pilot`) |
| Superseded | `results/pilot/` and `results/synthetic/` (1,500 epochs); `results/pilot_ds*/` and `data/graphs_ds/` (pilot pools, bug 3); `data/_backup/` (before the bug fixes) |

---

## 7. Open items

- **Judged, seeds 1 and 2: done (Nov 6, section 3.20).** The one prediction that failed is the oracle's Holm-corrected separation (0.079); everything else held. Nothing judged remains to run with this judge model.
- **Document importance:** recompute for all 12 writer runs when the OpenAlex quota allows (no judge model needed).
- **Needs Mateo:** a second backbone; agree on how his part is described; whether to rerun his seed-0 reports with the current writer so that 3.11 and 3.20 match.
- **Commit and push:** the bug-4 fix, E8–E21 code, the refitted results, `selections/final/`, the writer and judge scripts and `results/judged/` are not on GitHub yet.
- **Still open from the proposal:** the closed loop (step 4) against relevance-driven expansion at equal lookups, with the stopping diagnostic; ResearchQA (a stratified 200-question sample) and DeepResearch Bench II; blinded spot-checks of the judge; citation lookups charged against a matched budget; the public release.
- **Not rerun after bug 4:** E3 and Appendix A (superseded pilots).
- **Open questions about the model:** none on the model side after E16 and E20 (the β bound and the rank cap are settled; section 5, item 3), none on the input side after E17 (the second hop hurts), and none on the query side after E21 (the inductive role wins against graph ground truth and ties against the human lists). E22 places the graphs a factor of two above the density at which η would have mattered; the one thing not run there is a selection rerun on the half-density graphs, which the rule excluded and which E19–E20 argue would show nothing. The d_ev = 8 search's 2% tolerance is often unreachable because d_ev now moves in steps as a mode switches off (54% within 2%, 97% within 5%).
- **Report:** the second progress report should carry the corrections listed in section 4.

---

## Appendix A. Superseded: the 20 pilot pools

> **Superseded by E6, kept for the record.** This was the proposal's version run on Mateo's 20 *pilot* pools (3 search rounds, temperature 1.0) before the final pools existed. It is affected by bug 3 (about 12% of each pool's papers missing; bug 2 was fixed) and by bug 4 (its fits were not redone). Means over the 19 queries with at least one human-cited reference in the graph, at fixed budgets only (no matched budget, no DeepScholar picks).

**Expanded graphs built from Mateo's pools (Semantic Scholar), per query**

| query      | nodes   | pool papers   | refs added   | citers added   | edges   | human refs   | in pool   | in expanded graph   |
|:-----------|:--------|:--------------|:-------------|:---------------|:--------|:-------------|:----------|:--------------------|
| 2505.22757 | 463     | 84            | 255          | 124            | 3755    | 21           | 2         | 9                   |
| 2505.23290 | 512     | 134           | 272          | 106            | 6670    | 27           | 7         | 18                  |
| 2505.23353 | 530     | 154           | 269          | 107            | 4796    | 22           | 0         | 3                   |
| 2505.23996 | 455     | 75            | 259          | 121            | 4691    | 52           | 0         | 9                   |
| 2505.24334 | 491     | 112           | 254          | 125            | 4218    | 23           | 3         | 13                  |
| 2505.24443 | 471     | 95            | 253          | 123            | 6426    | 37           | 4         | 29                  |
| 2505.24575 | 484     | 105           | 256          | 123            | 3157    | 22           | 0         | 7                   |
| 2505.24754 | 510     | 130           | 256          | 124            | 4558    | 19           | 2         | 11                  |
| 2506.00085 | 510     | 130           | 256          | 124            | 4441    | 37           | 0         | 10                  |
| 2506.00333 | 480     | 101           | 272          | 107            | 8528    | 9            | 1         | 9                   |
| 2506.00418 | 531     | 152           | 258          | 121            | 4123    | 11           | 1         | 1                   |
| 2506.00434 | 502     | 122           | 255          | 125            | 5157    | 14           | 2         | 10                  |
| 2506.00832 | 465     | 88            | 267          | 110            | 4359    | 11           | 0         | 5                   |
| 2506.00958 | 475     | 97            | 255          | 123            | 5550    | 24           | 0         | 6                   |
| 2506.01037 | 508     | 129           | 267          | 112            | 7373    | 39           | 4         | 22                  |
| 2506.01071 | 485     | 106           | 269          | 110            | 7999    | 35           | 5         | 28                  |
| 2506.02547 | 484     | 107           | 250          | 127            | 5707    | 11           | 0         | 0                   |
| 2506.02634 | 429     | 51            | 265          | 113            | 6899    | 44           | 2         | 14                  |
| 2506.02838 | 492     | 113           | 258          | 121            | 3175    | 17           | 1         | 1                   |
| 2506.02853 | 486     | 108           | 266          | 112            | 8313    | 35           | 3         | 24                  |

Totals: 510 human-cited references; 37 (7.3%) in the pools, 229 (44.9%) in the expanded graphs. Mean 488 nodes, 5495 edges.

*Expanded setting* (any paper in the graph may be picked):

**Recall of related-work references**

| method                         | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:-------|:-------|:-------|:-------|:-------|
| fixed-k (search only)          | 0.033  | 0.046  | 0.060  | 0.071  | 0.075  |
| relevance only (main ablation) | 0.048  | 0.073  | 0.103  | 0.125  | 0.151  |
| most_cited                     | 0.101  | 0.161  | 0.192  | 0.223  | 0.247  |
| vendi                          | 0.042  | 0.064  | 0.090  | 0.129  | 0.156  |
| semantic_modes                 | 0.048  | 0.082  | 0.104  | 0.129  | 0.163  |
| symmetrized                    | 0.057  | 0.084  | 0.107  | 0.144  | 0.191  |
| raw_svd                        | 0.121  | 0.164  | 0.208  | 0.254  | 0.286  |
| usvt                           | 0.109  | 0.166  | 0.203  | 0.264  | 0.288  |
| dspectra_eta0                  | 0.071  | 0.098  | 0.131  | 0.189  | 0.226  |
| dspectra                       | 0.070  | 0.104  | 0.118  | 0.171  | 0.212  |

**D-SPECTRA minus each method (wins/losses over queries, paired Wilcoxon p)**

|                                | B=10                   | B=20                   | B=30                    | B=45                    | B=60                    |
|:-------------------------------|:-----------------------|:-----------------------|:------------------------|:------------------------|:------------------------|
| fixed-k (search only)          | +0.037 (10/0, p=0.005) | +0.058 (12/0, p=0.002) | +0.059 (14/2, p=0.005)  | +0.100 (15/1, p=<0.001) | +0.137 (16/0, p=<0.001) |
| relevance only (main ablation) | +0.021 (8/1, p=0.024)  | +0.031 (7/2, p=0.066)  | +0.016 (6/4, p=0.610)   | +0.046 (11/2, p=0.004)  | +0.061 (13/1, p=0.004)  |
| most_cited                     | -0.032 (7/7, p=0.730)  | -0.058 (5/10, p=0.293) | -0.074 (4/11, p=0.023)  | -0.052 (9/9, p=0.276)   | -0.036 (8/10, p=0.459)  |
| vendi                          | +0.027 (8/1, p=0.021)  | +0.040 (8/1, p=0.015)  | +0.029 (7/3, p=0.103)   | +0.042 (9/4, p=0.075)   | +0.055 (10/1, p=0.013)  |
| semantic_modes                 | +0.022 (8/1, p=0.018)  | +0.022 (6/1, p=0.063)  | +0.014 (8/4, p=0.410)   | +0.042 (9/1, p=0.013)   | +0.049 (11/3, p=0.009)  |
| symmetrized                    | +0.013 (7/2, p=0.192)  | +0.019 (6/2, p=0.069)  | +0.011 (6/5, p=0.398)   | +0.027 (9/5, p=0.096)   | +0.021 (9/4, p=0.162)   |
| raw_svd                        | -0.051 (3/9, p=0.028)  | -0.061 (2/12, p=0.004) | -0.089 (2/15, p=0.001)  | -0.083 (0/12, p=0.002)  | -0.074 (1/12, p=0.004)  |
| usvt                           | -0.039 (3/9, p=0.170)  | -0.062 (3/11, p=0.005) | -0.084 (0/16, p=<0.001) | -0.093 (0/13, p=0.001)  | -0.076 (1/13, p=0.003)  |
| dspectra_eta0                  | -0.001 (1/1, p=0.655)  | +0.006 (3/4, p=0.612)  | -0.013 (3/6, p=0.214)   | -0.018 (4/6, p=0.203)   | -0.014 (4/6, p=0.241)   |

*Pool-only setting* (only pool papers may be picked):

**Recall of related-work references**

| method                         | B=10   | B=20   | B=30   | B=45   | B=60   |
|:-------------------------------|:-------|:-------|:-------|:-------|:-------|
| fixed-k (search only)          | 0.033  | 0.046  | 0.060  | 0.071  | 0.075  |
| relevance only (main ablation) | 0.033  | 0.046  | 0.060  | 0.071  | 0.075  |
| most_cited                     | 0.053  | 0.057  | 0.064  | 0.069  | 0.075  |
| vendi                          | 0.035  | 0.045  | 0.051  | 0.058  | 0.071  |
| semantic_modes                 | 0.036  | 0.044  | 0.058  | 0.069  | 0.073  |
| symmetrized                    | 0.039  | 0.053  | 0.060  | 0.074  | 0.078  |
| raw_svd                        | 0.057  | 0.067  | 0.069  | 0.075  | 0.075  |
| usvt                           | 0.059  | 0.067  | 0.069  | 0.075  | 0.075  |
| dspectra_eta0                  | 0.047  | 0.064  | 0.069  | 0.075  | 0.075  |
| dspectra                       | 0.047  | 0.059  | 0.066  | 0.075  | 0.075  |

**D-SPECTRA minus each method (wins/losses over queries, paired Wilcoxon p)**

|                                | B=10                  | B=20                  | B=30                  | B=45                  | B=60                  |
|:-------------------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|
| fixed-k (search only)          | +0.014 (7/0, p=0.018) | +0.013 (4/0, p=0.068) | +0.007 (5/2, p=0.398) | +0.004 (2/0, p=0.180) | +0.000 (0/0, p=1.000) |
| relevance only (main ablation) | +0.014 (7/0, p=0.018) | +0.013 (4/0, p=0.068) | +0.007 (5/2, p=0.398) | +0.004 (2/0, p=0.180) | +0.000 (0/0, p=1.000) |
| most_cited                     | -0.006 (3/5, p=0.484) | +0.002 (3/3, p=0.917) | +0.002 (1/1, p=0.655) | +0.006 (1/0, p=0.317) | +0.000 (0/0, p=1.000) |
| vendi                          | +0.012 (7/1, p=0.161) | +0.014 (7/1, p=0.123) | +0.015 (6/1, p=0.176) | +0.017 (6/0, p=0.028) | +0.004 (2/0, p=0.180) |
| semantic_modes                 | +0.012 (6/0, p=0.028) | +0.015 (6/0, p=0.028) | +0.008 (6/2, p=0.327) | +0.006 (3/0, p=0.109) | +0.002 (1/0, p=0.317) |
| symmetrized                    | +0.008 (4/0, p=0.068) | +0.006 (3/1, p=0.273) | +0.006 (3/1, p=0.273) | +0.002 (1/0, p=0.317) | -0.003 (0/1, p=0.317) |
| raw_svd                        | -0.010 (0/4, p=0.068) | -0.008 (0/3, p=0.109) | -0.003 (0/1, p=0.317) | +0.000 (0/0, p=1.000) | +0.000 (0/0, p=1.000) |
| usvt                           | -0.012 (0/4, p=0.068) | -0.008 (0/3, p=0.109) | -0.003 (0/1, p=0.317) | +0.000 (0/0, p=1.000) | +0.000 (0/0, p=1.000) |
| dspectra_eta0                  | +0.000 (0/0, p=1.000) | -0.005 (0/2, p=0.180) | -0.003 (0/1, p=0.317) | +0.000 (0/0, p=1.000) | +0.000 (0/0, p=1.000) |

---

## Appendix B. Mateo's pilot report (verbatim)

> Mateo's report from Oct 21 (`D-SPECTRA_pilot_report.md`), included unchanged except that its headings are moved down two levels. It describes his 20-query pilot; his final runs came later (section 3.5). His three questions in it have since been answered: every system selects from his frozen pool, and D-SPECTRA is fitted on the pool plus its references and citing papers (E6); 2 search rounds are fine, since within-pool citations, not pool size, limit the fit; and Qwen's sampling settings with seeds 0–2 were adopted.

### D-SPECTRA pilot report: DeepScholar-base on Qwen3-8B

Oct 21, 2026 · Mateo

DeepScholar-base runs end to end on a local Qwen3-8B and yields about 125 arXiv candidates per query. Takeaways: search arXiv only, give every arm the same frozen pool per query, and settle sampling before the final runs.

#### Setup

I ran the first 20 queries three times on my RTX 3090: twice searching arXiv only (runs A and B, to measure run-to-run noise) and once searching arXiv plus the web. The model was Qwen3-8B-AWQ (a 4-bit version of Qwen3-8B) served through vLLM, with a 32k context and thinking off. In every run, search only returns papers published before the target paper, and DeepScholar's own LLM filter then picks which papers go to the writer.

| Setting | DeepScholar paper | Repo default | Our pilot | Final runs |
| --- | --- | --- | --- | --- |
| Search mode | recursive | agentic | recursive | recursive |
| Rounds × queries per round | 2 × 2 | 3 × 2 | 3 × 2 | 2 × 2 |
| Results kept per query | 50 | 10 | 50 | 50 |
| Papers passed to the writer | up to 30 | up to 30 | up to 30 | up to 30 |
| Corpus | arXiv only | arXiv + web | arXiv (+ one web run) | arXiv only |
| Model | GPT-4.1 or Llama-4-Scout | GPT-5-mini | Qwen3-8B-AWQ | Qwen3-8B-AWQ |
| Sampling | not stated | temperature 1.0 | temperature 1.0 | 0.7 / top_p 0.8 / top_k 20, seeds 0–2 (question 3) |

Our pilot matches the paper's setup except for the extra search round and the model.

#### Results

| Run | Papers in pool (mean) | Papers DeepScholar kept (mean) | Minutes per query |
| --- | --- | --- | --- |
| arXiv A | 125.9 | 22.1 | 3.8 |
| arXiv B | 123.1 | 21.4 | 2.6 |
| arXiv + web | 176.3 | 27.2 | 4.1 |

- **Search is noisy.** A and B share only 46% of their arXiv papers (range 14–86%). Every arm must select from the same frozen pool, or search noise swamps the comparison.
- **Web adds no arXiv coverage** (overlap 41% vs 46% noise, p = 0.39) **and leaks:** about 5 post-cutoff papers per query, and the model searched for the target paper by name.
- **Backbone:** Qwen3-4B kept only 2–3 papers per query; the 8B keeps about 22.

#### From the DeepScholar paper (arXiv 2508.20033, Table 3)

- **Retrieval is the bottleneck:** giving the writer the true references lifts their score from .286 to .808.
- **arXiv only, by design:** they restrict every system to the arXiv API to keep the corpus the same across systems, and in their test Tavily scores below arXiv on reference coverage (.070 vs .152). Our leakage finding is a second, independent reason.
- **Single runs only, no variance.** With our 46% run-to-run overlap, one run isn't enough; we'll report three seeds.

#### DeepScholar bugs I fixed (in my wrapper; their code is untouched)

| Bug | Fix |
| --- | --- |
| Every LLM call silently capped at 512 tokens; the filter rejected almost everything | pass the 10k limit to each stage |
| Only the last search round is kept | save all rounds as `pool_all.csv` |
| Model writes 5–10 search queries instead of 2, overflowing the context | keep the first 2 |
| LaTeX braces in an abstract crash the filter | replace `{ }` with `( )` |

#### Pools

The 20 pilot pools are on the `pools-pilot` branch in `pools/qwen3-8b-awq_k50/`. Each query has its own folder with two files:

- `query.json`: the target paper and its cutoff date.
- `pool_all.csv`: every paper search found, one row per paper. The useful columns are `title`, `snippet` (the abstract), `date`, `arxiv_id_from_url` (use this to look the paper up in OpenAlex) and `n_hits` (how many searches found it).

These are for building and testing your side. I'll replace them with the final pools once we lock the settings.

#### Questions for you

1. **Same pool: needs a change in `build_graphs.py`.** You said our method has to start from the same papers, so every arm selects from the DeepScholar pool. Right now `build_graphs.py` builds its own pool from OpenAlex (seed search, then their references and citers). For the same-pool setup it should take the papers in `pool_all.csv` and use OpenAlex only for the citation edges between them. Its cutoff already matches DeepScholar's and it removes the target paper, so there's no leak to fix.
2. **Pool size.** Pools have 40–170 papers (125 on average). With 2 search rounds they'd be about 16% smaller (about 107 on average, 39–157), going by the first two rounds of the pilot runs. To try that size, filter `pool_all.csv` to rows with `_call` ≤ 1. How many papers does your fit need to be stable? If it needs more, I can return more results per search without adding arXiv calls.
3. **Sampling.** Temperature 1.0 is the repo's default for GPT-5-mini, not something chosen for Qwen. The final runs use Qwen's recommended non-thinking settings (temperature 0.7, top_p 0.8, top_k 20) with seeds 0, 1, 2. Tell me if you'd rather keep 1.0.

#### Next on my side

1. **Runner updated for the final runs (done):**
   - 2 search rounds instead of 3, to match the paper (trimming a 3-round pool gives the right papers, but DeepScholar's filter and report still come from round 3, so its own scores need a real 2-round run);
   - Qwen's sampling settings with seeds 0–2 (question 3);
   - a record of which round found each paper, so the pools can be cut by round without guessing.
2. **Building the final pools for all 63 queries tonight, one per seed, then freezing them.** Every arm selects from the same frozen pool, so differences between arms come from selection, not from search noise. Running all three seeds gives us the run-to-run spread the paper doesn't report.
