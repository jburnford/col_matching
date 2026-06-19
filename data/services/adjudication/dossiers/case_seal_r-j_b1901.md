<!-- {"case_id": "case_seal_r-j_b1901", "bio_ids": ["seal_r-j_b1901", "seal_ralph-john_b1901"], "stint_ids": ["Seal, R. J___Northern Rhodesia___1949"]} -->
# Dossier case_seal_r-j_b1901

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Seal, R. J___Northern Rhodesia___1949'] have more than one claimant biography in this case.

## Biography `seal_r-j_b1901`

- Printed name: **SEAL, R. J**
- Birth year: 1901 (attested in editions [1956, 1957, 1958, 1959, 1960])
- Appears in editions: [1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1956-L24026.v` — printed in editions [1956, 1957, 1958, 1959, 1960]:**

> SEAL, R. J.—b. 1901; ed. City and Guilds Coll. and Univ. Coll., London; Richmond Coll., Ceylon, 1925; educ. offr., N. Rhod., 1940; asst. dir., African educ., 1952; dep. dir., 1958-59; author of school textbooks.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | Richmond Coll. | Ceylon | [1956, 1957, 1958, 1959, 1960] |
| 1 | 1952 | asst. dir., African educ | Ceylon *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960] |
| 2 | 1958–1959 | dep. dir | Ceylon *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960] |

## Biography `seal_ralph-john_b1901`

- Printed name: **SEAL, Ralph John**
- Birth year: 1901 (attested in editions [1951])
- Honours: A.R.I.C
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L42342.v` — printed in editions [1951]:**

> SEAL, Ralph John, M.Sc. (Lond.), A.R.I.C.—b. 1901; ed. City and Guilds Coll. and Univ. Coll. London., dip. educ. (Lond.); mstr., N. Rhod., 1940; educ. offr., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | mstr. | Northern Rhodesia | [1951] |

## Candidate stint `Seal, R. J___Northern Rhodesia___1949`

- Staff-list name: **Seal, R. J** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. J. Seal | Education Officer | Education | — | — |
| 1951 | R. J. Seal | Education Officer | Education | — | — |

### Deterministic checks: `seal_r-j_b1901` vs `Seal, R. J___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'SEAL' vs stint 'Seal, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `seal_ralph-john_b1901` vs `Seal, R. J___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'SEAL' vs stint 'Seal, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 19 vs bar 60: 'mstr.' ~ 'Education Officer'
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

