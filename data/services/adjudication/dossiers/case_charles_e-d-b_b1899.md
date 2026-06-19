<!-- {"case_id": "case_charles_e-d-b_b1899", "bio_ids": ["charles_e-d-b_b1899"], "stint_ids": ["Charles, E. D. B___St Vincent___1928", "Charles, E. D. B___Windward Islands___1933"]} -->
# Dossier case_charles_e-d-b_b1899

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `charles_e-d-b_b1899`

- Printed name: **CHARLES, E. D. B**
- Birth year: 1899 (attested in editions [1958, 1959, 1960])
- Appears in editions: [1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1958-L21306.v` — printed in editions [1958, 1959, 1960]:**

> CHARLES, E. D. B.—b. 1899; ed. Grenada Boys' Secondary Sch.; M.O., St. V., 1926; S.M.O., 1949; M.O. (health), J'ca., 1952; epidemiologist, 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | M.O. | St. Vincent | [1958, 1959, 1960] |
| 1 | 1949 | S.M.O | St. Vincent *(inherited from previous clause)* | [1958, 1959, 1960] |
| 2 | 1952 | M.O. (health) | Jamaica | [1958, 1959, 1960] |
| 3 | 1957 | epidemiologist | Jamaica *(inherited from previous clause)* | [1958, 1959, 1960] |

## Candidate stint `Charles, E. D. B___St Vincent___1928`

- Staff-list name: **Charles, E. D. B** | colony: **St Vincent** | listed 1928–1932 | editions [1928, 1929, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | E. D. B. Charles | District Medical Officer | Medical | — | — |
| 1929 | E. D. B. Charles | District Medical Officer | Medical | — | — |
| 1932 | E. D. B. Charles | District Medical Officer | Medical | — | — |

### Deterministic checks: `charles_e-d-b_b1899` vs `Charles, E. D. B___St Vincent___1928`

- [PASS] surname_gate: bio 'CHARLES' vs stint 'Charles, E. D. B' (exact)
- [PASS] initials: bio ['E', 'D', 'B'] ~ stint ['E', 'D', 'B']
- [PASS] age_gate: stint starts 1928, birth 1899 (age 29)
- [PASS] colony: 2 placed event(s) resolve to 'St Vincent'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1928-1932
- [FAIL] position_sim: best 15 vs bar 60: 'M.O.' ~ 'District Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Charles, E. D. B___Windward Islands___1933`

- Staff-list name: **Charles, E. D. B** | colony: **Windward Islands** | listed 1933–1939 | editions [1933, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | E. D. B. Charles | District Medical Officer | Medical | — | — |
| 1936 | E. D. B. Charles | District Medical Officer | Medical | — | — |
| 1937 | E. D. B. Charles | District Medical Officer | Medical | — | — |
| 1939 | E. D. B. Charles | District Medical Officer | Medical | — | — |

### Deterministic checks: `charles_e-d-b_b1899` vs `Charles, E. D. B___Windward Islands___1933`

- [PASS] surname_gate: bio 'CHARLES' vs stint 'Charles, E. D. B' (exact)
- [PASS] initials: bio ['E', 'D', 'B'] ~ stint ['E', 'D', 'B']
- [PASS] age_gate: stint starts 1933, birth 1899 (age 34)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
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

