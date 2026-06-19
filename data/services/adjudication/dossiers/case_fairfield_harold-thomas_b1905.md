<!-- {"case_id": "case_fairfield_harold-thomas_b1905", "bio_ids": ["fairfield_harold-thomas_b1905"], "stint_ids": ["Fairfield, H. T___Uganda___1933"]} -->
# Dossier case_fairfield_harold-thomas_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fairfield_harold-thomas_b1905`

- Printed name: **FAIRFIELD, Harold Thomas**
- Birth year: 1905 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32509.v` — printed in editions [1948, 1949, 1950, 1951]:**

> FAIRFIELD, Harold Thomas.—b. 1905; ed. Polytechnic; const., Kent county const., 1927; inspr. of police, Uga., 1930; asst. supt., 1940; senr. asst., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | const., Kent county const | — | [1948, 1949, 1950, 1951] |
| 1 | 1930 | inspr. of police | Uganda | [1948, 1949, 1950, 1951] |
| 2 | 1940 | asst. supt | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1947 | senr. asst | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Fairfield, H. T___Uganda___1933`

- Staff-list name: **Fairfield, H. T** | colony: **Uganda** | listed 1933–1951 | editions [1933, 1937, 1939, 1940, 1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | H. T. Fairfield | Inspector, Traffic Branch | Police and Prisons | — | — |
| 1937 | H. T. Fairfield | Inspectors | Traffic Branch | — | — |
| 1939 | H. T. Fairfield | Inspectors | Police | — | — |
| 1940 | H. T. Fairfield | Inspector | Police | — | — |
| 1949 | H. T. Fairfield | Superintendents, Assistants and Cadets | Police | — | — |
| 1951 | H. T. Fairfield | Superintendents, Assistants and Cadets | Police | — | — |

### Deterministic checks: `fairfield_harold-thomas_b1905` vs `Fairfield, H. T___Uganda___1933`

- [PASS] surname_gate: bio 'FAIRFIELD' vs stint 'Fairfield, H. T' (exact)
- [PASS] initials: bio ['H', 'T'] ~ stint ['H', 'T']
- [PASS] age_gate: stint starts 1933, birth 1905 (age 28)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1933-1951
- [FAIL] position_sim: best 46 vs bar 60: 'inspr. of police' ~ 'Inspector, Traffic Branch'
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

