# LLM dedup of the residual duplicate tail — method + loop (rock-solid, hand-off-able)

Goal: collapse the ~3,000 residual duplicate biographies that the deterministic
dedup passes (compile A–E) can't safely merge — fragments of one person split
across OCR surname garbles/truncations, thin careers, or noisy birth years.
Done **in-session** (Claude Code, $0) to harden the method; the same prompt +
schema can later drive a cheaper model (OpenRouter / DeepSeek) — cost-gated,
**NO GEMINI**, needs Jim's capped-estimate sign-off (see [[no-gemini-cost-overrun]]).

## The loop (resume here)
```bash
cd ~/col_matching && export COL_USE_AUGMENTED=1 PYTHONHASHSEED=0
python3 dedup_review.py --stats              # coverage; how many clusters remain
python3 dedup_review.py --limit 15 --min 2 --max 2   # next batch of dossiers (start small)
#   read each CLUSTER, decide which bios are ONE person, append merge groups to:
#   data/services/dedup/llm_merges.jsonl   (one JSON object per MERGE group)
# periodically (every ~50–100 merges) recompile + re-gate:
python3 -m col_match.services.cli compile      # reads the ledger (pass F), unions the groups
python3 -m col_match.services.cli infer_colony
python3 -m col_match.services.cli attach
python3 -m col_match.services.cli match
python3 -m col_match.services.cli eval_known   # MUST stay 0 FP both levels
```
`dedup_review.py` skips clusters whose versions are already in the ledger, so the
loop is resumable. Clusters = connected components of bios sharing a spelled
forename token AND a surname suffix-4 (the pass-E key), so OCR surname variants of
one person land together. ~2,098 clusters / ~7,875 bios at start; size-2 dominate.

## The adjudication rules (THE PROMPT — feed this + one cluster's dossier)
You are given a CLUSTER of biographies that share a surname-suffix and a spelled
forename. Partition them into distinct real people. Each bio shows: matched flag,
all version_ids, name, birth year, education, honours, full dated career, death.

**MERGE two bios (same person) only on POSITIVE same-person evidence:**
1. **Overlapping career** — ≥1 event agreeing on year (±1) AND place or position
   (e.g. both "1896 Penang ag. dep. registrar of deeds").
2. **Distinctive education** — near-identical education string (e.g. "King's Sch.,
   Canterbury and All Souls Coll., Oxford"). Education is near-unique per person.
3. **Shared honour + year** (e.g. KT.BACH/1898, C.M.G/1923) or **shared death year**.
4. **OCR surname/headword variant** — one surname is a clear garble/truncation of
   the other (ATTKEN→AITKEN, ABERY→CARBERY, ACARLTHUR→McARTHUR, THORODER→THEODORE)
   AND the forename + career are consistent. A single identical event suffices here.
5. **Thin/empty fragment** with the SAME full given name + a shared honour-year or a
   shared distinctive event (the careerless 1898 "Edward James Ackroyd" fragment).

**Birth year is OCR-noisy — do NOT split on it.** ±1–2 or one-digit differences
(1885/1886, 1834/1884, 1879/1889) are the SAME person. A large multi-digit gap is
weak evidence of *different* people but is not decisive alone — the career/education
decides.

**DO NOT MERGE (keep separate) when:**
- Different spelled forenames (Myles John vs John Thomas; Henry Charles vs Charles
  Drummond).
- Disjoint careers — different colonies/eras, no shared event (Adams Ernest, NSW
  1908 vs Adams Ernest Victor, Cape railway 1891).
- **Same name + adjacent birth year but DIVERGENT education/specialty** — the
  decisive discipline case: two "Alexander Graham" b.1896/1897, one a Scotland-
  trained MARINE surveyor (A.M.I.N.A), one a Perth-trained LAND surveyor (M.I.S.W.A)
  → different people. Name + birth alone is NEVER enough.
- Coincidental shared forename across genuinely different surnames (Adamson / Simson
  / Thomson all "John").
- Father/son namesakes: same full name, large birth gap, non-overlapping careers.

**DEFAULT TO NOT MERGING when uncertain.** A missed merge is recoverable; a false
merge corrupts a person permanently (the prime directive). Emit only high/medium-
confidence merges.

**OUTPUT** — one JSON object per merge group (singletons need no output):
```json
{"versions": ["<ALL version_ids of every bio in the group>"], "bios": ["<bio_ids>"],
 "reason": "<one line: the positive evidence>", "confidence": "high|medium"}
```
Include EVERY version_id of EVERY merged bio (robust to recompile regrouping).

## Mechanism (already built)
- `dedup_review.py` (repo root) — emits dossiers, skips ledger-covered clusters,
  `--stats` for coverage.
- Ledger `data/services/dedup/llm_merges.jsonl` — append-only, one merge group/line.
- compile **pass F** (`compile_biographies`, `llm_merge_groups`; wired in
  `cli.cmd_compile`) — unions the version groups; authoritative, gated by
  `eval_known`. `COL_NO_LLM_DEDUP=1` reverts. `_compose` makes the cleanest
  (most-events) fragment the canonical surname, so a garbled headword adopts the
  clean spelling on merge.

## Status (handoff)
**35 merge groups adjudicated + applied, 0 FP both levels** (ledger:
`data/services/dedup/llm_merges.jsonl`). Full decision log incl. NON-merges:
`data/services/dedup/dedup_decisions_opus.jsonl` (the DeepSeek A/B diff target).

**Session 2026-06-17b: +52 clusters adjudicated (22 merge, 30 no-merge).** Recorded
in `dedup_decisions_opus.jsonl` + `docs/dedup_gold_opus.md` Session-2 section. gate
0 FP both levels (career_splits 5/11 baseline). Merges incl. 8 dropped-initial OCR
surnames (An Buren=Van Buren, Andolo=Dandolo, Apper=Capper, Awcett=Fawcett...),
Anderson=Maxwell-Anderson, careerless fragments WITH a discriminator (Archibald
C.M.G., Allan Gordon dated event). Hardest non-merges held: same-name divergent
(Armstrong Robert b.1879≠b.1906), brothers (Aplin D'Auvergne), careerless
name-only fragments (Angelo, Arnott — no honour/event → NOT merged).

Earlier batches (now folded into the 35):
- Batch 1 (12 size-2 + 8 size-3 clusters → 7 merges). Examples: Aberdeen
  Earl↔Marquess, Abery↔Carbery, Acarlthur↔McArthur, Ackroyd thin-fragment,
  Theodore↔Thoroder, George-P-Adams fragments, Aitken↔Attken.
- Batch 2 (2026-06-17, 20 size-2/3 clusters → 6 merges, 14 correct non-merges):
  Adshead Williams↔Willetts (unlocked an unmatched bio), Agbebi↔Agebebi,
  Aggart↔Haggart (dropped-H, the Canadian politician), Aharne↔Ahearne,
  Alabaster Grinnell↔Grenville, Alcomb↔Halcomb (dropped-H). Non-merges held the
  line on the hard cases: Adams Ernest(NSW)≠Ernest Victor(Cape), Abramson
  (Transjordan)≠Hyamson(Palestine), and several near-namesake OCR-lookalike
  surnames (A'Beckett≠Beckett, Aanensen≠Jansen, Abraham≠Graham, Abrams≠Mirams).
gate stayed 0 FP both levels (career_splits stint 5→4). ~2,080 clusters /
~7,832 bios remain unreviewed.

## NEXT SESSION — do this
1. **(DONE 2026-06-17 — Batch 2 above)** ~~Complete 20 more clusters.~~ Repeat the
   same loop for the next 20 if continuing to grow the Opus gold set:
   `export COL_USE_AUGMENTED=1 PYTHONHASHSEED=0`, then
   `python3 dedup_review.py --limit 20 --min 2 --max 3`, read each, append merge groups
   to `data/services/dedup/llm_merges.jsonl` using the rules above, then recompile →
   infer_colony → attach → match → `eval_known` (MUST stay 0 FP). `--stats` to track.
2. **Then test DeepSeek before any wider hand-off.** `docs/dedup_gold_opus.md` is the
   20-cluster Opus gold + the exact regenerate recipe. Feed DeepSeek each cluster's
   dossier + the rules above; it must reproduce the 7 merges AND the 13 non-merges —
   especially Batch-2 #1 (do NOT merge the two same-name Alexander Grahams) and the
   partial-merge clusters. A false merge by DeepSeek = hard fail. Only widen to the
   backlog if agreement is clean. Cost-gate + Jim's sign-off; NO GEMINI.

## Hand-off to a cheaper model later
The prompt above + one cluster's dossier → merge-group JSON is model-agnostic.
To run on OpenRouter/DeepSeek: batch clusters (the targeted scope ≈ 1,290 calls /
~0.95M input tokens), enforce the JSON schema, append results to the same ledger,
then recompile + `eval_known`. Keep a 2nd-pass verifier on every proposed merge
(the gate is necessary but not sufficient for non-gold merges). Cost-gate +
sign-off first.
