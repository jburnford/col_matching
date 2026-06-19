<!-- {"case_id": "case_rutherford_i-s_b1897", "bio_ids": ["rutherford_i-s_b1897"], "stint_ids": ["Rutherford, I. S___Trinidad and Tobago___1949"]} -->
# Dossier case_rutherford_i-s_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rutherford_i-s_b1897`

- Printed name: **RUTHERFORD, I. S**
- Birth year: 1897 (attested in editions [1956])
- Appears in editions: [1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L23928.v` — printed in editions [1956]:**

> RUTHERFORD, I. S.—b. 1897; ed. Merchant Taylors' Sch., Crosby and L'pool Univ.; mil. serv., 1915-18, capt.; 2nd asst. petroleum technologist, Trin., 1945; asst., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | 2nd asst. petroleum technologist | Trinidad | [1956] |
| 1 | 1946 | asst | Trinidad *(inherited from previous clause)* | [1956] |

## Candidate stint `Rutherford, I. S___Trinidad and Tobago___1949`

- Staff-list name: **Rutherford, I. S** | colony: **Trinidad and Tobago** | listed 1949–1954 | editions [1949, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | I. S. Rutherford | Second Assistant Petroleum Technologist | MINES | — | — |
| 1953 | I. S. Rutherford | Assistant Petroleum Technologist | Civil Establishment | — | — |
| 1954 | I. S. Rutherford | Assistant Petroleum Technologist | Civil Establishment | — | — |

### Deterministic checks: `rutherford_i-s_b1897` vs `Rutherford, I. S___Trinidad and Tobago___1949`

- [PASS] surname_gate: bio 'RUTHERFORD' vs stint 'Rutherford, I. S' (exact)
- [PASS] initials: bio ['I', 'S'] ~ stint ['I', 'S']
- [PASS] age_gate: stint starts 1949, birth 1897 (age 52)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1954
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

