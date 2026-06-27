#!/bin/bash
# Self-contained education-parse job: boot the Qwen3.6 llama.cpp server on the
# allocated H100, wait until its OpenAI endpoint is live, run the education
# parser against localhost (no tunnel / no MFA), then stop the server.
#
#   ssh nibi 'cd ~/projects/def-jic823 && sbatch parse_education.slurm'
#
# Output: ~/projects/def-jic823/col_matching/data/iol/education_parsed.jsonl
# (resumable — re-sbatch to continue; successful rows are skipped).
#SBATCH --account=def-jic823
#SBATCH --job-name=qwen-parse-edu
#SBATCH --gres=gpu:h100:1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=02:00:00
#SBATCH --output=%x-%j.out

set -uo pipefail
module load apptainer/1.4.5

GGUF="$HOME/projects/def-jic823/models/qwen3.6-35b-a3b/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf"
SIF="$HOME/projects/def-jic823/containers/llama-cpp-server-cuda.sif"
VENV="$HOME/projects/def-jic823/parse_venv"
REPO="$HOME/projects/def-jic823/col_matching"
PORT=8003
SRVLOG="$REPO/server-$SLURM_JOB_ID.log"

echo "NODE=$(hostname -s)"; nvidia-smi -L

# 1) start the server in the background
apptainer run --nv --env LD_LIBRARY_PATH=/app "$SIF" \
  -m "$GGUF" --host 127.0.0.1 --port "$PORT" --n-gpu-layers 999 \
  --flash-attn on --ctx-size 49152 --parallel 16 --cont-batching \
  --batch-size 4096 --ubatch-size 1024 --jinja --threads 12 \
  --alias qwen3.6-35b-a3b > "$SRVLOG" 2>&1 &
SRV=$!
echo "server pid=$SRV  log=$SRVLOG"

# 2) wait until the endpoint answers (max ~10 min for model load)
READY=0
for i in $(seq 1 120); do
  if curl -sf "http://127.0.0.1:$PORT/v1/models" >/dev/null 2>&1; then
    echo "server READY after $((i*5))s"; READY=1; break
  fi
  if ! kill -0 "$SRV" 2>/dev/null; then
    echo "server process died before becoming ready; tail of log:"; tail -30 "$SRVLOG"; exit 1
  fi
  sleep 5
done
[ "$READY" = 1 ] || { echo "server not ready in time"; tail -30 "$SRVLOG"; kill "$SRV" 2>/dev/null; exit 1; }

# 3) run the parse on-node against localhost
source "$VENV/bin/activate"
cd "$REPO"
# CORPUS selects the output tree (data/iol or data/kg); default IOL.
#   sbatch --export=ALL,CORPUS=data/kg parse_education.slurm
CORPUS="${CORPUS:-data/iol}"
echo "CORPUS=$CORPUS"
COL_KG_OUT="$CORPUS" python3 kg_parse_education.py run \
  --base-url "http://127.0.0.1:$PORT/v1" --model qwen3.6-35b-a3b \
  --workers 16 --max-tokens 512
RC=$?

# 4) stop the server
kill "$SRV" 2>/dev/null || true
wait "$SRV" 2>/dev/null || true
echo "parse exit code=$RC"
exit $RC
