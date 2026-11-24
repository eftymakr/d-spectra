# E23: selection on graphs with 0.5 of the citations (rules/e23_sparse_selection_rules.md)

Thinnings (edge seeds): [np.int64(0), np.int64(1), np.int64(2)]; queries: 43 held-out, 20 design; mean citations per graph 2360.

cv rule: eta < 0 on 91% of fits (median eta -0.10); mean d_ev: cv 7.4, eta = 0 30.3, d8 8.0; USVT rank median 33.

## Recall at B = kept (mean over thinnings, then over queries)

| method | held-out (43) | design (20) |
|---|---|---|
| scocite_rel_cv | 0.155 | 0.207 |
| scocite_rel_eta0 | 0.154 | 0.207 |
| qlink_rel_eta0 | 0.153 | 0.202 |
| usvt_cocite_rel | 0.148 | 0.186 |
| qlink_rel_cv | 0.146 | 0.203 |
| cocite_rel | 0.141 | 0.179 |
| usvt | 0.132 | 0.181 |
| raw_svd | 0.132 | 0.183 |
| dspectra_eta0 | 0.128 | 0.173 |
| dspectra_d8 | 0.116 | 0.114 |
| dspectra_cv | 0.099 | 0.099 |
| most_cited | 0.091 | 0.153 |
| relevance_only | 0.086 | 0.064 |
| fixed_k | 0.057 | 0.035 |

## Primary family (held-out, paired Wilcoxon, Holm over 6)

| test | comparison | difference | wins/losses | p | Holm p |
|---|---|---|---|---|---|
| P1 | dspectra_cv - dspectra_eta0 | -0.0285 | 7/25 | 0.001 | 0.004 |
| P2 | dspectra_d8 - dspectra_eta0 | -0.0115 | 10/14 | 0.047 | 0.188 |
| P3 | qlink_rel_cv - qlink_rel_eta0 | -0.0071 | 9/19 | 0.165 | 0.330 |
| P4 | scocite_rel_cv - usvt_cocite_rel | +0.0075 | 21/12 | 0.075 | 0.226 |
| P5 | qlink_rel_cv - usvt_cocite_rel | -0.0014 | 18/14 | 0.647 | 0.647 |
| P6 | dspectra_cv - usvt | -0.0331 | 9/26 | 0.003 | 0.013 |

Per fit, Spearman between the cv fit's held-out AUC gain over eta = 0 and the recall difference of P1: rho = -0.11 (p = 0.115, n = 189).
