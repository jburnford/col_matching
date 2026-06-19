<!-- {"case_id": "case_pickford_w_e1909", "bio_ids": ["pickford_w_e1909"], "stint_ids": ["Pickford, W___British Central Africa___1906", "Pickford, W___Nyasaland___1908"]} -->
# Dossier case_pickford_w_e1909

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pickford_w_e1909'] carry a single initial only — the namesake trap applies.

## Biography `pickford_w_e1909`

- Printed name: **PICKFORD, W**
- Birth year: not printed
- Appears in editions: [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1910-L48090.v` — printed in editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]:**

> PICKFORD, W. — Dist. comsnr., E.A.P., 21st Aug., 1909.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | Dist. comsnr. | East Africa Protectorate | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |

## Candidate stint `Pickford, W___British Central Africa___1906`

- Staff-list name: **Pickford, W** | colony: **British Central Africa** | listed 1906–1907 | editions [1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | W. Pickford | 3rd class Assistant | Collectors | — | — |
| 1907 | W. Pickford | Eighteen 3rd class | Residents | — | — |

### Deterministic checks: `pickford_w_e1909` vs `Pickford, W___British Central Africa___1906`

- [PASS] surname_gate: bio 'PICKFORD' vs stint 'Pickford, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Central Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Pickford, W___Nyasaland___1908`

- Staff-list name: **Pickford, W** | colony: **Nyasaland** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | W. Pickford | Resident 3rd class | Residents | — | — |
| 1909 | W. Pickford | Resident, 3rd class | Residents | — | — |

### Deterministic checks: `pickford_w_e1909` vs `Pickford, W___Nyasaland___1908`

- [PASS] surname_gate: bio 'PICKFORD' vs stint 'Pickford, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
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

