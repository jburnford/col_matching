<!-- {"case_id": "case_foley_albert-maurice_b1897", "bio_ids": ["foley_albert-maurice_b1897"], "stint_ids": ["Foley, A. M___Trinidad and Tobago___1937", "Foley, A. M___Uganda___1927"]} -->
# Dossier case_foley_albert-maurice_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `foley_albert-maurice_b1897`

- Printed name: **FOLEY, Albert Maurice**
- Birth year: 1897 (attested in editions [1951])
- Honours: A.M.I.C.E, B.A
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L38092.v` — printed in editions [1951]:**

> FOLEY, Albert Maurice, B.A., B.A.I. (T.C.D.), A.M.I.C.E.—b. 1897; ed. Abbey Sch. and Dublin Univ.; asst. engrnr., P.W.D., Trin., 1935; div. engrnr., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | asst. engrnr., P.W.D. | Trinidad | [1951] |
| 1 | 1945 | div. engrnr | Trinidad *(inherited from previous clause)* | [1951] |

## Candidate stint `Foley, A. M___Trinidad and Tobago___1937`

- Staff-list name: **Foley, A. M** | colony: **Trinidad and Tobago** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | A. M. Foley | Assistant Engineer | District Engineers | — | — |
| 1939 | A. M. Foley | Assistant Engineer | PUBLIC WORKS DEPARTMENT | — | — |
| 1940 | A. M. Foley | Executive Engineer | Public Works | — | — |

### Deterministic checks: `foley_albert-maurice_b1897` vs `Foley, A. M___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'FOLEY' vs stint 'Foley, A. M' (exact)
- [PASS] initials: bio ['A', 'M'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1937, birth 1897 (age 40)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Foley, A. M___Uganda___1927`

- Staff-list name: **Foley, A. M** | colony: **Uganda** | listed 1927–1933 | editions [1927, 1928, 1929, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | A. M. Foley | Assistant Engineer | Municipal | — | — |
| 1928 | A. M. Foley | Assistant Engineer | Municipal | — | — |
| 1929 | A. M. Foley | Assistant Engineer | Public Works | — | — |
| 1933 | A. M. Foley | Assistant Engineer | Public Works Department | — | — |

### Deterministic checks: `foley_albert-maurice_b1897` vs `Foley, A. M___Uganda___1927`

- [PASS] surname_gate: bio 'FOLEY' vs stint 'Foley, A. M' (exact)
- [PASS] initials: bio ['A', 'M'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1927, birth 1897 (age 30)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1933
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

