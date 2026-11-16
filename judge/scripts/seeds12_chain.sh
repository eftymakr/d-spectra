#!/bin/bash
# Seeds 1 and 2 through the writer and the judge (rules: scratchpad/seeds12_rules.md).
# Writer (Qwen, 55% of GPU 1) runs next to the sparsification fits; the judge (70B) waits for
# SPARSE DONE. Each stage skips what already exists, so the chain can be rerun.
cd /home/eftychia/Spectra/judge || exit 1
S=/tmp/claude-1019/-home-eftychia-Spectra/18196075-5232-4277-9254-16a13fe9b9fa/scratchpad
R=/home/eftychia/Spectra/d-spectra
P=seeds12.progress
echo "seeds12 started $(date +%m-%d_%H:%M)" > $P
nohup bash serve_qwen.sh > qwen_server_s12.log 2>&1 < /dev/null &
for i in $(seq 1 80); do sleep 15; curl -s -m 5 http://127.0.0.1:18013/v1/models | grep -q qwen3 && break; done
curl -s -m 5 http://127.0.0.1:18013/v1/models | grep -q qwen3 || { echo "qwen failed to start" >> $P; exit 1; }
export CUDA_VISIBLE_DEVICES="" OMP_NUM_THREADS=2 OPENAI_API_KEY=local HOSTED_VLLM_API_KEY=local \
       HOSTED_VLLM_API_BASE=http://127.0.0.1:18013/v1
for pass in 1 2; do
  for seed in 1 2; do
    for m in dsbase_rerun fixed_k relevance_only dspectra cocite_rel usvt_cocite_rel qlink_rel oracle; do
      sel=""; [ "$m" != dsbase_rerun ] && sel="--selections $R/selections/final/s$seed/$m.csv"
      nice -n 19 eval-env/bin/python run_writer.py --outputs $R/outputs/dsbase_final/s$seed --pools $R/pools/final_r2_s$seed \
        $sel --out writer/s$seed/$m > logs_writer_s${seed}_${m}_p$pass.log 2>&1
      echo "s$seed $m pass $pass: $(ls writer/s$seed/$m 2>/dev/null | wc -l) reports, $(grep -c FAILED logs_writer_s${seed}_${m}_p$pass.log) failed $(date +%m-%d_%H:%M)" >> $P
    done
  done
done
for p in $(pgrep -f "api_server --model Qwen/Qwen3-8B-AWQ"); do kill $p; done
echo "WRITER DONE $(date +%m-%d_%H:%M)" >> $P
until grep -q "SPARSE DONE" $S/sparse.progress 2>/dev/null; do sleep 300; done
sleep 30
nohup bash serve_judge.sh > vllm_s12.log 2>&1 < /dev/null &
until curl -s -m 5 http://127.0.0.1:8011/v1/models | grep -q llama; do sleep 15; done
nohup vllm-env/bin/python relay.py > relay_s12.log 2>&1 < /dev/null &
sleep 5
echo "judge up $(date +%m-%d_%H:%M)" >> $P
for seed in 1 2; do
  for m in dsbase_rerun fixed_k relevance_only dspectra cocite_rel usvt_cocite_rel qlink_rel oracle; do
    [ -f results/writer_s$seed/$m/nugget_coverage/aggregated_results.csv ] && continue
    ./run_judge.sh /home/eftychia/Spectra/judge/writer/s$seed/$m /home/eftychia/Spectra/judge/results/writer_s$seed/$m > logs_judge_s${seed}_$m.log 2>&1
    echo "s$seed $m judged exit $? $(date +%m-%d_%H:%M)" >> $P
  done
done
for p in $(pgrep -f "judge/relay.py") $(pgrep -f "Meta-Llama-3.1-70B-Instruct-GPTQ-INT4"); do kill $p; done
echo "SEEDS12 DONE $(date +%m-%d_%H:%M)" >> $P
