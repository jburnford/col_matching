# Grounding HONOURS / awards to Wikidata

Resumable loop for the **honour / award layer** of the KG. Jim's rule (same as
roles): ground the AWARD TYPE to its Wikidata QID where one matches (e.g.
`C.M.G.` → **Q12177413** Companion of the Order of St Michael & St George),
internal-mint `colkg:<honour>` where Wikidata has no matching grade. British
orders are GRADED — CMG / KCMG / GCMG are three distinct QIDs; grades are NOT
collapsed. Branch qualifiers (military / civil) ride on the EDGE, not the node.

**Resume prompt after /clear:**
> Ground the next 30 honours — follow docs/GROUND_HONOURS.md

## Pipeline (all at repo root)

1. `kg_honour_norm.py` — shared parser `parse_honour(raw) -> (base, modifiers, category)`.
   Joins single-letter acronyms ("c.m.g" → "cmg"), peels "(mil.)"/"(civil)" as a
   modifier, strips clasp/bar noise, folds Knt/Kt → "knight bachelor". Pure noise
   (bare "medal"/"board"/"clasp") → `_unknown` control bucket (not grounded).
2. `kg_honour_worklist.py` → `data/kg/honour_worklist.jsonl`
   `{institution:<base>, type, count, person_ids, examples}`.
   **1,632 distinct honours / 16,040 mentions**; control `_unknown`=264.
   Head is very concentrated: top 20 = 67% of mentions, top 50 = 77%, top 100 = 83%.
3. **Grounding** — the env-overridable `kg_ground_institutions.py` harness serves
   this worklist. ALWAYS export first:
   ```bash
   export COL_WORK=data/kg/honour_worklist.jsonl
   export COL_CACHE=data/kg/honour_grounding.jsonl
   python3 kg_ground_institutions.py pending --n 30   # top uncached, count-desc
   python3 kg_ground_institutions.py record /tmp/hon.jsonl   # merge decisions
   python3 kg_ground_institutions.py stats
   ```
   Use the **Wikidata MCP `search_items`** (≤5 calls/msg) — NOT the REST API.
   Cache rows: `{institution, type, id, label, instance_of, country_qid, source,
   match_type}`, id = `Q…` or `colkg:<Slug>`. source = mcp / reuse / internal.
4. `kg_emit_honours.py` → `honour_nodes.jsonl` + `honour_edges.jsonl`. Auto-internal-
   mints any uncached non-control honour (tail covered without a bulk pass).
   Modifiers + year + award_raw emitted on each edge. `_unknown` → honour_id=null.
5. `kg_dedup_nodes.py` — run after emit. Plain label-norm fold (QID wins) collapses
   spelled-out award strings ("Colonial Police Medal") onto their acronym QID.

## Disposition (per base-honour)

- **mcp** — ground to the specific GRADE QID. Verify the search description says
  "award / rank / appointment / decoration / medal", not a person or category.
- **reuse** — a variant of an already-grounded honour (QC ≡ KC → Q1533366;
  QPM ≡ KPM → Q2792177, monarch-renamed same award).
- **internal** — a real honour/membership with NO distinct WD grade QID
  (`colkg:mice` Member ICE, `colkg:mvo` 5th-class RVO member). Also academic
  degrees if Jim wants them OUT of honours — see open question below.
- **_unknown** — noise, left ungrounded by the worklist (not your concern).

## STATE — last updated 2026-06-24

- **25 honours grounded → 68% of 16,040 mentions point to a Wikidata QID**
  (21 distinct decoration QIDs; the rest internal/reuse).
- Head done (count ≥ 60): cmg Q12177413 · obe Q10762848 · mbe Q12201526 ·
  kcmg Q12177415 · mc Q1335064 · cbe Q12201477 · knight bachelor Q833163 ·
  cpm Q3195318 · gcmg Q12177423 · cb Q12177472 · iso Q1810753 · dso Q615838 ·
  kc/qc Q1533366 · pc Q28841847 · kcb Q12177470 · frgs Q20006267 · kbe Q12201445 ·
  gcb Q12177451 · mice colkg · gcb · kpm/qpm Q2792177 · cvo Q12193183 ·
  dfc Q1229534 · mvo colkg.
- **NEXT uncached head** (count-desc): ed (76, Efficiency Decoration?) ·
  td (74, Territorial Decoration) · ma (67, Master of Arts — DEGREE) ·
  b sc (52, Bachelor of Science — DEGREE) · then the count-30..50 band.

## OPEN QUESTION for Jim

The award field mixes true honours with **academic degrees** (M.A., B.Sc., LL.B.,
M.D., Ph.D.) and **professional fellowships/memberships** (F.R.G.S., M.I.C.E.,
M.R.C.S.). All ground to Wikidata QIDs, but degrees aren't really "honours."
Options: (a) ground them in-place to degree QIDs; (b) route them to a separate
`qualifications` layer; (c) leave internal-minted. Default so far: ground
fellowships, internal-mint memberships, **degrees still pending a decision.**
