#!/bin/bash
#SBATCH --job-name=qwen-iol-nobio
#SBATCH --account=def-jic823
#SBATCH --nodes=1
#SBATCH --gpus-per-node=h100:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=3:00:00
#SBATCH --output=/home/jic823/projects/def-jic823/qwen_roster/qwen_iolnobio_%j.out
#SBATCH --error=/home/jic823/projects/def-jic823/qwen_roster/qwen_iolnobio_%j.err

# ============================================================
# No-bio dedup cycle (docs/NOBIO_DEDUP_KICKOFF.md steps 1+2):
#   wl_nobio.jsonl  ~2.0k roster-vs-roster pairs  --mode iolnobio
#     (chain_grad / chain_chain / grad_exit / chain_exit residue)
#   wl_abc.jsonl   ~12k class-C identity-vs-bio   --mode iolabc
#   wl_chain.jsonl  600 chain-coherence sample    --mode iolchain
# ~1-2h GPU after model load. Resumable — resubmit to continue.
#
# Before submitting, copy inputs up (from the col_matching root):
#   scp data/iol/identity/adjudicate/wl_nobio.jsonl \
#       data/iol/identity/adjudicate/wl_abc.jsonl \
#       nibi:~/projects/def-jic823/qwen_roster/
#   scp nibi/qwen_classc_worker.py \
#       nibi:~/projects/def-jic823/qwen_roster/
# Afterwards, fetch res_nobio.jsonl + res_abc.jsonl back into
#   data/iol/identity/adjudicate/ for the apply step.
# ============================================================
set -u
JOB_DIR="/home/$USER/projects/def-jic823/qwen_roster"
MODEL_DIR="/home/$USER/projects/def-jic823/models/qwen3-30b-a3b-fp8"
WHEEL_CACHE="/home/$USER/projects/def-jic823/wheel_cache"

echo "Job $SLURM_JOB_ID on $SLURMD_NODENAME"; date

module load StdEnv/2023 gcc cuda/12.6 python/3.11 arrow cudnn opencv

# HOME is over quota — keep EVERY write off /home.
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
# NOTE: no `| tee` — in `cmd | tee &`, $! is tee's PID and the shutdown kill
# leaves vLLM holding the GPU for the rest of the walltime.
python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_DIR" \
    --served-model-name qwen3-30b-a3b \
    --port 8000 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.90 \
    --disable-log-requests \
    > "$JOB_DIR/vllm_$SLURM_JOB_ID.log" 2>&1 &
VLLM_PID=$!

for i in $(seq 1 40); do
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        echo "vLLM ready after $((i * 30))s"; break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then echo "vLLM died"; exit 1; fi
    sleep 30
done
curl -s http://localhost:8000/health > /dev/null || { echo "vLLM never came up"; exit 1; }

echo "=== wl_nobio (--mode iolnobio) ==="; date
python3 "$JOB_DIR/qwen_classc_worker.py" \
    --worklist "$JOB_DIR/wl_nobio.jsonl" \
    --out "$JOB_DIR/res_nobio.jsonl" \
    --url http://localhost:8000/v1 \
    --model qwen3-30b-a3b \
    --mode iolnobio \
    --workers 16

echo "=== wl_abc (--mode iolabc) ==="; date
python3 "$JOB_DIR/qwen_classc_worker.py" \
    --worklist "$JOB_DIR/wl_abc.jsonl" \
    --out "$JOB_DIR/res_abc.jsonl" \
    --url http://localhost:8000/v1 \
    --model qwen3-30b-a3b \
    --mode iolabc \
    --workers 16

echo "=== wl_chain (--mode iolchain) ==="; date
python3 "$JOB_DIR/qwen_classc_worker.py" \
    --worklist "$JOB_DIR/wl_chain.jsonl" \
    --out "$JOB_DIR/res_chain.jsonl" \
    --url http://localhost:8000/v1 \
    --model qwen3-30b-a3b \
    --mode iolchain \
    --workers 16

echo "=== workers done ==="; date
kill $VLLM_PID 2>/dev/null
for i in $(seq 1 12); do
    kill -0 $VLLM_PID 2>/dev/null || break
    sleep 5
done
kill -9 $VLLM_PID 2>/dev/null
wait $VLLM_PID 2>/dev/null
echo "job complete"
