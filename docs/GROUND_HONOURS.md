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
4. `kg_emit_honours.py` → splits into TWO layers via `kg_honour_norm.honour_class`:
   - `honour_nodes.jsonl` + `honour_edges.jsonl` — state honours (orders/decorations/
     medals/appointments: CMG, MC, KC, PC...).
   - `qualification_nodes.jsonl` + `qualification_edges.jsonl` — academic degrees
     (MA/BSc/MD via curated DEGREE set) + professional memberships (FRCS/MICE via the
     `*RC*`/`MI*` regex + curated MEMBERSHIP set). Same grounding cache + QIDs.
   Auto-internal-mints any uncached non-control award. Modifiers + year + award_raw on
   each edge. `_unknown` → id=null. **Classifier is curated, NOT pure-regex**: `mm`
   (Military Medal), `dsc` (Distinguished Service Cross), `mbe`, "french croix de
   guerre" must stay HONOURS — verify new tail entries don't misroute.
5. `kg_dedup_nodes.py` — run after emit. Plain label-norm fold (QID wins) collapses
   spelled-out award strings ("Colonial Police Medal") onto their acronym QID.

## Disposition (per base-honour)

- **mcp** — ground to the specific GRADE QID. Verify the search description says
  "award / rank / appointment / decoration / medal", not a person or category.
- **reuse** — a variant of an already-grounded honour (QC ≡ KC → Q1533366;
  QPM ≡ KPM → Q2792177, monarch-renamed same award).
- **internal** — a real honour/membership with NO distinct WD grade QID
  (`colkg:mice` Member ICE, `colkg:mvo` 5th-class RVO member).
- **_unknown** — noise, left ungrounded by the worklist (not your concern).

## STATE — last updated 2026-06-24 (after layer split)

- **41 awards grounded.** Two layers now:
  - **honours**: 14,684 edges, **72% to a Wikidata QID** (20 decoration QIDs).
  - **qualifications**: 1,356 edges, **49% to a QID** (16 degree/fellowship QIDs):
    MA Q2091008, BA Q1765120, BSc Q787674, MSc Q950900, DSc Q2248352, LLD Q959320,
    DD Q1984623, MD Q913404 · FRCS Q3631327, MRCS Q6815098, FRS Q15631401,
    FRAS Q26111565, FZS Q25513903, FRSE Q5438598, FRSA Q15271633, FRGS Q20006267.
- Head done (count ≥ 60): cmg Q12177413 · obe Q10762848 · mbe Q12201526 ·
  kcmg Q12177415 · mc Q1335064 · cbe Q12201477 · knight bachelor Q833163 ·
  cpm Q3195318 · gcmg Q12177423 · cb Q12177472 · iso Q1810753 · dso Q615838 ·
  kc/qc Q1533366 · pc Q28841847 · kcb Q12177470 · frgs Q20006267 · kbe Q12201445 ·
  gcb Q12177451 · mice colkg · gcb · kpm/qpm Q2792177 · cvo Q12193183 ·
  dfc Q1229534 · mvo colkg.
- **NEXT uncached head** (count-desc): ed (76, Efficiency Decoration) ·
  td (74, Territorial Decoration) · mm (43, Military Medal) · amice (46, → qual) ·
  fgs (39, → qual) · lrcp (34, → qual) · then the count-20..40 band (mixed
  honours + qual). dd/dcl/etc degrees and the *RC*/MI* memberships auto-route.

## RESOLVED 2026-06-24

Jim chose a **separate qualifications layer**: degrees + professional memberships
emit to `qualification_*.jsonl`, the honour layer keeps only state honours. Done.
Remaining tail grounding (count-desc) feeds BOTH layers from the one cache/worklist.
