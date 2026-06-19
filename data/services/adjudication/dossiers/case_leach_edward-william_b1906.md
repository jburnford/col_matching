<!-- {"case_id": "case_leach_edward-william_b1906", "bio_ids": ["leach_edward-william_b1906"], "stint_ids": ["Leach, E. W___Trinidad and Tobago___1949"]} -->
# Dossier case_leach_edward-william_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `leach_edward-william_b1906`

- Printed name: **LEACH, Edward William**
- Birth year: 1906 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955])
- Honours: A.I.C.T.A
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1948-L33975.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955]:**

> LEACH, Edward William, B.Sc. (Agric.) (Lond.), A.I.C.T.A.—b. 1906; ed. Eastbourne Gram. Sch., Reading Univ., post grad. courses at Oxford Univ. and I.C.T.A.; supt. of agric., Nig., 1928; senr. agric. offr., 1939; senr. agric. supt., Gam., 1939; dep. dir. of agric. (crop husbandry) Trin., 1945; dir. agric., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | supt. of agric. | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1939 | senr. agric. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 2 | 1945 | dep. dir. of agric. (crop husbandry) Trin | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 3 | 1948 | dir. agric | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |

## Candidate stint `Leach, E. W___Trinidad and Tobago___1949`

- Staff-list name: **Leach, E. W** | colony: **Trinidad and Tobago** | listed 1949–1952 | editions [1949, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. W. Leach | Director and Registrar, Agricultural Co-operative Societies | Agriculture | — | — |
| 1952 | E. W. Leach | Director of Agriculture and Registrar, Agricultural Co-operative Societies | Civil Establishment | — | — |

### Deterministic checks: `leach_edward-william_b1906` vs `Leach, E. W___Trinidad and Tobago___1949`

- [PASS] surname_gate: bio 'LEACH' vs stint 'Leach, E. W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['E', 'W']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1952
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

