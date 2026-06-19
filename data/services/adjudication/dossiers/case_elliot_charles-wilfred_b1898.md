<!-- {"case_id": "case_elliot_charles-wilfred_b1898", "bio_ids": ["elliot_charles-wilfred_b1898"], "stint_ids": ["Elliot, C. W___Kenya___1949", "Elliot, W___British Honduras___1923"]} -->
# Dossier case_elliot_charles-wilfred_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Elliot, C. W___Kenya___1949` is also gate-compatible with biography(ies) outside this case: ['elliot_charles-wilfred_b1894'] (already linked elsewhere or filtered).
- NOTE: stint `Elliot, W___British Honduras___1923` is also gate-compatible with biography(ies) outside this case: ['elliot_charles-wilfred_b1894', 'elliot_john-william_e1869'] (already linked elsewhere or filtered).

## Biography `elliot_charles-wilfred_b1898`

- Printed name: **ELLIOT, CHARLES WILFRED**
- Birth year: 1898 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L66378.v` — printed in editions [1939]:**

> ELLIOT, CHARLES WILFRED, M.C.—B. 1898; ed. Sleaford and Edin. Univ. (dept. forestry); on war serv., 1914-19; asst. conserv., forests, Kenya, Nov., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | asst. conserv., forests | Kenya | [1939] |

## Candidate stint `Elliot, C. W___Kenya___1949`

- Staff-list name: **Elliot, C. W** | colony: **Kenya** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. W. Elliot | Senior Assistant Conservators of Forests | Forestry | — | — |
| 1950 | C. W. Elliot | Senior Assistant Conservators of Forests | FORESTRY | — | — |

### Deterministic checks: `elliot_charles-wilfred_b1898` vs `Elliot, C. W___Kenya___1949`

- [PASS] surname_gate: bio 'ELLIOT' vs stint 'Elliot, C. W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['C', 'W']
- [PASS] age_gate: stint starts 1949, birth 1898 (age 51)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Elliot, W___British Honduras___1923`

- Staff-list name: **Elliot, W** | colony: **British Honduras** | listed 1923–1937 | editions [1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | Elliot | Wireless Operators | Post Office and Radio Telegraph Department | — | — |
| 1924 | W. Elliot | Wireless Operator | Post Office and Radio Telegraph Department | — | — |
| 1927 | W. Elliot | Wireless Operator | Telephone and Telegraph Department | — | — |
| 1928 | W. Elliot | Wireless Operators | Telephone and Telegraph Department | — | — |
| 1929 | W. Elliot | Wireless Operators | Telephone and Telegraph Department | — | — |
| 1930 | W. Elliot | Wireless Operator | Telephone and Telegraph Department | — | — |
| 1931 | W. Elliot | Wireless Operators | Telephone and Telegraph Department | — | — |
| 1932 | W. Elliot | Wireless Operator | Radio Telegraph Department | — | — |
| 1933 | W. Elliot | Wireless Operator | Radio Telegraph Department | — | — |
| 1934 | W. Elliot | Operator | Radio Telegraph Department | — | — |
| 1936 | W. Elliot | Operator | Wireless Branch | — | — |
| 1937 | W. Elliot | Operator | Wireless Branch | — | — |

### Deterministic checks: `elliot_charles-wilfred_b1898` vs `Elliot, W___British Honduras___1923`

- [PASS] surname_gate: bio 'ELLIOT' vs stint 'Elliot, W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1923, birth 1898 (age 25)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1937
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

