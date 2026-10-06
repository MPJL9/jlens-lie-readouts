#!/bin/bash
# Copy the code and the model inputs to the cluster. The user runs this on the Mac.
# Never deletes anything on the cluster, and never touches runs/, exports/ or slurm/logs/.
# Needs the SSH control connection: ssh -o ControlMaster=auto -o ControlPersist=8h \
#   -o ControlPath=/tmp/ssh-jlens_mm liucfe@andromeda.bc.edu true
set -euo pipefail
cd "$(dirname "$0")/.."
SOCK=${SOCK:-/tmp/ssh-jlens_mm}
DEST=liucfe@andromeda.bc.edu:/scratch/liucfe/jlens_redo/
ssh -o ControlPath="$SOCK" liucfe@andromeda.bc.edu "mkdir -p /scratch/liucfe/jlens_redo/slurm/logs"
rsync -avz -e "ssh -o ControlPath=$SOCK" \
  --exclude="__pycache__/" --exclude=".DS_Store" --exclude="slurm/logs/" \
  src slurm inputs "$DEST"
