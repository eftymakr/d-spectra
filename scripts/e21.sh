#!/bin/bash
# E21: inductive citing role for cold-start queries. Rules: scratchpad/e21_rules.md.
# Waits for E20 (same GPU), then one fit per graph with the pseudo-query nodes removed,
# then the CPU stages (pseudo-query evaluation, real queries, tests).
cd /home/eftychia/Spectra/d-spectra || exit 1
S=/tmp/claude-1019/-home-eftychia-Spectra/18196075-5232-4277-9254-16a13fe9b9fa/scratchpad
until grep -q "E20 DONE" $S/e20.progress 2>/dev/null; do sleep 300; done
export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 CUDA_VISIBLE_DEVICES=1
N=6
echo "e21 started $(date +%m-%d_%H:%M)" > $S/e21.progress
for k in $(seq 0 $((N-1))); do
  nice -n 19 .venv/bin/python scripts/coldstart_e21.py --stage fit --worker $k/$N > logs/e21_fit_$k.log 2>&1 < /dev/null &
done
wait
echo "fits: $(ls results/e21/fits/*.npz | wc -l) $(date +%m-%d_%H:%M)" >> $S/e21.progress
export CUDA_VISIBLE_DEVICES="" OMP_NUM_THREADS=4
nice -n 19 .venv/bin/python scripts/coldstart_e21.py --stage eval > logs/e21_eval.log 2>&1
nice -n 19 .venv/bin/python scripts/coldstart_e21.py --stage real > logs/e21_real.log 2>&1
nice -n 19 .venv/bin/python scripts/coldstart_e21.py --stage tests > logs/e21_tests.log 2>&1
echo "E21 DONE $(date +%m-%d_%H:%M)" >> $S/e21.progress
