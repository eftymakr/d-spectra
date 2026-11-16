#!/bin/bash
# Judge every writer output of seed 0: pause the depth-2 d_ev = 8 fits, swap the
# Qwen writer for the Llama-70B judge on GPU 1, judge 9 systems (3 at a time),
# then stop the judge and resume the depth-2 fits.
cd /home/eftychia/Spectra/judge || exit 1
S=/tmp/claude-1019/-home-eftychia-Spectra/18196075-5232-4277-9254-16a13fe9b9fa/scratchpad
for p in $(pgrep -f "scratchpad/e17_depth2.sh") $(pgrep -f "fit_variants.py.*e17_d2_d8"); do kill $p; done
for p in $(pgrep -f "api_server --model Qwen/Qwen3-8B-AWQ"); do kill $p; done
sleep 20
echo "paused fits, stopped writer: $(nvidia-smi --query-gpu=memory.used --format=csv,noheader -i 1) $(date +%m-%d_%H:%M)" > judge_chain.progress
nohup bash serve_judge.sh > vllm.log 2>&1 < /dev/null &
until curl -s -m 5 http://127.0.0.1:8011/v1/models | grep -q llama; do sleep 15; done
nohup vllm-env/bin/python relay.py > relay.log 2>&1 < /dev/null &
sleep 5
echo "judge up $(date +%m-%d_%H:%M)" >> judge_chain.progress
judge() { ./run_judge.sh /home/eftychia/Spectra/judge/writer/s0/$1 /home/eftychia/Spectra/judge/results/writer_s0/$1 > logs_judge_$1.log 2>&1
          echo "$1 judged exit $? $(date +%m-%d_%H:%M)" >> judge_chain.progress; }
for group in "dsbase_rerun dspectra oracle" "qlink_rel usvt_cocite_rel scocite_rel" "cocite_rel relevance_only fixed_k"; do
  for m in $group; do judge $m & done
  wait
done
for p in $(pgrep -f "judge/relay.py") $(pgrep -f "Meta-Llama-3.1-70B-Instruct-GPTQ-INT4"); do kill $p; done
sleep 20
echo "JUDGE DONE $(date +%m-%d_%H:%M)" >> judge_chain.progress
(nohup bash $S/e17_d8.sh > /home/eftychia/Spectra/d-spectra/logs/e17_d8_chain.log 2>&1 < /dev/null &)
echo "depth-2 d8 fits resumed $(date +%m-%d_%H:%M)" >> judge_chain.progress
