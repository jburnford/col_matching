<!-- {"case_id": "case_stronach_john-clark_b1887", "bio_ids": ["stronach_john-clark_b1887"], "stint_ids": ["Stronach, J. C___Kenya___1928"]} -->
# Dossier case_stronach_john-clark_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stronach_john-clark_b1887`

- Printed name: **STRONACH, JOHN CLARK**
- Birth year: 1887 (attested in editions [1935, 1936, 1937, 1939, 1940])
- Honours: B.A., B.A.I.
- Appears in editions: [1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L62514.v` — printed in editions [1935, 1936, 1937, 1939, 1940]:**

> STRONACH, JOHN CLARK, B.A., B.A.I.—B. 1887; ed. St. Andrews Coll., Dublin, Dublin Univ. and Eng. Sch. T.C.D.; asst. engrn., Indian pub. wks., 1911; exec. engrn., 1919; New Delhi constrn., 1913-26; seconded to Kenya as supdg.-engnr. (bdgs.), 1926-29; transf'd. Kenya, 1930; ag. dir., P.W., 1930 and 1934; D.P.W., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | asst. engrn. | India | [1935, 1936, 1937, 1939, 1940] |
| 1 | 1913–1926 | New Delhi constrn. | — | [1935, 1936, 1937, 1939, 1940] |
| 2 | 1919 | exec. engrn. | — | [1935, 1936, 1937, 1939, 1940] |
| 3 | 1926–1929 | supdg.-engnr. (bdgs.) | Kenya | [1935, 1936, 1937, 1939, 1940] |
| 4 | 1930 | transf'd. | Kenya | [1935, 1936, 1937, 1939, 1940] |
| 5 | 1930–1934 | ag. dir., P.W. | — | [1935, 1936, 1937, 1939, 1940] |
| 6 | 1936 | D.P.W. | — | [1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Stronach, J. C___Kenya___1928`

- Staff-list name: **Stronach, J. C** | colony: **Kenya** | listed 1928–1934 | editions [1928, 1929, 1930, 1932, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | J. C. Stronach | Superintending Engineer, Buildings | Loan Staff | — | — |
| 1929 | J. C. Stronach | Superintending Engineer, Buildings | Loan Staff | — | — |
| 1930 | J. C. Stronach | Superintending Engineer, Buildings | Loan Staff | — | — |
| 1932 | J. C. Stronach | Superintendent Engineer | Public Works Department | — | — |
| 1934 | J. C. Stronach | Superintendent Engineer | Public Works Department | — | — |

### Deterministic checks: `stronach_john-clark_b1887` vs `Stronach, J. C___Kenya___1928`

- [PASS] surname_gate: bio 'STRONACH' vs stint 'Stronach, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1928, birth 1887 (age 41)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1928-1934
- [FAIL] position_sim: best 46 vs bar 60: 'supdg.-engnr. (bdgs.)' ~ 'Superintending Engineer, Buildings'
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

