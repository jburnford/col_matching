<!-- {"case_id": "case_sanker-adams_a_b1928", "bio_ids": ["sanker-adams_a_b1928"], "stint_ids": ["Sankar-Adams, A___British Guiana___1964", "Sankar-Adams, Mrs. A___British Guiana___1963"]} -->
# Dossier case_sanker-adams_a_b1928

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sanker-adams_a_b1928'] carry a single initial only — the namesake trap applies.
- Phase 1 found `sanker-adams_a_b1928` ↔ `Sankar-Adams, A___British Guiana___1964` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `sanker-adams_a_b1928` ↔ `Sankar-Adams, Mrs. A___British Guiana___1963` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `sanker-adams_a_b1928`

- Printed name: **SANKER-ADAMS, A**
- Birth year: 1928 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L24576.v` — printed in editions [1963, 1964, 1965, 1966]:**

> SANKER-ADAMS, Mrs. A.—b. 1928; ed. Bishops' H. Sch., B.G., and Somerville Coll., Oxford; barrister-at-law; prin. legal advr., B.G., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1962 | prin. legal advr. | British Guiana | [1963, 1964, 1965, 1966] |

## Candidate stint `Sankar-Adams, A___British Guiana___1964`

- Staff-list name: **Sankar-Adams, A** | colony: **British Guiana** | listed 1964–1966 | editions [1964, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | Mrs. A. Sankar-Adams | Principal Legal Adviser | Civil Establishment | — | — |
| 1966 | Mrs. A. Sankar-Adams | Principal Legal Adviser | Civil Establishment | — | — |

### Deterministic checks: `sanker-adams_a_b1928` vs `Sankar-Adams, A___British Guiana___1964`

- [PASS] surname_gate: bio 'SANKER-ADAMS' vs stint 'Sankar-Adams, A' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1964, birth 1928 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1964-1966
- [PASS] position_sim: best 79 vs bar 60: 'prin. legal advr.' ~ 'Principal Legal Adviser'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1964, 1966] pos~79 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Sankar-Adams, Mrs. A___British Guiana___1963`

- Staff-list name: **Sankar-Adams, Mrs. A** | colony: **British Guiana** | listed 1963–1965 | editions [1963, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | Mrs. A. Sankar-Adams | Principal Legal Adviser | Law Officers | — | — |
| 1965 | Mrs. A. Sankar-Adams | Principal Legal Adviser | Civil Establishment | — | — |

### Deterministic checks: `sanker-adams_a_b1928` vs `Sankar-Adams, Mrs. A___British Guiana___1963`

- [PASS] surname_gate: bio 'SANKER-ADAMS' vs stint 'Sankar-Adams, Mrs. A' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['M', 'A']
- [PASS] age_gate: stint starts 1963, birth 1928 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1963-1965
- [PASS] position_sim: best 79 vs bar 60: 'prin. legal advr.' ~ 'Principal Legal Adviser'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1963, 1965] pos~79 (bar: >=2)
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

