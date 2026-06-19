<!-- {"case_id": "case_thierens_p-a_b1925", "bio_ids": ["thierens_p-a_b1925"], "stint_ids": ["Thierens, P. A___British Guiana___1963"]} -->
# Dossier case_thierens_p-a_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `thierens_p-a_b1925`

- Printed name: **THIERENS, P. A.**
- Birth year: 1925 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L22388.v` — printed in editions [1964, 1965, 1966]:**

> THIERENS, P. A.—b. 1925; ed. Queen's Coll., B.G.; temp. clk., cl. II, B.G., 1944; clk., cl. II, 1946, cl. I, 1953; asst. dist. comsnr., 1955; dist. comsnr., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944–1944 | temp. clk., cl. II | British Guiana | [1964, 1965, 1966] |
| 1 | 1946–1946 | clk., cl. II | — | [1964, 1965, 1966] |
| 2 | 1953–1953 | cl. I | — | [1964, 1965, 1966] |
| 3 | 1955–1955 | asst. dist. comsnr. | — | [1964, 1965, 1966] |
| 4 | 1962–1962 | dist. comsnr. | — | [1964, 1965, 1966] |

## Candidate stint `Thierens, P. A___British Guiana___1963`

- Staff-list name: **Thierens, P. A** | colony: **British Guiana** | listed 1963–1966 | editions [1963, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | P. A. Thierens | District Commissioner | Civil Establishment | — | — |
| 1965 | P. A. Thierens | District Commissioner | Civil Establishment | — | — |
| 1966 | P. A. Thierens | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `thierens_p-a_b1925` vs `Thierens, P. A___British Guiana___1963`

- [PASS] surname_gate: bio 'THIERENS' vs stint 'Thierens, P. A' (exact)
- [PASS] initials: bio ['P', 'A'] ~ stint ['P', 'A']
- [PASS] age_gate: stint starts 1963, birth 1925 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1966
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

