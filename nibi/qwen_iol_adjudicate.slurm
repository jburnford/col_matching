#!/bin/bash
#SBATCH --job-name=qwen-iol-adjudicate
#SBATCH --account=def-jic823
#SBATCH --nodes=1
#SBATCH --gpus-per-node=h100:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=1:00:00
#SBATCH --output=/home/jic823/projects/def-jic823/qwen_roster/qwen_ioladj_%j.out
#SBATCH --error=/home/jic823/projects/def-jic823/qwen_roster/qwen_ioladj_%j.err

# ============================================================
# IOL consolidated adjudication batch (docs/IOL_NEXT_SESSION.md
# items 1+3): all pending pools in one job —
#   wl_dedup.jsonl   15   A6 under-merge pairs      --mode ioldedup
#   wl_exit.jsonl   547   A7 + exit-ambiguous       --mode iolexit
#   wl_roll.jsonl    32   honours-roll conflicts    --mode iolroll
#   wl_birth.jsonl   94   ambiguous birth repairs   --mode iolbirth
#   wl_civil.jsonl 2213   civil-list residue        (parse worker)
# ~2.9k prompts total; minutes of GPU after model load.
# Resumable — resubmit to continue.
#
# Before submitting, copy inputs up (from the col_matching root):
#   scp data/iol/identity/adjudicate/wl_*.jsonl \
#       nibi:~/projects/def-jic823/qwen_roster/
#   scp nibi/qwen_classc_worker.py nibi/qwen_civil_parse_worker.py \
#       nibi:~/projects/def-jic823/qwen_roster/
# Afterwards, fetch res_*.jsonl back into
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

run_pool () {  # run_pool <wl-basename> <mode>
    local wl="$1" mode="$2"
    [ -s "$JOB_DIR/${wl}.jsonl" ] || { echo "SKIP $wl (missing)"; return; }
    echo "=== $wl (--mode $mode) ==="; date
    python3 "$JOB_DIR/qwen_classc_worker.py" \
        --worklist "$JOB_DIR/${wl}.jsonl" \
        --out "$JOB_DIR/${wl/wl_/res_}.jsonl" \
        --url http://localhost:8000/v1 \
        --model qwen3-30b-a3b \
        --mode "$mode" \
        --workers 16
}

run_pool wl_dedup ioldedup
run_pool wl_exit  iolexit
run_pool wl_roll  iolroll
run_pool wl_birth iolbirth

if [ -s "$JOB_DIR/wl_civil.jsonl" ]; then
    echo "=== wl_civil (parse worker) ==="; date
    python3 "$JOB_DIR/qwen_civil_parse_worker.py" \
        --worklist "$JOB_DIR/wl_civil.jsonl" \
        --out "$JOB_DIR/res_civil.jsonl" \
        --url http://localhost:8000/v1 \
        --model qwen3-30b-a3b \
        --workers 16
fi

echo "=== workers done ==="; date
kill $VLLM_PID 2>/dev/null
for i in $(seq 1 12); do
    kill -0 $VLLM_PID 2>/dev/null || break
    sleep 5
done
kill -9 $VLLM_PID 2>/dev/null
wait $VLLM_PID 2>/dev/null
echo "job complete"
