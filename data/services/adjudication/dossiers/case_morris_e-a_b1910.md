<!-- {"case_id": "case_morris_e-a_b1910", "bio_ids": ["morris_e-a_b1910"], "stint_ids": ["Morris, E. A___Jamaica___1930"]} -->
# Dossier case_morris_e-a_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 113 official(s) with this surname in the graph's staff lists; 39 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Morris, E. A___Jamaica___1930` is also gate-compatible with biography(ies) outside this case: ['morris_alfred_b1874'] (already linked elsewhere or filtered).

## Biography `morris_e-a_b1910`

- Printed name: **MORRIS, E. A**
- Birth year: 1910 (attested in editions [1964, 1965, 1966])
- Honours: O.B.E (1961)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L20033.v` — printed in editions [1964, 1965, 1966]:**

> MORRIS, E. A., O.B.E. (1961).—b. 1910; ed. Hampton Gram. Sch. and Univ. of London; C.A.'s off., 1928; mil. serv., 1942–46, sqdn. Idr.; H.E.O., 1942; S.E.O., 1949; asst. hd. of dept., 1956; hd., appts. dept., 1958; hd. shipping dept., 1962; hd. stores dept., 1962; co-dir. O. and M. Unit, 1960; asst. C.A., 1964.

**Version `col1957-L25826.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> MORRIS, E. A., O.B.E. (1961).—b. 1910; C.O., C.A.’s off., 1928; mil. serv., 1942-46, sqdn. ldr.; H.E.O., 1942; S.E.O., 1949; asst. hd. of dept., 1956; hd., appts. dept., 1958; hd. stores dept., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | C.A.'s off | Colonial Office | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1942 | H.E.O | Colonial Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1949 | S.E.O | Colonial Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1956 | asst. hd. of dept | Colonial Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1958 | hd., appts. dept | Colonial Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1960 | co-dir. O. and M. Unit | — | [1964, 1965, 1966] |
| 6 | 1962 | hd. shipping dept | — | [1964, 1965, 1966] |
| 7 | 1962 | hd. stores dept | Colonial Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 8 | 1964 | asst. C.A | — | [1964, 1965, 1966] |

## Candidate stint `Morris, E. A___Jamaica___1930`

- Staff-list name: **Morris, E. A** | colony: **Jamaica** | listed 1930–1940 | editions [1930, 1931, 1933, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | E. A. Morris | 2nd Class Clerk | Head Office | — | — |
| 1931 | E. A. Morris | 1st Class Clerks | Public Works | — | — |
| 1933 | E. A. Morris | 1st Class Clerks | Department of Public Works | — | — |
| 1937 | E. A. Morris | 1st Class Clerks | Public Works | — | — |
| 1940 | E. A. Morris | Financial Clerk | Head Office | — | — |

### Deterministic checks: `morris_e-a_b1910` vs `Morris, E. A___Jamaica___1930`

- [PASS] surname_gate: bio 'MORRIS' vs stint 'Morris, E. A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1930, birth 1910 (age 20)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1940
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

