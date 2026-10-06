#!/bin/bash
#SBATCH --job-name=redo_readout
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --output=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.out
#SBATCH --error=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.err
# stage 5: J-lens and logit-lens readouts (GPU). Submitted by the user, normally through slurm/pipeline.sh,
# which sets the GPU, memory and CPU count. Rerunnable: finished work is skipped.
set -euo pipefail
source /scratch/liucfe/jlens_redo/slurm/env.sh
: "${MODEL:?set MODEL}"
echo "$(date) $SLURM_JOB_NAME MODEL=$MODEL host=$(hostname)"
python3 src/readout.py --model "$MODEL" ${EXTRA:-}
