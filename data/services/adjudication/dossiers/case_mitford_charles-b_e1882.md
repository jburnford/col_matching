<!-- {"case_id": "case_mitford_charles-b_e1882", "bio_ids": ["mitford_charles-b_e1882"], "stint_ids": ["Mitford, C. B___Gambia___1889", "Mitford, C. B___Sierra Leone___1888"]} -->
# Dossier case_mitford_charles-b_e1882

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Mitford, C. B___Gambia___1889` is also gate-compatible with biography(ies) outside this case: ['mitford_charles-b_e1882-2'] (already linked elsewhere or filtered).
- NOTE: stint `Mitford, C. B___Sierra Leone___1888` is also gate-compatible with biography(ies) outside this case: ['mitford_charles-b_e1882-2'] (already linked elsewhere or filtered).

## Biography `mitford_charles-b_e1882`

- Printed name: **MITFORD, CHARLES B**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34866.v` — printed in editions [1886]:**

> MITFORD, CHARLES B.—Storekeeper, public works department, Trinidad, 9th January, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Storekeeper, public works department | Trinidad | [1886] |

## Candidate stint `Mitford, C. B___Gambia___1889`

- Staff-list name: **Mitford, C. B** | colony: **Gambia** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | C. B. Mitford | Treasurer | Treasury | — | — |
| 1890 | C. B. Mitford | Treasurer | Civil Establishment | — | — |

### Deterministic checks: `mitford_charles-b_e1882` vs `Mitford, C. B___Gambia___1889`

- [PASS] surname_gate: bio 'MITFORD' vs stint 'Mitford, C. B' (exact)
- [PASS] initials: bio ['C', 'B'] ~ stint ['C', 'B']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Mitford, C. B___Sierra Leone___1888`

- Staff-list name: **Mitford, C. B** | colony: **Sierra Leone** | listed 1888–1896 | editions [1888, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | C. B. Mitford | Assistant Colonial Secretaries and Treasurers | Secretariat and Treasury | — | — |
| 1894 | C. B. Mitford | Colonial Treasurer | Treasury Department | — | — |
| 1896 | C. B. Mitford | Colonial Treasurer | Treasury Department | — | — |

### Deterministic checks: `mitford_charles-b_e1882` vs `Mitford, C. B___Sierra Leone___1888`

- [PASS] surname_gate: bio 'MITFORD' vs stint 'Mitford, C. B' (exact)
- [PASS] initials: bio ['C', 'B'] ~ stint ['C', 'B']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1896
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

