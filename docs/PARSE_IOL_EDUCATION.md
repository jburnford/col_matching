# Parse + ground the IOL education layer (LLM parse, then Wikidata)

Quality path for the India Office List **education institutions**. Jim's call
(2026-06-26): *quality over speed* — parse the free-text `education` clause with
the local **Qwen3.6** model on nibi instead of the brittle regex extractor
(measured: regex reaches only ~56% of non-empty rows and regresses on the
irregular tail — `University College London`, `Christ's Hospital`,
`Universities of Glasgow and Edinburgh`, colleges written without a keyword).

The LLM step replaces ONLY the prose→institution extraction. Grounding the
extracted surfaces to Wikidata reuses the existing `kg_ground_institutions.py`
loop (and the 427-row 1937 seed cache).

Always `export COL_KG_OUT=data/iol` first.

## Workload
- `data/iol/graph_stage3/education.jsonl` = 17,063 person rows (prose education).
- **6,825 DISTINCT education strings** (the LLM only parses these once each;
  results fan back to person_ids in stage E). Short job — minutes, not hours.

---

## Stage A — serve Qwen on nibi (H100)
```
scp nibi/serve_qwen.slurm nibi:~/projects/def-jic823/      # if changed
ssh nibi 'cd ~/projects/def-jic823 && sbatch serve_qwen.slurm'
ssh nibi 'squeue -u $USER'                                  # wait for RUNNING
ssh nibi 'grep SERVE_NODE ~/projects/def-jic823/qwen-serve-<JOBID>.out'
```
Serves an OpenAI-compatible endpoint on the node's **:8003** (GGUF Q4 via
llama.cpp, `--jinja --flash-attn on --parallel 16`, 12h walltime).

## Stage B — tunnel from WSL (⚠️ nibi now requires MFA for NEW logins)
A fresh `ssh -N -L` tunnel FAILS the MFA prompt. Reuse the live ControlMaster
(adds a forward with NO new login); pick a FREE local port (e.g. 8004):
```
ssh -O forward -L 8004:<SERVE_NODE>:8003 nibi
```
(`scp`/`squeue` over `nibi` reuse the same master.) Verify:
`curl -s http://127.0.0.1:8004/v1/models`.

## Stage C — PILOT (eyeball quality before the full run)
```
COL_KG_OUT=data/iol python3 kg_parse_education.py run \
  --base-url http://127.0.0.1:8004/v1 --model qwen3.6-35b-a3b \
  --workers 16 --limit 30
```
Inspect `data/iol/education_parsed.jsonl`: institutions clean, colleges bound to
parents, degrees/prizes dropped, no hallucinated institutions. Resumable (the
30 pilot rows are kept; the full run skips them).

## Stage D — full parse (resumable; ~6.8k strings)
```
COL_KG_OUT=data/iol python3 kg_parse_education.py run \
  --base-url http://127.0.0.1:8004/v1 --model qwen3.6-35b-a3b --workers 16
```
Skips successful rows on resume; only `_error` rows (server death) are retried.
Run under `nohup ... &` (log it) if the tunnel may drop. Output:
`data/iol/education_parsed.jsonl` (one row per distinct string:
`{"education": "...", "institutions": [{"name","type"}]}`).

## Stage E — build the grounding worklist (no LLM)
```
COL_KG_OUT=data/iol python3 kg_parse_education.py worklist
```
Fans parsed institutions back to person_ids →
`data/iol/education_worklist.jsonl` in the schema
`kg_ground_institutions.py` consumes (`institution`/`type`/`count`/`person_ids`/
`examples`). Prints the distinct-institution count + top 25.

## Stage F — ground to Wikidata (fold first, then MCP; seeded with 427)
Follow `docs/GROUND_INSTITUTIONS.md`. Env for the whole loop:
```
export COL_WORK=data/iol/education_worklist.jsonl
export COL_CACHE=data/iol/institutions_grounding.jsonl
```
**F0 — FOLD PRE-PASS (zero MCP). Run first AND after every MCP batch:**
```
COL_KG_OUT=data/iol python3 kg_fold_institutions.py --out data/iol/inst_folds_NNN.jsonl
COL_KG_OUT=data/iol python3 kg_ground_institutions.py record data/iol/inst_folds_NNN.jsonl
```
Folds worklist surfaces that normalise to an entity already cached (seed or
freshly grounded), under a different surface/label. The first pass lifted IOL
coverage 52.2%→**80.6%** (148 folds, R.I.E. College/Edinburgh/Eton/Winchester…)
because the seed held many QIDs only under their label form.

**F1 — MCP loop on the residual** (~1,049 institutions, mostly local colonial /
Indian schools + obscure colleges):
```
COL_KG_OUT=data/iol python3 kg_ground_institutions.py stats             # coverage
COL_KG_OUT=data/iol python3 kg_ground_institutions.py pending --n 50    # count-desc tail
#  -> MCP search_items + get_statements per /place-disambig (≤5/msg), write batch JSONL
#     pick the educational-institution QID (NOT a building/boat-club/painting/person)
COL_KG_OUT=data/iol python3 kg_ground_institutions.py record <batch.jsonl>
```
4-way disposition: `mcp_verified` (QID) / `reuse` / `internal` (`colkg:<Slug>`,
single-referent local school) / `ambiguous` (bare multi-referent surface — id:null,
never internal-mint, per [[kg-institution-ambiguous-surfaces]]).

**F2 — VERIFY every MCP/agent batch against live Wikidata (0-FP gate):**
```
python3 verify_institution_qids.py data/iol/institutions_grounding.jsonl
```
Institution analogue of verify_place_qids.py — flags **NONINST** (person/
building/ship/painting grounded by mistake), **STUB** (statement-less), and
**CLASS** (grounded to a generic type like Q967098 grammar school, not a specific
institution). This already caught seed errors (HMS Conway→training-vessel,
Q967098 grammar-school class). Subagents hallucinate plausible-but-wrong QIDs —
always run this before trusting a batch.

### Type + subtype cohorts (carried on every worklist row)
`kg_parse_education.py` tags `type` (school/university/university_college/
military_academy/inn_of_court/professional) AND a cohort `subtype`:
- schools → grammar | public | school
- universities → oxbridge | ancient_scottish | redbrick (Q1202123) | london |
  irish | indian | university
- military → sandhurst | woolwich | naval | addiscombe | staff | indian_military
EIC pipeline split at grounding: `East India College, Haileybury` (civil/ICS) vs
`Haileybury & Imperial Service College` (public school, Q5639263) vs
`Addiscombe` military seminary (Q142575) — distinct QIDs, never lumped.

## Stage F — 3-BATCH RESUME PLAN (paste after /clear)

State at handoff: **575 grounded / 80.6% mention coverage**; **~1,049 institutions
pending** (~3,500 mentions). Ground in **3 batches of ~350** (count-descending).
The head is famous + easy (Haileybury College 337, University of Bombay 173,
Thomason College 113, Inner Temple 76, University of Rangoon 56, St Andrews 46,
SOAS 46…); the tail is local colonial/Indian schools (many → `internal` or
`ambiguous`). Each batch is self-contained and resumable.

**ALL 3 BATCHES DONE + EMITTED 2026-06-26.** FINAL: **887 Wikidata QIDs / 700
internal / 39 ambiguous → 99.6% mention coverage (18,097/18,177); 0 pending.**
Emitted **1,585 institutions.jsonl nodes + 9,328 education_edges.jsonl over 6,624
persons, 83% QID-grounded** (Stage G, default COL_NODES/COL_EDGES).
- B1 (count-desc head 337→2; cache 575→935): 350 grounded (28 mcp / 92 reuse /
  219 internal / 11 ambiguous) + 10 fold-post. Coverage 80.6%→94.9%.
- B2 (count≤2, 345 surfaces): 27 mcp / 85 reuse / 213 internal / 20 ambiguous →
  97.7%.
- B3 (count==1 singletons, 342): 16 mcp / 83 reuse / 238 internal / 5 ambiguous →
  99.6%. Verifier demoted **H.M.S. Conway Q5631958** (P31=training vessel/shipwreck,
  the recurring seed-error class) → internal.
All batches verified 0-FP. Held 0.4% = 39 bare multi-referent surfaces (ambiguous).
⚠️ The EIC QID `Q1432447` cited above is WRONG (= Thousand Palms, California); the
**East India Company College (civil/ICS) is Q142599**. Used: Haileybury & ISC public
school Q5639263, EIC civil college Q142599, Addiscombe military Q142575 — all split.
⚠️ WikidataMCP `search_items` degraded mid-run; several well-known British schools
were conservatively internal-minted (Owens College Manchester, Clitheroe Grammar,
St Peter's College Adelaide, Government College Lahore, Battersea Polytechnic,
Guy's/St George's medical schools…) — re-checkable on a healthy endpoint.
Batches written: data/iol/inst_mcp_b1.jsonl, inst_folds_b1post.jsonl.
**REMAINING: 689 pending = ALL count≤2 (only 872 mentions)** — the local-school
floor (ROI cliff, mostly `internal`/`ambiguous`). Batches 2–3 split this ~345 each;
coverage gain per batch will be small (≤~2.5pt) since the head is exhausted.

**Resume prompt:**
> Ground the IOL education residual, batch N of 3 — follow docs/PARSE_IOL_EDUCATION.md
> stage F (export COL_KG_OUT=data/iol; COL_WORK=data/iol/education_worklist.jsonl;
> COL_CACHE=data/iol/institutions_grounding.jsonl first).

**Per-batch procedure (≈350 institutions):**
```
export COL_KG_OUT=data/iol
export COL_WORK=data/iol/education_worklist.jsonl
export COL_CACHE=data/iol/institutions_grounding.jsonl

# 1. fold pre-pass (free; sweeps variants of anything grounded last batch)
python3 kg_fold_institutions.py --out data/iol/inst_folds_b<N>.jsonl
python3 kg_ground_institutions.py record data/iol/inst_folds_b<N>.jsonl

# 2. next ~350 pending (count-desc); split across 3-4 subagents, each doing
#    MCP search_items + get_statements per /place-disambig, ≤5 calls/msg.
python3 kg_ground_institutions.py pending --n 350 > /tmp/inst_pending_b<N>.jsonl
#    Disposition each: mcp_verified QID | reuse | internal (colkg, single local
#    school) | ambiguous (bare multi-referent, id:null). Pick the EDUCATIONAL
#    entity (not a building/boat-club/painting/person). EIC split: East India
#    College Haileybury (civil) vs Haileybury & ISC Q5639263 vs Addiscombe Q142575.

# 3. write batch QIDs to data/iol/inst_mcp_b<N>.jsonl, then VERIFY (0-FP gate)
python3 verify_institution_qids.py data/iol/inst_mcp_b<N>.jsonl     # fix NONINST/STUB/CLASS
python3 kg_ground_institutions.py record data/iol/inst_mcp_b<N>.jsonl

# 4. coverage check
python3 kg_ground_institutions.py stats
```
After batch 3, run Stage G (emit). Target: ground the ~929 head, internal-mint /
ambiguous the obscure tail; expect ~90%+ mention coverage (singleton local-school
floor, same ROI cliff as places).

## Stage G — emit institution nodes + education edges
```
export COL_WORK=data/iol/education_worklist.jsonl
export COL_CACHE=data/iol/institutions_grounding.jsonl
COL_KG_OUT=data/iol python3 kg_ground_institutions.py emit   # -> data/iol/graph_stage3/
```
(`emit` is now rooted on `COL_KG_OUT` — was hardcoded to `data/kg`.)

## Resume prompt (paste after /clear)
> Parse + ground the IOL education layer — follow docs/PARSE_IOL_EDUCATION.md
> (export COL_KG_OUT=data/iol first). Serve Qwen on nibi, run the parse, then
> the grounding loop.

See `[[iol-kg-build]]` and `[[kg-institution-grounding]]`.
