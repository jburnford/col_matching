<!-- {"case_id": "case_rhodes_alice-leopold_b1884", "bio_ids": ["rhodes_alice-leopold_b1884"], "stint_ids": ["Rhodes, A. L___Trinidad and Tobago___1925"]} -->
# Dossier case_rhodes_alice-leopold_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rhodes_alice-leopold_b1884`

- Printed name: **RHODES, ALICE LEOPOLD**
- Birth year: 1884 (attested in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940])
- Honours: M.B.E (1936)
- Appears in editions: [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1929-L63492.v` — printed in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]:**

> RHODES, ALICE LEOPOLD, M.B.E. (1936).—B. 1884; war serv., 1915-19; gen. foreman, gov. printing and stationery dept., Trinidad, 1921; typography instr., bd. of indus. training, 1922; mem., bd. indus. training, 1923; gov. printer, 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | gen. foreman, gov. printing and stationery dept. | Trinidad | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 1 | 1922 | typography instr., bd. of indus. training | Trinidad *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 2 | 1923 | mem., bd. indus. training | Trinidad *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 3 | 1925 | gov. printer | Trinidad *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |

## Candidate stint `Rhodes, A. L___Trinidad and Tobago___1925`

- Staff-list name: **Rhodes, A. L** | colony: **Trinidad and Tobago** | listed 1925–1940 | editions [1925, 1927, 1928, 1929, 1931, 1933, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | A. L. Rhodes | General Foreman | Miscellaneous | — | — |
| 1927 | A. L. Rhodes | Government Printer | Miscellaneous | — | — |
| 1928 | A. L. Rhodes | Government Printer | Miscellaneous | — | — |
| 1929 | A. L. Rhodes | Government Printer | Miscellaneous | — | — |
| 1931 | A. L. Rhodes | Government Printer | Miscellaneous | — | — |
| 1933 | A. L. Rhodes | Government Printer | Miscellaneous | — | — |
| 1934 | A. L. Rhodes | Government Printer | Miscellaneous | — | — |
| 1937 | A. L. Rhodes | Government Printer | Printing and Stationery Department | — | — |
| 1939 | A. L. Rhodes | Government Printer | Printing and Stationery Department | — | — |
| 1940 | A. L. Rhodes | Government Printer | Printing and Stationery | — | — |

### Deterministic checks: `rhodes_alice-leopold_b1884` vs `Rhodes, A. L___Trinidad and Tobago___1925`

- [PASS] surname_gate: bio 'RHODES' vs stint 'Rhodes, A. L' (exact)
- [PASS] initials: bio ['A', 'L'] ~ stint ['A', 'L']
- [PASS] age_gate: stint starts 1925, birth 1884 (age 41)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1940
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

