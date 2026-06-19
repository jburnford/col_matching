<!-- {"case_id": "case_mitchell_a-g_b1923", "bio_ids": ["mitchell_a-g_b1923"], "stint_ids": ["Mitchell, A. G___Western Pacific___1957", "Mitchell, A. G___Western Pacific___1961"]} -->
# Dossier case_mitchell_a-g_b1923

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 118 official(s) with this surname in the graph's staff lists; 46 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mitchell_a-g_b1923`

- Printed name: **MITCHELL, A. G**
- Birth year: 1923 (attested in editions [1964, 1965, 1966])
- Honours: D.F.M
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L19941.v` — printed in editions [1964, 1965, 1966]:**

> MITCHELL, A. G., D.F.M.—b. 1923; ed. Dulwich Coll. and Downing Coll., Camb.; mil. serv., 1942-45, f/o; estab. offr., Sudan 1951; admin. offr., cl. B, B.S.I.P., 1955; asst. sec., W.P.H.C., 1955; D.O., 1959; secon. N. Hebs., 1960; cl. A, 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | estab. offr., Sudan | — | [1964, 1965, 1966] |
| 1 | 1955 | admin. offr., cl. B, B.S.I.P | — | [1964, 1965, 1966] |
| 2 | 1955 | asst. sec., W.P.H.C | — | [1964, 1965, 1966] |
| 3 | 1959 | asst. sec., W.P.H.C | Dominions Office | [1964, 1965, 1966] |
| 4 | 1960 | secon. N. Hebs | Dominions Office *(inherited from previous clause)* | [1964, 1965, 1966] |
| 5 | 1962 | cl. A | Dominions Office *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Mitchell, A. G___Western Pacific___1957`

- Staff-list name: **Mitchell, A. G** | colony: **Western Pacific** | listed 1957–1958 | editions [1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | A. G. Mitchell | Assistant Secretaries | Civil Establishment | — | — |
| 1958 | A. G. Mitchell | Assistant Secretary | Civil Establishment | — | — |

### Deterministic checks: `mitchell_a-g_b1923` vs `Mitchell, A. G___Western Pacific___1957`

- [PASS] surname_gate: bio 'MITCHELL' vs stint 'Mitchell, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1957, birth 1923 (age 34)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1958
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Mitchell, A. G___Western Pacific___1961`

- Staff-list name: **Mitchell, A. G** | colony: **Western Pacific** | listed 1961–1966 | editions [1961, 1962, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | A. G. Mitchell | Administrative Officer, Class B | British National Administration | — | — |
| 1962 | A. G. Mitchell | Administrative Officer, Class B | British National Administration | — | — |
| 1964 | A. G. Mitchell | Administrative Officer, Class A | British National Administration | — | — |
| 1965 | A. G. Mitchell | Administrative Officer, Class A | British National Administration | — | — |
| 1966 | A. G. Mitchell | Administrative Officer, Class A | British National Administration | — | — |

### Deterministic checks: `mitchell_a-g_b1923` vs `Mitchell, A. G___Western Pacific___1961`

- [PASS] surname_gate: bio 'MITCHELL' vs stint 'Mitchell, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1961, birth 1923 (age 38)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1966
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

