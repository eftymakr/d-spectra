#!/bin/bash
# Writer backbone: Qwen3-8B-AWQ on vLLM 0.8.5, GPU 1, localhost:18013, 35% of the card.
cd /home/eftychia/Spectra/judge || exit 1
export CUDA_VISIBLE_DEVICES=1 OMP_NUM_THREADS=4
exec nice -n 10 qwen-env/bin/python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen3-8B-AWQ \
  --served-model-name qwen3-8b-awq openai/qwen3-8b-awq hosted_vllm/qwen3-8b-awq \
  --host 127.0.0.1 --port 18013 --max-model-len 24576 --gpu-memory-utilization 0.55 \
  --max-num-seqs 16 --disable-log-requests
