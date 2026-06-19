<!-- {"case_id": "case_dover_h-b_e1913", "bio_ids": ["dover_h-b_e1913"], "stint_ids": ["Dover, H. B___Kenya___1915"]} -->
# Dossier case_dover_h-b_e1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dover_h-b_e1913`

- Printed name: **DOVER, H. B**
- Birth year: not printed
- Appears in editions: [1917, 1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1917-L49150.v` — printed in editions [1917, 1918, 1919, 1920, 1921, 1922]:**

> DOVER, H. B.—Asst. traffic man., Uganda rly., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | Asst. traffic man., Uganda rly | Uganda | [1917, 1918, 1919, 1920, 1921, 1922] |

## Candidate stint `Dover, H. B___Kenya___1915`

- Staff-list name: **Dover, H. B** | colony: **Kenya** | listed 1915–1917 | editions [1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | H. B. Dover | Assistant Traffic Managers | Traffic | — | — |
| 1917 | H. B. Dover | Assistant Traffic Managers | Traffic | — | — |

### Deterministic checks: `dover_h-b_e1913` vs `Dover, H. B___Kenya___1915`

- [PASS] surname_gate: bio 'DOVER' vs stint 'Dover, H. B' (exact)
- [PASS] initials: bio ['H', 'B'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1917
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

