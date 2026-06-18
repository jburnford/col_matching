# Unmatched-matching LOOP — resume here (handoff 2026-06-17c)

## 2026-06-17c: `dedup_early_career` (compile pass E) DONE — 1,051 dup fragments collapsed, 0 FP
Jim's ask: improve dedup using richer variables (schooling, jobs, ranks, locations), weighted to the
EARLY career ("first quarter/half of the LONGEST form of the potentially matching bios") where
duplicate fragments still agree before careers accumulate/diverge. BUILT as a new **compile pass E**
(`compile._early_career_same_person` + the pass-E block in `compile_biographies`; env
`COL_NO_DEDUP_EARLY=1` reverts). Aggressiveness = **birth-year-tolerant** (Jim's choice). Built in TWO
rounds — base (education) then extended (tail signals) — both 0 FP.
- **Block**: (spelled-forename token + surname SUFFIX[-4:]). A dropped headword prefix
  (Griffiths→FFITHS) preserves the suffix, so this reaches the garbled/truncated-surname duplicates
  that pass A (surname+initial block) and passes B/C (birth-year-required) all MISS.
- **Merge = `_early_career_same_person`, FOUR independent acceptance paths** (all require an
  `_early_window_overlap` event — events agreeing year±1 + place/position within the first HALF of the
  longer entry's career span; the year-aligned event is the father/son guard, two generations can't
  hold the same post the same year):
  1. `em>=2 AND education_sim>=85` (education near-unique; early events alone too generic);
  2. `em>=1 AND full_name_equal` (exact multi-token given name, OCR-tolerant — the big tail win);
  3. `em>=1 AND shared honour-year`;
  4. `em>=1 AND shared death/terminal-year`.
- **Birth-year tolerant**: NOT a hard block (the old hard block over-split same people whose birth year
  was OCR-noisy — e.g. LINDSELL 1885/1886 with 16 shared events). A large, non-one-digit birth gap
  (possible father/son) still demands `em>=2 OR honour-year OR terminal-year` (a 2nd corroborator).
- **Result**: 1,071 merges; biographies 30,319→29,268 (1,051 duplicate fragments collapsed).
  eval_known **0 FP both levels**, gold `career_splits` IMPROVED stint 11→5, record 14→11 (pass E
  consolidates gold-career fragments, doesn't mis-merge). candidates reconcile 0. Coverage 47.9%→48.2%.
- **Validated**: of 908 new merged groups, all 36 with name "contradictions" were manually confirmed
  SAME person — the contradictions are OCR garbles / title-abbrevs ("Sir"→STR/SIE, "Capt"→CART,
  "Earl of"→EARLOR) / dropped middle names (Winston Leonard Spencer vs Winston Spencer Churchill;
  Stanley Melbourne Bruce). The other 872 have fully-agreeing names. OCR-memory cases all merged:
  MACHO→Camacho, RNESS→Furness, STWOOD→Eastwood, WINSTEKT→Winstedt, SHERWOOD→Isherwood.
- **Coverage RATE barely moves — and that's expected**: dedup removes duplicate noise from BOTH the
  matched numerator and the bio denominator. The win is DATA QUALITY: 1,051 fewer spurious "distinct
  people". `measure_situation.py`: dup-of-matched noise 3,658→3,157 (−500).
- **Calibration harnesses (the key method)** `measure_dedup_signal.py` + `measure_dedup_tail.py`: label
  same-surname + shared-spelled-forename pairs by birth year (equal=pos, diff=neg), then RE-segment the
  negatives — small/one-digit-OCR birth gaps are SAME person, only large multi-digit gaps are true
  father/son. This proved (a) early career alone too generic, (b) education / full-name / honour-year /
  death-year make the conjunction near-unique, (c) birth-year is itself OCR-noisy. EVERY "false merge"
  in both harnesses turned out to be a same-person OCR-birth-noise pair → true FP ~0.
- **CAVEAT — compile non-determinism**: compile has ~0.1% run-to-run drift (±37 bios). PYTHONHASHSEED=0
  does NOT fully fix it; source unidentified, PRE-EXISTING. Does NOT affect correctness — merge
  predicates are deterministic, eval_known gates 0 FP every run.
- **Remaining dedup tail ~3,157**: still duplicates of a matched person but the fragments carry only
  INITIALS (no spelled full name) and no honour/death year + no shared career event — nothing
  discriminating enough to separate from a namesake at 0 FP. LLM/human-review territory, not a
  deterministic lever. Pre-pass-E backups in `/tmp/dedup_backup/`.

# Unmatched-matching LOOP — resume here (handoff 2026-06-17b)

## 2026-06-17b: `truncation_surname` lever DONE — +1 union net, 0 FP (built, gated, modest)
Deterministic prefix-truncation-tolerant surname path for the OCR headword-truncation class
(memory `unmatched-ocr-root-cause.md`: Griffiths→FFITHS, Camacho→MACHO — services-section bold
entry-header loses its first 1-3 chars; the CLEAN record surname already exists). A bio surname
that is a clean SUFFIX of an official surname (dropped prefix 1..3, len≥5) is matched only with
strong same-person corroboration. Built per the approved plan
(`~/.claude/plans/cheaper-alternative-before-re-ocr-sparkling-kahn.md`):
- `match.py`: `_truncation_index`/`_truncation_block` (built once, O(officials)); `_align(trunc=True)`
  requires a SHARED SPELLED forename (the key FP guard — excludes initials-only OWELL→Powell/Howell)
  PLUS printed position ≥ `TRUNC_POS`(70) / shared honour / ≥2 cooc; −20 fuzzy penalty kept.
  Constants `MAX_DROP=3, MIN_TRUNC_LEN=5, TRUNC_POS=70`; env `COL_NO_TRUNC=1` reverts.
- `attach.py`: parallel suffix branch (`rsur.endswith(bsur)`, drop 1..3, len≥5) with the same guards;
  also gated by `COL_NO_TRUNC`. Marks attachments `trunc_surname=True`.
- `candidates.py`: mirrors the trunc retrieval (reconciliation — `phase1_matches_not_reproduced` = 0).
- **Bonus fix 1 (`match._disambiguate`):** `by_bio_colony` now applies exact-outranks-fuzzy (mirrors
  the `by_stint` rule) — a weak fuzzy/trunc candidate must not knock out a strong EXACT match for the
  same bio+colony. Caught the `oryndon` regression (CORYNDON's truncated backfill stint vs the clean
  Coryndon trunc candidate both basutoland → ambiguity dropped the good exact match). Strictly safer
  (keeps the stronger evidence), 0 FP.
- **Bonus fix 2 (`cli.cmd_candidates`):** now applies `apply_recovered_places` like `cmd_match` does
  — without the overlay, recovered-colony matches couldn't reproduce and reconciliation was spuriously
  3151. Now 0.

**WHY THE GAIN IS TINY (+1 net union, not the ~17% the class suggested):** `measure_truncation.py`
shows 1,508 unmatched placed bios HAVE a truncation candidate, but only 16 pass the (mandatory, for
0-FP) shared-spelled-forename + printed-pos≥70 guards, and only **1 nets new union** (`evens_percival`
EVENS→Stevens, Trinidad). The match.py stint path adds **0** live stint matches: every truncated
headword that passes is a DUPLICATE fragment of a person already matched via their CLEAN-edition
headword, so exact-outranks-fuzzy correctly dominates. The +1 + 1 more (rench→French NSW, already in
union) come from the attach.py record path. **Conclusion: the OCR-truncation class, once you require
same-person corroboration (which you MUST to avoid false merges), is dominated by duplicate fragments
of already-matched people — it is correct but yields little NET union, and re-OCR would be bounded the
same way.** Spot-check of all 18 accepted pairs: every one a genuine truncation (FFITH→Griffith,
ITZPATRICK→Fitzpatrick, MENTI→Clementi, WETTENHAM→Swettenham...), no short-suffix namesake pollution.
Do NOT loosen the shared-spelled-forename guard to chase the other ~1,490 retrieval candidates — that
reintroduces the initials-only FP class the 543-career eval_known is too small to catch.

# Unmatched-matching LOOP — resume here (handoff 2026-06-17a)

Goal: drive down the count of unmatched biographies by diagnosing random unmatched
bios, fixing the **root-cause class** (not the instance) so each fix cascades, re-running
the pipeline, and never regressing the 0-FP gate. Keep `match_issues.html` updated as the
living log of hard / LLM-heavy classes.

## Current state
- **Matched union: 14,508 / 30,319 bios = 47.9%** (was 12,508 / 41.2% at session start; +2,000 across
  7 levers this session, all 0 FP). Levers: ambiguity_guard +533, inherited_position +604,
  federation_rollup +333, single_colony_fill +235, sa_eastafrica_rollup +134, prose_colony +107,
  bracket_colony +54.
- **`federation_rollup` lever DONE: +333 union, 0 FP.** `gazetteer.PLACE_ALIASES` territorial
  groupings, surfaced by scanning colony_fail cases for (bio_colony→record_colony) pairs that
  WOULD pass tenure+position (the scan also surfaced namesake noise like tanganyika→FMS — those were
  NOT added; only territorially-justified groupings). Added: Leeward Islands (antigua/stkitts/nevis/
  dominica/montserrat/virginislands), Windward Islands (grenada/stvincent/stlucia/barbados/dominica),
  trinidad↔trinidadandtobago, eastafricaprotectorate→eastafrica, kenya/uganda→kenyaanduganda,
  tanga→tanganyika, Australian states→australia. Spot-check clean (Boucaut→australia, Laborde→Windward,
  Sciortino VI→Leeward). The scan (in transcript) is the repeatable method for finding more.
- **`single_colony_fill` lever DONE: +235 union, 0 FP.** Extended `apply_bracket_places`: if every
  placed event in a bio shares a common colony target, fill ALL its place-less dated events with that
  colony (leading/trailing too, not just two-sided brackets — HUMPHRYS all-Antigua career). Multi-
  colony bios keep the strict between-two-same-colony bracket. Spot-check clean.
- **`sa_eastafrica_rollup` lever DONE: +134 union, 0 FP.** Territorial-evolution
  gazetteer roll-ups (`PLACE_ALIASES`): South-African provinces → Union of South Africa
  (transvaal/capeofgoodhope/capecolony/capeprovince/natal/orangefreestate/orangerivercolony →
  {southafrica, unionofsouthafrica}, additive) and bare "East Africa" → {kenya, eastafricaprotectorate}.
  Bio names the province, record filed under the union/successor; the roll-up makes colony compatible
  and tenure+position+initials still re-gate. Spot-check clean (Hofmeyr, Shenton Thomas, Beyers →
  correct Union/Kenya stints). Re-run infer_colony→attach→match.
- **`inherited_position` lever DONE (handoff 2026-06-17a): +604 union, 0 FP.** Biggest lever after
  ambiguity. An inherited place is normally weak (can only ADD support, never establish a match —
  the carry may span a missed colony change). BUT a near-exact position match
  (`HIGH_POS_INHERITED=85` token_set_ratio) on top of exact surname+initials+colony+tenure is strong
  independent evidence the carry is correct, so the inherited event is PROMOTED to printed-quality
  in `match._align` (env `COL_NO_INHERIT_POS=1` reverts). TURNER (motivating case): HK printed 1948
  then an inherited tail; the 1955 HK "Assistant Commissioner" stint matches at pos 100 but was
  rejected because only inherited events overlapped it. Stricter than the normal printed bar (60),
  so promoted single-initial matches are safer than ones the matcher already accepts. Spot-check of
  the +1,052 stint bios was clean (Smith "Reginald Montague Bosworth"→Basutoland, Pelletier C.A.P
  →Canada). Only `match` re-run needed.
- **`bracket_colony` lever DONE (handoff 2026-06-17a): +54 union, 0 FP.** A place-less dated event
  bracketed (by year) between two placed events resolving to the SAME colony is attached to that
  colony (continuous-career interpolation; the compiled bio concatenates editions so within-entry
  inheritance can't span gaps). `infer_colony.apply_bracket_places`, called inside
  `apply_recovered_places` AFTER the record overlay (so it can use just-recovered endpoints). NO
  recompile / infer_colony rerun needed — runs at attach/match load time; just re-run attach+match.
  RUSHTON (motivating case): WA 1896 + WA 1919 bracket place-less 1901 railway-secretary clauses →
  tenure overlaps the WA 1905-17 stint the raw OCR confirms → matched (pos 100, cooc 5yr).
  `measure_bracket.py` = harness (330 events/180 bios ceiling; realized +54 — many bracket bios are
  colonial politicians whose only records are backfill-synthetic & fail position).
- **`prose_colony` lever DONE (handoff 2026-06-17a): +107 union, 0 FP** (also −39 dup bios from
  better dedup). This was ADJUDICATION_GUIDE §0 lever #1. Root cause: `rules_parse` resolves a
  place only from a clause's LAST comma segment; a colony stated mid-clause ("puisne judge,
  Uganda, and mem. ct. of appeal, 1934") was dropped → event went place-less/wrongly-inherited.
  `compile.recover_places_from_prose` (called in `cmd_compile` after `recover_places_from_positions`)
  scans the NON-last comma segments of each dated place-less/inherited event's `text_span` for a
  gazetteer colony and attaches the first hit as printed-quality. Recovered 3,755 places; only ~122
  had a matchable record (`measure_prose_colony.py` = harness; the rest are colonial politicians /
  local officials NOT in the imperial staff lists — same placeless ceiling). Safe like infer_colony:
  the recovered place only PROPOSES a colony; `match` re-gates colony+tenure+position+ambiguity, so
  a mis-attached colony can't force a wrong match. Spot-check clean (Francis→Uganda puisne judge).
  Requires full chain (compile→infer_colony→attach→match); augment_officials is NOT needed (officials
  unchanged). Note: bio denominator shrank 30,358→30,319 because the better place data merges more
  duplicate fragments in compile.
- **`ambiguity_guard` lever DONE (handoff 2026-06-16d): +533 union, 0 FP.** This was
  ADJUDICATION_GUIDE §0 lever #2 — the deterministic levers were NOT fully exhausted. Root
  cause: `match._disambiguate` treated SAME-ENTITY pairs as genuine contests and dropped them.
  Three safe refinements (all in `match._disambiguate`, gated on the same-person/same-official
  tests; env `COL_NO_AMBIG_REFINE=1` reverts to the old guard for measurement):
  (a) **by_stint duplicate-fragment keep** — when every bio contesting one stint is a confident
  duplicate of the others (shared SPELLED forename, OCR-tolerant via `_shared_spelled_forename`)
  AND each matches the stint's official name TIGHTLY (`_tight_name_match`: initials EQUAL after
  honorific strip, or shared spelled forename — NOT a deficient subsequence), keep all the links
  (Brewin "Winbolt"/"Wimbolt", Vigors "dogné"/"dogne" — one person, many fragments).
  (b) **by_bio_colony same-official keep** — when a bio's two same-colony stints are the SAME
  official re-listed with a printed honorific/initial variant (`_same_official`: equal initials
  after stripping `_HONORIFICS`, or shared spelled forename), they corroborate, don't contest
  (Drew "John Michael"/"The Hon. J. M."; Hill "S. J."/"Col. Stephen J.").
  (c) **tight-beats-loose** — when a bio matches several same-colony stints and ≥1 is name-tight,
  drop the ones matched only via a LOOSE initial-deficient subsequence — they are namesakes
  `_align`'s loose name gate let through (the classic **de Kretser** trap: "Edward" [E] must NOT
  attach to the "H. E. S" stint, but DOES attach to its tight "E" stint). This both removes a
  latent FP class and is what keeps the gate at 0 FP. `measure_ambiguity.py` = the sizing harness;
  78 secondary namesake links were correctly pruned (0 bios became unmatched). `ambiguity_drop`
  class fell 9%→2% (now genuine different-person contests + single-initial residue).
- **`position_fuzz` lever DONE (handoff 2026-06-16c): +1,146 union, 0 FP.** Root cause: the
  stint matcher (`match.py`) and the candidate annotator (`candidates.py`) scored position
  with plain `_norm`, while `attach.py` already used `_pos_norm` (abbreviation-expanded). Wired
  `_pos_norm` into both position-scoring sites in `match.py` (`_align` + `_cooc_scan`) and into
  `candidates._annotate` (so the classifier matches matcher reality). THEN fixed `_pos_norm`
  itself to split on hyphens/slashes (`re.sub(r"[-/]"," ",…)` before `_norm`) — it was deleting
  them and fusing words ("surveyor-general"->"surveyorgeneral"), hiding tokens AND their abbrev
  expansions. NOT a bar change (60 still stands); position is one corroborating dimension on top
  of exact-surname+initials+colony+tenure+printed-place. Spot-checked the 60-72 band: all clean
  (HOPPS,H.D.~Hopps,H.D.; res.mag.~Resident Magistrate). `_pos_norm` is shared by compile's
  dedup, so the WHOLE chain was re-run; gate stayed 0 FP, positives-linked rose (stint 233->255,
  record 191->199). `measure_posfuzz.py` is the measurement harness.
- **`fuzzy_surname` lever DONE (handoff 2026-06-16b).** Widened both fuzzy-surname gates from
  dist-1 to dist-2 for short surnames: `match._surname_block` (`max_dist=2` for all len≥5)
  and `attach.py` (`len≥6 & dist≤2`). The matcher's `_align(require_strong=True)` and
  attach's exact-colony+year+position≥60 bars still govern; **added a positive-initials
  guard in attach for fuzzy hits** (record must carry agreeing initials — `_initials_compatible`
  passed vacuously on dash-forename records like "— Sanders", a dist-2 common-surname FP hole).
  Net +92 union bios, all genuine OCR garbles (BLACKMORR~Blackmore, DOBIGHGIN~Dowbiggin,
  PAILTHORPE~Palthorpe). Gate stayed 0 FP both levels. Residual `fuzzy_surname` (~24% of
  sample) is now the hard tail: below-bar corroboration / len-5 / disambiguation drops — needs
  LLM adjudication, not a wider block.
- **`col-services eval_known` = 0 false positives at both levels.** This is the prime
  directive — re-run it after EVERY matching change; it must exit 0. A missed link is
  recoverable, a wrong merge is not.
- **CRITICAL:** the live `matches/*.jsonl` were produced with `COL_USE_AUGMENTED=1` (the
  backfill-augmented match target). **Always `export COL_USE_AUGMENTED=1`** for the loop, or
  attach/match silently revert to the base Neo4j fetch (~7k matched) and you'll think things
  regressed.
- Nothing is committed. Files persist on disk between sessions.

## Resume (read-only diagnosis)
```bash
cd ~/col_matching && export COL_USE_AUGMENTED=1
python3 classify_unmatched.py --n 240 --seed 0   # -> rewrites match_issues.html (distribution + fix evidence)
python3 diagnose_unmatched.py --seed 7           # deep single random bio; also --bio <id> / --decade 1900
```

## After a fix, re-run the chain (order matters), then gate
```bash
export COL_USE_AUGMENTED=1
python3 -m col_match.services.cli compile          # only if parser/dedup/gazetteer-place changed
python3 -m col_match.services.cli augment_officials # only if backfill/synth changed
python3 -m col_match.services.cli infer_colony      # regenerate Tier A recovered_places
python3 -m col_match.services.cli attach
python3 -m col_match.services.cli match
python3 -m col_match.services.cli eval_known        # MUST be 0 FP (exit 0)
python3 classify_unmatched.py --n 240 --seed 0      # refresh the log, watch the drop
```

## DETERMINISTIC LEVER STATUS (updated 2026-06-17a) — NOT exhausted; keep looping
Do NOT declare deterministic levers "exhausted" — that call has been wrong twice (the ambiguity
guard and bracketing were both found AFTER an exhaustion claim). The method that keeps working:
READ random unmatched bios with `diagnose_unmatched.py --seed N`, find a recurring structural miss,
measure it (`measure_*.py`), build it gated to 0 FP. Levers harvested so far: ambiguity_guard
(+533), prose_colony (+107), bracket_colony (+54). **Open lever candidates surfaced by sampling
(NOT yet built):**
- **Mc/Mac (and other prefix) dedup miss** — `mcgregor_gregor_e1907` is an unmerged duplicate of
  the MATCHED `macgregor_gregor_e1907`; merging unlocks the unmatched fragment. compile pass C is
  OCR-tolerant (dist≤2) but needs 2 event anchors / shared birth year; thin fragments slip through.
  Candidate: a targeted Mc↔Mac surname-normalization merge pass (gate 0 FP). Measure first.
- **extraction_gap with confirmed OCR** — BARROW C.M.M. is in raw OCR (Tanganyika 1961, "Principal
  Immigration Officer", initials match) but the record was never synthesized into officials_augmented.
  This is the backfill lever; `--include-surname-only` is gated (wrong-person risk) but the
  initials+position-confirmed subset is low-risk — worth measuring as a SAFE backfill tier.
Beyond these, the placeless/raw-OCR ceiling below holds and the LLM/decision classes need Jim's call. Smaller deterministic polish still possible (gazetteer
roll-ups for specific sub-colonies, more `_HONORIFICS`) but no large cascading lever remains.

## PLACELESS/RAW-OCR CEILING (measured 2026-06-16c — still valid)
`placeless_strong` was investigated and is NOT a deterministic lever. `measure_placeless.py`:
of placeless strong-position events on unmatched bios, **26,487 (8,260 bios) have NO graph
record** at (surname, year±2) — recovering the place can't lift a match with nothing to match
against. Only ~548 are single-colony/pos≥60 (mostly held in Tier A's review tier by the FP
guard); 3,234 are genuinely multi-colony ambiguous. **Tier B `infer_colony --raw-ocr` was RUN**
(now the diagnostic in `inference_report.md`): of 39,817 no-record place-less clauses, **72%
(28,699) have the surname absent from the OCR entirely** (military/London/pre-coverage/garble —
the structural ceiling), 15% multi-colony, 12% weak-position, and only **664 clauses / 554 bios
(1.7%) are cleanly recoverable** — and those point at OCR rows the graph never extracted, so they
need record SYNTHESIS (backfill), not just place recovery. Not worth a build for <2% of residue.

### What's left needs a DECISION from Jim (not a deterministic fix)
The residual unmatched are now dominated by classes no string/normalization change can move:
- **no_record / surname-absent-from-OCR (~big)**: not in the staff-list corpus. Hard ceiling.
- **namesake_no_record (~20%)**: only same-surname record is a *different person*. Correct non-match.
- **fuzzy-tail + position-semantic + ambiguity_drop (~45% combined)**: LLM-adjudication territory.
Two gated options, both needing sign-off: (1) backfill `--include-surname-only` to synthesize
records for surname-present cases (wrong-person risk; eval_known-gated); (2) LLM dossier
adjudication of ambiguity_drop/namesake/semantic cases — **NO GEMINI**; either in-session via
Claude Code (zero API cost, per-bio not cascading) or a sign-off'd metered backend with
cap+ledger. `candidates.py`/`dossier.py`/`adjudicate.py` are already built for this.

### (historical) earlier next-lever note — placeless sub-levers
`placeless_strong` = a strong-position event with NO place; `infer_colony` (Tier A) can't anchor
it because the colony is stated nowhere placed. Sub-levers: (a) Tier B `infer_colony --raw-ocr`
(coded, UNRUN) — reverse-look-up the colony from the raw staff-list OCR by (surname,year);
(b) widen `infer_colony` position floor only where a single colony is implied. Validate 0 FP.
`ambiguity_drop` (~9%, rose as more candidates pass-bar) = pass-bar exact candidates that the
ambiguity guard dropped because same-name competitors tie. These are the Fable/dossier-adjudication
targets (the `candidates.py` enumeration + `dossier.py` already exist) — but that path is
LLM/cost-gated (NO GEMINI; needs Jim's sign-off + capped estimate; can adjudicate in-session
via Claude Code). `diagnose_unmatched.py --decade 19xx` / `--bio <id>` surfaces examples.

### `position_fuzz` deterministic path is SPENT (done 2026-06-16c)
The abbreviation+hyphen normalization harvested ~1,150 union bios. Residual position_fuzz (~12%)
is now SEMANTIC (different words for the same role: 'specialist surgeon'~'Medical Officers',
'dir., commercial intelligence'~'Commissioner of Commerce') — a role-synonym map or LLM, NOT more
string normalization. Do NOT lower bar 60 (it was set by measured FPs).

### `fuzzy_surname` deterministic path is SPENT (done 2026-06-16b)
The safe, corroborated dist-2 garbles are harvested. Residual is below-bar (weak/no position,
single-initial, disambiguation-dropped). Do NOT widen the block further (dist-3 / len<5 / drop
the strong bar all measured or will measure FPs). LLM-adjudication territory, cost-gated.

## Issue distribution (match_issues.html — open it; of ~12.7k placed-unmatched, seed 0 n=240, 16d)
| class | % | status | note |
|---|--:|---|---|
| fuzzy_surname | 34 | hard-tail | deterministic part DONE; residual below-bar / LLM. Now the dominant residual. |
| namesake_no_record | 22 | hard | only same-surname record is a different person elsewhere |
| placeless_strong | 12 | medium | strong position event, no place; raw-OCR ceiling (see below) |
| no_record | 11 | hard | not in service / OCR-garbled |
| position_fuzz | 8 | hard-tail | deterministic part DONE; residual is SEMANTIC synonyms / LLM |
| other | 4 | hard | exact cand passes colony+tenure+pos but no match (investigate) |
| extraction_gap | 4 | **llm** | surname in OCR, never extracted; grade-list re-extraction (metered) |
| ambiguity_drop | 2 | done | was 9% — `ambiguity_guard` lever harvested it; residue = genuine diff-person / single-initial |
- Duplicate bio present fell ~28%→16% of sampled (the lever now keeps duplicate fragments matched
  together). Remaining duplicates: compile's two-anchor rule is deliberately conservative; thin
  fragments still won't MERGE (but both now match the same stint, so both are in the union).

- **federation_rollup + sa_eastafrica_rollup + single_colony_fill** (see Current state). The
  colony_fail-scan method (tally bio→record colony pairs that would pass tenure+position; add only
  the territorially-justified groupings, skip namesake noise) is the repeatable way to find more
  roll-ups. MEASURED DUDS — do NOT add: British Guiana counties (5 bios), Rhodesia/Nyasaland
  federation (0 bios). colony_fail is still 22% of unmatched but the residue is mostly genuine
  namesakes (same surname, unrelated colony = different person) — correct non-matches.
- **inherited_position promotion** (`match._align`, `HIGH_POS_INHERITED=85`). Inherited-place event
  with pos≥85 establishes a match. +604 union, 0 FP. Do NOT lower the 85 bar without re-gating (it
  is the precision margin compensating for the weak place). `COL_NO_INHERIT_POS=1` reverts.
- **bracket_colony interpolation** (`infer_colony.apply_bracket_places`). Place-less event between
  two same-colony placed events inherits that colony. +54 union, 0 FP. `measure_bracket.py`.
- **prose_colony place recovery** (`compile.recover_places_from_prose`, wired in `cmd_compile`).
  Scans non-last comma segments of dated place-less/inherited events for a mid-clause gazetteer
  colony; +107 union, 0 FP. 3,755 recovered, ~122 matchable (rest are non-staff-list politicians).
  `measure_prose_colony.py` is the harness. Do NOT widen to free-word scanning (FP-prone); the
  comma-segment + match-regate design is what keeps it at 0 FP.
- **ambiguity_guard same-entity refinements** (`match._disambiguate`: by_stint duplicate-keep,
  by_bio_colony same-official keep, tight-beats-loose namesake prune; `_HONORIFICS`,
  `_shared_spelled_forename`, `_tight_name_match`, `_same_official`, `_all_same_person`). +533
  union, 0 FP. `measure_ambiguity.py` is the harness. Do NOT loosen `_tight_name_match` (it is
  what blocks the de Kretser FP) and do NOT use bare initial-subsequence as a same-person test
  (single-initial collisions). Residual ambiguity_drop is genuine diff-person contests / LLM.
- **placeless_strong / Tier B raw-OCR investigated & RUN** — not a lever (see ceiling section
  above). `measure_placeless.py` + `inference_report.md` Tier B section hold the numbers.
  `recovered_places_rawocr.jsonl` (664 rows) is NOT applied to bios by design.
- **position_fuzz normalization** (`_pos_norm` wired into `match.py` `_align`+`_cooc_scan` and
  `candidates._annotate`; `_pos_norm` now splits hyphens/slashes). +1,146 union, 0 FP.
  `measure_posfuzz.py` is the harness. Residual is semantic-synonym, not string-normalizable.
- **fuzzy_surname dist-2 widening** (`match._surname_block` max_dist=2; `attach.py` len≥6 dist≤2
  + positive-initials guard for fuzzy). +92 union, 0 FP. `measure_fuzzy_widen.py` is the
  measurement harness if you want to re-inspect.
- Tier A place-less colony inference (`infer_colony.py`) + intra-bio multi-colony disambiguation.
- Malaya gazetteer roll-up + grounded `data/services/place_rollup.json` (capitals + empire KG).
  **Roll-up is SPENT** — the residual "missing roll-ups" are count-1 namesake noise.
- Backfill wiring: `augment_officials` → `graph_cache/officials_augmented.jsonl` (confirmed-only;
  `--include-surname-only` is the gated next option, wrong-person risk).
- Forename dedup (`_FORENAME_ABBREV`) + abbreviation place-recovery (`recover_places_from_positions`)
  in `compile.py`; directional place forms in `gazetteer.ABBREV`.
- CO-London extraction (Phase 3): decided AGAINST (only ~205 bios, mostly undated/non-CO/politicians).

## Cost discipline
Metered LLM work (grade-list re-extraction, the `llm` classes) needs a printed capped estimate
through the OpenRouter client and Jim's sign-off first. **Gemini is banned.**

## Tooling (repo root, all uncommitted)
`classify_unmatched.py` (batch classifier → `match_issues.html`), `diagnose_unmatched.py`
(deep single bio), `triage_unmatched.py`, `decompose_gaps.py`, `build_place_rollup.py`,
`check_brooke_wiring.py`, `diagnose_broadrick.py`, `diagnose_parse_loss.py`, `size_co_london.py`.
Memory: `colony-inference-built.md` has the full lever history.
```
