#!/bin/bash
# Every method's seed-0 list through the same writer (Qwen3-8B-AWQ, localhost:18013),
# plus DeepScholar-base's own kept lists rerun through it. One query at a time per
# method, methods in sequence; a query already written is skipped on rerun.
cd /home/eftychia/Spectra/judge || exit 1
R=/home/eftychia/Spectra/d-spectra
export CUDA_VISIBLE_DEVICES="" OMP_NUM_THREADS=2 OPENAI_API_KEY=local HOSTED_VLLM_API_KEY=local \
       HOSTED_VLLM_API_BASE=http://127.0.0.1:18013/v1
run() {  # method [selections]
  nice -n 19 eval-env/bin/python run_writer.py --outputs $R/outputs/dsbase_final/s0 --pools $R/pools/final_r2_s0 \
    --out writer/s0/$1 ${2:+--selections $2} > logs_writer_$1.log 2>&1
  echo "$1 $(grep -c 'linked' logs_writer_$1.log) ok, $(grep -c FAILED logs_writer_$1.log) failed, $(date +%m-%d_%H:%M)" >> writer_s0.progress
}
run dsbase_rerun
for m in dspectra qlink_rel usvt_cocite_rel cocite_rel relevance_only fixed_k oracle; do
  run $m $R/selections/final/s0/$m.csv
done
echo "ALL DONE $(date +%m-%d_%H:%M)" >> writer_s0.progress
