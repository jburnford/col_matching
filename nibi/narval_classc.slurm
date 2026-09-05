#!/bin/bash
#SBATCH --account=def-jic823_gpu
#SBATCH --job-name=classc-delta
#SBATCH --gres=gpu:a100:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=3:00:00
#SBATCH --output=%x-%j.out
#
# Class-C adjudication on Narval with Qwen3.8-27B-FP8 served by the canada50
# vLLM container (twin of canada50/Canada50/cluster/narval_qwen38.slurm).
# Staging (login node):
#   mkdir -p ~/projects/def-jic823/col_matching_jobs && scp nibi/qwen_classc_worker.py \
#       nibi/narval_classc.slurm data/volume/classc/classc_worklist_delta.jsonl narval:~/projects/def-jic823/col_matching_jobs/
#   ssh narval 'cd ~/projects/def-jic823/col_matching_jobs && sbatch narval_classc.slurm'
# Resumable: resubmit to continue (the worker skips ids already in --out).
# Env: WORKLIST / OUT / MODE (default link) / WORKERS (default 8) / SKEPTIC=1
set -euo pipefail
C50=${C50:-$HOME/projects/def-jic823/canada50}
JOBS=${JOBS:-$HOME/projects/def-jic823/col_matching_jobs}
MODEL_DIR=${MODEL_DIR:-$C50/models/Qwen3.8-27B-FP8}
SIF=${SIF:-$C50/containers/vllm.sif}
MODEL_NAME=${MODEL_NAME:-Qwen/Qwen3.8-27B-FP8}
WORKLIST=${WORKLIST:-$JOBS/classc_worklist_delta.jsonl}
OUT=${OUT:-$JOBS/classc_results_delta_narval.jsonl}
PORT=${PORT:-$((8000 + SLURM_JOB_ID % 1000))}

module load apptainer 2>/dev/null || module load apptainer/1.3.5 2>/dev/null || true
CTR=$(command -v apptainer)
echo "node $(hostname)  job $SLURM_JOB_ID  $(date)"; nvidia-smi -L || true
export APPTAINERENV_HF_HUB_OFFLINE=1 APPTAINERENV_HF_HOME=$C50/hf_cache APPTAINERENV_VLLM_LOGGING_LEVEL=INFO
RUN=("$CTR" exec --nv --bind "$C50":"$C50" --bind "$JOBS":"$JOBS" "$SIF" python3)

"${RUN[@]}" -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_DIR" --served-model-name "$MODEL_NAME" \
    --port "$PORT" --host 127.0.0.1 \
    --max-model-len "${MAXLEN:-16384}" --gpu-memory-utilization "${GPU_UTIL:-0.93}" \
    --max-num-seqs "${MAX_SEQS:-8}" \
    --limit-mm-per-prompt '{"image":0,"video":0}' \
    --reasoning-parser qwen3 --trust-remote-code \
    > "$JOBS/vllm-server-$SLURM_JOB_ID.log" 2>&1 &
SERVER=$!
trap 'kill $SERVER 2>/dev/null || true' EXIT
for i in $(seq 1 240); do
  curl -sf "http://127.0.0.1:$PORT/health" >/dev/null 2>&1 && { echo "server up after ${i}x5s"; break; }
  kill -0 $SERVER 2>/dev/null || { echo "server died — see $JOBS/vllm-server-$SLURM_JOB_ID.log"; exit 1; }
  sleep 5
done

"${RUN[@]}" "$JOBS/qwen_classc_worker.py" --worklist "$WORKLIST" --out "$OUT" \
    --url "http://127.0.0.1:$PORT/v1" --model "$MODEL_NAME" \
    --mode "${MODE:-link}" --workers "${WORKERS:-8}" ${SKEPTIC:+--skeptic} ${LIMIT:+--limit "$LIMIT"}
echo "done $(date)"
