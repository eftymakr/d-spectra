#!/bin/bash
# E23 (rules/e23_sparse_selection_rules.md): d8 / eta0 / cv fits on the 63 seed-0 graphs with half
# of the citations kept, three thinnings (edge seeds 0-2), then the selection evaluation. GPU 1.
# Progress: logs/e23.progress, ends with "E23 DONE".
cd /home/eftychia/Spectra/d-spectra || exit 1
export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 CUDA_VISIBLE_DEVICES=1
P=pools/final_r2_s0; G=data/graphs_small; N=9; PR=logs/e23.progress
echo "e23 started $(date +%m-%d_%H:%M)" > $PR
for es in 0 1 2; do
  for k in $(seq 0 $((N-1))); do
    nice -n 19 .venv/bin/python scripts/fit_variants.py --pools $P --graphs $G --worker $k/$N --out results/e23_k50_e$es \
      --fits d8 eta0 cv --edge_keep 0.5 --edge_seed $es > logs/e23_e${es}_$k.log 2>&1 < /dev/null &
  done
  wait
  echo "edge_seed=$es: $(ls results/e23_k50_e$es/operators | grep -c '^[0-9.]*json$') fits $(date +%m-%d_%H:%M)" >> $PR
done
nice -n 19 .venv/bin/python scripts/sparse_select_e23.py --operators results/e23_k50_e0 results/e23_k50_e1 results/e23_k50_e2 \
  --edge_keep 0.5 --out results/e23 > logs/e23_eval.log 2>&1 && echo "evaluated" >> $PR || echo "EVAL FAILED" >> $PR
echo "E23 DONE $(date +%m-%d_%H:%M)" >> $PR
