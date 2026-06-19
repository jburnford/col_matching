<!-- {"case_id": "case_pink_william-herbert-laurence_b1910", "bio_ids": ["pink_william-herbert-laurence_b1910"], "stint_ids": ["Pink, W. H. L___Jamaica___1949", "Pink, W. H. L___Windward Islands___1936"]} -->
# Dossier case_pink_william-herbert-laurence_b1910

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pink_william-herbert-laurence_b1910`

- Printed name: **PINK, William Herbert Laurence**
- Birth year: 1910 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L34955.v` — printed in editions [1949, 1950, 1951]:**

> PINK, William Herbert Laurence.—b. 1910; ed. King Edward Sch., Portsmouth; inspir. police, St. L., 1935; inspir., St. V., 1939; 3rd cl. inspir., J'ca., 1941; 2nd cl., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | inspir. police | St. Lucia | [1949, 1950, 1951] |
| 1 | 1939 | inspir. | St. Vincent | [1949, 1950, 1951] |
| 2 | 1941 | 3rd cl. inspir. | Jamaica | [1949, 1950, 1951] |
| 3 | 1943 | 2nd cl | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Pink, W. H. L___Jamaica___1949`

- Staff-list name: **Pink, W. H. L** | colony: **Jamaica** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. H. L. Pink | Senior Assistant Superintendents of Police | POLICE | — | — |
| 1950 | W. H. L. Pink | Senior Assistant Superintendent of Police | Police | — | — |
| 1951 | W. H. L. Pink | Senior Assistant Superintendent of Police | POLICE | — | — |

### Deterministic checks: `pink_william-herbert-laurence_b1910` vs `Pink, W. H. L___Jamaica___1949`

- [PASS] surname_gate: bio 'PINK' vs stint 'Pink, W. H. L' (exact)
- [PASS] initials: bio ['W', 'H', 'L'] ~ stint ['W', 'H', 'L']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 13 vs bar 60: '2nd cl' ~ 'Senior Assistant Superintendent of Police'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Pink, W. H. L___Windward Islands___1936`

- Staff-list name: **Pink, W. H. L** | colony: **Windward Islands** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | W. H. L. Pink | Inspector of Police | Police and Gaols | — | — |
| 1937 | W. H. L. Pink | Assistant Superintendent of Police | Police and Gaols | — | — |
| 1939 | W. H. L. Pink | Inspector of Police | Police and Gaols | — | — |

### Deterministic checks: `pink_william-herbert-laurence_b1910` vs `Pink, W. H. L___Windward Islands___1936`

- [PASS] surname_gate: bio 'PINK' vs stint 'Pink, W. H. L' (exact)
- [PASS] initials: bio ['W', 'H', 'L'] ~ stint ['W', 'H', 'L']
- [PASS] age_gate: stint starts 1936, birth 1910 (age 26)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

