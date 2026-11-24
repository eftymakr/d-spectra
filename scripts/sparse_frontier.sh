#!/bin/bash
# Sparsification frontier (scratchpad/sparse_rules.md): the cv fits' eta grid refitted on the
# 63 graphs with 50%, 25% and 10% of the citations kept. GPU 1, next to the writer (the judge
# chain waits for SPARSE DONE before starting the 70B).
cd /home/eftychia/Spectra/d-spectra || exit 1
S=/tmp/claude-1019/-home-eftychia-Spectra/18196075-5232-4277-9254-16a13fe9b9fa/scratchpad
export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 CUDA_VISIBLE_DEVICES=1
P=pools/final_r2_s0; G=data/graphs_small; N=6
echo "sparse started $(date +%m-%d_%H:%M)" > $S/sparse.progress
for keep in 0.5 0.25 0.1; do
  tag=$(python3 -c "print(int($keep*100))")
  for k in $(seq 0 $((N-1))); do
    nice -n 19 .venv/bin/python scripts/fit_variants.py --pools $P --graphs $G --worker $k/$N --out results/sparse_k$tag \
      --fits cv --edge_keep $keep > logs/sparse_k${tag}_$k.log 2>&1 < /dev/null &
  done
  wait
  echo "keep=$keep: $(ls results/sparse_k$tag/operators | grep -c '^[0-9.]*json$') fits $(date +%m-%d_%H:%M)" >> $S/sparse.progress
done
echo "SPARSE DONE $(date +%m-%d_%H:%M)" >> $S/sparse.progress
