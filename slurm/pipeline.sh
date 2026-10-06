#!/bin/bash
# Submit the whole data-generation pipeline for one model as a chain of Slurm jobs.
# The user runs this on the login node; it only calls sbatch. Each job starts after the
# previous one succeeds:
#
#   sample (round 1) -> judge -> sample (round 2, top-up) -> judge the new samples
#     -> judge second pass -> select -> forward -> readout
#
# Usage:
#   MODEL=qwen3.6-27b bash slurm/pipeline.sh
#   MODEL=qwen3.6-27b SMOKE=1 bash slurm/pipeline.sh     # 2 items per set first, to check
#   MODEL=gemma-3-27b-it GPUREQ="--gres=gpu:h200:1" bash slurm/pipeline.sh   # force one GPU type
#   MODEL=qwen3.6-27b JUDGE_EXTRA="--no-fallback" bash slurm/pipeline.sh   # judge options
#
# A smoke run is a valid start of the full run: rerunning without SMOKE continues from it.
set -euo pipefail
cd /scratch/liucfe/jlens_redo
mkdir -p slurm/logs runs exports
: "${MODEL:?set MODEL=gemma-3-12b-it | gemma-3-27b-it | qwen3.6-27b | gpt-oss-20b}"
# 27B models and gpt-oss-20b (bf16 weights ~40 GB) need an 80 GB+ card: A100-80GB or H200
case "$MODEL" in
  gemma-3-27b-it|qwen3.6-27b|gpt-oss-20b) GPUREQ="${GPUREQ:---gres=gpu:1 --constraint=vr80g|vr144g}"; MEM="${MEM:-120G}" ;;
  gemma-3-12b-it) GPUREQ="${GPUREQ:---gres=gpu:l40s:1}"; MEM="${MEM:-48G}" ;;
  *) echo "unknown MODEL $MODEL"; exit 1 ;;
esac
SAVE=crop; [ "$MODEL" = qwen3.6-27b ] && SAVE=full     # whole-transcript residuals for Qwen only
LIMIT=""; [ -n "${SMOKE:-}" ] && LIMIT="--limit 2"
TAG=$(echo "$MODEL" | tr -c 'a-z0-9\n' '_')
GPUJOB="$GPUREQ --mem=$MEM --cpus-per-task=8"
CPUJOB="--cpus-per-task=2 --mem=8G"

sub() {   # sub <name> <resources> <dependency or ""> <script> [VAR=value ...]; prints the job id
  local name=$1 res=$2 dep="" script=$4; [ -n "$3" ] && dep="--dependency=afterok:$3"
  shift 4
  env MODEL="$MODEL" "$@" sbatch --parsable --job-name="redo_${name}_${TAG}" $res $dep --export=ALL "$script"
}
S1=$(sub sample1 "$GPUJOB" ""    slurm/sample.sh  ROUND=1 EXTRA="$LIMIT")
J1=$(sub judge1  "$CPUJOB" "$S1" slurm/judge.sh   PASS=first  EXTRA="${JUDGE_EXTRA:-}")
S2=$(sub sample2 "$GPUJOB" "$J1" slurm/sample.sh  ROUND=2 SETS=scenario)
J2=$(sub judge2  "$CPUJOB" "$S2" slurm/judge.sh   PASS=first  EXTRA="${JUDGE_EXTRA:-}")
J3=$(sub judge3  "$CPUJOB" "$J2" slurm/judge.sh   PASS=second EXTRA="${JUDGE_EXTRA:-}")
SE=$(sub select  "$CPUJOB" "$J3" slurm/select.sh)
FW=$(sub forward "$GPUJOB" "$SE" slurm/forward.sh SAVE=$SAVE EXTRA="$LIMIT")
RO=$(sub readout "$GPUJOB" "$FW" slurm/readout.sh)
echo "submitted for $MODEL (GPU request: $GPUREQ; residuals $SAVE${SMOKE:+; SMOKE}):"
echo "  sample1 $S1 | judge1 $J1 | sample2 $S2 | judge2 $J2 | judge3 $J3 | select $SE | forward $FW | readout $RO"
echo "watch: squeue -u \$USER    logs: slurm/logs/redo_<stage>_${TAG}_<jobid>.out"
