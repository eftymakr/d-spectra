#!/bin/bash
# E20: held-out citation AUC at rank caps 64 and 128 (SPECTRA's rank-cap-binding
# criterion: does link prediction improve with the cap?). E9 already has the eta = 0 and
# d_ev = 8 fits and the recall at these caps (unchanged); only the held-out-link fits
# (cv: the 7-eta grid without 10% of citations) are new. Rules: scratchpad/e19_e20_rules.md.
# Waits for the judge repair chain so the fits do not share GPU 1 with the 70B judge.
cd /home/eftychia/Spectra/d-spectra || exit 1
S=/tmp/claude-1019/-home-eftychia-Spectra/18196075-5232-4277-9254-16a13fe9b9fa/scratchpad
until grep -q "CHAIN4 DONE" /home/eftychia/Spectra/judge/e18.progress; do sleep 300; done
export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 CUDA_VISIBLE_DEVICES=1
P=pools/final_r2_s0; G=data/graphs_small; N=6
echo "e20 started $(date +%m-%d_%H:%M)" > $S/e20.progress
for r in 64 128; do
  for k in $(seq 0 $((N-1))); do
    nice -n 19 .venv/bin/python scripts/fit_variants.py --pools $P --graphs $G --worker $k/$N --out results/e20_r$r \
      --rank $r --fits cv > logs/e20_r${r}_$k.log 2>&1 < /dev/null &
  done
  wait
  echo "r=$r: $(ls results/e20_r$r/operators | grep -c '^[0-9.]*json$') fits $(date +%m-%d_%H:%M)" >> $S/e20.progress
done
echo "E20 DONE $(date +%m-%d_%H:%M)" >> $S/e20.progress
