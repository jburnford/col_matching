<!-- {"case_id": "case_scrunby_charles-burdnett_e1899", "bio_ids": ["scrunby_charles-burdnett_e1899"], "stint_ids": ["Scruby, C. B___Lagos___1905"]} -->
# Dossier case_scrunby_charles-burdnett_e1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `scrunby_charles-burdnett_e1899` ↔ `Scruby, C. B___Lagos___1905` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Scruby, C. B___Lagos___1905` is also gate-compatible with biography(ies) outside this case: ['scruby_charles-burdett_b1876'] (already linked elsewhere or filtered).

## Biography `scrunby_charles-burdnett_e1899`

- Printed name: **SCRUNBY, CHARLES BURDNETT**
- Birth year: not printed
- Appears in editions: [1907]

### Verbatim printed entry text (OCR)

**Version `col1907-L46750.v` — printed in editions [1907]:**

> SCRUNBY, CHARLES BURDNETT, B.A.—Ed. priv. and Sidney Sussex Coll., Camb., and in France; asst. collr., Br. Cent. Africa Prot., 1899; ag. vice-consul, Fort Johnston, 1901; dist. comsrr., Lagos, 1902; ag. collr. of cust., 1904; asst. to comsrr. for Egba bdry. delimitation, 1904-5; certif. from schl. of mil. engnr., Chatham, in mil. topography and astronomy, 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | asst. collr., Br. Cent. Africa Prot | — | [1907] |
| 1 | 1901 | ag. vice-consul, Fort Johnston | — | [1907] |
| 2 | 1902 | dist. comsrr. | Lagos | [1907] |
| 3 | 1904 | ag. collr. of cust | Lagos *(inherited from previous clause)* | [1907] |
| 4 | 1905 | certif. from schl. of mil. engnr., Chatham, in mil. topography and astronomy | Lagos *(inherited from previous clause)* | [1907] |

## Candidate stint `Scruby, C. B___Lagos___1905`

- Staff-list name: **Scruby, C. B** | colony: **Lagos** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | C. B. Scruby | District Commissioner | Supreme Court | — | — |
| 1906 | C. B. Scruby | District Commissioners | Supreme Court | — | — |

### Deterministic checks: `scrunby_charles-burdnett_e1899` vs `Scruby, C. B___Lagos___1905`

- [PASS] surname_gate: bio 'SCRUNBY' vs stint 'Scruby, C. B' (fuzzy:1)
- [PASS] initials: bio ['C', 'B'] ~ stint ['C', 'B']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Lagos'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1905-1906
- [PASS] position_sim: best 62 vs bar 60: 'dist. comsrr.' ~ 'District Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Adjudication constraints (binding)

- The prime directive is NO FALSE MERGES. A missed link is recoverable; a
  wrong one silently corrupts the historical record. When in doubt, leave
  the stint unassigned.
- Surname identity is NOT evidence: every candidate here already shares the
  surname (it is the blocking key). Only position, place, dates, honours,
  initials/forenames, and edition co-occurrence count.
- Single-initial biographies (e.g. "J. Lewis") must never be merged on
  shared-stint or tenure-overlap evidence alone; they need a strong
  independent dimension (specific position match, shared honour, or
  multi-edition co-occurrence).
- A stint belongs to AT MOST one biography. If two biographies in this case
  could plausibly hold the same stint, assign it to neither.
- Respect hard chronology: nobody serves before age ~15 or after death.
- Generic junior titles (clerk, cadet, assistant) recur constantly; a title
  match alone on a common office is weak evidence.

