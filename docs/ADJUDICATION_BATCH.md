# Consolidated Nibi adjudication batch — RUN AND APPLIED

*2026-07-11. Executes docs/IOL_NEXT_SESSION.md items 1-3. Batch ran as
Nibi job 17521812 (10 min: 6 model load + ~3.5 inference) and the full
apply cycle is DONE — see "Applied" at the bottom. Check green on the
new baselines.*

## Applied (same day, job 17521812)

- **Verdicts**: A6 9 same / 6 different (4 recorded as ledger `split`
  rows so the screen stops re-flagging; the GHAZANFAR ALI KHAN refutation
  was overridden — same name+birth+O.B.E. 1918, judge split on "Cent.
  Provs vs Nagpur", Nagpur *is* the Cent. Provs capital); exits 13
  namesake death-links suppressed, 129 ambiguous events promoted, 2
  events-after-death confirmed (1 benign edition-lag singleton, 1 fusion
  candidate parked as a `review` ledger row); roll conflicts 9 adopted /
  23 namesakes; births 94/94 repaired on-menu.
- **Ledgers**: `merge_decisions.jsonl` (+14: 8 add, 1 override-add, 4
  split, 1 review), `exit_link_overrides.jsonl` (142, consumed by the
  now-override-aware `iol_link_exits.py`), `person_overlays.jsonl`
  (2,648: 105 birth_year, 479 honour_year, 2,064 death_date) consumed by
  `kg_dedup_stage3_apply.py --overlay` (new flag; ids resolve through
  the map so absorbed targets land on canonicals).
- **Rebuilt**: map 11,104 rows → **19,342 persons**, KG re-emitted,
  education worklist re-fanned. Screens post-apply: **A2 105→0, A7
  15→2, A6 residue 1 pair** (genuinely new; next batch). Baselines
  updated in-commit; `iol_identity_check.py` green.
- **Civil**: res_civil applied at extraction (`llm_reparse` 4,440
  records, `llm_unparseable` 1,246 kept+flagged); layer now **115,571
  records**, residue 4,228→1,135 flagged (1.0%), 522 unique lines left.
  Civil linker on rebuilt everything: 38,214 links / 6,383 persons;
  gradation linker: 3,152 identities linked, 1,097 pre-1886 extensions.

## What was built this session

1. **Roll↔bio honours join** (`iol_link_rolls.py`, new): the honours-roll
   layer (81,435 grade-roll entries) joined to the person table's 4,299
   Indian-order honours on tiered name keys (full-name, then surname with
   a given-name-compatibility gate). Results
   (`data/iol/identity/roll_links.jsonl`, report `ROLL_LINKS.md`):
   - **agree 1,964** — 98% of matched dated bio mentions match the roll
     exactly: external validation of both layers;
   - **date_fill 624** — undated bio honours receiving a unique roll date
     (**470** with a single claimant person = the safe overlay set);
   - **conflict 32** — dated mentions that disagree with a unique roll
     date (the garbled-year queue). The kickoff's "282 conflicts" were
     mostly namesakes: 137 rows where the given names contradict the roll
     are excluded deterministically (plus 68 fill-side, 52 agree-side).

2. **Worker modes** (`nibi/qwen_classc_worker.py`): `iolexit` (casualty
   event vs person; death is decisive), `iolroll` (roll entry vs bio
   honour; roll date authoritative when same person), `iolbirth`
   (pick among candidate OCR birth repairs; returns `birth_year`).

3. **Worklists** (`iol_build_adjudication_batch.py` →
   `data/iol/identity/adjudicate/`, ids pool-prefixed):

   | worklist | prompts | pool | mode |
   |---|---|---|---|
   | wl_dedup.jsonl | 15 | A6 same-honour duplicate pairs (rebuilt table) | ioldedup |
   | wl_exit.jsonl | 547 | A7 events-after-death 15 + exit-ambiguous 253 events × candidates (532) | iolexit |
   | wl_roll.jsonl | 32 | roll-date conflicts | iolroll |
   | wl_birth.jsonl | 94 | A2 multi-candidate birth repairs | iolbirth |
   | wl_civil.jsonl | 2,213 | civil-list residue raw lines (unique) | (parse worker) |

4. **Civil-list Ditto fix** (in-parser, `iol_civil._resolve_ditto`):
   connector-aware splice against the preceding office in-block
   (" to "/" of "/comma tails, head-noun alignment for bare
   "Assistant do."), chains resolved in order, coholder runs skipped.
   Layer rebuilt: **3,044 resolved** (`ditto_resolved` flag), 7
   unresolved at block starts, 57 multi-ditto leftovers → residue
   worklist. `raw_line` cap raised 300→1200 chars (11,050 records were
   truncated; 121 giant lines remain at cap).

5. **Civil residue worklist** (`iol_civil_residue.py`): 4,228 flagged
   records (3.5% — fragment names 2,191, mis-split punct 1,569, overlong
   offices 334, prose leaks, ditto leftovers) → 2,213 unique raw lines
   for `nibi/qwen_civil_parse_worker.py` (new; office—holders JSON,
   resumable, validated).

## Run (user, on Nibi)

```bash
# from col_matching root, locally:
scp data/iol/identity/adjudicate/wl_*.jsonl \
    nibi:~/projects/def-jic823/qwen_roster/
scp nibi/qwen_classc_worker.py nibi/qwen_civil_parse_worker.py \
    nibi/qwen_iol_adjudicate.slurm nibi:~/projects/def-jic823/qwen_roster/
# on nibi:
cd ~/projects/def-jic823/qwen_roster && sbatch qwen_iol_adjudicate.slurm
# afterwards, locally:
scp 'nibi:~/projects/def-jic823/qwen_roster/res_*.jsonl' \
    data/iol/identity/adjudicate/
```

~2.9k prompts; minutes of GPU after model load (walltime 1h is generous).
Resumable — resubmit to continue.

## Apply plan (next session, after results return)

One overlay cycle, ledger discipline throughout (append-only,
ACCUMULATIVE; screens rerun post-apply; baselines updated in the same
commit as any rebuild):

- **res_dedup** same → union rows in `merge_decisions.jsonl` (the A6
  path used for the 28 unions last cycle).
- **res_exit** a7:: different → drop the exit link; same → over-merge
  candidate (person continues after death) → split queue.
  exitamb:: exactly one candidate "same" → promote to `exit_links.jsonl`.
- **res_roll** same → adopt roll date for the bio honour (overlay);
  different → keep bio year, mark namesake.
- **res_birth** repair → birth-year overlay row (with the 11
  single-candidate A2 rows that skip the judge).
- **Deterministic overlays ready now, applied in the same cycle**: 2,058
  death dates from `exit_links.jsonl`, 470 safe roll date_fills, 11 A2
  repairs.
- **res_civil** → rewrite flagged civil records keyed by `raw_key`
  (`data/iol/civil/residue_records.jsonl` maps lines → records).
- Rerun `iol_link_exits.py` + all screens + `iol_identity_check.py`
  after the person-table overlay apply.

## Bios-fix cycle (2026-07-12, follow-on)

Three extractor fixes (max-span section rule, no-comma headwords,
mid-text splits — commit 5817c47) recovered 7,856 bios: 5,851 from the
iliol_1930/1911 truncations, 266 + 1,755 de-swallowed (the mid-text pass
recovers the swallowed VICEROY peerage entries: Ampthill, Cromer,
Cranbrook...). Corpus 265,959 bios -> 30,257 stage-2 chains. Structuring
delta was small — cumulative bios mean recovered attestations mostly
extend existing chains — 2,066 chains re-structured on Nibi (17538390 /
17539777 / 17539820), 1,438 never-deduped delta pairs judged
(17539869: 1,247 same), all folded through the accumulative ledgers.
Final: **19,513 persons, 125,297 events**, roll agreement 99%, check
green on baselines 30,252 / 10,739 / 19,513 (A2 8, A7 4 = next batch's
pools, arrivals from the recovered bios). 5 monster segments (170-330KB
accumulator run-aways) remain unstructurable — segmentation cap queued.
GOTCHA for reruns: `kg_textchain_dedup.py --write` is CWD-relative;
pass the full data/iol path.
