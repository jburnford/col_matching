# KG biography structuring — in-session LLM loop runbook

**Purpose.** Build a strong reference set of LLM-structured Colonial Office List
biographies (parsed by Claude/Opus in-session, $0) to compare against what Qwen
3.6 produces on the GPU box. Each loop iteration structures one batch of ~25
biographies. The pipeline is resumable, so this survives context clears.

## One iteration — do exactly this

1. **Dump the next batch** (vary `--seed` each iteration, e.g. the iteration
   number, so successive dumps differ; already-structured persons are skipped):

   ```bash
   python3 kg_build.py dump --n 25 --seed <N>
   ```

   Output: a header line `# <K> persons remain unstructured (<D> done); dumping 25`
   then one JSON line per person: `{"person_id": "...", "text": "<normalized entry>"}`.
   If `dumping 0`, the run is COMPLETE — stop the loop.

2. **Structure each person.** For every dumped line, emit ONE JSON object
   matching the schema + rules below. Extract ONLY what is printed; never invent.

3. **Write the batch** with the Write tool to a NEW file (never overwrite):

   ```
   data/kg/struct_in/batch_seed<N>.jsonl
   ```

   one object per line. Each object MUST carry its `person_id`.

4. **Validate** (Python reviews the LLM — drops any place/year not in the source):

   ```bash
   python3 kg_build.py validate
   ```

   Report the line it prints (count + facts dropped). A few drops are normal;
   many drops on one batch means re-check that batch's places/years.

5. **Report progress** (`<D> done` from step 1) and continue to the next
   iteration with `--seed <N+1>`. Target: keep going until ~150–200 persons are
   structured (a solid reference set) or the dump reports 0 remaining.

## Output object schema (one per line)

```json
{"person_id": "kgp_...", "surname": "...", "given_names": "...|null",
 "birth_year": 1872, "education": "ed. ...|null",
 "honours": [{"award": "C.M.G.", "year": 1905}],
 "events": [{"position": "assistant colonial secretary", "place": "Ceylon",
             "year_start": 1914, "year_end": null, "place_inherited": false,
             "is_acting": false, "org_type": "civil"}],
 "terminal": {"kind": "retired", "year": 1919}}
```

## Extraction rules (same as col_match/kg/extract.py KG_BIO_SYSTEM)

- **events** — one object per distinct posting. EXPLODE compound/concurrent
  clauses into separate events ("reg.-gen., 1887, and M.L.C., 1889" = two;
  "ag. comsnr., 1915-16; and from 1919" = two).
- **position** — as printed (the normalized expansion is fine).
- **place** — the colony/territory/locality named in the clause, AS PRINTED
  ("Ceylon", "Negombo", "N. Nigeria"). If the clause names no place, carry over
  the previous clause's place and set `place_inherited=true`. **Do NOT guess or
  upgrade a locality to its parent colony** — grounding happens later. Inheritance
  stops when a transfer is stated.
- **year_start/year_end** — `year_end` null for a single year; "1900-02" → 1902.
- **is_acting** — true when the post is acting ("ag."/"acting").
- **org_type** — "military" for army/navy/regiment/expedition/campaign postings,
  else "civil".
- **honours** — decorations with their AWARD year if printed in parens
  ("C.M.G. (1905)"); award-years are NOT career events.
- **birth_year** — only if explicitly printed ("B. 1872"); else null. NEVER infer
  from the earliest career date.
- **education** — the "ed. ..." string as one metadata string; university class
  honours stay here, NOT as events.
- **terminal** — {kind: retired|resigned|died|pensioned|other, year} if the entry
  states the career ended, else null.

## Known data issue (flag, don't fix in the loop)

Some canonical entries are **multi-person contamination**: surnames beginning
"ST." / "O'" / "Mc" can defeat headword segmentation, so one dumped `text` may
concatenate several distinct people (e.g. a SAINSBURY entry that runs on into
ST. ALDWYN, ST. AUBYN, ST. JOHNSTON …). When a `text` clearly contains multiple
distinct biographies, structure ONLY the first/primary person and add
`"flags": ["multi_person_block"]` to that object. (Root-cause fix —
`volume/bios._HEADWORD` to recognise dotted "ST."-prefixed headwords — is a
separate code task, not loop work.)

## After the reference set is built

- Qwen produces its own structures via `col_match/kg/extract.parse_via_client`
  (QwenClient, GPU box). Compare Qwen vs this Opus reference set per person_id.
- Then: full place grounding (`kg_build.py ground` worklist → MCP loop) and
  `kg_build.py emit`.
