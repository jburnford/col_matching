<!-- {"case_id": "case_gregor_a_b1918", "bio_ids": ["gregor_a_b1918"], "stint_ids": ["Gregory, A. M___Gambia___1957"]} -->
# Dossier case_gregor_a_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gregor_a_b1918'] carry a single initial only — the namesake trap applies.

## Biography `gregor_a_b1918`

- Printed name: **GREGOR, A**
- Birth year: 1918 (attested in editions [1964, 1965])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L17571.v` — printed in editions [1964, 1965]:**

> GREGOR, A.—b. 1918; ed. Paisley Gram. Sch. and Glasgow Vet. Coll.; mil. serv., 1940-47, capt.; vet. offr., N. Rhod., 1953. (Zambia Govt. service.)

**Version `col1966-L15106.v` — printed in editions [1966]:**

> GREGOR, A.—b. 1918; ed. Lochwinnoch Public Sch., Paisley Gram. Sch., Speirs Sch., Beith, Glasgow Univ., and Glasgow Vet. Coll.; mil. serv., 1940-47, capt.; vet. offr., N. Rhod., 1953. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | vet. offr. | Northern Rhodesia | [1964, 1965, 1966] |

## Candidate stint `Gregory, A. M___Gambia___1957`

- Staff-list name: **Gregory, A. M** | colony: **Gambia** | listed 1957–1964 | editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | A. M. Gregory | Director of Education | Civil Establishment | — | — |
| 1958 | A. M. Gregory | Director of Education | Civil Establishment | — | — |
| 1959 | A. M. Gregory | Director of Education | Civil Establishment | — | — |
| 1960 | A. M. Gregory | Director of Education | Civil Establishment | — | — |
| 1961 | A. M. Gregory | Director of Education | Civil Establishment | — | — |
| 1962 | A. M. Gregory | Director of Education | Civil Establishment | — | — |
| 1963 | A. M. Gregory | Secretary to Ministry and Director of Education | Ministry of Education | — | — |
| 1964 | A. M. Gregory | Secretary to Ministry and Director of Education | Ministry of Education | — | — |

### Deterministic checks: `gregor_a_b1918` vs `Gregory, A. M___Gambia___1957`

- [PASS] surname_gate: bio 'GREGOR' vs stint 'Gregory, A. M' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1957, birth 1918 (age 39)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1964
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

