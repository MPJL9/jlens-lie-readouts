#!/bin/bash
#SBATCH --job-name=redo_exp3_cut
#SBATCH --partition=short
#SBATCH --time=03:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --output=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.out
#SBATCH --error=/scratch/liucfe/jlens_redo/slurm/logs/%x_%j.err
# Experiment 3, data step (PLAN.md Section 7): cut the cached residual streams at the template
# positions of a list built by scripts/exp3/build_cut_list.py, at a few band layers (CPU, no GPU).
# Submitted by the user:
#   MODEL=qwen3.6-27b LAYERS="35 41 47 53 58" sbatch --export=ALL slurm/exp3_cut.sh
#   MODEL=gemma-3-12b-it LAYERS="17 23 29 35 40" LIST=inputs/exp3_cut_list_gemma_3_12b_it.jsonl DTYPE=float32 sbatch --export=ALL slurm/exp3_cut.sh
#   MODEL=gemma-3-27b-it LAYERS="27 33 39 46 52" LIST=inputs/exp3_cut_list_gemma_3_27b_it.jsonl DTYPE=float32 sbatch --export=ALL slurm/exp3_cut.sh
#   MODEL=qwen3.6-27b LAYERS="35 41 47 50 53 58" LIST=inputs/exp3_cut_list_last.jsonl OUT=exp3_last sbatch --export=ALL slurm/exp3_cut.sh
#   MODEL=qwen3.6-27b LAYERS="50" LIST=inputs/exp3_cut_list_layer50.jsonl OUT=exp3_layer50 sbatch --export=ALL slurm/exp3_cut.sh
#   MODEL=qwen3.6-27b LAYERS="47 50" LIST=inputs/exp3_cut_list_postans.jsonl OUT=exp3_postans sbatch --export=ALL slurm/exp3_cut.sh
# The fourth line cuts the last token before the self-report answer (build_cut_list.py --last) into
# runs/<model>/exp3_last/ (about 0.35 GB); the fifth (2026-10-05) cuts the newline after the response on both
# splits and the newline after the Q9 answer on the build split at layer 50 only (build_cut_list.py --layer50,
# a few MB); the sixth (2026-10-05) cuts the answer token and the tokens around it under Q9 on both splits at
# layers 47 and 50 (build_cut_list.py --postans, about 30 MB). OUT defaults to exp3.
# LIST defaults to the list of Qwen. DTYPE defaults to float16; Gemma needs float32 (its residual
# stream has values above 65,000). Writes runs/<model>/exp3/ (Qwen about 1.5 GB, Gemma-12B 0.8 GB,
# Gemma-27B 1.2 GB). One model per job. Rerunnable: a finished set is skipped. Progress goes
# to .err; the last line of .out is "CUT DONE: ...".
set -euo pipefail
source /scratch/liucfe/jlens_redo/slurm/env.sh
: "${MODEL:?set MODEL}"
: "${LAYERS:?set LAYERS}"
echo "$(date) $SLURM_JOB_NAME MODEL=$MODEL LAYERS=$LAYERS LIST=${LIST:-inputs/exp3_cut_list.jsonl} DTYPE=${DTYPE:-float16} OUT=${OUT:-exp3} host=$(hostname)"
python3 src/cut_positions.py --model "$MODEL" --layers $LAYERS --list "${LIST:-inputs/exp3_cut_list.jsonl}" --dtype "${DTYPE:-float16}" --out "${OUT:-exp3}"
