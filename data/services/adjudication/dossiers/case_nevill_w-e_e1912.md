<!-- {"case_id": "case_nevill_w-e_e1912", "bio_ids": ["nevill_w-e_e1912"], "stint_ids": ["Nevill, W. E___Kenya___1914"]} -->
# Dossier case_nevill_w-e_e1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nevill_w-e_e1912`

- Printed name: **NEVILL, W. E**
- Birth year: not printed
- Appears in editions: [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1914-L48836.v` — printed in editions [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]:**

> NEVILL, W. E.—Locomotive superintendent, Uganda Railway, July, 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | Locomotive superintendent, Uganda Railway | Uganda | [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923] |

## Candidate stint `Nevill, W. E___Kenya___1914`

- Staff-list name: **Nevill, W. E** | colony: **Kenya** | listed 1914–1918 | editions [1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | W. E. Nevill | Locomotive, Carriage and Wagon Department | Accounts | — | — |
| 1915 | W. E. Nevill | Chief Mechanical Engineer | Locomotive, Carriage and Wagon Department | — | — |
| 1917 | W. E. Nevill | Chief Mechanical Engineer | Locomotive, Carriage and Wagon Department | — | — |
| 1918 | W. E. Nevill | Chief Mechanical Engineer | Locomotive, Carriage and Wagon Department | — | — |

### Deterministic checks: `nevill_w-e_e1912` vs `Nevill, W. E___Kenya___1914`

- [PASS] surname_gate: bio 'NEVILL' vs stint 'Nevill, W. E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

