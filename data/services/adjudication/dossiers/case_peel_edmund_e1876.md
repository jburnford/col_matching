<!-- {"case_id": "case_peel_edmund_e1876", "bio_ids": ["peel_edmund_e1876"], "stint_ids": ["Peel, C. E___Straits Settlements___1936", "Peel, Edmund___Labuan___1886"]} -->
# Dossier case_peel_edmund_e1876

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['peel_edmund_e1876'] carry a single initial only — the namesake trap applies.

## Biography `peel_edmund_e1876`

- Printed name: **PEEL, EDMUND**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1894]

### Verbatim printed entry text (OCR)

**Version `col1888-L35471.v` — printed in editions [1888, 1889, 1894]:**

> PEEL, EDMUND.—Lieut. R.A., 1876 to 1883; served through the Afghan campaign, 1878-80 (medal); assistant inspector, Gold Coast constabulary, 1883; on special service, Sierra Leone, on the staff of Sir S. Rowe, 1885, and again in 1886; inspector-general of constabulary, Lagos, 1886; ditto, Jamaica, 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876–1883 | Lieut. R.A | — | [1888, 1889, 1894] |
| 1 | 1878–1880 | served through the Afghan campaign | — | [1888, 1889, 1894] |
| 2 | 1883 | assistant inspector, Gold Coast constabulary | Gold Coast | [1888, 1889, 1894] |
| 3 | 1885 | on special service, Sierra Leone, on the staff of Sir S. Rowe | Gold Coast *(inherited from previous clause)* | [1888, 1889, 1894] |
| 4 | 1886 | again in | Gold Coast *(inherited from previous clause)* | [1888, 1889, 1894] |
| 5 | 1886 | inspector-general of constabulary | Lagos | [1888, 1889, 1894] |
| 6 | 1891 | inspector-general of constabulary | Jamaica | [1888, 1889, 1894] |

## Candidate stint `Peel, C. E___Straits Settlements___1936`

- Staff-list name: **Peel, C. E** | colony: **Straits Settlements** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | C. E. Peel | Engineer-in-Charge, s.y. "Sea Belle II," | Marine | — | — |
| 1939 | C. E. Peel | Second Engineer, s.s.y. "Sea Belle II" | Marine | — | — |

### Deterministic checks: `peel_edmund_e1876` vs `Peel, C. E___Straits Settlements___1936`

- [PASS] surname_gate: bio 'PEEL' vs stint 'Peel, C. E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['C', 'E']
- [PASS] age_gate: stint starts 1936; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Peel, Edmund___Labuan___1886`

- Staff-list name: **Peel, Edmund** | colony: **Labuan** | listed 1886–1888 | editions [1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | J. Peel | — | — | — | — |
| 1888 | E. Peel | Officer in charge of Prison Discipline, Assistant Inspector | Prison | — | — |
| 1888 | Edmund Peel | Inspector General | Constabulary | — | — |

### Deterministic checks: `peel_edmund_e1876` vs `Peel, Edmund___Labuan___1886`

- [PASS] surname_gate: bio 'PEEL' vs stint 'Peel, Edmund' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Labuan'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1888
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

