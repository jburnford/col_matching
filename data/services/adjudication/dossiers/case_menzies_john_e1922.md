<!-- {"case_id": "case_menzies_john_e1922", "bio_ids": ["menzies_john_e1922"], "stint_ids": ["Menzies, J___Tobago___1920", "Menzies, J___Trinidad and Tobago___1925"]} -->
# Dossier case_menzies_john_e1922

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['menzies_john_e1922'] carry a single initial only — the namesake trap applies.

## Biography `menzies_john_e1922`

- Printed name: **MENZIES, JOHN**
- Birth year: not printed
- Appears in editions: [1927, 1928, 1929]

### Verbatim printed entry text (OCR)

**Version `col1927-L61343.v` — printed in editions [1927, 1928, 1929]:**

> MENZIES, JOHN.—Warden, St. David, Trinidad, 16th June, 1922; warden, Caroni, 1st Dec., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | Warden, St. David | Trinidad | [1927, 1928, 1929] |
| 1 | 1925 | warden, Caroni | Trinidad *(inherited from previous clause)* | [1927, 1928, 1929] |

## Candidate stint `Menzies, J___Tobago___1920`

- Staff-list name: **Menzies, J** | colony: **Tobago** | listed 1920–1921 | editions [1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | J. Menzies | Asst. Warden | Wardens | — | — |
| 1921 | J. Menzies | Asst. Warden | Legal | — | — |

### Deterministic checks: `menzies_john_e1922` vs `Menzies, J___Tobago___1920`

- [PASS] surname_gate: bio 'MENZIES' vs stint 'Menzies, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1920; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1921
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Menzies, J___Trinidad and Tobago___1925`

- Staff-list name: **Menzies, J** | colony: **Trinidad and Tobago** | listed 1925–1929 | editions [1925, 1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | J. Menzies | Warden | Wardens | — | — |
| 1927 | J. Menzies | Warden | Legal | — | — |
| 1928 | J. Menzies | Warden | Wardens | — | — |
| 1929 | J. Menzies | Warden | Wardens | — | — |

### Deterministic checks: `menzies_john_e1922` vs `Menzies, J___Trinidad and Tobago___1925`

- [PASS] surname_gate: bio 'MENZIES' vs stint 'Menzies, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1925; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1929
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

