<!-- {"case_id": "case_dick_george-sidney_b1896", "bio_ids": ["dick_george-sidney_b1896"], "stint_ids": ["Dick, G. S___Sierra Leone___1939"]} -->
# Dossier case_dick_george-sidney_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dick_george-sidney_b1896`

- Printed name: **DICK, George Sidney**
- Birth year: 1896 (attested in editions [1948, 1949, 1950, 1951])
- Honours: O.B.E
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32230.v` — printed in editions [1948, 1949, 1950, 1951]:**

> DICK, George Sidney, O.B.E., B.Sc. (Eng.)—b. 1896; ed. Carhoustie Sch., Harris Acad., Dundee, and St. Andrew's Univ.; on mil. serv. 1914-19, 2nd lieut.; asst. engrnr., rlwys. construc., G.C., 1923; asst. engrnr., rlwys., Nig., 1928; ch. engrnr., rlwys., S.L., 1938; asst. ch. engrnr., rlwys., Nig., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | asst. engrnr., rlwys. construc. | Gold Coast | [1948, 1949, 1950, 1951] |
| 1 | 1928 | asst. engrnr., rlwys. | Nigeria | [1948, 1949, 1950, 1951] |
| 2 | 1938 | ch. engrnr., rlwys. | Sierra Leone | [1948, 1949, 1950, 1951] |
| 3 | 1946 | asst. ch. engrnr., rlwys. | Nigeria | [1948, 1949, 1950, 1951] |

## Candidate stint `Dick, G. S___Sierra Leone___1939`

- Staff-list name: **Dick, G. S** | colony: **Sierra Leone** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | G. S. Dick | Chief Engineer | Railway Department | — | — |
| 1940 | G. S. Dick | Chief Engineer | Railway Department | — | — |

### Deterministic checks: `dick_george-sidney_b1896` vs `Dick, G. S___Sierra Leone___1939`

- [PASS] surname_gate: bio 'DICK' vs stint 'Dick, G. S' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G', 'S']
- [PASS] age_gate: stint starts 1939, birth 1896 (age 43)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 55 vs bar 60: 'ch. engrnr., rlwys.' ~ 'Chief Engineer'
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

