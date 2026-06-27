# Knowledge-Graph Fixes — running list

Grounding / data-quality issues in the **CO + IOL knowledge graphs** surfaced while
building the interactive atlas. The atlas applies display-only workarounds (noted
below); the *proper* fix belongs in the KG place-grounding / emit pipeline. Keep
appending here — do not fix in the viz layer beyond cosmetic patches.

Legend: **viz-patched** = worked around in `build_static_atlas.py` for display only ·
**needs re-ground** = real grounding bug that mislocates data.

---

## Place grounding

### 1. Country over-collapse — colonies pooled into the modern sovereign country  ⚠️ needs re-ground
Several distinct colonies were grounded to one **country** QID, so their careers
all land at that country's capital instead of the real colonial seat.

| QID | true entity | wrongly absorbed (colony_label × count) | effect |
|-----|-------------|------------------------------------------|--------|
| **Q408** | Australia | Australia 434, Western Australia 82, Victoria 19, NSW 9, Swan River 7, Queensland 7, Tasmania 3 | all AUS colonies → Canberra |
| **Q833** | Malaysia | **Penang 1178**, Straits Settlements 2 (also shows "Sarawak") | Penang/Straits → Kuala Lumpur |
| **Q30** | United States | "New Hampshire Colony" 29, "Baker Island" 20 (raw = U.S.A./United States/America) | minor; refs really are the USA |
| **Q16** | Canada | Upper Canada 1623, New Brunswick 8 | Upper Canada / NB → Ottawa |
| **Q148** | China (PRoC) | "Weihaiwei" 58 (raw = "China") | China consular posts → Beijing |

> Note: Wikidata canonical labels are **anachronistic** for 1820–1966 (Q148 = "People's
> Republic of China", 1949) and P1813 short-names are ISO codes ("MYS"), so labels
> must be **curated by hand** (LABEL_FIX), not auto-pulled. Current curated set:
> Q16→Canada, Q30→United States, Q408→Australia, Q833→Malaya, Q148→China. The
> single-but-wrong cases (China→"Weihaiwei") are NOT caught by the >1-label detector.

- **Atlas workaround:** `LABEL_FIX` restores the canonical Wikidata label (Canada / United States / Australia / Malaysia) so markers are honest. Coordinates already correct *for the country* (capital seat).
- **Proper fix:** re-ground the absorbed surfaces to their own colony QIDs — e.g. Victoria → Q36687, New South Wales → Q3224, Western Australia → Q3206, Queensland → Q36074, Tasmania → Q34366, Penang → Q4730, Straits Settlements → Q1163660, Upper Canada → Q221045. Then each gets its own seat (Melbourne, Sydney, Perth, Brisbane, Hobart, George Town, Singapore, Toronto).
- **Detection query:** place QIDs with >1 distinct `colony_label` in `career_events.jsonl` (10 found; the 6 not listed here are benign era-variants — Bengal/Bombay/Madras Crown-vs-Company, Cape, Burma, Mesopotamia/Iraq).

### 2. `colony_label` is noisy / last-write-wins  (contributing cause of #1)
A single `colony_qid` can carry multiple `colony_label` values across events; the
emit/labels step keeps an arbitrary one. Prefer the QID's canonical Wikidata label,
or the most frequent consistent colony_label, when emitting place labels.

---

## Person grounding / dedup

### 6. `career_facts` person_ids not reconciled to deduped `persons.jsonl`  ✅ FIXED 2026-06-26
**Root cause was NOT a logic bug — `career_facts.jsonl` was simply STALE** (dated
2026-06-24, before the 2026-06-26 appointment-chain re-dedup). `career_events.jsonl`
and `role_edges.jsonl` were already clean (0 orphans); only the standalone
`career_facts.jsonl` predated the re-dedup, so it carried ~2,983 CO pre-merge ids →
"?" names + double-counting. The LadybugDB was always correct (it *synthesizes*
facts from `career_events` at load, not from this file).
- **Why it hadn't been regenerated:** `kg_emit_career_facts.py` still joined
  `employment_edges` by `(person_id, seq)`, but the re-dedup made employers
  PERSON-LEVEL (no seq) → the script crashed on regen.
- **Fix applied:** updated `kg_emit_career_facts.py` — orgs are person-level now
  (org_id=None per event, mirrors `kg_load_ladybug.load_facts`), and made it
  `COL_KG_OUT`-aware. Regenerated **CO** (0 orphans, +647 transfers / +58 places
  recovered that the stale file lacked) and generated **IOL** career_facts for parity
  (0 orphans). Atlas now verified 0 orphan / 0 dup arcs; "?" 7.6% → 0.08%.
- The atlas's `build_canon()` attestation-fold is now redundant but kept as a
  defensive guard against future staleness.

### 7. Residual within-corpus person duplication  ✅ MOSTLY FIXED 2026-06-26 (cross-form dedup)
**Root cause:** `kg_dedup_stage3_candidates.py` blocks same-name groups on
(surname, FULL given_names), so two records of one person whose given-name *form*
differs — initials-vs-full (MACKAY "I. V. G." / "Iaan Vandin Gordon") or a 1-char
OCR token slip (PREVOST "...DE TEISSIER" / "...DE TRISSIER") — never land in the same
block and are never compared. The atlas corridor view surfaced this as inflated
counts (British N. Borneo⇄Gold Coast showed 9 officials, really 7).
- **Fix:** new `kg_dedup_crossform.py` — blocks on **surname only** and lets a
  STRONG SHARED CAREER EVENT drive the merge (Jim's steer). Name gate = initials↔full
  (`_names_compatible`) + OCR-tolerant token alignment (Levenshtein≤1 on tokens ≥5 ch).
  Safety gate = a shared exact appointment **(job@place@YEAR)** or a shared birth year
  — both defeat the **father/son dynasty** trap (e.g. the two George Leakes of WA, who
  share WA law offices in *different* years; `gap<0` overlap is NOT safe, since
  father/son careers overlap too). No-year/no-birth pairs go to a `.held.jsonl` review
  file, not auto-merged.
- **+ SURNAME OCR variants (2nd pass):** GREG/GREIG, THOMPSON/THOMSON, Mac/Mc, dropped
  headword letters (erguson/ferguson, alpy/valpy) land in *different* surname blocks,
  so block instead on a shared SPECIFIC appointment (job@place@YEAR) and require the
  surnames OCR-near (Levenshtein≤1, len≥4) + given names compatible. Stricter auto-gate
  (surname is the primary key): need ≥2 DISTINCT shared appointments OR a full
  (non-initials) given-name match OR a shared birth year; else HELD.
- **CANONICAL NAME selection (kg_dedup_stage3_apply.py):** the surviving record now
  takes the surname spelling carried by the MOST attestations (an OCR slip recurs in
  fewer editions) + the FULLEST given-name form (expands "I. V. G." → "Iaan Vandin
  Gordon"), instead of the old "member with most events". Surname and given may come
  from different members = best reconstruction.
- **Applied both corpora, 0 new over-merges, 0 grounding-QID conflicts:**
  **CO 30,080 → 28,216** (1,864 merges), **IOL 20,362 → 19,144** (1,218 merges). All
  edge layers re-emitted/remapped (0 orphans), both LadybugDBs + the atlas rebuilt.
  HELD for later review: CO 155 + IOL 64 weak pairs (no-year/no-birth, or surname-OCR
  initials-only with a single shared appointment; a few genuine father/son to keep split).
- **Still open:** **107 cross-corpus** dupes — same official in BOTH CO and IOL,
  unjoined (Norman, Willingdon). → person grounding / cross-corpus link (see #3).

### 3. Peerage-titled top appointees not grounded to Wikidata  (from earlier session)
Viceroys / GGs appear under peerage titles (DUFFERIN, WILLINGDON, MARQUESS OF…) and
were skipped by the surname-keyed person-grounding pass, so cross-corpus bridges
(CO Canada governor ↔ IOL Viceroy) can't be auto-joined. Willingdon is 3 distinct
ungrounded person_ids across CO+IOL. **Fix:** title-aware grounding pass to stitch
these and populate `wikidata_qid`.

---

### 5. Null-surname person records  (minor)
Some persons have `surname=null` and render as "?, GIVEN NAMES" in the atlas (and
sort first in lists). OCR/parse gap in the bio-name extraction. Low priority; viz
could fall back to given-names display.

---

## Coordinate seats (mostly handled in viz, note for KG)

### 4. Seat-of-government vs centroid — handled in atlas, consider porting to KG
The atlas resolves each place to its capital (Wikidata **P36 → P625**) so officials
land at the administrative seat, not the geographic centroid (`improve_place_coords.py`).
17 tiny princely states still fall back to centroid (seat ≈ centroid there). If the
KG/LadybugDB ever needs coordinates, reuse `resolve_seats()` rather than raw P625.
