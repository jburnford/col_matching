#!/bin/bash
#SBATCH --job-name=qwen-roster
#SBATCH --account=def-jic823
#SBATCH --nodes=1
#SBATCH --gpus-per-node=h100:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=10:00:00
#SBATCH --output=/home/jic823/projects/def-jic823/qwen_roster/qwen_roster_%j.out
#SBATCH --error=/home/jic823/projects/def-jic823/qwen_roster/qwen_roster_%j.err

# ============================================================
# Qwen residue pass: extract officer records from Colonial
# Office List roster blocks the rules parser could not handle.
# vLLM serves qwen3-30b-a3b-fp8 locally; worker streams the
# worklist through it. Resumable — resubmit to continue.
# ============================================================
set -u
JOB_DIR="/home/$USER/projects/def-jic823/qwen_roster"
MODEL_DIR="/home/$USER/projects/def-jic823/models/qwen3-30b-a3b-fp8"
WHEEL_CACHE="/home/$USER/projects/def-jic823/wheel_cache"

echo "Job $SLURM_JOB_ID on $SLURMD_NODENAME"; date

module load StdEnv/2023 gcc cuda/12.6 python/3.11 arrow cudnn opencv

# HOME is over quota — keep EVERY write off /home (venv seeding, pip cache,
# triton/vllm caches, user-site fallbacks all redirected to scratch/tmpdir).
export XDG_CACHE_HOME="/scratch/$USER/.cache"
export XDG_DATA_HOME="/scratch/$USER/.local_share"
export XDG_CONFIG_HOME="/scratch/$USER/.config"
export PIP_CACHE_DIR="/scratch/$USER/.cache/pip"
export TRITON_CACHE_DIR="/scratch/$USER/.cache/triton"
export HF_HOME="/scratch/$USER/.cache/huggingface"
export VLLM_CACHE_ROOT="/scratch/$USER/.cache/vllm"
export FLASHINFER_WORKSPACE_DIR="/scratch/$USER/.cache/flashinfer"
export PYTORCH_ALLOC_CONF=expandable_segments:True
export PYTHONNOUSERSITE=1
mkdir -p "$HF_HOME" "$VLLM_CACHE_ROOT" "$FLASHINFER_WORKSPACE_DIR" \
         "$XDG_DATA_HOME" "$XDG_CONFIG_HOME" "$PIP_CACHE_DIR" "$TRITON_CACHE_DIR"

virtualenv --no-download "$SLURM_TMPDIR/venv"
if [ ! -f "$SLURM_TMPDIR/venv/bin/activate" ]; then
    echo "FATAL: venv creation failed"; exit 1
fi
source "$SLURM_TMPDIR/venv/bin/activate"
command -v python | grep -q "$SLURM_TMPDIR" || { echo "FATAL: venv python not active"; exit 1; }
pip install --no-index --upgrade pip
pip install --no-index torch transformers accelerate pybase64

# opencv stub (vllm dep not needed for text serving)
mkdir -p "$SLURM_TMPDIR/opencv_stub"
cat > "$SLURM_TMPDIR/opencv_stub/setup.py" << 'STUBEOF'
from setuptools import setup
setup(name='opencv-python-headless', version='4.11.0', py_modules=[])
STUBEOF
pip install "$SLURM_TMPDIR/opencv_stub/"
pip install --no-index "$WHEEL_CACHE/vllm-0.12.0+computecanada-cp38-abi3-linux_x86_64.whl"

echo "=== starting vLLM: $MODEL_DIR ==="
python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_DIR" \
    --served-model-name qwen3-30b-a3b \
    --port 8000 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.90 \
    --disable-log-requests \
    2>&1 | tee "$JOB_DIR/vllm_$SLURM_JOB_ID.log" &
VLLM_PID=$!

for i in $(seq 1 40); do
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        echo "vLLM ready after $((i * 30))s"; break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then echo "vLLM died"; exit 1; fi
    sleep 30
done
curl -s http://localhost:8000/health > /dev/null || { echo "vLLM never came up"; exit 1; }

echo "=== worker start ==="; date
python3 "$JOB_DIR/qwen_roster_worker.py" \
    --worklist "$JOB_DIR/qwen_worklist.jsonl" \
    --out "$JOB_DIR/qwen_roster_results.jsonl" \
    --url http://localhost:8000/v1 \
    --model qwen3-30b-a3b \
    --workers 16

echo "=== worker done ==="; date
kill $VLLM_PID 2>/dev/null
wait $VLLM_PID 2>/dev/null
echo "job complete"
