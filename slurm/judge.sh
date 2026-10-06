#!/bin/bash
#SBATCH --job-name=redo_judge
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --output=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.out
#SBATCH --error=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.err
# stage 2: LLM judge (CPU + Anthropic API). Submitted by the user, normally through slurm/pipeline.sh,
# which sets the GPU, memory and CPU count. Rerunnable: finished work is skipped.
set -euo pipefail
source /scratch/liucfe/jlens_redo/slurm/env.sh
: "${MODEL:?set MODEL}"
echo "$(date) $SLURM_JOB_NAME MODEL=$MODEL host=$(hostname)"
[ -f "$HOME/.anthropic_env" ] || { echo "FATAL: ~/.anthropic_env not found"; exit 1; }
source "$HOME/.anthropic_env"
python3 -c "import anthropic" || { echo "FATAL: the anthropic package is not installed in the environment"; exit 1; }
python3 src/judge.py --model "$MODEL" --pass "${PASS:-first}" ${EXTRA:-}
