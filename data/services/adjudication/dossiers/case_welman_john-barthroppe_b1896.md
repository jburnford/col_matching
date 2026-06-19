<!-- {"case_id": "case_welman_john-barthroppe_b1896", "bio_ids": ["welman_john-barthroppe_b1896"], "stint_ids": ["Welman, J. B___Nigeria___1923"]} -->
# Dossier case_welman_john-barthroppe_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `welman_john-barthroppe_b1896`

- Printed name: **WELMAN, JOHN BARTHROPPE**
- Birth year: 1896 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L71698.v` — printed in editions [1939]:**

> WELMAN, JOHN BARTHROPPE.—B. 1896; ed. Southey Hall, Worthing, Chateau de Rots near St. Germain-en-Laye; milly. serv. in Egypt, S. Arabia and Mesopotamia, 1914-19; admvte. offr., cls. IV, Nigeria, 1920; cls. III, 1928; ag. sec., N. Provs., Nov.-Dec., 1935; admvte. offr., cls. II, 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | milly. serv. in Egypt, S. Arabia and Mesopotamia | — | [1939] |
| 1 | 1920 | admvte. offr., cls. IV | Nigeria | [1939] |
| 2 | 1928 | cls. III | Nigeria *(inherited from previous clause)* | [1939] |
| 3 | 1935 | ag. sec., N. Provs., Nov.- | Nigeria *(inherited from previous clause)* | [1939] |
| 4 | 1936 | admvte. offr., cls. II | Nigeria *(inherited from previous clause)* | [1939] |

## Candidate stint `Welman, J. B___Nigeria___1923`

- Staff-list name: **Welman, J. B** | colony: **Nigeria** | listed 1923–1925 | editions [1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | J. B. Welman | Assistant Secretary | Civil Establishment | — | — |
| 1925 | J. B. Welman | 294 District Officers | Political | — | — |

### Deterministic checks: `welman_john-barthroppe_b1896` vs `Welman, J. B___Nigeria___1923`

- [PASS] surname_gate: bio 'WELMAN' vs stint 'Welman, J. B' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1923, birth 1896 (age 27)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1925
- [FAIL] position_sim: best 41 vs bar 60: 'admvte. offr., cls. IV' ~ '294 District Officers'
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

