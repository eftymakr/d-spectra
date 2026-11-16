#!/bin/bash
# Local judge: Llama-3.1-70B-Instruct (GPTQ 4-bit) behind an OpenAI-compatible API,
# GPU 1 only, localhost only. Memory capped at 90% of the card so the fit workers fit.
cd /home/eftychia/Spectra/judge || exit 1
export CUDA_VISIBLE_DEVICES=1 OMP_NUM_THREADS=4
exec nice -n 10 vllm-env/bin/python -m vllm.entrypoints.openai.api_server \
  --model hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4 \
  --served-model-name llama-3.1-70b-instruct openai/llama-3.1-70b-instruct hosted_vllm/llama-3.1-70b-instruct \
  --host 127.0.0.1 --port 8011 \
  --max-model-len 12288 --gpu-memory-utilization 0.91 --kv-cache-dtype fp8 \
  --max-num-seqs 8 --disable-log-requests
