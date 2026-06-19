<!-- {"case_id": "case_wilby_george-stainburn_b1905", "bio_ids": ["wilby_george-stainburn_b1905", "wilby_george-stanburn_b1905"], "stint_ids": ["Wilby, G. S___Hong Kong___1949"]} -->
# Dossier case_wilby_george-stainburn_b1905

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Wilby, G. S___Hong Kong___1949'] have more than one claimant biography in this case.

## Biography `wilby_george-stainburn_b1905`

- Printed name: **WILBY, GEORGE STAINBURN**
- Birth year: 1905 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71792.v` — printed in editions [1939, 1940]:**

> WILBY, GEORGE STAINBURN, B.A. (Hons.) (Oxon.).—B. 1905; asst. educn., Nigeria, 1928; asst. mast., educn., dept. Hong Kong, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | asst. educn. | Nigeria | [1939, 1940] |
| 1 | 1935 | asst. mast., educn., dept. Hong Kong | Nigeria *(inherited from previous clause)* | [1939, 1940] |

## Biography `wilby_george-stanburn_b1905`

- Printed name: **WILBY, George Stanburn**
- Birth year: 1905 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36849.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WILBY, George Stanburn.—b. 1905; ed. Queen Elizabeth's Gram. Sch., Wakefield, and Univ. Coll., Oxford, M.A. (Oxon); on mil. serv., H.K.V.D.C., 1941-45, lieut.; supt., educ., Nig., 1928; mstr., educ. dept., H.K., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | supt., educ. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1935 | mstr., educ. dept. | Hong Kong | [1948, 1949, 1950, 1951] |

## Candidate stint `Wilby, G. S___Hong Kong___1949`

- Staff-list name: **Wilby, G. S** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. S. Wilby | Masters | Education Department | — | — |
| 1950 | G. S. Wilby | Masters | Education | — | — |
| 1951 | G. S. Wilby | Masters | Education | — | — |

### Deterministic checks: `wilby_george-stainburn_b1905` vs `Wilby, G. S___Hong Kong___1949`

- [PASS] surname_gate: bio 'WILBY' vs stint 'Wilby, G. S' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G', 'S']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `wilby_george-stanburn_b1905` vs `Wilby, G. S___Hong Kong___1949`

- [PASS] surname_gate: bio 'WILBY' vs stint 'Wilby, G. S' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G', 'S']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

