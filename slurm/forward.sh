#!/bin/bash
#SBATCH --job-name=redo_forward
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --output=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.out
#SBATCH --error=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.err
# stage 4: self-report answers and residual streams (GPU). Submitted by the user, normally through slurm/pipeline.sh,
# which sets the GPU, memory and CPU count. Rerunnable: finished work is skipped.
set -euo pipefail
source /scratch/liucfe/jlens_redo/slurm/env.sh
: "${MODEL:?set MODEL}"
echo "$(date) $SLURM_JOB_NAME MODEL=$MODEL host=$(hostname)"
python3 src/forward.py --model "$MODEL" --save "${SAVE:?set SAVE=full or crop}" ${EXTRA:-}
