<!-- {"case_id": "case_chenery_ernest-martin_b1912", "bio_ids": ["chenery_ernest-martin_b1912"], "stint_ids": ["Chenery, E. M___Trinidad and Tobago___1937"]} -->
# Dossier case_chenery_ernest-martin_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chenery_ernest-martin_b1912`

- Printed name: **CHENERY, Ernest Martin**
- Birth year: 1912 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Honours: A.R.C.S, D.I.C
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1957-L21882.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> CHENERY, E. M.—b. 1912; ed. Felixstowe Gram. Sch. and Imp. Coll. of Science and Tech., London Univ.; soil chmst., Trin., 1936; senr. chmst., Uga., 1950; chief research offr., agric. dept., 1958-60; publ. 20 scientific pp. on bio-geochemistry, soil science and analytical chemistry.

**Version `col1948-L31745.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CHENERY, Ernest Martin, Ph.D., D.I.C., B.Sc., A.R.C.S.—b. 1912; ed. Felixstowe Gram. Sch. and I.C.S. Tech., Univ. of Lond.; soil chem., dep. of agric., Trin., 1936; chem., agric. dept., Uga., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | soil chmst. | Trinidad | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1950 | senr. chmst. | Uganda | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961] |
| 2 | 1958–1960 | chief research offr., agric. dept | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Chenery, E. M___Trinidad and Tobago___1937`

- Staff-list name: **Chenery, E. M** | colony: **Trinidad and Tobago** | listed 1937–1949 | editions [1937, 1939, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | E. M. Chenery | Assistant Chemist, Soil Survey | Scientific and Technical Staff | — | — |
| 1939 | E. M. Chenery | Assistant Chemist, Soil Survey | Department of Agriculture | — | — |
| 1949 | E. M. Chenery | Soil Chemist | Agriculture | — | — |

### Deterministic checks: `chenery_ernest-martin_b1912` vs `Chenery, E. M___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'CHENERY' vs stint 'Chenery, E. M' (exact)
- [PASS] initials: bio ['E', 'M'] ~ stint ['E', 'M']
- [PASS] age_gate: stint starts 1937, birth 1912 (age 25)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1949
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

