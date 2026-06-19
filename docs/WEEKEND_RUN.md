# Weekend run: structure the full corpus on the GPU box

Run `kg_structure_corpus.py` ON the box `hist-clifford-pgx` (where the Qwen3.6
vLLM is served at `localhost:8003`), so there is no SSH tunnel to depend on.

Structures all ~34,743 deduped persons (`persons.deduped2.jsonl`) into KG JSON
using the bake-off winner — `qwen3.6-35b-a3b`, keys prompt, thinking OFF, temp 0
— concurrent + resumable. Output: `data/kg/llm_struct_corpus.jsonl`.

## 1. Code onto the box

Code + raw OCR are on GitHub (`jburnford/col_matching`). The **data is
gitignored**, so move it separately.

Option A — rsync the whole working dir from WSL (code + data, one shot):
```
rsync -avz --exclude='.git' --exclude='raw_ocr' --exclude='__pycache__' \
  --exclude='data/services' --exclude='data/kg/struct_model' \
  /home/jic823/col_matching/ jic823@hist-clifford-pgx.usask.ca:~/col_matching/
```

Option B — clone code on the box, rsync only the data:
```
# on the box:
git clone git@github.com:jburnford/col_matching.git ~/col_matching   # or: git pull
# from WSL — the gitignored inputs the runner needs:
rsync -avz --mkpath data/kg/bios data/kg/persons.deduped2.jsonl \
  jic823@hist-clifford-pgx.usask.ca:~/col_matching/data/kg/
```

## 2. Deps on the box
```
python3 -m pip install --user openai rapidfuzz python-dotenv
```
(Run from the repo root so `import col_match` resolves from cwd — no install of
the package itself needed.)

## 3. Launch (unattended)
```
cd ~/col_matching
nohup python3 kg_structure_corpus.py run \
  --base-url http://localhost:8003/v1 --model qwen3.6-35b-a3b --workers 8 \
  > structure_corpus.log 2>&1 &
```
- Resumable: re-running skips persons already in the output. Safe to kill/restart.
- Bump `--workers` (e.g. 12–16) if the box has headroom; lower if vLLM saturates.
- Monitor: `tail -f structure_corpus.log` — prints `ok/bad`, bio/s, and ETA every 100.

## 4. Validate when done (cheap, no LLM)
```
python3 kg_structure_corpus.py validate --in data/kg/llm_struct_corpus.jsonl
# -> data/kg/llm_struct_corpus.valid.jsonl
```
Then pull `llm_struct_corpus.valid.jsonl` back to WSL for Phase 3 (final dedup on
structured events) + grounding/emit via `kg_build.py`.

## Notes
- Thinking MUST be off: vLLM ignores OpenRouter's `reasoning` flag, so the runner
  sends `chat_template_kwargs.enable_thinking=false`. With it on, long bios eat the
  token budget and return no JSON (~67% failure observed).
- Context is 16,384 tokens; bios + ~300-token output fit comfortably.
