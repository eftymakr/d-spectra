#!/bin/bash
# E24: retry the held-out queries of the expanded arm that timed out (same settings; run_filter.py skips finished ones).
cd /home/eftychia/Spectra/judge || exit 1
R=/home/eftychia/Spectra/d-spectra
export CUDA_VISIBLE_DEVICES="" OMP_NUM_THREADS=2 OPENAI_API_KEY=local HOSTED_VLLM_API_KEY=local HOSTED_VLLM_API_BASE=http://127.0.0.1:18013/v1
for pass in 1 2; do
  nice -n 19 eval-env/bin/python run_filter.py --arm expanded --out $R/outputs/filter_expanded/s0 --rows 20 62 >> logs_e24_expanded_retry.log 2>&1
  n=$(ls -d $R/outputs/filter_expanded/s0/0[2-6][0-9]_* 2>/dev/null | wc -l)
  echo "expanded retry pass $pass: $n of 43 held-out queries done $(date +%m-%d_%H:%M)" >> e24.progress
  [ "$n" -ge 43 ] && break
done
echo "E24 DONE $(date +%m-%d_%H:%M)" >> e24.progress
