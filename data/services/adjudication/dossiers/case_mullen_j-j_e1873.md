<!-- {"case_id": "case_mullen_j-j_e1873", "bio_ids": ["mullen_j-j_e1873"], "stint_ids": ["Mullen, J___Queensland___1878", "Mullen, J___Tanganyika___1921"]} -->
# Dossier case_mullen_j-j_e1873

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mullen_j-j_e1873`

- Printed name: **MULLEN, J. J**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28795.v` — printed in editions [1883]:**

> MULLEN, J. J.—Government medical officer, Jamaica, 1873.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1873 | Government medical officer | Jamaica | [1883] |

## Candidate stint `Mullen, J___Queensland___1878`

- Staff-list name: **Mullen, J** | colony: **Queensland** | listed 1878–1883 | editions [1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | J. Mullen | Member | Legislative Council | — | — |
| 1879 | J. Mullen | Member of Legislative Council | Legislative Council | — | — |
| 1880 | J. Mullen | Member | Legislative Council | — | — |
| 1883 | J. Mullen | Member | Legislative Council | — | — |

### Deterministic checks: `mullen_j-j_e1873` vs `Mullen, J___Queensland___1878`

- [PASS] surname_gate: bio 'MULLEN' vs stint 'Mullen, J' (exact)
- [PASS] initials: bio ['J', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Queensland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Mullen, J___Tanganyika___1921`

- Staff-list name: **Mullen, J** | colony: **Tanganyika** | listed 1921–1922 | editions [1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | J. Mullen | Clerk | Secretariat | — | — |
| 1922 | J. Mullen | Clerk | Secretariat | — | — |

### Deterministic checks: `mullen_j-j_e1873` vs `Mullen, J___Tanganyika___1921`

- [PASS] surname_gate: bio 'MULLEN' vs stint 'Mullen, J' (exact)
- [PASS] initials: bio ['J', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1922
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

