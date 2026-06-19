<!-- {"case_id": "case_banks_leslie-wilson_b1906", "bio_ids": ["banks_leslie-wilson_b1906"], "stint_ids": ["Banks, W___Mauritius___1936"]} -->
# Dossier case_banks_leslie-wilson_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `banks_leslie-wilson_b1906`

- Printed name: **BANKS, Leslie Wilson**
- Birth year: 1906 (attested in editions [1948, 1949, 1950, 1951])
- Honours: M.B, O.B.E (1957)
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1948-L30960.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BANKS, Leslie Wilson, M.B., Ch.B. (Edin.), D.T.M. & H. (Edin.).—b. 1906; ed. George Watson's Coll., and Edin. Univ.; med. offr., Nig., 1931; S.M.O., 1950.

**Version `col1957-L20877.v` — printed in editions [1957, 1958, 1959]:**

> BANKS, L. W., O.B.E. (1957).—b. 1906; ed. Lanark Gram. Sch., Geo. Watson's Boys Sch. and Edin. Univ.; M.O., Nig., 1931; S.M.O., 1950-58.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | med. offr. | Nigeria | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |
| 1 | 1950 | S.M.O | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |

## Candidate stint `Banks, W___Mauritius___1936`

- Staff-list name: **Banks, W** | colony: **Mauritius** | listed 1936–1937 | editions [1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | W. Banks | Civil Chaplain | Church of England | — | — |
| 1937 | W. Banks | Civil Chaplain | Church of England | — | — |

### Deterministic checks: `banks_leslie-wilson_b1906` vs `Banks, W___Mauritius___1936`

- [PASS] surname_gate: bio 'BANKS' vs stint 'Banks, W' (exact)
- [PASS] initials: bio ['L', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1936, birth 1906 (age 30)
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1937
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

