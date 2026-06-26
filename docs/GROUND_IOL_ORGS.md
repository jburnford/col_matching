# Ground the IOL employer / organisation layer (career-event place_raw → Wikidata)

DONE 2026-06-26. Sibling of the education layer (`docs/PARSE_IOL_EDUCATION.md`):
the career-event layer carries a `place_raw` that is often an EMPLOYER (a railway,
a government department, a survey, a police force, a regiment, the India Office)
rather than a geographic place — left ungrounded by the place pipeline. This layer
collects those org surfaces and grounds them with the same harness used for
education institutions.

Always `export COL_KG_OUT=data/iol` first.

## Stage A — build the worklist (no LLM)
```
COL_KG_OUT=data/iol python3 kg_org_worklist.py
```
Scans `data/iol/graph_stage3/career_events.jsonl`, keeps ungrounded `place_raw`
values matching an ORG regex (railway/department/survey/police/regiment/customs/
treasury/secretariat/...), groups case-insensitively → `data/iol/org_worklist.jsonl`
(`{institution,type,count,person_ids,examples}`, count-desc).
**746 distinct surfaces / 5,572 mentions** (railway 2,561 · department 1,013 ·
survey 540 · police 458 · public_works 375 · …).
(`kg_org_worklist.py` was made `COL_KG_OUT`-rooted this session — was hardcoded to
`data/kg`; uses `col_match.kg.paths.kg_out()`.)

## Stage B — ground to Wikidata (same harness as education; fold + MCP)
Env for the whole loop:
```
export COL_WORK=data/iol/org_worklist.jsonl
export COL_CACHE=data/iol/org_grounding.jsonl
```
Seed: 3 verified global-department QIDs lifted from the CO List org cache
(`data/kg/org_grounding.jsonl`) whose surfaces also appear here — **War Office
Q2060703, Colonial Office Q1110907, Admiralty Q396266**. The rest of the CO org
cache is African/Malay railways (no India overlap), so NOT seeded; the Indian
railways were grounded fresh (they are marginal/internal in CO but central here).

Per-batch loop (count-descending), identical to `docs/GROUND_INSTITUTIONS.md`:
```
# 1. fold pre-pass (free; sweeps variants of anything grounded last batch)
python3 kg_fold_institutions.py --out data/iol/org_folds_bN.jsonl
python3 kg_ground_institutions.py record data/iol/org_folds_bN.jsonl
# 2. next pending (count-desc), split across subagents doing MCP search_items +
#    get_statements (≤5/msg). Pick the ORG entity (railway company / govt agency /
#    military unit / college) — NEVER a place, person, building, or railway LINE.
python3 kg_ground_institutions.py pending --n NNN > /tmp/org_pending_bN.jsonl
# 3. VERIFY (0-FP gate) then record
python3 verify_institution_qids.py data/iol/org_mcp_bN.jsonl   # fix NONINST/STUB/CLASS
python3 kg_ground_institutions.py record data/iol/org_mcp_bN.jsonl
python3 kg_ground_institutions.py stats
```

### What was done (3 batches, count-desc)
- **B1** count≥4 head (238 surfaces): 37 mcp / 28 reuse / 128 internal / 45 ambiguous.
- **B2** count 2–3 tail (187): 12 mcp / 25 reuse / 133 internal / 17 ambiguous.
- **B3** count==1 singletons (297): reuse-first round (full 41-QID reference) →
  5 mcp / 80 reuse / 182 internal / 30 ambiguous. OCR clusters collapsed to one
  slug + reuse (Dhond-Manmad ×7, Bhavnagar-Gondal, Kathiawar ×4).

### Final state
**157 Wikidata QIDs / 498 internal / 93 ambiguous → 76.5% mention coverage**
(4,262/5,572). The held **23.5% is genuinely unresolvable bare umbrellas** —
"Indian State railways" (566) + "state railways" (204) name no specific company.
Emitted **655 organisation nodes + 2,263 employment edges** over **1,732 persons**;
**42% of edges carry a Wikidata QID** (vs 22% in the CO org layer — Indian railways
are well-covered on Wikidata).

### 0-FP gate catches + reconciliations this session
- `verify_institution_qids.py` flagged **Q7286408 Rajputana-Malwa** as P31=*railway
  line* (not an org) → demoted to internal. Same rule killed Kalka-Simla, Rajputana-
  Malwa line forms in subagents.
- **"foreign office"** (bare, 5 mentions) → demoted to **ambiguous**: in the IOL it is
  multi-referent (British FO Q58211956 vs the Govt-of-India Foreign Department).
- **"Indian Police Service" Q3517917** (post-1948 IPS that *replaces* Imperial Police)
  → folded to **Indian Imperial Police Q16847284** for the pre-1947 corpus.
- Cross-subagent split reconciled: BB&CI / Calcutta&SE / North Western / Calcutta
  medical variants that one chunk grounded and another internal-minted → folded all
  onto the QID (8 surfaces).
- ⚠️ Bad hints in the first prompt that subagents CAUGHT: East India College
  Q1432447 (= Thousand Palms, CA — correct civil college Q142599, education layer)
  and Survey of India Q2154100 (= a disambig page — correct **Q1359276**).

## Stage C — emit (org-specific node/edge filenames; do NOT clobber education)
```
export COL_WORK=data/iol/org_worklist.jsonl
export COL_CACHE=data/iol/org_grounding.jsonl
export COL_NODES=organisations.jsonl COL_EDGES=employment_edges.jsonl
COL_KG_OUT=data/iol python3 kg_ground_institutions.py emit
# -> data/iol/graph_stage3/organisations.jsonl  (655 nodes, ambiguous excluded)
# -> data/iol/graph_stage3/employment_edges.jsonl (2,263 person→org edges)
```

See `[[iol-kg-build]]`, `[[kg-institution-grounding]]`,
`[[kg-institution-ambiguous-surfaces]]`.
