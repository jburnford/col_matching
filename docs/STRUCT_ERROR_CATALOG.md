# Structuring error catalog — every-10th audit

LLM-read review (not deterministic) of every 10th biography from
`data/kg/llm_struct_corpus.jsonl`, each struct compared against its source text
by a Claude reviewer. Raw findings: `data/kg/review/findings.json`; reviewed
pairs: `data/kg/review/every10.jsonl`.

## Headline (first 1,859 structured → 186 sampled)

- **129/186 fully clean (69%)**, 0 LLM/JSON failures.
- **74 findings on 56 records; only 8 are "major" → ~3% of records carry a major error.**
- The other ~97% are clean or carry only minor, mostly **deterministically fixable** issues.
- Error profile is dominated by a few *systematic* patterns, not random model noise — most are post-processable without re-running the LLM.

## Frequency

| Category | n | Severity skew |
|---|---:|---|
| POSITION_GARBLED | 17 | mostly minor (1 major) |
| MISSED_HONOUR | 11 | minor |
| MISSED_EVENT | 11 | minor (3 major) |
| WRONG_PLACE | 6 | minor (1 major) |
| HALLUCINATION | 5 | minor (1 major) |
| INHERITANCE | 4 | minor |
| WRONG_DATE | 4 | minor (1 major) |
| MISSED_EDUCATION | 4 | minor |
| TERMINAL | 4 | 1 major |
| NAME_PARSE | 4 | minor |
| ORG_TYPE | 3 | minor |
| NOT_A_PERSON | 1 | data issue, struct correct |

## Root-cause clusters (what to actually fix)

### 1. Abbreviation mis-expansion — the single biggest class (~10 findings)
The model expands period-abbreviations wrongly, and consistently:
- `off.` (office) → "officer" — idx 620, 530, 1330
- `col.` (colonel) → "colonial" — idx 670, 870
- `govt.` (governor) → "government" — idx 670, 750
- `offr. in ch.` (officer in **charge**) → "officer in **chief**" — idx 480, 1130
- `Jun.` (June) → "junior" — idx 380
- `HON.` (Honourable) → "honorary", folded into given_names — idx 690, 1580
**Fix:** a deterministic abbreviation-expansion table applied post-LLM (or a few-shot block in the prompt). These are predictable and high-frequency.

### 2. "ditto"/"do." not resolved (~4 findings)
`ditto`/`do.` left literally in `position` or `place` instead of carrying the prior line's value — idx 120, 470, 340, 1770.
**Fix:** deterministic forward-fill pass: any position/place equal to `ditto`/`do.`/`ditto.` inherits the previous event's value (set `place_inherited=true`).

### 3. Place ↔ position confusion (~6 findings, 1 major)
- place abbreviation written as the position: `F.M.S.`, `Uga.` — idx 70, 770
- month abbreviation read as a place: `Mar.` → place — idx 1700 (**major**)
- unit/org name as place: "Palestinian Gendarmerie", `F.A.P.` — idx 560, 790
**Fix:** validate `place` against a gazetteer/month-name stoplist; if a position is empty but a known place token sits in it, swap. The month-as-place case is catchable with a deterministic guard.

### 4. "Knight Bachelor" split into two awards (3 findings)
`KT. BACH. (1907)` / `KNT. BACH.` → two awards `KT` + `BACH` — idx 1380, 1570, 1680. Perfectly systematic.
**Fix:** merge-rule `{KT|KNT} + BACH[.] → "Knight Bachelor"` in post-processing.

### 5. "Mentioned in despatches" dropped or miscategorized (~7 findings)
`ment. in desps.` / `men. in desps.` either dropped or stored as an event instead of an honour — idx 10, 450, 570, 670, 870, 1120, 1840. Same for `K.C.`, King's Police Medal, Order of St John — idx 160, 890, 1560, 1850.
**Fix:** prompt nudge listing despatch-mentions and post-nominal honours (K.C., medals, orders) as `honours`; or a deterministic sweep of the source for `ment. in desp` and `K.C.`

### 6. Degrees dropped from education (4 findings)
Education captures schools but omits degree letters: `B.A., LL.B.`, `B.Sc.`, `M.B.`, `LL.D.` — idx 360, 370, 800, 1480.
**Fix:** prompt: include post-nominal degrees in `education`.

### 7. place_inherited mislabeled (4 findings)
`place_inherited=true` on the **first** event (nothing to inherit) — idx 240, 770; or `inherited=true` with `place` left null — idx 440, 640.
**Fix:** deterministic — first event can never inherit; `inherited=true` requires a non-null resolved place.

### 8. Over-claimed TERMINAL status (4 findings, 1 major)
Model invents `resigned`/`retired` when only *one role* ended and the career visibly continued — idx 400 (**major**, invented outright), 1120, 1200, 1280.
**Fix:** only emit terminal if it's the last dated item AND no later event exists; treat "resigned [office]" mid-career as an event end, not a terminal.

### 9. Dated events dumped into the education string (part of MISSED_EVENT majors)
Bar admissions, M.P./M.H.A. seats, military commissions get written into `education` instead of `events` — idx 1310, 1340, 1850; and some dated events simply dropped — idx 1280, 1400×2 (**major**).
**Fix:** prompt clarification on what's an event vs education; harder to fully fix deterministically — these are the residual true model misses.

### 10. NAME_PARSE (4 findings)
Honorifics/ridings folded into `given_names` (idx 690, 1260, 1580); one dropped letter `Veluppillai→Velupillai` (idx 1610).
**Fix:** strip leading honorifics (`HON.`, `RT. HON.`, `SIR`) and trailing parenthetical ridings from given_names deterministically.

### 11. ORG_TYPE civil↔military (3 findings)
Civil colonial posts (veterinary officer, administrative cadet, "served in Fiji") tagged `military` — idx 450, 940, 1760.
**Fix:** default `civil` unless an explicit military token (regt., R.N., R.A.F., rank) is present.

## Takeaways
- **The model is reliable on the core task** (name, birth year, the event spine, dates) — 69% perfectly clean and only ~3% major-error rate on a faithful reading.
- **~8 of the 11 clusters are deterministic post-processing**, not model-capability gaps: abbreviation table, ditto forward-fill, Knight-Bachelor merge, inheritance guard, terminal guard, honorific strip, org_type default. Building these as a `normalize_struct` pass would clear the large majority of findings without touching the (expensive) LLM run.
- **The residual true model misses** are: occasional dropped dated events (esp. early legislative/bar roles) and events mislanded in the education string — worth a targeted prompt tweak, but they're rare and mostly minor.
- **Data hygiene:** front-matter/editorial blocks (idx 0) are in the person spine and structure to all-null — cheap to filter pre-emit.

## Round 2 — fresh 100-bio sample (`sample100.jsonl`, idx 5–31,487)

Non-overlapping sample spread across the *whole* corpus (round 1 was front-loaded on early/simple entries). Raw findings: `data/kg/review/findings_sample100.json`.

- **51/100 clean, 62 findings, 9 records (~9%) with a major error.** Lower clean rate than round 1 because this reaches the dense later-edition careers and titled/peerage entries.
- Confirmed every round-1 cluster **and surfaced new ones:**

| New pattern | Cat | Fix locus |
|---|---|---|
| `temp.` (temporary) → `is_acting=true` | ACTING_FLAG | **postnorm** (done) |
| Military rank/title folded into given_names (`CAPTAIN`, `LIEUT.-GENERAL`, peerage) | NAME_PARSE | **postnorm** (done) |
| `min.` → "minister" (should be *Ministry*) | POSITION_GARBLED | pre-LLM (done) |
| `gov.`/`govt.` → "governor" (should be *government/governing*) | POSITION_GARBLED | pre-LLM (done) |
| `col.` → "colonial" (should be *colony*) | POSITION_GARBLED | pre-LLM (done) |
| Invented `year_end == year_start` (sometimes `< year_start`) on single-date appointments | WRONG_DATE/OTHER | validate nulls `end<start`; same-year left (residual) |
| Education abbrev garble (`Univ. C.T.`→"university court", `Sec. Sch.`→"secretary school") | OTHER | pre-LLM partial; residual |
| Degrees/post-nominals dropped (`D.C.L.`, `D.Litt`, `A.M.Inst.C.E.`) | MISSED_EDUCATION/HONOUR | prompt (residual) |
| Concatenated second biography (OCR-merged entry) dropped | OTHER | data hygiene (rare) |

## Fixes built (this round)

**`col_match/kg/postnorm.py` — `normalize_struct(struct) -> (clean, changes)`**, a deterministic post-pass wired into `kg_structure_corpus.py validate` (runs before source validation; every change recorded under `_norm`). Over the combined 286-struct audit set it changes **31% of structs** (idempotent, no source needed):

| Fix | count (286) |
|---|---:|
| inheritance fill (materialize LLM-flagged inherited place) | 160 |
| given_names honorific/rank/title strip | 38 |
| ditto/do. position+place resolve | 11 |
| Knight Bachelor merge | 7 |
| place_inherited flag repair (first-event / null-place) | 7 |
| `temp.`→acting repair | 3 |
| "officer in chief"→"officer in charge" | 3 |

Deliberately **not** auto-fixed: `org_type` military↔civil (a position-only rule over-fired on 35% of structs — the military signal is often in the source dates, not the position noun; better fixed at the prompt).

**`col_match/kg/normalize.py` — ambiguous abbreviations left raw pre-LLM.** `off`/`gov`/`govt`/`col`/`min` are no longer force-expanded into one sense before the model sees them (they were the single largest POSITION_GARBLED source); `position_norm` still expands them downstream. Helps any *future* run; the current corpus is already structured with the old behavior, so its residue is what postnorm + validate clean.

## Residual (LLM-capability, not deterministically fixable)
Dropped dated events (esp. early legislative/bar/summary roles), events landed in the education string, dropped despatch-mentions/degrees, same-year invented `year_end`. Rare and mostly minor — candidates for a targeted prompt revision if a re-structuring pass is ever run.

## Round 3 — 300-bio sample (`sample300.jsonl`, idx 3–32,594, 12 reviewers ×25)

Largest sweep, full-corpus spread, no overlap with the prior 386. **~149/300 clean (50%)**; findings dominated by a handful of patterns, most now auto-fixed.

**`year_end` fabrication is the #1 pattern corpus-wide.** The LLM invents an end year on point appointments. postnorm now nulls the safe form (`year_end == year_start`) — **350 nulls across the 300 sample (~1.2/struct)**.

⚠️ **A rejected fix, kept as a warning.** I also tried nulling `year_end == next-event-start` (false contiguous spans). Spot-checking against source caught it **destroying legitimate ranges**: "served in East Africa campaign, **1914-16**" and "Clerk in public treasury, **1859 to 1865**" are real source ranges, but the next post starts the same year the prior ended (normal career flow), so the rule nulled real data. **Removed.** Lesson: any year rule that can't see the source must be provably non-destructive — `ye==ys` is; `ye==next-start` isn't.

**New patterns this round (folded into postnorm where safe):**

| Pattern | Cat | Action |
|---|---|---|
| Rank/title in given_names (`CAPT.`, `MAJ.-GEN.`, `ADMIRAL`, `LORD`, `RIGHT REV.`, `Bt.`) | NAME_PARSE | postnorm strip (added `Bt.`) |
| `secon.` (secondment) / `acctt.` (accountant) → `is_acting=true` | ACTING_FLAG | postnorm acting-recompute |
| ditto/`acted as` carrying acting → `is_acting` should be true | ACTING_FLAG | postnorm acting-recompute |
| `Hon. Frederick` → fabricated honour `"honorary F"` | HALLUCINATION | postnorm drops honorific-fragment awards |
| Order's `Mily.`/`Civ.` division split into its own award | HONOUR | postnorm folds suffix back |
| `place_inherited=true` with an explicit *different* place | INHERITANCE | postnorm clears flag |
| **Concatenated multi-bios** (one OCR entry = 2–6 people; only first structured) | OTHER | **data hygiene — see below** |
| War/campaign/unit/language as `place` (`Gallipoli`, `S. African war`, `T.T.`, `Swahili`) | WRONG_PLACE | **grounding stoplist — see below** |
| More ambiguous pre-expansions (`pol.`=political/police, `comm.`=commerce, `prot.`=protector, `treas.`=treasury, `coun.`=counsel, `lab.`=laboratory, `dep.`=department, `Sec. Sch.`=secondary) | POSITION_GARBLED | future pre-LLM list |

## postnorm coverage after round 3 (verified on the unseen 300)

`normalize_struct` changes **53% of structs** (158/300, 633 changes), idempotent, source-free:
`year_end_null` 350 · `inheritance_fill` 175 · `inheritance_flagfix` 38 · `given_names_strip` 36 · `ditto_resolve` 12 · `acting_fix` 10 · `honour_fragment_drop` 6 · `knight_bachelor` 5 · `honour_mily_fold` 1.

## Residual that postnorm/validate CANNOT fix (next-stage work)

1. **Concatenated multi-biographies** — the highest-value residual. An OCR-merged entry holds 2–6 distinct people; structuring captures only the first, so the rest are **missing persons** (~1% of entries seen, one held 6). This is a **persons-spine data-hygiene gap**, not a structuring bug — detectable by counting `SURNAME,`-style headers per source entry. Should be logged/triaged before the KG is called complete.
2. **Place noise → grounding** — war names, unit abbreviations, month abbreviations, language names, and title fragments land in `place`. These would pollute the Wikidata worklist; a **place stoplist/sanity guard belongs at the `ground` stage**, before lookups.
3. **Rare true model misses** — dropped early dated events (bar/legislative/conference), events in the education string, dropped despatch-mentions/degrees. Rare, mostly minor; candidates for a prompt revision only if re-structuring.

## Method note
Three rounds, 686 bios total: 6 reviewers ×31 (every-10th), 5 ×20 (sample-100), 12 ×25 (sample-300), each reading source-vs-struct (no string matching), on the API so the local vLLM job was unaffected. Re-runnable as the corpus grows: rebuild the sample and re-fan.
