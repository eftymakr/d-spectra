# E23 reading (2026-11-24; run finished 11-19 05:06)

Rules: rules/e23_sparse_selection_rules.md (written 11-18 before the run). Scores: summary.md,
tests.csv, rows.csv. Script check at full density: results/e23_check reproduces the report's
seed-0 held-out recalls (D-SPECTRA 0.115, USVT 0.132, query link 0.168, USVT co-citation 0.175
over all 43 queries).

Setting: 63 seed-0 graphs, half of the citations kept (mean 2,360), three thinnings, recall at
B = kept averaged over thinnings, 43 held-out queries, Holm over 6.

## Predictions
1. cv rule picks a negative eta on most graphs: HOLDS (91% of fits, median -0.10; d_ev 7.4 against
   30.3 at eta = 0).
2. P1-P3 null (|difference| < 0.01): FAILS for P1, in the wrong direction for the method.
   P1 dspectra_cv - dspectra_eta0 = -0.029 (7 wins / 25 losses, Holm p = 0.004): choosing the
   capacity by held-out AUC makes coverage selection worse. P2 (d_ev = 8) -0.012, Holm 0.19.
   P3 (query link) -0.007, Holm 0.33.
3. Model-based selectors lose less from thinning than USVT-based ones: direction HOLDS, not
   significant. scocite_cv - usvt_cocite goes from -0.016 at full density to +0.008 at half
   (21/12, p = 0.075, Holm 0.23); qlink_cv - usvt_cocite from -0.020 to -0.001. P6 dspectra_cv -
   usvt = -0.033 (Holm 0.013): the coverage selector on the small model is significantly worse
   than on USVT's modes.

## Decision (per the rules)
None of P1, P3 is positive, and none of P4-P6 is positive after Holm. Capacity control's benefit
at half density is confined to prediction. The stronger statement the data support: in the one
regime where the smaller model predicts held-out citations better (E22, 52 of 63 graphs), using it
for selection costs recall (0.128 -> 0.099 for the coverage selector). Better prediction and better
selection come apart here as they did at full density (E13), now with the sign reversed.
No further density, thinning scheme or setting is tried.

## Descriptive
- What losing half the citations costs (held-out recall, keep 1.0 -> 0.5): USVT co-citation
  0.175 -> 0.148, co-citation 0.164 -> 0.141, query link (eta = 0) 0.168 -> 0.153, SPECTRA
  co-citation (eta = 0) 0.168 -> 0.154, USVT modes 0.132 -> 0.132, D-SPECTRA d_ev = 8
  0.115 -> 0.116, D-SPECTRA eta = 0 0.116 -> 0.128. The count-based selectors lose the most; the
  model-based link selectors become the best two at half density, by margins that are not
  significant.
- Per fit, the held-out AUC gain of the cv fit over eta = 0 does not predict the recall
  difference (rho = -0.11, p = 0.12, n = 189).

## For the report
One sentence in the capacity section and one row in the experiment log: E22's "real capacity
control" holds for prediction only; E23 shows the selected smaller model recovers fewer
human-cited references (Holm p = 0.004). The sentence "SPECTRA's penalty is therefore a real
capacity control on this kind of data" should say "for prediction".
