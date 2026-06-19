<!-- {"case_id": "case_rowe_william-john-vivian_e1878", "bio_ids": ["rowe_william-john-vivian_e1878"], "stint_ids": ["Rowe, J___Gold Coast___1889", "Rowe, W___Jamaica___1877"]} -->
# Dossier case_rowe_william-john-vivian_e1878

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 30 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rowe_william-john-vivian_e1878`

- Printed name: **ROWE, WILLIAM JOHN VIVIAN**
- Birth year: not printed
- Appears in editions: [1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1888-L35841.v` — printed in editions [1888, 1889]:**

> ROWE, WILLIAM JOHN VIVIAN, L. and L.M.K.Q.C.P.I., Feb., 1883.—Served in F.A.M.P. in Galecka and Gaika wars, 1878-79 (medal); medical officer, Basutoland, Sept., 1884; Fell. Roy. Col. Inst.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878–1879 | Served in F.A.M.P. in Galecka and Gaika wars | — | [1888, 1889] |
| 1 | 1884 | medical officer | Basutoland | [1888, 1889] |

## Candidate stint `Rowe, J___Gold Coast___1889`

- Staff-list name: **Rowe, J** | colony: **Gold Coast** | listed 1889–1894 | editions [1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | J. Rowe | Foremen of Works | Public Works and Survey | — | — |
| 1890 | J. Rowe | Foremen of Works | Public Works and Survey | — | — |
| 1894 | J. Rowe | Foreman of Works | Public Works Department | — | — |

### Deterministic checks: `rowe_william-john-vivian_e1878` vs `Rowe, J___Gold Coast___1889`

- [PASS] surname_gate: bio 'ROWE' vs stint 'Rowe, J' (exact)
- [PASS] initials: bio ['W', 'J', 'V'] ~ stint ['J']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1894
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Rowe, W___Jamaica___1877`

- Staff-list name: **Rowe, W** | colony: **Jamaica** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. Rowe | Archdeacon of Cornwall | Ecclesiastical Department | — | — |
| 1878 | W. Rowe | Archdeacon of Cornwall | Ecclesiastical Department | — | — |
| 1879 | W. Rowe | Archdeacon of Cornwall | Ecclesiastical Department | — | — |

### Deterministic checks: `rowe_william-john-vivian_e1878` vs `Rowe, W___Jamaica___1877`

- [PASS] surname_gate: bio 'ROWE' vs stint 'Rowe, W' (exact)
- [PASS] initials: bio ['W', 'J', 'V'] ~ stint ['W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
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

