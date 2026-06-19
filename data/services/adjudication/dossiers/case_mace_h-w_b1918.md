<!-- {"case_id": "case_mace_h-w_b1918", "bio_ids": ["mace_h-w_b1918"], "stint_ids": ["Mace, H. W___High Commission Territories___1963", "Mace, H. W___Swaziland___1962"]} -->
# Dossier case_mace_h-w_b1918

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mace_h-w_b1918`

- Printed name: **MACE, H. W**
- Birth year: 1918 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L24787.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> MACE, H. W.—b. 1918; ed. Fawnhope County Sch., and St. Peter's Train. Coll., Hereford; mil. serv., 1940–46, Q.M.S.; clk., Basuto., 1946; Swaz., 1954; contrlr., stores, 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | clk. | Basutoland | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1954 | Swaz | Basutoland *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1956 | contrlr., stores | Basutoland *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Mace, H. W___High Commission Territories___1963`

- Staff-list name: **Mace, H. W** | colony: **High Commission Territories** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | H. W. Mace | Controller of Stores | SECRETARIAT | — | — |
| 1964 | H. W. Mace | Controller of Stores | Civil Establishment | — | — |

### Deterministic checks: `mace_h-w_b1918` vs `Mace, H. W___High Commission Territories___1963`

- [PASS] surname_gate: bio 'MACE' vs stint 'Mace, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1963, birth 1918 (age 45)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1964
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Mace, H. W___Swaziland___1962`

- Staff-list name: **Mace, H. W** | colony: **Swaziland** | listed 1962–1965 | editions [1962, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | H. W. Mace | Controller of Stores | Secretariat | — | — |
| 1965 | H. W. Mace | Controller of Stores | Law Officers | — | — |

### Deterministic checks: `mace_h-w_b1918` vs `Mace, H. W___Swaziland___1962`

- [PASS] surname_gate: bio 'MACE' vs stint 'Mace, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1962, birth 1918 (age 44)
- [FAIL] colony: no placed event resolves to 'Swaziland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1962-1965
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

