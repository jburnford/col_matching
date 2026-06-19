<!-- {"case_id": "case_hammond_j-a_b1925", "bio_ids": ["hammond_j-a_b1925"], "stint_ids": ["Hammond, J. A___Gold Coast___1949"]} -->
# Dossier case_hammond_j-a_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hammond_j-a_b1925`

- Printed name: **HAMMOND, J. A**
- Birth year: 1925 (attested in editions [1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L21948.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> HAMMOND, J. A.—b. 1925; ed. Gresham's Royal Vet. Coll., Edin. Univ.; vet. offr., Tang., 1951; vet. research offr., 1961-65. (Tanzania Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | vet. offr. | Tanganyika | [1962, 1963, 1964, 1965, 1966] |
| 1 | 1961–1965 | vet. research offr | Tanganyika *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Hammond, J. A___Gold Coast___1949`

- Staff-list name: **Hammond, J. A** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. A. Hammond | Accountants | Public Works | — | — |
| 1951 | J. A. Hammond | Accountants | Accounting and Storekeeping Staff | — | — |

### Deterministic checks: `hammond_j-a_b1925` vs `Hammond, J. A___Gold Coast___1949`

- [PASS] surname_gate: bio 'HAMMOND' vs stint 'Hammond, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1949, birth 1925 (age 24)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

