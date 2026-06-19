<!-- {"case_id": "case_henderson_alexander-victor-simpson_b1897", "bio_ids": ["henderson_alexander-victor-simpson_b1897"], "stint_ids": ["Henderson, A. V. S___Gold Coast___1932", "Henderson, A. V___Hong Kong___1914"]} -->
# Dossier case_henderson_alexander-victor-simpson_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 78 official(s) with this surname in the graph's staff lists; 28 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `henderson_alexander-victor-simpson_b1897`

- Printed name: **HENDERSON, Alexander Victor Simpson**
- Birth year: 1897 (attested in editions [1948, 1949, 1950, 1951])
- Honours: B.A, B.A.I
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33281.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HENDERSON, Alexander Victor Simpson, B.A., B.A.I.—b. 1897; ed. Rathmines Coll., Dublin, and Dublin Univ.; on mil. serv., 1915-19; asst. engnr., P.W.D., G.C., 1926; exec. engnr., gr. I, 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. engnr., P.W.D. | Gold Coast | [1948, 1949, 1950, 1951] |
| 1 | 1944 | exec. engnr., gr. I | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Henderson, A. V. S___Gold Coast___1932`

- Staff-list name: **Henderson, A. V. S** | colony: **Gold Coast** | listed 1932–1936 | editions [1932, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | A. V. S. Henderson | Executive Engineer | Public Works Department | — | — |
| 1936 | A. V. S. Henderson | Executive Engineer | Public Works Department | — | — |

### Deterministic checks: `henderson_alexander-victor-simpson_b1897` vs `Henderson, A. V. S___Gold Coast___1932`

- [PASS] surname_gate: bio 'HENDERSON' vs stint 'Henderson, A. V. S' (exact)
- [PASS] initials: bio ['A', 'V', 'S'] ~ stint ['A', 'V', 'S']
- [PASS] age_gate: stint starts 1932, birth 1897 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1932-1936
- [FAIL] position_sim: best 38 vs bar 60: 'asst. engnr., P.W.D.' ~ 'Executive Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Henderson, A. V___Hong Kong___1914`

- Staff-list name: **Henderson, A. V** | colony: **Hong Kong** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | A. V. Henderson | Assistant Mistress | Belilios Public School | — | — |
| 1915 | Miss A. V. Henderson | Assistant Mistress | Belilios Public School | — | — |

### Deterministic checks: `henderson_alexander-victor-simpson_b1897` vs `Henderson, A. V___Hong Kong___1914`

- [PASS] surname_gate: bio 'HENDERSON' vs stint 'Henderson, A. V' (exact)
- [PASS] initials: bio ['A', 'V', 'S'] ~ stint ['A', 'V']
- [PASS] age_gate: stint starts 1914, birth 1897 (age 17)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1915
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

