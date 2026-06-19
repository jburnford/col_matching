<!-- {"case_id": "case_osborne_r-e_b1921", "bio_ids": ["osborne_r-e_b1921"], "stint_ids": ["Osborne, R. E. D___Leeward Islands___1951"]} -->
# Dossier case_osborne_r-e_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 35 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `osborne_r-e_b1921`

- Printed name: **OSBORNE, R. E**
- Birth year: 1921 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L26123.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> OSBORNE, R. E.—b. 1921; ed. Munro Coll., J’ca, I.C.T.A. and Reading Univ.; junr. agric. offr., J’ca, 1939; gr. I, 1946; agric. offr., gr. II, secon., W.I., banana research scheme, 1948; gr. I, 1951; senr. agric. offr., 1952; chief agric. offr., 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | junr. agric. offr. | Jamaica | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1946 | gr. I | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1948 | agric. offr., gr. II, secon., W.I., banana research scheme | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1951 | gr. I | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1952 | senr. agric. offr | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1956 | chief agric. offr | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Osborne, R. E. D___Leeward Islands___1951`

- Staff-list name: **Osborne, R. E. D** | colony: **Leeward Islands** | listed 1951–1952 | editions [1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | R. E. D. Osborne | — | Legislative Council | — | — |
| 1952 | R. E. D. Osborne | Elected Official | Legislative Council | — | — |

### Deterministic checks: `osborne_r-e_b1921` vs `Osborne, R. E. D___Leeward Islands___1951`

- [PASS] surname_gate: bio 'OSBORNE' vs stint 'Osborne, R. E. D' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R', 'E', 'D']
- [PASS] age_gate: stint starts 1951, birth 1921 (age 30)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1952
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

