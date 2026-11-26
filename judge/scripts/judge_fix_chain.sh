#!/bin/bash
# After the corrected writer rerun and E24: swap Qwen for the Llama-70B judge on GPU 1 and judge the
# corrected seed-0 reports (held-out rows 20-62), same judge and patch as Nov 2-6, plus document
# importance (d-spectra/rules/docimp_rules.md). Progress: judge_fix.progress, ends with JUDGEFIX DONE.
cd /home/eftychia/Spectra/judge || exit 1
P=judge_fix.progress
until grep -q "WRITERFIX DONE" writer_fix_s0.progress 2>/dev/null && grep -q "E24 DONE" e24.progress 2>/dev/null; do sleep 300; done
for p in $(pgrep -f "api_server --model Qwen/Qwen3-8B-AWQ"); do kill $p; done
sleep 30
echo "writer stopped: $(nvidia-smi --query-gpu=memory.used --format=csv,noheader -i 1) $(date +%m-%d_%H:%M)" > $P
nohup bash serve_judge.sh > vllm_fix.log 2>&1 < /dev/null &
n=0; until curl -s -m 5 http://127.0.0.1:8011/v1/models | grep -q llama; do sleep 15; n=$((n+1)); [ $n -gt 120 ] && { echo "JUDGE SERVER FAILED TO START $(date +%m-%d_%H:%M)" >> $P; exit 1; }; done
pgrep -f "relay.py" > /dev/null || { nohup vllm-env/bin/python relay.py > relay_fix.log 2>&1 < /dev/null & sleep 5; }
echo "judge up $(date +%m-%d_%H:%M)" >> $P
judge() { EVALS="nugget_coverage reference_coverage cite_p claim_coverage coverage_relevance_rate document_importance" \
            ./run_judge.sh /home/eftychia/Spectra/judge/writer_fix/s0/$1 /home/eftychia/Spectra/judge/results/writerfix_s0/$1 $(seq 20 62) > logs_judgefix_$1.log 2>&1
          echo "$1 judged exit $? ($(grep -c 'Error fetching citation count' logs_judgefix_$1.log) failed OpenAlex lookups) $(date +%m-%d_%H:%M)" >> $P; }
for group in "dsbase_rerun dspectra oracle" "qlink_rel usvt_cocite_rel cocite_rel" "relevance_only fixed_k"; do
  for m in $group; do judge $m & done
  wait
done
for p in $(pgrep -f "Meta-Llama-3.1-70B-Instruct-GPTQ-INT4"); do kill $p; done
echo "JUDGEFIX DONE $(date +%m-%d_%H:%M)" >> $P
