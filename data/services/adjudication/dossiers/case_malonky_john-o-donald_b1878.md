<!-- {"case_id": "case_malonky_john-o-donald_b1878", "bio_ids": ["malonky_john-o-donald_b1878"], "stint_ids": ["Maloney, J. O___Barbados___1905", "Maloney, J. O___Leeward Islands___1908"]} -->
# Dossier case_malonky_john-o-donald_b1878

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `malonky_john-o-donald_b1878`

- Printed name: **MALONKY, JOHN O'DONALD**
- Birth year: 1878 (attested in editions [1913])
- Appears in editions: [1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1913-L47912.v` — printed in editions [1913]:**

> MALONKY, JOHN O'DONALD.—B. 1878; asst. for sugar cane experiments, Barbados, 1904-1906; tempy. cotton instructor, Nevis, Oct., 1906, to Jan., 1907; ag. instrucr., Nevis, April, 1907.

**Version `col1911-L46568.v` — printed in editions [1911, 1912]:**

> MALONEY, JOHN O'DONALD.—B. 1878; asst. for sugar cane experiments, Barbados, 1904-1906; tempy. cotton instructor, Nevis, Oct., 1906, to Jan., 1907; ag. instructor, Nevis, April, 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904–1906 | asst. for sugar cane experiments | Barbados | [1911, 1912, 1913] |
| 1 | 1906–1907 | tempy. cotton instructor | Nevis | [1911, 1912, 1913] |
| 2 | 1907 | ag. instrucr. | Nevis | [1911, 1912, 1913] |

## Candidate stint `Maloney, J. O___Barbados___1905`

- Staff-list name: **Maloney, J. O** | colony: **Barbados** | listed 1905–1908 | editions [1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | J. O. Maloney | Junior Assistant | Sugar Cane Experiments | — | — |
| 1906 | J. O. Maloney | Junior Assistant | Sugar Cane Experiments | — | — |
| 1907 | J. O. Maloney | Junior Assistant | Sugar Cane Experiments | — | — |
| 1908 | J. O. Maloney | Junior Assistant | Sugar Cane Experiments | — | — |

### Deterministic checks: `malonky_john-o-donald_b1878` vs `Maloney, J. O___Barbados___1905`

- [PASS] surname_gate: bio 'MALONKY' vs stint 'Maloney, J. O' (fuzzy:1)
- [PASS] initials: bio ['J', 'O'] ~ stint ['J', 'O']
- [PASS] age_gate: stint starts 1905, birth 1878 (age 27)
- [PASS] colony: 1 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1908
- [FAIL] position_sim: best 43 vs bar 60: 'asst. for sugar cane experiments' ~ 'Junior Assistant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Maloney, J. O___Leeward Islands___1908`

- Staff-list name: **Maloney, J. O** | colony: **Leeward Islands** | listed 1908–1912 | editions [1908, 1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | J. O. Maloney | Agricultural Instructor (Nevis) | Public Works, &c. | — | — |
| 1911 | J. O. Maloney | Agricultural Instructor | Public Works, &c. | — | — |
| 1912 | J. O. Maloney | Agricultural Instructor (Nevis) | Public Works | — | — |

### Deterministic checks: `malonky_john-o-donald_b1878` vs `Maloney, J. O___Leeward Islands___1908`

- [PASS] surname_gate: bio 'MALONKY' vs stint 'Maloney, J. O' (fuzzy:1)
- [PASS] initials: bio ['J', 'O'] ~ stint ['J', 'O']
- [PASS] age_gate: stint starts 1908, birth 1878 (age 30)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1912
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

