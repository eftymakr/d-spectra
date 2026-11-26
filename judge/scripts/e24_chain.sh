#!/bin/bash
# E24 (d-spectra/rules/e24_llm_filter_rules.md): the baseline's filter on the pool (replication) and on the expanded graph.
cd /home/eftychia/Spectra/judge || exit 1
R=/home/eftychia/Spectra/d-spectra
export CUDA_VISIBLE_DEVICES="" OMP_NUM_THREADS=2 OPENAI_API_KEY=local HOSTED_VLLM_API_KEY=local HOSTED_VLLM_API_BASE=http://127.0.0.1:18013/v1
P=e24.progress; echo "e24 started $(date +%m-%d_%H:%M)" > $P
run() {  # arm first last
  nice -n 19 eval-env/bin/python run_filter.py --arm $1 --out $R/outputs/filter_$1/s0 --rows $2 $3 >> logs_e24_$1.log 2>&1
  echo "$1 rows $2-$3: $(ls $R/outputs/filter_$1/s0 2>/dev/null | wc -l) queries done, $(grep -c FAILED logs_e24_$1.log) failed, $(grep -c 'truncated by the max_tokens' logs_e24_$1.log) truncated, $(date +%m-%d_%H:%M)" >> $P
}
run pool 20 62; run expanded 20 62; run pool 0 19; run expanded 0 19
echo "E24 DONE $(date +%m-%d_%H:%M)" >> $P
