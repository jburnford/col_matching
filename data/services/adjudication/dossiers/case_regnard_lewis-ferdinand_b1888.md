<!-- {"case_id": "case_regnard_lewis-ferdinand_b1888", "bio_ids": ["regnard_lewis-ferdinand_b1888"], "stint_ids": ["Regnard, F___Mauritius___1937"]} -->
# Dossier case_regnard_lewis-ferdinand_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `regnard_lewis-ferdinand_b1888`

- Printed name: **REGNARD, LEWIS FERDINAND**
- Birth year: 1888 (attested in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1929-L63453.v` — printed in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> REGNARD, MAJOR LEWIS FERDINAND.—B. 1888; ed. R. Coll., Mauritius, Imp. Coll. of Sci. and Technology and McGill Univ. (B.Sc.); 2nd lieutenant, R.E., Nov., 1914; war serv., France, Belgium and Palestine, 1914-20; major, R.E., 1918-20; regular army R. of O.; asst. D.P.W. and surveys, Mauritius, 1921; D.P.W., 1926; M.L.C.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | 2nd lieutenant, R.E | — | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1918–1920 | major, R.E | — | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1921 | asst. D.P.W. and surveys | Mauritius | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1926 | D.P.W | Mauritius *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Regnard, F___Mauritius___1937`

- Staff-list name: **Regnard, F** | colony: **Mauritius** | listed 1937–1939 | editions [1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | F. Regnard | Director of Public Works and Surveys | Public Works and Surveys | — | Major |
| 1939 | F. Regnard | Director of Public Works and Surveys | Public Works and Surveys | — | Major |

### Deterministic checks: `regnard_lewis-ferdinand_b1888` vs `Regnard, F___Mauritius___1937`

- [PASS] surname_gate: bio 'REGNARD' vs stint 'Regnard, F' (exact)
- [PASS] initials: bio ['L', 'F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1937, birth 1888 (age 49)
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1939
- [FAIL] position_sim: best 15 vs bar 60: 'D.P.W' ~ 'Director of Public Works and Surveys'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

