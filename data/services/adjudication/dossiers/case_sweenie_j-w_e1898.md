<!-- {"case_id": "case_sweenie_j-w_e1898", "bio_ids": ["sweenie_j-w_e1898", "sweetie_j-w_e1898"], "stint_ids": ["Sweenie, J. W___Kenya___1909"]} -->
# Dossier case_sweenie_j-w_e1898

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Sweenie, J. W___Kenya___1909'] have more than one claimant biography in this case.

## Biography `sweenie_j-w_e1898`

- Printed name: **SWEENIE, J. W**
- Birth year: not printed
- Appears in editions: [1910, 1912, 1920]

### Verbatim printed entry text (OCR)

**Version `col1910-L49013.v` — printed in editions [1910, 1912, 1920]:**

> SWEENIE, J. W.—Asst. traffic man., Uganda rly., Aug., 1898.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898 | Asst. traffic man., Uganda rly | Uganda | [1910, 1912, 1920] |

## Biography `sweetie_j-w_e1898`

- Printed name: **SWEETIE, J. W**
- Birth year: not printed
- Appears in editions: [1914, 1917, 1918, 1922]

### Verbatim printed entry text (OCR)

**Version `col1914-L50212.v` — printed in editions [1914, 1917, 1918, 1922]:**

> SWEETIE, J. W.—Asst. traffic man., Uganda rly., Aug., 1898.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898 | Asst. traffic man., Uganda rly | Uganda | [1914, 1917, 1918, 1922] |

## Candidate stint `Sweenie, J. W___Kenya___1909`

- Staff-list name: **Sweenie, J. W** | colony: **Kenya** | listed 1909–1918 | editions [1909, 1910, 1911, 1912, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | J. W. Sweenie | Traffic | Railway | — | — |
| 1910 | J. W. Sweenie | Traffic | Traffic | — | — |
| 1911 | J. W. Sweenie | Traffic | Accounts | — | — |
| 1912 | J. W. Sweenie | Traffic | Traffic | — | — |
| 1914 | J. W. Sweenie | Traffic | Accounts | — | — |
| 1915 | J. W. Sweenie | Assistant to Manager | Railway | — | — |
| 1917 | J. W. Sweenie | Assistant to Manager | Railway | — | — |
| 1918 | J. W. Sweenie | Assistant to Manager | Railway | — | — |

### Deterministic checks: `sweenie_j-w_e1898` vs `Sweenie, J. W___Kenya___1909`

- [PASS] surname_gate: bio 'SWEENIE' vs stint 'Sweenie, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `sweetie_j-w_e1898` vs `Sweenie, J. W___Kenya___1909`

- [PASS] surname_gate: bio 'SWEETIE' vs stint 'Sweenie, J. W' (fuzzy:1)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1918
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

