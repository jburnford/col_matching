<!-- {"case_id": "case_hadden_william-edward_b1912", "bio_ids": ["hadden_william-edward_b1912"], "stint_ids": ["Hadden, W. E___Gambia___1949"]} -->
# Dossier case_hadden_william-edward_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hadden_william-edward_b1912`

- Printed name: **HADDEN, William Edward**
- Birth year: 1912 (attested in editions [1957, 1959])
- Appears in editions: [1951, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1957-L23696.v` — printed in editions [1957, 1959]:**

> HADDEN, W. E.—b. 1912; ed. Queen Eliz. Gram. Sch., Wimborne, St. Thos. Hosp., London Univ.; mil. serv., 1940-43, capt., R.A.M.C.; M.O., Nig., 1938; Gam., 1945; M.O.H., 1949; asst. I.G.; med. servs., Nig., 1954; D.D.M.S., N. regn., 1954-58.

**Version `col1958-L23210.v` — printed in editions [1958]:**

> HADEN, W. E.—b. 1912; ed. Queen Eliz. Gram. Sch., Wimborne, St. Thos. Hosp., London Univ.; mil. serv., 1940-43, capt., R.A.M.C.; M.O., Nig., 1938; Gam., 1945; M.O.H., 1949; asst. I.-G., med. servs., Nig., 1954; D.D.M.S., N. regn., 1954.

**Version `col1951-L38712.v` — printed in editions [1951]:**

> HADDEN, William Edward, M.B.B.S. (Lond.), L.R.C.P. (Lond.), D.T.M. & H. (Eng.), D.A. (R.C.S., Eng.), D.P.H. (Eng.).—b. 1912; ed. Queen Elizabeth's Gram. Sch. and St. Thos. Hosp. Med. Sch.; on mil. serv., 1940-43, capt.; med. offr., Nig., 1938; Gam., 1945; M.O.H., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | M.O. | Nigeria | [1951, 1957, 1958, 1959] |
| 1 | 1945 | Gam | Nigeria *(inherited from previous clause)* | [1951, 1957, 1958, 1959] |
| 2 | 1949 | M.O.H | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959] |
| 3 | 1950 | M.O.H | Nigeria *(inherited from previous clause)* | [1951] |
| 4 | 1954 | med. servs. | Nigeria | [1957, 1958, 1959] |

## Candidate stint `Hadden, W. E___Gambia___1949`

- Staff-list name: **Hadden, W. E** | colony: **Gambia** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. E. Hadden | Medical Officer | Medical and Health | — | — |
| 1950 | W. E. Hadden | Medical Officers | Medical and Health | — | — |
| 1951 | W. E. Hadden | Medical Officer of Health | Medical and Health | — | — |

### Deterministic checks: `hadden_william-edward_b1912` vs `Hadden, W. E___Gambia___1949`

- [PASS] surname_gate: bio 'HADDEN' vs stint 'Hadden, W. E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

