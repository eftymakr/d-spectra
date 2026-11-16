#!/bin/bash
# DeepScholar-Bench judge with the local Llama-3.1-70B (via the localhost relay on 18012).
# usage: [EVALS="nugget_coverage ..."] run_judge.sh <input folder> <output folder> [file ids...]
# EVALS (optional) limits the run to those metrics (--evals), e.g. to redo one that failed.
IN=$1; OUT=$2; shift 2
cd /home/eftychia/Spectra/deepscholar-bench || exit 1
export NUGGETIZER_TIMEOUT=1800 LOTUS_LM_TIMEOUT=1800  # local 70B on a shared GPU is slower than the API
export OPENALEX_API_KEY=$(grep "^OPENALEX_API_KEY=" /home/eftychia/Spectra/d-spectra/.env | cut -d= -f2-)
export CUDA_VISIBLE_DEVICES="" OMP_NUM_THREADS=2 OPENAI_API_KEY=local HOSTED_VLLM_API_KEY=local \
       OPENAI_BASE_URL=http://127.0.0.1:18012/v1 HOSTED_VLLM_API_BASE=http://127.0.0.1:18012/v1
exec nice -n 19 /home/eftychia/Spectra/judge/eval-env/bin/python -m eval.main --modes deepscholar_base \
  --input-folder "$IN" --model-name hosted_vllm/llama-3.1-70b-instruct --output-folder "$OUT" \
  ${EVALS:+--evals $EVALS} ${1:+--file-id "$@"}
