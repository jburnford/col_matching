<!-- {"case_id": "case_milliken_m_b1923", "bio_ids": ["milliken_m_b1923", "milliken_w-m_b1910"], "stint_ids": ["Milliken, M___West Indies Federation___1961"]} -->
# Dossier case_milliken_m_b1923

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['milliken_m_b1923'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Milliken, M___West Indies Federation___1961'] have more than one claimant biography in this case.

## Biography `milliken_m_b1923`

- Printed name: **MILLIKEN, M**
- Birth year: 1923 (attested in editions [1960, 1961, 1962, 1963])
- Appears in editions: [1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1960-L26075.v` — printed in editions [1960, 1961, 1962, 1963]:**

> MILLIKEN, M.—b. 1923; ed. Auckland Gram. Sch., and Univ. of N.Z.; mil. serv., 1941–44; N. Rhod., 1950–52; min. of agric., fish. and food, London, 1954–58; agric. economist, T.W.I., 1958; fed. statistician, 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950–1952 | — | Northern Rhodesia | [1960, 1961, 1962, 1963] |
| 1 | 1954–1958 | min. of agric., fish. and food, London | Northern Rhodesia *(inherited from previous clause)* | [1960, 1961, 1962, 1963] |
| 2 | 1958 | agric. economist, T.W.I | Northern Rhodesia *(inherited from previous clause)* | [1960, 1961, 1962, 1963] |
| 3 | 1959 | fed. statistician | Northern Rhodesia *(inherited from previous clause)* | [1960, 1961, 1962, 1963] |

## Biography `milliken_w-m_b1910`

- Printed name: **MILLIKEN, W. M**
- Birth year: 1910 (attested in editions [1954, 1955, 1956, 1957])
- Honours: C.V.O (1956), O.B.E
- Appears in editions: [1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1954-L21600.v` — printed in editions [1954, 1955, 1956, 1957]:**

> MILLIKEN, W. M., C.V.O. (1956), O.B.E.—b. 1910; ed. Kings Coll. and Univ. Coll., Auckland, N.Z.; mil. serv., 1940-46, maj.; cadet, Nig., 1938; cl. II, 1949; cl. I, 1953; sec., premier and ex. co., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | cadet | Nigeria | [1954, 1955, 1956, 1957] |
| 1 | 1949 | cl. II | Nigeria *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |
| 2 | 1953 | cl. I | Nigeria *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |
| 3 | 1954 | sec., premier and ex. co | Nigeria *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |

## Candidate stint `Milliken, M___West Indies Federation___1961`

- Staff-list name: **Milliken, M** | colony: **West Indies Federation** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | M. Milliken | Federal Statistician | Law Officers | — | — |
| 1962 | M. Milliken | Federal Statistician | Law Officers | — | — |

### Deterministic checks: `milliken_m_b1923` vs `Milliken, M___West Indies Federation___1961`

- [PASS] surname_gate: bio 'MILLIKEN' vs stint 'Milliken, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1961, birth 1923 (age 38)
- [FAIL] colony: no placed event resolves to 'West Indies Federation'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `milliken_w-m_b1910` vs `Milliken, M___West Indies Federation___1961`

- [PASS] surname_gate: bio 'MILLIKEN' vs stint 'Milliken, M' (exact)
- [PASS] initials: bio ['W', 'M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1961, birth 1910 (age 51)
- [FAIL] colony: no placed event resolves to 'West Indies Federation'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
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

