<!-- {"case_id": "case_onwu_simon-ezievuo_b1908", "bio_ids": ["onwu_simon-ezievuo_b1908"], "stint_ids": ["Onwu, S. E___Nigeria___1956"]} -->
# Dossier case_onwu_simon-ezievuo_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `onwu_simon-ezievuo_b1908`

- Printed name: **ONWU, Simon Ezievuo**
- Birth year: 1908 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961])
- Honours: D.T.M, M.B, M.V.O, O.B.E
- Appears in editions: [1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1956-L23334.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961]:**

> ONWU, S. E., O.B.E., M.V.O.—b. 1908; ed. Udi Govt. Sch., St. Mary's, Onitsha, Wesleyan Boys' High Sch. and King's Coll., Lagos, Univ. Coll., London and Edin. Univ.; apptd., Nig., 1933; M.O., 1935; S.M.O., 1949; D.D.M.S., 1952; D.M.S., E. Nig., 1956.

**Version `col1948-L35031.v` — printed in editions [1948, 1949, 1950, 1951]:**

> ONWU, Simon Ezievuo, M.B., Ch.B. (Edin.), D.T.M., D.T.M. (Liv.), L.M. (Dublin).—b. 1908; ed. Wesleyan Boys' High Sch. and King's Coll., Lagos (exhib.), Univ. Coll., Lond. and Edin. Univ.; med. offr., Nig., 1933; S.M.O., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | apptd. | Nigeria | [1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1935 | M.O | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |
| 2 | 1949 | S.M.O | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |
| 3 | 1950 | S.M.O | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1952 | D.D.M.S | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |
| 5 | 1956 | D.M.S. | Eastern Nigeria | [1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Onwu, S. E___Nigeria___1956`

- Staff-list name: **Onwu, S. E** | colony: **Nigeria** | listed 1956–1960 | editions [1956, 1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | S. E. Onwu | Deputy Director of Medical Services | Civil Establishment, Eastern Region | — | — |
| 1958 | S. E. Onwu | Director of Medical Services | Civil Establishment | — | — |
| 1958 | S. E. Onwu | Director of Medical Services | — | — | — |
| 1960 | S. E. Onwu | Chief Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `onwu_simon-ezievuo_b1908` vs `Onwu, S. E___Nigeria___1956`

- [PASS] surname_gate: bio 'ONWU' vs stint 'Onwu, S. E' (exact)
- [PASS] initials: bio ['S', 'E'] ~ stint ['S', 'E']
- [PASS] age_gate: stint starts 1956, birth 1908 (age 48)
- [PASS] colony: 6 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1956-1960
- [FAIL] position_sim: best 21 vs bar 60: 'D.D.M.S' ~ 'Deputy Director of Medical Services'
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

