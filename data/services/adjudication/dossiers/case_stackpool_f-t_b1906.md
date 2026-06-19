<!-- {"case_id": "case_stackpool_f-t_b1906", "bio_ids": ["stackpool_f-t_b1906"], "stint_ids": ["Stackpool, F. T___Fiji___1950", "Stackpool, F. T___Western Pacific___1933"]} -->
# Dossier case_stackpool_f-t_b1906

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stackpool_f-t_b1906`

- Printed name: **STACKPOOL, F. T**
- Birth year: 1906 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1958-L27194.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> STACKPOOL, F. T.—b. 1906; pharmacist, B.S.I.P., 1929; chief pharmacist and stores supvr., Ken., 1951-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | pharmacist, B.S.I.P | — | [1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1951–1962 | chief pharmacist and stores supvr. | Kenya | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Stackpool, F. T___Fiji___1950`

- Staff-list name: **Stackpool, F. T** | colony: **Fiji** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | F. T. Stackpool | Government Pharmacist and Medical Storekeeper | Medical | — | — |
| 1951 | F. T. Stackpool | Government Pharmacist and Medical Storekeeper | MEDICAL | — | — |

### Deterministic checks: `stackpool_f-t_b1906` vs `Stackpool, F. T___Fiji___1950`

- [PASS] surname_gate: bio 'STACKPOOL' vs stint 'Stackpool, F. T' (exact)
- [PASS] initials: bio ['F', 'T'] ~ stint ['F', 'T']
- [PASS] age_gate: stint starts 1950, birth 1906 (age 44)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Stackpool, F. T___Western Pacific___1933`

- Staff-list name: **Stackpool, F. T** | colony: **Western Pacific** | listed 1933–1939 | editions [1933, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | F. T. Stackpool | Dispenser and Clerk | Medical Department | — | — |
| 1936 | F. T. Stackpool | Dispenser and Clerk (temporary) | Medical Department | — | — |
| 1937 | F. T. Stackpool | Dispenser and Clerk | Medical Department | — | — |
| 1939 | F. T. Stackpool | Dispenser and Clerk | Medical Department | — | — |

### Deterministic checks: `stackpool_f-t_b1906` vs `Stackpool, F. T___Western Pacific___1933`

- [PASS] surname_gate: bio 'STACKPOOL' vs stint 'Stackpool, F. T' (exact)
- [PASS] initials: bio ['F', 'T'] ~ stint ['F', 'T']
- [PASS] age_gate: stint starts 1933, birth 1906 (age 27)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1939
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

