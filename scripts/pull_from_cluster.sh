#!/bin/bash
# Pull the generated data to data/cluster/ on the Mac. The user runs this.
# Brings: the readout exports (for the viewer and the analysis) and the small run files
# (samples, judge verdicts, transcripts, sequences, summaries). Never the whole residual streams;
# only Experiment 3's cut at a few template positions and layers (runs/<model>/exp3/*.npy, about
# 1.5 GB, written by slurm/exp3_cut.sh).
set -euo pipefail
cd "$(dirname "$0")/.."
SOCK=${SOCK:-/tmp/ssh-jlens_mm}
SRC=liucfe@andromeda.bc.edu:/scratch/liucfe/jlens_redo
mkdir -p data/cluster/runs data/cluster/exports
rsync -avz -e "ssh -o ControlPath=$SOCK" --exclude="cache/" --include="*/" --include="*.jsonl" --include="*.json" \
  --include="exp3*/*.npy" --exclude="*" --prune-empty-dirs "$SRC/runs/" data/cluster/runs/
rsync -avz -e "ssh -o ControlPath=$SOCK" "$SRC/exports/" data/cluster/exports/
python3 - <<'PY'
import json, os
root = "data/cluster/exports"
models = sorted(d for d in os.listdir(root) if os.path.exists(os.path.join(root, d, "manifest.json")))
json.dump(models, open(os.path.join(root, "index.json"), "w"))
print("models with exports:", models)
PY
