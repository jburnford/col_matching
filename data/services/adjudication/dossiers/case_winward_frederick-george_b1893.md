<!-- {"case_id": "case_winward_frederick-george_b1893", "bio_ids": ["winward_frederick-george_b1893"], "stint_ids": ["Winward, F. G___Sierra Leone___1929", "Winward, F. G___Sierra Leone___1949"]} -->
# Dossier case_winward_frederick-george_b1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `winward_frederick-george_b1893`

- Printed name: **WINWARD, Frederick George**
- Birth year: 1893 (attested in editions [1948])
- Honours: C.B.E
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L36991.v` — printed in editions [1948]:**

> WINWARD, Frederick George, C.B.E.—b. 1893; on mil. serv. 1914-19 and 1939-44, lt.-col.; dir. of supplies, S.L., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | dir. of supplies | Sierra Leone | [1948] |

## Candidate stint `Winward, F. G___Sierra Leone___1929`

- Staff-list name: **Winward, F. G** | colony: **Sierra Leone** | listed 1929–1937 | editions [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | F. G. Winward | Quartermaster | Sierra Leone Battalion, Royal West African Frontier Force | — | Captain |
| 1930 | F. G. Winward | Quartermaster | — | — | Captain |
| 1931 | F. G. Winward | Quartermaster | Military | — | Captain |
| 1932 | F. G. Winward | Quartermaster | — | — | Captain |
| 1933 | F. G. Winward | Quartermaster | — | — | Captain |
| 1934 | F. G. Winward | Quartermaster | — | — | Captain |
| 1936 | F. G. Winward | Quartermaster | — | — | Captain |
| 1937 | F. G. Winward | Quartermaster | Royal West African Frontier Force | — | Captain |

### Deterministic checks: `winward_frederick-george_b1893` vs `Winward, F. G___Sierra Leone___1929`

- [PASS] surname_gate: bio 'WINWARD' vs stint 'Winward, F. G' (exact)
- [PASS] initials: bio ['F', 'G'] ~ stint ['F', 'G']
- [PASS] age_gate: stint starts 1929, birth 1893 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1937
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Winward, F. G___Sierra Leone___1949`

- Staff-list name: **Winward, F. G** | colony: **Sierra Leone** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. G. Winward | Director | Commerce and Industry | — | — |
| 1950 | F. G. Winward | Director | COMMERCE AND INDUSTRY | — | — |

### Deterministic checks: `winward_frederick-george_b1893` vs `Winward, F. G___Sierra Leone___1949`

- [PASS] surname_gate: bio 'WINWARD' vs stint 'Winward, F. G' (exact)
- [PASS] initials: bio ['F', 'G'] ~ stint ['F', 'G']
- [PASS] age_gate: stint starts 1949, birth 1893 (age 56)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 35 vs bar 60: 'dir. of supplies' ~ 'Director'
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

