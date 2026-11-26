#!/bin/bash
# Bug-5 rerun: every seed-0 list through the corrected writer (no 512-token cap), outputs writer_fix/s0/<system>.
# Same writer settings, prompts, seed and lists as run_writer_all.sh. Progress: writer_fix_s0.progress.
cd /home/eftychia/Spectra/judge || exit 1
R=/home/eftychia/Spectra/d-spectra
export CUDA_VISIBLE_DEVICES="" OMP_NUM_THREADS=2 OPENAI_API_KEY=local HOSTED_VLLM_API_KEY=local HOSTED_VLLM_API_BASE=http://127.0.0.1:18013/v1
P=writer_fix_s0.progress; echo "writer fix started $(date +%m-%d_%H:%M)" > $P
run() {
  nice -n 19 eval-env/bin/python run_writer.py --outputs $R/outputs/dsbase_final/s0 --pools $R/pools/final_r2_s0 \
    --out writer_fix/s0/$1 ${2:+--selections $2} > logs_writerfix_$1.log 2>&1
  echo "$1 $(grep -c 'linked' logs_writerfix_$1.log) ok, $(grep -c FAILED logs_writerfix_$1.log) failed, $(grep -c 'truncated by the max_tokens' logs_writerfix_$1.log) truncated, $(date +%m-%d_%H:%M)" >> $P
}
run dsbase_rerun
for m in dspectra oracle qlink_rel usvt_cocite_rel cocite_rel relevance_only fixed_k; do run $m $R/selections/final/s0/$m.csv; done
echo "WRITERFIX DONE $(date +%m-%d_%H:%M)" >> $P
