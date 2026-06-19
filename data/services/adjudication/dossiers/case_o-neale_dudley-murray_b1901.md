<!-- {"case_id": "case_o-neale_dudley-murray_b1901", "bio_ids": ["o-neale_dudley-murray_b1901"], "stint_ids": ["O'Neale, D. M___Trinidad and Tobago___1929"]} -->
# Dossier case_o-neale_dudley-murray_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `o-neale_dudley-murray_b1901`

- Printed name: **O'NEALE, Dudley Murray**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958])
- Appears in editions: [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958]

### Verbatim printed entry text (OCR)

**Version `col1948-L35027.v` — printed in editions [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958]:**

> O'NEALE, Dudley Murray, B.Sc. (civ. engnr.).—b. 1901; ed. Merchiston Castle Sch., and Edin. Univ.; on mil. serv., 1937-44, capt.; asst. engnr., P.W.D., Trin., 1928; exec. engnr., 1938; senr., 1942; div. engnr., 1944; first asst. dir., wks. and hydraulics, 1949; dep. dir., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | asst. engnr., P.W.D. | Trinidad | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958] |
| 1 | 1938 | exec. engnr | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958] |
| 2 | 1942 | senr | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958] |
| 3 | 1944 | div. engnr | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958] |
| 4 | 1949 | first asst. dir., wks. and hydraulics | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958] |

## Candidate stint `O'Neale, D. M___Trinidad and Tobago___1929`

- Staff-list name: **O'Neale, D. M** | colony: **Trinidad and Tobago** | listed 1929–1940 | editions [1929, 1931, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | D. M. O'Neale | 1st Grade District Engineer | District Engineers | — | — |
| 1931 | D. M. O'Neale | Assistant Engineer | Public Works Department | — | — |
| 1934 | D. M. O'Neale | Assistant Engineer | District Engineers | — | — |
| 1937 | D. M. O'Neale | Assistant Engineer | District Engineers | — | — |
| 1939 | D. M. O'Neale | Assistant Engineer | PUBLIC WORKS DEPARTMENT | — | — |
| 1940 | D. M. O'Neale | Executive Engineer | Public Works | — | — |

### Deterministic checks: `o-neale_dudley-murray_b1901` vs `O'Neale, D. M___Trinidad and Tobago___1929`

- [PASS] surname_gate: bio 'O'NEALE' vs stint 'O'Neale, D. M' (exact)
- [PASS] initials: bio ['D', 'M'] ~ stint ['D', 'M']
- [PASS] age_gate: stint starts 1929, birth 1901 (age 28)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1940
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

