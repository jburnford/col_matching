<!-- {"case_id": "case_whittaker_harry-stanley_b1882", "bio_ids": ["whittaker_harry-stanley_b1882"], "stint_ids": ["Whittaker, H. S___British Guiana___1923", "Whittaker, H. S___British Honduras___1917"]} -->
# Dossier case_whittaker_harry-stanley_b1882

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `whittaker_harry-stanley_b1882`

- Printed name: **WHITTAKER, HARRY STANLEY**
- Birth year: 1882 (attested in editions [1934, 1935, 1936])
- Appears in editions: [1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1934-L64041.v` — printed in editions [1934, 1935, 1936]:**

> WHITTAKER, HARRY STANLEY, A.M.I.M. & C.E., A.M.I.Struct.E.—B. 1882; prev. serv., Br. Honduras, 1911-20; asst. engnr., Br. Guiana, 1920; seconded sea defences, 1920-22; exec. engnr., P.W.D., 1922; ag. dist. comsrr., in addn., 1932-33.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911–1920 | prev. serv., Br. Honduras | — | [1934, 1935, 1936] |
| 1 | 1920 | asst. engnr. | British Guiana | [1934, 1935, 1936] |
| 2 | 1922 | exec. engnr., P.W.D | British Guiana *(inherited from previous clause)* | [1934, 1935, 1936] |
| 3 | 1932–1933 | ag. dist. comsrr., in addn | British Guiana *(inherited from previous clause)* | [1934, 1935, 1936] |

## Candidate stint `Whittaker, H. S___British Guiana___1923`

- Staff-list name: **Whittaker, H. S** | colony: **British Guiana** | listed 1923–1930 | editions [1923, 1924, 1925, 1927, 1928, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | H. S. Whittaker | Executive Engineer | Public Works | — | — |
| 1924 | H. S. Whittaker | Executive Engineer | Public Works | — | — |
| 1925 | H. S. Whittaker | Executive Engineer | Public Works | — | — |
| 1927 | H. S. Whittaker | Executive Engineer | Public Works | — | — |
| 1928 | H. S. Whittaker | Executive Engineer | Public Works | — | — |
| 1930 | H. S. Whittaker | Executive Engineer | Public Works | — | — |

### Deterministic checks: `whittaker_harry-stanley_b1882` vs `Whittaker, H. S___British Guiana___1923`

- [PASS] surname_gate: bio 'WHITTAKER' vs stint 'Whittaker, H. S' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1923, birth 1882 (age 41)
- [PASS] colony: 3 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1923-1930
- [PASS] position_sim: best 62 vs bar 60: 'exec. engnr., P.W.D' ~ 'Executive Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Whittaker, H. S___British Honduras___1917`

- Staff-list name: **Whittaker, H. S** | colony: **British Honduras** | listed 1917–1920 | editions [1917, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | H. S. Whittaker | Assistant Engineer | Public Works | — | — |
| 1918 | H. S. Whittaker | Assistant Engineer | Public Works | — | — |
| 1919 | H. S. Whittaker | Assistant Engineer | Public Works | — | — |
| 1920 | H. S. Whittaker | Assistant Engineer | Public Works | — | — |

### Deterministic checks: `whittaker_harry-stanley_b1882` vs `Whittaker, H. S___British Honduras___1917`

- [PASS] surname_gate: bio 'WHITTAKER' vs stint 'Whittaker, H. S' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1917, birth 1882 (age 35)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1920
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

