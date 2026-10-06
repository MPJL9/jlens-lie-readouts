#!/bin/bash
# Download the released data into data/cluster/ (the layout the scripts expect). Needs the huggingface_hub
# package: pip install -U huggingface_hub
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p data/cluster
hf download Sakarein/jlens-lie-readouts --repo-type dataset --local-dir data/cluster
python3 - <<'PY'
import json, os
root = "data/cluster/exports"
models = sorted(d for d in os.listdir(root) if os.path.exists(os.path.join(root, d, "manifest.json")))
json.dump(models, open(os.path.join(root, "index.json"), "w"))
print("models with exports:", models)
PY
