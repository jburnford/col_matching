<!-- {"case_id": "case_hodges_a-w_b1907", "bio_ids": ["hodges_a-w_b1907", "hodges_alfred-walter_b1893"], "stint_ids": ["Hodges, A. W___Hong Kong___1927"]} -->
# Dossier case_hodges_a-w_b1907

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Hodges, A. W___Hong Kong___1927'] have more than one claimant biography in this case.

## Biography `hodges_a-w_b1907`

- Printed name: **HODGES, A. W**
- Birth year: 1907 (attested in editions [1955, 1956, 1957])
- Appears in editions: [1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1955-L21158.v` — printed in editions [1955, 1956, 1957]:**

> HODGES, A. W.—b. 1907; ed. Sydney High Sch.; Queensland State public service, 1922; Australian C'wealth civil service, 1942; asst. compt., inc. tax., Mal., 1948; senr. asst. compt., inland rev., Fed. of Mal., 1952; compt., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | Queensland State public service | Queensland | [1955, 1956, 1957] |
| 1 | 1942 | Australian C'wealth civil service | Queensland *(inherited from previous clause)* | [1955, 1956, 1957] |
| 2 | 1948 | asst. compt., inc. tax. | Malaya | [1955, 1956, 1957] |
| 3 | 1952 | senr. asst. compt., inland rev., Fed. of Mal | Malaya *(inherited from previous clause)* | [1955, 1956, 1957] |

## Biography `hodges_alfred-walter_b1893`

- Printed name: **HODGES, ALFRED WALTER**
- Birth year: 1893 (attested in editions [1937, 1940])
- Honours: A.R.I.B.A
- Appears in editions: [1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L61809.v` — printed in editions [1937, 1940]:**

> HODGES, ALFRED WALTER, A.R.I.B.A., Chartered & Reg. Archt.—B. 1893; ed. and archt. training, Exeter; war service, R.E. & R.A.F., 1914; archt. asst., England, 1919; archt., P.W.D., Hong Kong, 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | archt. asst., England | — | [1937, 1940] |
| 1 | 1925 | archt., P.W.D. | Hong Kong | [1937, 1940] |

## Candidate stint `Hodges, A. W___Hong Kong___1927`

- Staff-list name: **Hodges, A. W** | colony: **Hong Kong** | listed 1927–1940 | editions [1927, 1928, 1929, 1930, 1931, 1932, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | A. W. Hodges | Engineers | Architectural | — | — |
| 1928 | A. W. Hodges | Engineers | Architectural | — | — |
| 1929 | A. W. Hodges | Engineers | Architectural | — | — |
| 1930 | A. W. Hodges | Engineer | Architectural | — | — |
| 1931 | A. W. Hodges | Engineer | Architectural | — | — |
| 1932 | A. W. Hodges | Architect | Public Works Department | — | — |
| 1934 | A. W. Hodges | Architect | Public Works Department | — | — |
| 1937 | A. W. Hodges | Architect | Public Works Department | — | — |
| 1939 | A. W. Hodges | Architect | Public Works Department | — | — |
| 1940 | A. W. Hodges | Architects | Public Works Department | — | — |

### Deterministic checks: `hodges_a-w_b1907` vs `Hodges, A. W___Hong Kong___1927`

- [PASS] surname_gate: bio 'HODGES' vs stint 'Hodges, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1927, birth 1907 (age 20)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `hodges_alfred-walter_b1893` vs `Hodges, A. W___Hong Kong___1927`

- [PASS] surname_gate: bio 'HODGES' vs stint 'Hodges, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1927, birth 1893 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1940
- [FAIL] position_sim: best 56 vs bar 60: 'archt., P.W.D.' ~ 'Architect'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1937] pos~56 (bar: >=2)
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

