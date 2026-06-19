<!-- {"case_id": "case_simon_julien_e1863", "bio_ids": ["simon_julien_e1863"], "stint_ids": ["Simon, J___Leeward Islands___1877", "Sim\u00e9on, J___Mauritius___1908", "Sim\u00e9on, J___Mauritius___1921"]} -->
# Dossier case_simon_julien_e1863

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['simon_julien_e1863'] carry a single initial only — the namesake trap applies.

## Biography `simon_julien_e1863`

- Printed name: **SIMON, Julien**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29491.v` — printed in editions [1883]:**

> SIMON, Julien.—Fourth revenue officer, Dominica, 1863; 3rd revenue officer, 1874.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1863 | Fourth revenue officer | Dominica | [1883] |
| 1 | 1874 | 3rd revenue officer | Dominica *(inherited from previous clause)* | [1883] |

## Candidate stint `Simon, J___Leeward Islands___1877`

- Staff-list name: **Simon, J** | colony: **Leeward Islands** | listed 1877–1880 | editions [1877, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Simon | 3rd Officer | Revenue Officers | — | — |
| 1879 | J. Simon | 3rd Officer | Civil Establishment | — | — |
| 1880 | J. Simon | 3rd Officer | Civil Establishment | — | — |

### Deterministic checks: `simon_julien_e1863` vs `Simon, J___Leeward Islands___1877`

- [PASS] surname_gate: bio 'SIMON' vs stint 'Simon, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Siméon, J___Mauritius___1908`

- Staff-list name: **Siméon, J** | colony: **Mauritius** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | J. Siméon | Roman Catholic Chaplains | Rodrigues | — | — |
| 1909 | J. Siméon | Roman Catholic Chaplain | Rodrigues | — | — |

### Deterministic checks: `simon_julien_e1863` vs `Siméon, J___Mauritius___1908`

- [PASS] surname_gate: bio 'SIMON' vs stint 'Siméon, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Siméon, J___Mauritius___1921`

- Staff-list name: **Siméon, J** | colony: **Mauritius** | listed 1921–1925 | editions [1921, 1922, 1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | J. Siméon | 2nd Class Priest | Roman Catholic Church | — | — |
| 1922 | J. Siméon | 2nd Class Priest | Roman Catholic Church | — | — |
| 1923 | J. Siméon | 2nd Class Priest | Roman Catholic Church | — | — |
| 1925 | J. Siméon | 2nd Class Priest | Roman Catholic Church | — | — |

### Deterministic checks: `simon_julien_e1863` vs `Siméon, J___Mauritius___1921`

- [PASS] surname_gate: bio 'SIMON' vs stint 'Siméon, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1925
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

