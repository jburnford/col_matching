<!-- {"case_id": "case_carter_edward-stanley_b1888", "bio_ids": ["carter_edward-stanley_b1888"], "stint_ids": ["Carter, E. S___Hong Kong___1922"]} -->
# Dossier case_carter_edward-stanley_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 80 official(s) with this surname in the graph's staff lists; 31 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `carter_edward-stanley_b1888`

- Printed name: **CARTER, EDWARD STANLEY**
- Birth year: 1888 (attested in editions [1934, 1935, 1936, 1937, 1939])
- Appears in editions: [1934, 1935, 1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1934-L57494.v` — printed in editions [1934, 1935, 1936, 1937, 1939]:**

> CARTER, EDWARD STANLEY.—B. 1888; ed. Carpenter's Co. Tech. Inst.; war serv., 1914-19; asst. engr., P.W.D., Hong Kong, 1920; seconded, Kowloon-Canton Rly., 1926-27 and in 1929; ag. mgr. and ch. engr., do., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | war serv. | — | [1934, 1935, 1936, 1937, 1939] |
| 1 | 1920–1920 | asst. engr., P.W.D. | Hong Kong | [1934, 1935, 1936, 1937, 1939] |
| 2 | 1926–1929 | seconded, Kowloon-Canton Rly. | — | [1934, 1935, 1936, 1937, 1939] |
| 3 | 1938–1938 | ag. mgr. and ch. engr., do. | — | [1934, 1935, 1936, 1937, 1939] |

## Candidate stint `Carter, E. S___Hong Kong___1922`

- Staff-list name: **Carter, E. S** | colony: **Hong Kong** | listed 1922–1939 | editions [1922, 1923, 1924, 1925, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | E. S. Carter | Engineer | General Staff | — | — |
| 1923 | E. S. Carter | Engineers | General Staff | — | — |
| 1924 | E. S. Carter | Engineers | General Staff | — | — |
| 1925 | E. S. Carter | Engineers | General Works | — | — |
| 1928 | E. S. Carter | Engineer | General Works | — | — |
| 1929 | E. S. Carter | Engineers | General Works | — | — |
| 1930 | E. S. Carter | Engineer | General Works | — | — |
| 1931 | E. S. Carter | Engineer | General Works | — | — |
| 1932 | E. S. Carter | Engineer | Public Works Department | — | — |
| 1933 | E. S. Carter | Engineers | Public Works Department | — | — |
| 1934 | E. S. Carter | Engineer | Public Works Department | — | — |
| 1937 | E. S. Carter | Engineer | Public Works Department | — | — |
| 1939 | E. S. Carter | Engineer | Public Works Department | — | — |

### Deterministic checks: `carter_edward-stanley_b1888` vs `Carter, E. S___Hong Kong___1922`

- [PASS] surname_gate: bio 'CARTER' vs stint 'Carter, E. S' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1922, birth 1888 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1939
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

