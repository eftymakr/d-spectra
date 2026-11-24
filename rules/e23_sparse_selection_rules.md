# E23: does capacity control improve selection where it improves prediction? Rules (2026-11-18, before any run)

Question. E22 found one regime in which SPECTRA's capacity control matters: with half of the
citations removed, the smallest model on the eta grid predicts held-out citations better than
eta = 0 on 52 of 63 graphs (+0.011 AUC). E22 measured prediction only ("No selection reruns").
E23 asks the selection question in that regime: on the half-density graphs, does choosing the
capacity (eta by held-out AUC, or the proposal's d_ev = 8) change which human-cited references
the selectors recover, and do the model-based selectors hold up better than the USVT-based ones
when citations are missing?

## Graphs and fits
- The 63 depth-1 graphs of search seed 0 (data/graphs_small, pools/final_r2_s0), all nodes kept,
  each citation kept with probability 0.5 (fit_variants.py --edge_keep 0.5, numpy
  default_rng(edge_seed) per graph). Three thinnings, edge_seed 0, 1, 2 (edge_seed 0 is E22's).
- fit_variants.py --fits d8 eta0 cv, rank 32, 6,000 epochs, beta_max 5, fit seed 0, the 7-eta grid
  of E22. Outputs results/e23_k50_e{0,1,2}/operators. One density only (0.5): E22 showed no
  capacity benefit at 0.25 and 0.1, so those levels cannot answer the question.
- Every method sees only the thinned graph: fits, USVT, co-citation counts, in-degree, and the
  anchors (most relevant pool papers with at least one remaining outgoing citation). Relevance and
  the ground truth (the human-cited references in the graph's node set) do not depend on edges.

## Methods (frozen settings of export_final.py; B = kept, expanded setting)
- Coverage selector F(S), alpha 0.5, gamma 5: dspectra_eta0, dspectra_cv, dspectra_d8; usvt and
  raw_svd modes of the thinned matrix.
- Query link + relevance (10 anchors, weight 0.75): qlink_rel_eta0, qlink_rel_cv.
- SPECTRA co-citation + relevance (5 anchors, all modes, 0.75): scocite_rel_eta0, scocite_rel_cv.
- cocite_rel (10 anchors), usvt_cocite_rel (5 anchors), most_cited, relevance_only, fixed_k.
- Check of the script: the same code at edge_keep = 1.0 on E8's fits (results/e8_small) must
  reproduce the seed-0 held-out recalls of the report (D-SPECTRA 0.120 over the 41 reachable
  queries, query link 0.177, USVT co-citation 0.184) before any thinned result is read.

## Statistic and tests
- Per query: recall of human-cited references at B = kept, averaged over the three thinnings;
  0 where no reference is reachable (as in the seed-averaged tables). Unit = query; held-out 43
  for the tests, design 20 reported separately.
- Primary family, paired Wilcoxon, Holm over 6:
  P1 dspectra_cv - dspectra_eta0        (capacity by held-out AUC, coverage selector)
  P2 dspectra_d8 - dspectra_eta0        (the proposal's target)
  P3 qlink_rel_cv - qlink_rel_eta0      (capacity by held-out AUC, link selector)
  P4 scocite_rel_cv - usvt_cocite_rel   (model vs denoising, same anchors)
  P5 qlink_rel_cv - usvt_cocite_rel
  P6 dspectra_cv - usvt                 (coverage selector on model modes vs USVT modes)
- Descriptive: each method's recall at keep 0.5 against keep 1.0 (what losing half the citations
  costs); the eta and d_ev the cv rule picks; per-graph Spearman between the held-out AUC gain of
  the cv fit over eta = 0 and the recall difference of P1.
- Interim looks at edge_seed 0 alone are allowed for monitoring and decide nothing.

## Predictions
1. Sanity: the cv rule picks a negative eta on most graphs (E22: best eta -0.1 on 47 of 63).
2. P1, P2, P3: |mean difference| < 0.01 and not significant. A +0.011 AUC gain is small, and at
   full density a 0.11 AUC gap between the fit and USVT did not change selection (E13).
3. P4-P6: the model-based selectors lose less recall from thinning than the USVT-based ones, so
   each difference is larger (more positive) at keep 0.5 than at keep 1.0; P4 > 0. Low confidence;
   not expected to survive Holm.

## Decision rule
- P1 or P3 positive after Holm: the report states that capacity control improves selection in the
  sparse regime (the first selection-level evidence for the spectral term), with keep = 0.25 run
  next as a dose-response check under the same rules.
- Only P4-P6 positive after Holm: the fitted model is the more robust selector under missing
  citations; capacity control itself remains shown only at the prediction level.
- None: capacity control's benefit at half density is confined to prediction, and the report says so.
- No other density, thinning scheme, method setting or budget is tried after the results are seen.
