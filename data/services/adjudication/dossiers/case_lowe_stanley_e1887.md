<!-- {"case_id": "case_lowe_stanley_e1887", "bio_ids": ["lowe_stanley_e1887"], "stint_ids": ["Lowe, A. S___North Borneo___1928", "Lowe, J. S___Bahamas___1914"]} -->
# Dossier case_lowe_stanley_e1887

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['lowe_stanley_e1887'] carry a single initial only — the namesake trap applies.

## Biography `lowe_stanley_e1887`

- Printed name: **LOWE, STANLEY**
- Birth year: not printed
- Appears in editions: [1890, 1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1890-L35360.v` — printed in editions [1890, 1894, 1896]:**

> LOWE, MAJOR STANLEY.—Comm'dt., Bechuanaland police, 1887; major in augmented force, 1889; C.C. and R.M., Taungs, Brit. Bechuanaland, 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1887 | Comm'dt., Bechuanaland police | Bechuanaland | [1890, 1894, 1896] |
| 1 | 1889 | major in augmented force | Bechuanaland *(inherited from previous clause)* | [1890, 1894, 1896] |

## Candidate stint `Lowe, A. S___North Borneo___1928`

- Staff-list name: **Lowe, A. S** | colony: **North Borneo** | listed 1928–1932 | editions [1928, 1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | A. S. Lowe | Assistant Engineer | Civil Establishment | — | — |
| 1930 | A. S. Lowe | Consulting and Inspecting Engineer in England | Civil Establishment | — | — |
| 1932 | A. S. Lowe | Consulting and Inspecting Engineer in England | Civil Establishment | — | — |

### Deterministic checks: `lowe_stanley_e1887` vs `Lowe, A. S___North Borneo___1928`

- [PASS] surname_gate: bio 'LOWE' vs stint 'Lowe, A. S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['A', 'S']
- [PASS] age_gate: stint starts 1928; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1932
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Lowe, J. S___Bahamas___1914`

- Staff-list name: **Lowe, J. S** | colony: **Bahamas** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | J. S. Lowe | Relieving Officer | Medical Department | — | — |
| 1915 | J. S. Lowe | Relieving Officer | Medical Department | — | — |

### Deterministic checks: `lowe_stanley_e1887` vs `Lowe, J. S___Bahamas___1914`

- [PASS] surname_gate: bio 'LOWE' vs stint 'Lowe, J. S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1915
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

