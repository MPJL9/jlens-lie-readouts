#!/bin/bash
#SBATCH --job-name=redo_dyl_probe
#SBATCH --partition=short
#SBATCH --time=03:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=24G
#SBATCH --output=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.out
#SBATCH --error=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.err
# DYL probe baseline (PLAN.md Section 5.8): AISI's released probe applied offline to the cached
# residual streams (CPU, no GPU). One job per model, submitted by the user:
#   MODEL=qwen3.6-27b sbatch --job-name=redo_dyl_probe_qwen3_6_27b --export=ALL slurm/dyl_probe.sh
# Rerunnable: rows already in runs/<model>/dyl_probe.jsonl are skipped. Progress goes to .err.
set -euo pipefail
source /scratch/liucfe/jlens_redo/slurm/env.sh
: "${MODEL:?set MODEL}"
echo "$(date) $SLURM_JOB_NAME MODEL=$MODEL host=$(hostname)"
python3 src/dyl_probe.py --model "$MODEL" ${EXTRA:-}
