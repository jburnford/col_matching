<!-- {"case_id": "case_mouat_a_e1909", "bio_ids": ["mouat_a_e1909"], "stint_ids": ["Mouat, A. J___Canada___1880", "Mouat, A___Kenya___1911", "Mouat, Alexander N___Canada___1919"]} -->
# Dossier case_mouat_a_e1909

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mouat_a_e1909'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Mouat, A. J___Canada___1880` is also gate-compatible with biography(ies) outside this case: ['mouat_a_e1901'] (already linked elsewhere or filtered).
- NOTE: stint `Mouat, A___Kenya___1911` is also gate-compatible with biography(ies) outside this case: ['mouat_a_e1901'] (already linked elsewhere or filtered).
- NOTE: stint `Mouat, Alexander N___Canada___1919` is also gate-compatible with biography(ies) outside this case: ['mouat_a_e1901'] (already linked elsewhere or filtered).

## Biography `mouat_a_e1909`

- Printed name: **MOUAT, A.**
- Birth year: not printed
- Appears in editions: [1914]

### Verbatim printed entry text (OCR)

**Version `col1914-L48750.v` — printed in editions [1914]:**

> MOUAT, A.—Med. off., E.A.P., Aug., 1909. M.O.H., Kisumu, Apr., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | Med. off. | East Africa Protectorate | [1914] |
| 1 | 1913 | M.O.H. | Kisumu | [1914] |

## Candidate stint `Mouat, A. J___Canada___1880`

- Staff-list name: **Mouat, A. J** | colony: **Canada** | listed 1880–1883 | editions [1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | A. J. Mouat | Assayer | Assay Office (Cariboo) | — | — |
| 1883 | A. J. Mouat | Assayer | Assay Office (Cariboo) | — | — |

### Deterministic checks: `mouat_a_e1909` vs `Mouat, A. J___Canada___1880`

- [PASS] surname_gate: bio 'MOUAT' vs stint 'Mouat, A. J' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Mouat, A___Kenya___1911`

- Staff-list name: **Mouat, A** | colony: **Kenya** | listed 1911–1917 | editions [1911, 1912, 1914, 1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | A. Mouat | Temporary Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1912 | A. Mouat | Temporary Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1914 | A. Mouat | Medical Officer of Health | Medical (East Africa and Uganda) | — | — |
| 1915 | A. Mouat | Medical Officer of Health | Medical (East Africa and Uganda) | — | — |
| 1917 | A. Mouat | Medical Officer of Health | Medical (East Africa and Uganda) | — | — |

### Deterministic checks: `mouat_a_e1909` vs `Mouat, A___Kenya___1911`

- [PASS] surname_gate: bio 'MOUAT' vs stint 'Mouat, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1911-1917
- [FAIL] position_sim: best 44 vs bar 60: 'Med. off.' ~ 'Medical Officer of Health'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Mouat, Alexander N___Canada___1919`

- Staff-list name: **Mouat, Alexander N** | colony: **Canada** | listed 1919–1922 | editions [1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | A. N. Mouat | Comptroller General | Department of Finance | — | — |
| 1920 | A. N. Mouat | Comptroller-General | Department of Finance | — | — |
| 1922 | Alexander N. Mouat | Comptroller-General | Controlling and Audit Branch | — | — |

### Deterministic checks: `mouat_a_e1909` vs `Mouat, Alexander N___Canada___1919`

- [PASS] surname_gate: bio 'MOUAT' vs stint 'Mouat, Alexander N' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A', 'N']
- [PASS] age_gate: stint starts 1919; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1922
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

