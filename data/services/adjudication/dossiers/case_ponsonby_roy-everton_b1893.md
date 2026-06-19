<!-- {"case_id": "case_ponsonby_roy-everton_b1893", "bio_ids": ["ponsonby_roy-everton_b1893"], "stint_ids": ["Ponsonby, R. E___Tanganyika___1923"]} -->
# Dossier case_ponsonby_roy-everton_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ponsonby_roy-everton_b1893`

- Printed name: **PONSONBY, ROY EVERTON**
- Birth year: 1893 (attested in editions [1931, 1932])
- Appears in editions: [1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1931-L67441.v` — printed in editions [1931, 1932]:**

> PONSONBY, ROY EVERTON, A.M. Inst. C.E.—B. 1893; ed. Otago High Schol., New Zealand, St. Paul's Schol. and King's Coll., London; served R.E., 1916-19; asst. engr., P.W.D., Tanganyika Territory, Jan., 1922; sen. asst. engr., Aug., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916–1919 | served R.E | — | [1931, 1932] |
| 1 | 1922 | asst. engr., P.W.D., Tanganyika Territory | Tanganyika | [1931, 1932] |
| 2 | 1929 | sen. asst. engr | Tanganyika *(inherited from previous clause)* | [1931, 1932] |

## Candidate stint `Ponsonby, R. E___Tanganyika___1923`

- Staff-list name: **Ponsonby, R. E** | colony: **Tanganyika** | listed 1923–1925 | editions [1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | R. E. Ponsonby | Assistant Engineers | Public Works Department | — | — |
| 1924 | R. E. Ponsonby | Assistant Engineers | Public Works Department | — | — |
| 1925 | R. E. Ponsonby | Assistant Engineer | Public Works Department | — | — |

### Deterministic checks: `ponsonby_roy-everton_b1893` vs `Ponsonby, R. E___Tanganyika___1923`

- [PASS] surname_gate: bio 'PONSONBY' vs stint 'Ponsonby, R. E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R', 'E']
- [PASS] age_gate: stint starts 1923, birth 1893 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1925
- [FAIL] position_sim: best 42 vs bar 60: 'asst. engr., P.W.D., Tanganyika Territory' ~ 'Assistant Engineer'
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

