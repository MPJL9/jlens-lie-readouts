# Sourced by every job script: paths, the Python environment, and a GPU check.
export PYTHONUNBUFFERED=1
export HF_HOME=/scratch/liucfe/hf_cache
cd /scratch/liucfe/jlens_redo
# reuses the environment built for the earlier project (torch, transformers, jlens, anthropic)
source /scratch/liucfe/jlens_lie/env/bin/activate
if [ -n "${SLURM_JOB_ID:-}" ] && [ -n "${CUDA_VISIBLE_DEVICES:-}" ]; then
  python3 -c "import torch,sys; sys.exit(not torch.cuda.is_available())" \
    || { echo "FATAL: GPU allocated but torch cannot see it"; exit 1; }
fi
