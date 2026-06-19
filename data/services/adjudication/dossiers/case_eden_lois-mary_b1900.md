<!-- {"case_id": "case_eden_lois-mary_b1900", "bio_ids": ["eden_lois-mary_b1900"], "stint_ids": ["Eden, L. M___Kenya___1937"]} -->
# Dossier case_eden_lois-mary_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `eden_lois-mary_b1900`

- Printed name: **EDEN, Lois Mary**
- Birth year: 1900 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L32390.v` — printed in editions [1948, 1949]:**

> EDEN, Lois Mary.—b. 1900; ed. Devizes Sec. Sch., Univ. of Lond. and Camb. Training Coll., B.A. (hons.) (Lond.), Camb. teacher's dipl.; hist. mistress, Loughborough High Sch., 1923, Rodean Sch., Jo'burg, 1926-29, City and County Sch. for Girls, Chester, 1930-31; hist. mistress, Ken. High Sch., 1932.

**Version `col1950-L35183.v` — printed in editions [1950]:**

> EDEN, Lois Mary.—b. 1900; ed. Devizes Sec. Sch., Univ. of Lond. and Camb. Training Coll., B.A. (hons.) (Lond.), Camb. teacher's dip.; hist. mistress, Ken. High Sch., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923–1923 | hist. mistress | — | [1948, 1949] |
| 1 | 1926–1929 | hist. mistress | South Africa | [1948, 1949] |
| 2 | 1930–1931 | hist. mistress | — | [1948, 1949] |
| 3 | 1932 | hist. mistress | Kenya | [1948, 1949, 1950] |

## Candidate stint `Eden, L. M___Kenya___1937`

- Staff-list name: **Eden, L. M** | colony: **Kenya** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | L. M. Eden | Education Officer—European Education | Education | — | — |
| 1939 | Miss L. M. Eden | Education Officer, European Education | Education | — | — |
| 1940 | Miss L. M. Eden | Education Officers—European Education | Education | — | — |

### Deterministic checks: `eden_lois-mary_b1900` vs `Eden, L. M___Kenya___1937`

- [PASS] surname_gate: bio 'EDEN' vs stint 'Eden, L. M' (exact)
- [PASS] initials: bio ['L', 'M'] ~ stint ['L', 'M']
- [PASS] age_gate: stint starts 1937, birth 1900 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 31 vs bar 60: 'hist. mistress' ~ 'Education Officers—European Education'
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

