<!-- {"case_id": "case_baird_matthew_e1917", "bio_ids": ["baird_matthew_e1917"], "stint_ids": ["Baird, E. M___Uganda___1924", "Baird, R. M___New Zealand___1917"]} -->
# Dossier case_baird_matthew_e1917

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 19 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['baird_matthew_e1917'] carry a single initial only — the namesake trap applies.

## Biography `baird_matthew_e1917`

- Printed name: **BAIRD, MATTHEW**
- Birth year: not printed
- Appears in editions: [1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1918-L48408.v` — printed in editions [1918, 1919, 1920, 1921, 1922]:**

> BAIRD, MATTHEW.—Min. of educn., Victoria, Nov., 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | Min. of educn. | Victoria | [1918, 1919, 1920, 1921, 1922] |

## Candidate stint `Baird, E. M___Uganda___1924`

- Staff-list name: **Baird, E. M** | colony: **Uganda** | listed 1924–1928 | editions [1924, 1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | E. M. Baird | Ploughing Instructor | Agricultural Department | — | — |
| 1925 | E. M. Baird | Ploughing Instructor | Agricultural Department | — | — |
| 1927 | E. M. Baird | Ploughing Instructor | Agricultural Department | — | — |
| 1928 | E. M. Baird | Ploughing Instructor | Agricultural Department | — | — |

### Deterministic checks: `baird_matthew_e1917` vs `Baird, E. M___Uganda___1924`

- [PASS] surname_gate: bio 'BAIRD' vs stint 'Baird, E. M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['E', 'M']
- [PASS] age_gate: stint starts 1924; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1928
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Baird, R. M___New Zealand___1917`

- Staff-list name: **Baird, R. M** | colony: **New Zealand** | listed 1917–1919 | editions [1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | R. M. Baird | District Telegraph Engineer | Post and Telegraph Department | — | — |
| 1918 | R. M. Baird | District Telegraph Engineer | Post and Telegraph Department | — | — |
| 1919 | R. M. Baird | District Telegraph Engineer | Post and Telegraph Department | — | — |

### Deterministic checks: `baird_matthew_e1917` vs `Baird, R. M___New Zealand___1917`

- [PASS] surname_gate: bio 'BAIRD' vs stint 'Baird, R. M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['R', 'M']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1919
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

