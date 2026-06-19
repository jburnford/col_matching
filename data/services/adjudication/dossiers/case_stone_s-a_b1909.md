<!-- {"case_id": "case_stone_s-a_b1909", "bio_ids": ["stone_s-a_b1909"], "stint_ids": ["Stone, S. A___British Honduras___1949", "Stone, S. A___Northern Rhodesia___1959"]} -->
# Dossier case_stone_s-a_b1909

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 45 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stone_s-a_b1909`

- Printed name: **STONE, S. A**
- Birth year: 1909 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L22117.v` — printed in editions [1964, 1965, 1966]:**

> STONE, S. A.—b. 1909; ed. Herbert Strutt Sch., Derbyshire; U.K. local govt., 1928–44; acctnt. gen., B. Bond., 1945; fin. sec. 1948; N. Rhod., 1952; dep. acctnt. gen., 1957; ch. acctnt, 1958; asst. sec., 1962–65. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928–1944 | U.K. local govt | — | [1964, 1965, 1966] |
| 1 | 1945 | acctnt. gen., B. Bond | — | [1964, 1965, 1966] |
| 2 | 1948 | fin. sec | — | [1964, 1965, 1966] |
| 3 | 1952 | fin. sec | Northern Rhodesia | [1964, 1965, 1966] |
| 4 | 1957 | dep. acctnt. gen | Northern Rhodesia *(inherited from previous clause)* | [1964, 1965, 1966] |
| 5 | 1958 | ch. acctnt | Northern Rhodesia *(inherited from previous clause)* | [1964, 1965, 1966] |
| 6 | 1962–1965 | asst. sec | Northern Rhodesia *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Stone, S. A___British Honduras___1949`

- Staff-list name: **Stone, S. A** | colony: **British Honduras** | listed 1949–1952 | editions [1949, 1950, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. A. Stone | Financial Secretary | Treasury | — | — |
| 1950 | S. A. Stone | Financial Secretary | Treasury | — | — |
| 1951 | S. A. Stone | Financial Secretary | Treasury | — | — |
| 1952 | S. A. Stone | Financial Secretary | Civil Establishment | — | — |

### Deterministic checks: `stone_s-a_b1909` vs `Stone, S. A___British Honduras___1949`

- [PASS] surname_gate: bio 'STONE' vs stint 'Stone, S. A' (exact)
- [PASS] initials: bio ['S', 'A'] ~ stint ['S', 'A']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1952
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Stone, S. A___Northern Rhodesia___1959`

- Staff-list name: **Stone, S. A** | colony: **Northern Rhodesia** | listed 1959–1960 | editions [1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | S. A. Stone | Deputy Accountant General | Civil Establishment | — | — |
| 1960 | S. A. Stone | Deputy Accountant-General | Civil Establishment | — | — |

### Deterministic checks: `stone_s-a_b1909` vs `Stone, S. A___Northern Rhodesia___1959`

- [PASS] surname_gate: bio 'STONE' vs stint 'Stone, S. A' (exact)
- [PASS] initials: bio ['S', 'A'] ~ stint ['S', 'A']
- [PASS] age_gate: stint starts 1959, birth 1909 (age 50)
- [PASS] colony: 4 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1959-1960
- [PASS] position_sim: best 72 vs bar 60: 'dep. acctnt. gen' ~ 'Deputy Accountant General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

