# Knowledge-Graph Fixes — running list

Grounding / data-quality issues in the **CO + IOL knowledge graphs** surfaced while
building the interactive atlas. The atlas applies display-only workarounds (noted
below); the *proper* fix belongs in the KG place-grounding / emit pipeline. Keep
appending here — do not fix in the viz layer beyond cosmetic patches.

Legend: **viz-patched** = worked around in `build_static_atlas.py` for display only ·
**needs re-ground** = real grounding bug that mislocates data.

---

## Place grounding

### 1. Pre-federation colonies grounded to the MODERN entity (state/nation), inconsistently across corpora  ✅ MOSTLY FIXED 2026-06-27
**FIX (2026-06-27):** `kg_reground_colonies.py` re-grounds already-cached colony
surfaces per a PERIOD-CORRECT, PLACE-TYPED rule (Jim), both corpora. IOL 42 / CO 13
surfaces. Verified on the atlas: Victoria→Q56850459 (Melbourne), India→British Raj
Q129286, Jodhpur→Q6207845, Baluchistan→Q3303188, Central Provinces→Q521864. The
colony layer (`resolve_colony`) auto-de-collapses since the new place_qid IS itself
a manifest polity (colony_qid = itself, not Q408). NB **India: IOL was already right
(British Raj); fixed CO to match** (opposite of "CO is reference"). Egypt: manifest
Q2474428 is a non-place "aspect of history" → forced Q79. Excluded city/annexed
false-matches (South Africa→BSAC, Patna/Surat/Benares cities, Oudh/Satara/Jhansi
annexed, etc.). STILL OPEN: Penang (deferred — Straits Settlements would mislocate to
Singapore), upstream manifest patches (Egypt entity, Cape Q4806993→Q370736, India
join), LadybugDB rebuild, LABEL_FIX trim. Original diagnosis below.

**Corrected diagnosis 2026-06-27.** There IS a foundational authority for this: the
**empire-evolution KG** `/home/jic823/empire-evolution-wpcs/data/qid_manifest.tsv`
(740 colonies; cols: colony_id, name, **wikidata_id** = the pre-federation entity,
**modern_nation_qids**, established_year, end_date, region, colony_type, capital,
successor_dominion). So `Q56850459` = "Victoria (Colony) 1851–1901" → modern Q408 is the
**CORRECT** historical entity, not a bug — the manifest deliberately models the colony,
not the modern state.

The real problem is **inconsistency + modern-collapse stragglers**:
- **CO** mostly joins the manifest correctly (match_type=`manifest`): Victoria→Q56850459,
  NSW→Q18348382, Queensland→Q28401203, Tasmania→Q5148519, WA→Q57676556, Upper Canada→Q795427,
  Straits Settlements→Q376178, South Australia→Q35715. **These are RIGHT (the colony entities).**
- **IOL** did NOT join the manifest → grounded the SAME colonies to **modern states**:
  Victoria→Q36687, NSW→Q3224, Queensland→Q36074, Tasmania→Q34366 (and Australia→Q408,
  China/Weihaiwei→Q148, Canada→Q16). **These are WRONG (modern, post-federation).**
- **CO MCP stragglers** that bypassed the manifest: **Penang→Q188096** (modern *state of
  Malaysia*, mcp_unverified) — manifest says penang_prince_of_wales_island = **Q1150673**
  (pre-1826 trading post) and post-1826 Penang ⊂ Straits Settlements Q376178.
- Generic country surfaces ("Australia" 427 ev→Q408, "Canada" 1557→Q16, "China" 54→Q148)
  are genuinely the nation in those bios — leave as nation OR flag ambiguous; not the bug.

- **Proper fix:** make BOTH corpora ground colony surfaces to the **foundational-KG
  manifest** entities (the pre-federation colony QIDs), date-aware where a surface spans
  the federation/cession boundary. CO is the reference; bring IOL into line + fix the CO
  Penang straggler. Re-run `kg_join_manifest.py` for IOL (check it's COL_KG_OUT-aware),
  patch the few MCP stragglers, re-emit both corpora, rebuild atlas, **drop LABEL_FIX**
  (entities will then be correct, so the display patch is no longer needed).
- **Secondary (surface-ambiguity, harder):** the bare surface "Victoria" has 5+ referents
  (Victoria BC / Australia / Cape / Hong Kong / Lake Victoria); grounding ALL "Victoria"→
  Q56850459 mis-attracts the non-Australian ones. Needs per-mention context (the official's
  other postings / colony) to disambiguate. Flagged earlier as Q56850459 attractor.
- **Atlas workaround still in place:** `LABEL_FIX` in build_static_atlas (display-only).

### 2. `colony_label` is noisy / last-write-wins  (contributing cause of #1)
A single `colony_qid` can carry multiple `colony_label` values across events; the
emit/labels step keeps an arbitrary one. Prefer the QID's canonical Wikidata label,
or the most frequent consistent colony_label, when emitting place labels.

### 8. Ceylon "North-Western Province" → Canadian North-Western Territory  ✅ FIXED 2026-06-27
Surfaced from the atlas (HALL W.G., a Ceylon roads engineer, looked like he ended
up in Canada). The spelled-out form "North-Western Province" / bare "N.W.P." was not
recognised by the directional-abbreviation resolver, so it fell through to a flat
cache hit: `Q1998931` (Canadian *North-Western Territory*, 20 CO events — ALL Ceylon
officials) or `Q138521` (the *India* North-Western Provinces, 66 of 70 CO events
Ceylon). Correct Ceylon entity = **Q876339**.
- **Fix:** `resolve_context.py` now parses spelled-out directional forms and treats
  "North-Western Province"/"N.W.P." (spacing-tolerant) as a Ceylon-vs-India ambiguous
  case (like the existing C.P. = Central Provinces vs Cape Province). Added a Ceylon
  town set so context resolves even when the only siblings are Ceylon towns. CO-only
  cache surgery removed the bad flat NWP rows + seeded the resolved-query rows; IOL
  left alone (there N.W.P.→Q138521 is correctly India). Re-ran resolve+emit.
- **Result:** Q1998931 (Canada) 20→0; Q876339 (Ceylon NWP) 0→106; Q138521 remaining
  = 2, both genuinely India. Bonus: many previously-ungrounded spelled-out Ceylon
  province events (southern/northern/western) now grounded via the same extension.

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

### 9. "Victoria" — British Columbia vs the Australian colony  ✅ FIXED 2026-06-27
Surfaced from the atlas (BREWSTER, premier of British Columbia, showed "legislative
ass. for Victoria" in Australia). The bare surface "Victoria" was flat-grounded to the
Australian colony Q56850459, so BC officials (Brewster, Elliott, Pearse — Victoria is
the BC capital + an electoral district) were mislocated. **Fix:** `resolve_context.py`
treats "Victoria" as context-dependent (BC/Vancouver-Island signal → Q1973 British
Columbia, which geolocates to its seat Victoria, BC; else the Australian colony).
**Also fixed a latent per-person-resolution bug:** the resolution map keyed persons as
`kgp_<bio>` while the spine's `attestations` are bare bio-ids, so per-person overrides
never matched and everything fell back to the global majority — `kg_emit_stage3` now
strips the prefix. This repaired Victoria→BC and the India-vs-Ceylon N.-W. Province
minority split. Both corpora re-emitted.

---

## Session 2026-06-28 — Wikidata cross-validation + geography/label audit

Context: validated the KG against the ~1,100 Wikidata-grounded officials (independent
gold standard) and audited the place→colony layer by coordinates + WD-label identity.
Fixed at root (committed 845a67d and earlier): 7 namesake person mis-groundings; 4
country→colony QID transpositions (Sierra Leone→Somaliland etc.); the resolve_colony
label-before-crosswalk precedence bug; 8 reused-QID colony mislabels (Weihaiwei→China,
Baluchistan→North-West Frontier, Baker Island→United States, Cape Coast Castle→British
Gold Coast …); merged the duplicate Gold Coast nodes via `data/kg/colony_canon.json`.
See memory `kg-geography-transposition-fixes`, `kg-grounding-validation`. Remaining:

### 10. Vague-region surfaces mis-attributed to a specific colony  **needs re-ground**
`Q252 'Dutch East Indies (British Occupation)'` (79 facts) attracts surfaces that the
1811–16 British occupation never covered: **"New Guinea" (12)** and **"Australasia" (11)**
— vague regional toponyms the LLM/grounder mapped to Java/DEI. Same class as the old
"Southeast Asia → British New Guinea". Fix: re-ground these vague regional surfaces
(ideally drop colony, or split to the right entity); don't let a region collapse onto a
specific colony. ~23 facts.

### 11. Coarse country-QID nodes co-exist with the proper sub-colony — **CORRECT, do NOT merge**
After the label fixes, several *modern-country* colony nodes sit beside the *specific*
colonial entity, and **this is intentional** — they hold different things:
`Q148 China`(99, consular/treaty-port postings: Shanghai, Beijing, Canton) vs
`Q15939896 Weihaiwei`(36, the leased territory); `Q41 Greece`(65, mainland/WWI Salonika)
vs `Q1063498 United States of the Ionian Islands`(50, the protectorate); `Q843
North-West Frontier`(52) vs `Q3303188 Baluchistan`(10). **Note for future cleanup: do
NOT fold these into colony_canon.json** the way Gold Coast was — China ≠ Weihaiwei. Open
*modeling* question only: China/United States/Greece/France are "place of service abroad",
not British colonies; the colony layer conflates "colony" with "where served". By design
for now.

### 12. Correctly-grounded officials whose career rolled up to metropole only  **needs re-ground**
`John Anderson` (Q6218961) is correctly grounded (Governor of the Straits Settlements &
Ceylon) but his KG career events resolve to **"United Kingdom (metropole)" only** — his
real colonies were dropped to the metropole fallback. Representative of a residual class
of the placeless-officials problem (see `placeless-officials-diagnosis`): the WD-has-more
audit (`data/kg/graph_stage3/wikidata_has_more.json`, 224 persons) is the lead list for
finding these. Fix: for grounded persons, reconcile career colonies against WD P39
jurisdictions; recover the dropped colonies.

### 13. Person under-merge — 30 Wikidata QIDs map to ≥2 KG person records  **needs dedup**
30 QIDs each ground 2+ distinct `person_id`s = the same real person split across records
that the surname/given-name + role/year dedup never joined (often peerage-title vs
family-name, or OCR variants across edition gaps). This is an *independent* dedup signal
from the grounding. Fix: a QID-blocked merge pass (block on shared wikidata_qid, then the
usual name/career compatibility gate). List derivable from `person_grounding.final.jsonl`.

### 14. Per-person-ambiguous "Victoria" surfaces left ungrounded (by design)  **needs per-person ground**
The Victoria re-grounding (this session) deliberately did NOT blanket-ground surfaces that
mean different places for different people, to avoid mislocating one: **"Victoria district"**
= Western Australia (ELIOT) vs Cape (HAW); **"Victoria county"** = Mauritius (D'HOTMAN);
bare Cape East/West and the Australian multi-colony lists. A single cache QID would be
wrong for someone. Fix: route these through the per-person context resolver
(`resolve_context.py`), not the surface-keyed grounding cache. ~6 facts.

### 15. Remote British territories on metropole fallback + 1-use context noise  (minor)
Coordinate audit residue, all benign: `Falkland Islands Dependencies` and `Diego Garcia`
roll to "United Kingdom (metropole)" (legitimately British, just no own colony node);
single-use context places attach to the person's colony (Versailles→Bechuanaland,
France→Northern Rhodesia, Syria→metropole) — extraction artifacts, ~1 fact each. Low
priority; could drop sub-1-use foreign context places from the colony layer.
