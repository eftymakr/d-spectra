#!/bin/bash
# Document importance for the seed-0 systems (d-spectra/rules/docimp_rules.md). No GPU, no judge model.
cd /home/eftychia/Spectra/judge || exit 1
P=docimp.progress; echo "docimp started $(date +%m-%d_%H:%M)" > $P
for m in dsbase_rerun dspectra usvt_cocite_rel qlink_rel cocite_rel relevance_only fixed_k oracle; do
  EVALS=document_importance ./run_judge.sh /home/eftychia/Spectra/judge/writer/s0/$m /home/eftychia/Spectra/judge/results/docimp_s0/$m > logs_docimp_$m.log 2>&1
  echo "$m: $(grep -c 429 logs_docimp_$m.log) lines with 429, $(tail -n +2 results/docimp_s0/$m/document_importance/deepscholar_base.csv 2>/dev/null | wc -l) queries $(date +%m-%d_%H:%M)" >> $P
done
echo "DOCIMP DONE $(date +%m-%d_%H:%M)" >> $P
