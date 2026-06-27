#!/bin/bash
# Serve Qwen3.6-35B-A3B (Q4_K_XL GGUF) via llama.cpp on a nibi H100, exposing an
# OpenAI-compatible endpoint on :8003. Tunnel from the workstation with
#   ssh -N -L 8003:<SERVE_NODE>:8003 nibi
# then drive kg_structure_corpus.py --base-url http://127.0.0.1:8003/v1 locally.
#SBATCH --account=def-jic823
#SBATCH --job-name=qwen-serve
#SBATCH --gres=gpu:h100:1
#SBATCH --cpus-per-task=12
#SBATCH --mem=64G
#SBATCH --time=01:00:00
#SBATCH --output=%x-%j.out

module load apptainer/1.4.5

GGUF="$HOME/projects/def-jic823/models/qwen3.6-35b-a3b/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf"
SIF="$HOME/projects/def-jic823/containers/llama-cpp-server-cuda.sif"

echo "SERVE_NODE=$(hostname -s)"
echo "SERVE_NODE_FQDN=$(hostname -f)"
echo "GGUF=$GGUF"
nvidia-smi -L

# Use `apptainer run` (image entrypoint = /app/llama-server) with LD_LIBRARY_PATH
# set so the binary finds its libs in /app (exec didn't apply the image env).
# --jinja enables the GGUF chat template incl. chat_template_kwargs
# (so the structuring client's enable_thinking=false is honoured).
# --cont-batching + --parallel 8 = throughput for the concurrent worker pool.
apptainer run --nv --env LD_LIBRARY_PATH=/app "$SIF" \
  -m "$GGUF" \
  --host 0.0.0.0 --port 8003 \
  --n-gpu-layers 999 \
  --flash-attn on \
  --ctx-size 49152 \
  --parallel 16 --cont-batching \
  --batch-size 4096 --ubatch-size 1024 \
  --jinja \
  --threads 12 \
  --alias qwen3.6-35b-a3b
