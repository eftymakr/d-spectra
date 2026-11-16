#!/bin/bash
# Writer backbone: Qwen3-8B-AWQ on vLLM 0.8.5 (torch 2.6 cu124), GPU 1, localhost only,
# 35% of the card so the fit workers keep running next to it.
cd /home/eftychia/Spectra/judge || exit 1
export CUDA_VISIBLE_DEVICES=1 OMP_NUM_THREADS=4 HF_HUB_ENABLE_HF_TRANSFER=0
uv pip install --python qwen-env/bin/python "transformers==4.51.3" "huggingface_hub<1" || exit 1
qwen-env/bin/python -c "from huggingface_hub import snapshot_download; print(snapshot_download('Qwen/Qwen3-8B-AWQ'))" || exit 1
nice -n 10 qwen-env/bin/python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen3-8B-AWQ \
  --served-model-name qwen3-8b-awq openai/qwen3-8b-awq hosted_vllm/qwen3-8b-awq \
  --host 127.0.0.1 --port 18013 --max-model-len 32768 --gpu-memory-utilization 0.35 \
  --max-num-seqs 16 --disable-log-requests > qwen_server.log 2>&1 &
for i in $(seq 1 60); do sleep 10; curl -s http://127.0.0.1:18013/v1/models | grep -q qwen3 && break; done
curl -s http://127.0.0.1:18013/v1/chat/completions -H "Content-Type: application/json" -d '{"model":"qwen3-8b-awq","messages":[{"role":"user","content":"Say OK."}],"max_tokens":20,"chat_template_kwargs":{"enable_thinking":false}}'
echo; echo "SERVER UP $(date +%m-%d_%H:%M)"
