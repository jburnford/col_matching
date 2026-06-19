<!-- {"case_id": "case_humphries_g-j_b1900", "bio_ids": ["humphries_g-j_b1900"], "stint_ids": ["Humphries, G___Kenya___1922"]} -->
# Dossier case_humphries_g-j_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `humphries_g-j_b1900`

- Printed name: **HUMPHRIES, G. J**
- Birth year: 1900 (attested in editions [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: O.B.E (1954)
- Appears in editions: [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1949-L33080.v` — printed in editions [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> HUMPHRIES, G. J., O.B.E. (1954).—b. 1900; ed. St. James Sch., Tyresham, Magdalen Coll. Sch., Brackley, and Reading Univ.; mil. serv., 1939-46, lt.-col.; survr., Nig., 1928; senr., 1945; dep. dir., o'seas surveys, 1946; dir. and surveys advr. to S. of S. & D.T.C., 1963; dir. and surveys advr. to O.D.M., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | survr. | Nigeria | [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1945 | senr | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1946 | dep. dir., o'seas surveys | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1963 | dir. and surveys advr. to S. of S. & D.T.C | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1964 | dir. and surveys advr. to O.D.M | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Humphries, G___Kenya___1922`

- Staff-list name: **Humphries, G** | colony: **Kenya** | listed 1922–1928 | editions [1922, 1924, 1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | G. Humphries | Headmistress | Education | — | — |
| 1924 | G. Humphries | Headmistress | Education | — | — |
| 1925 | Mrs. G. Humphries | Headmistress | Education | — | — |
| 1927 | Mrs. G. Humphries | Principal (Lady) | Education | — | — |
| 1928 | G. Humphries | Principal (Lady) | Education | — | — |

### Deterministic checks: `humphries_g-j_b1900` vs `Humphries, G___Kenya___1922`

- [PASS] surname_gate: bio 'HUMPHRIES' vs stint 'Humphries, G' (exact)
- [PASS] initials: bio ['G', 'J'] ~ stint ['G']
- [PASS] age_gate: stint starts 1922, birth 1900 (age 22)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1928
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

