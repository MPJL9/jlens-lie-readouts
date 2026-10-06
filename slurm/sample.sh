#!/bin/bash
#SBATCH --job-name=redo_sample
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --output=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.out
#SBATCH --error=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.err
# stage 1: sample responses (GPU). Submitted by the user, normally through slurm/pipeline.sh,
# which sets the GPU, memory and CPU count. Rerunnable: finished work is skipped.
set -euo pipefail
source /scratch/liucfe/jlens_redo/slurm/env.sh
: "${MODEL:?set MODEL}"
echo "$(date) $SLURM_JOB_NAME MODEL=$MODEL host=$(hostname)"
python3 src/sample.py --model "$MODEL" --round "${ROUND:-1}" --sets ${SETS:-scenario nopressure unrelated} ${EXTRA:-}
