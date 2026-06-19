<!-- {"case_id": "case_rhodes_m-c_b1905", "bio_ids": ["rhodes_m-c_b1905"], "stint_ids": ["Rhodes, M. C___Kenya___1949"]} -->
# Dossier case_rhodes_m-c_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rhodes_m-c_b1905`

- Printed name: **RHODES, M. C**
- Birth year: 1905 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L23759.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> RHODES, M. C.—b. 1905; ed. Sebright Sch., Worc., and B'ham Univ.; engrn. (roads bch.), P.W.D., Ken., 1948; asst. D.P.W. (roads), Nyasa., 1955-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | engrn. (roads bch.), P.W.D. | Kenya | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1955–1961 | asst. D.P.W. (roads) | Nyasaland | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Rhodes, M. C___Kenya___1949`

- Staff-list name: **Rhodes, M. C** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | M. C. Rhodes | Construction Engineer (Roads) | Development and Reconstruction Staff | — | — |
| 1951 | M. C. Rhodes | Engineers | Development and Reconstruction Staff | — | — |

### Deterministic checks: `rhodes_m-c_b1905` vs `Rhodes, M. C___Kenya___1949`

- [PASS] surname_gate: bio 'RHODES' vs stint 'Rhodes, M. C' (exact)
- [PASS] initials: bio ['M', 'C'] ~ stint ['M', 'C']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 52 vs bar 60: 'engrn. (roads bch.), P.W.D.' ~ 'Construction Engineer (Roads)'
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

