#!/bin/bash
#SBATCH --job-name=redo_check
#SBATCH --partition=short
#SBATCH --time=00:20:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --output=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.out
#SBATCH --error=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.err
# Check the environment before the first run. Submitted by the user:
#   sbatch slurm/check_env.sh                                   # CPU only
#   sbatch --gres=gpu:1 --constraint="vr80g|vr144g" slurm/check_env.sh   # also checks a GPU
# Read the result: cat slurm/logs/redo_check_<jobid>.out
set -euo pipefail
source /scratch/liucfe/jlens_redo/slurm/env.sh
[ -f "$HOME/.anthropic_env" ] && source "$HOME/.anthropic_env" || echo "note: ~/.anthropic_env not found"
python3 src/check_env.py ${EXTRA:-}
