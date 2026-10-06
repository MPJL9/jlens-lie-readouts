#!/bin/bash
# Submit the extra unrelated set for one model as a chain of Slurm jobs (PLAN.md Section 2.2;
# user decision of 2026-10-01: 1,000 more filtered Alpaca prompts, none repeating the first 300).
# The user runs this on the login node; it only calls sbatch. Each job starts after the previous
# one succeeds:
#
#   sample (greedy, the extra prompts only) -> select -> forward with inline readout -> DYL probe
#
# - select runs with --must-keep-existing: it stops without writing if any transcript that is
#   already selected would change, so the finished runs stay as they are.
# - forward runs with --inline-readout: the readouts are exported straight from the forward pass
#   and the residual streams are not saved. --probe-vector keeps one small file per transcript
#   (the residual at the token before the Q9 answer, about 0.7 MB for a 27B model), so the DYL
#   probe baseline gets a score on the same transcripts. Set PROBE=0 to leave that out (then the
#   probe job is not submitted either).
# - TEMPLATE=1 adds --template-residuals: the residual streams at the template positions only
#   are kept as well (for Experiment 3's fits on unrelated chats; Qwen: about 105 MB per
#   transcript, so up to about 105 GB for 1,000). Off by default.
# - no judge: the unrelated sets are not judged.
#
# Usage:
#   MODEL=gemma-3-12b-it SMOKE=1 bash slurm/pipeline_extra.sh   # 2 prompts first, to check
#   MODEL=gemma-3-12b-it bash slurm/pipeline_extra.sh           # the full run continues from the smoke run
# Every stage skips finished work, so a job that hits the 12 h limit can be submitted again.
set -euo pipefail
cd /scratch/liucfe/jlens_redo
mkdir -p slurm/logs runs exports
: "${MODEL:?set MODEL=gemma-3-12b-it | gemma-3-27b-it | qwen3.6-27b | gpt-oss-20b}"
# refuse to submit from code or inputs that predate the push
[ "$(wc -l < inputs/unrelated_extra.jsonl 2>/dev/null || echo 0)" -eq 1000 ] \
  || { echo "inputs/unrelated_extra.jsonl is missing or not 1000 lines: run scripts/push_to_cluster.sh on the Mac first"; exit 1; }
grep -q -- "--inline-readout" src/forward.py && grep -q "def export_part" src/readout.py \
  && grep -q -- "--must-keep-existing" src/select_transcripts.py && grep -q "unrelated_extra" src/sample.py \
  || { echo "src/ on the cluster is older than this script: run scripts/push_to_cluster.sh on the Mac first"; exit 1; }
TAG=$(echo "$MODEL" | tr -c 'a-z0-9\n' '_')
[ -s "runs/$TAG/transcripts.jsonl" ] || { echo "runs/$TAG/transcripts.jsonl not found: the main run for $MODEL must exist"; exit 1; }
# the whole model goes on the GPU (forward passes), plus the lens maps (about 7 GB for a 27B model)
case "$MODEL" in
  gemma-3-27b-it|qwen3.6-27b|gpt-oss-20b) GPUREQ="${GPUREQ:---gres=gpu:1 --constraint=vr80g|vr144g}"; MEM="${MEM:-120G}" ;;
  gemma-3-12b-it) GPUREQ="${GPUREQ:---gres=gpu:l40s:1}"; MEM="${MEM:-48G}" ;;
  *) echo "unknown MODEL $MODEL"; exit 1 ;;
esac
LIMIT=""; [ -n "${SMOKE:-}" ] && LIMIT="--limit 2"
PV="--probe-vector"; [ "${PROBE:-1}" = 0 ] && PV=""
TR=""; [ "${TEMPLATE:-0}" = 1 ] && TR="--template-residuals"
GPUJOB="$GPUREQ --mem=$MEM --cpus-per-task=8"
CPUJOB="--cpus-per-task=2 --mem=8G"

sub() {   # sub <name> <resources> <dependency or ""> <script> [VAR=value ...]; prints the job id
  local name=$1 res=$2 dep="" script=$4; [ -n "$3" ] && dep="--dependency=afterok:$3"
  shift 4
  env MODEL="$MODEL" "$@" sbatch --parsable --job-name="redo_${name}_${TAG}" $res $dep --export=ALL "$script"
}
S=$(sub  xsample  "$GPUJOB" ""    slurm/sample.sh  ROUND=1 SETS=unrelated_extra EXTRA="$LIMIT")
SE=$(sub xselect  "$CPUJOB" "$S"  slurm/select.sh  EXTRA="--must-keep-existing")
FW=$(sub xforward "$GPUJOB" "$SE" slurm/forward.sh SAVE=crop EXTRA="--sets unrelated_extra --inline-readout $PV $TR $LIMIT")
echo "submitted the extra unrelated set for $MODEL (GPU request: $GPUREQ${SMOKE:+; SMOKE}${TR:+; template residuals kept}):"
if [ -n "$PV" ]; then
  DP=$(sub xprobe "--cpus-per-task=2 --mem=24G" "$FW" slurm/dyl_probe.sh)
  echo "  sample $S | select $SE | forward + readout $FW | DYL probe $DP"
else
  echo "  sample $S | select $SE | forward + readout $FW"
fi
echo "watch: squeue -u \$USER    logs: slurm/logs/redo_<stage>_${TAG}_<jobid>.err (progress) and .out"
