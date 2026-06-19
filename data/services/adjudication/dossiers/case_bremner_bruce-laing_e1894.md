<!-- {"case_id": "case_bremner_bruce-laing_e1894", "bio_ids": ["bremner_bruce-laing_e1894"], "stint_ids": ["Bremner, B. L___Kenya___1910", "Bremner, B. L___Kenya___1918"]} -->
# Dossier case_bremner_bruce-laing_e1894

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bremner_bruce-laing_e1894`

- Printed name: **BREMNER, BRUCE LAING**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1908-L43398.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]:**

> BREMNER, BRUCE LAING.—Ed. at Craigmount house schl., Edin., and premium apprentice, L. & N.W. rly. shops, Crewe, 1880 to 1884; L. & N.W. rly., loco. dept., 1894 to 1897; asst. loco. supt., Uganda rly., 1898.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894–1897 | L. & N.W. rly., loco. dept | — | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |
| 1 | 1898 | asst. loco. supt., Uganda rly | Uganda | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |

## Candidate stint `Bremner, B. L___Kenya___1910`

- Staff-list name: **Bremner, B. L** | colony: **Kenya** | listed 1910–1913 | editions [1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | B. L. Bremner | Locomotive, Carriage and Wagon Department | Locomotive, Carriage and Wagon Department | — | — |
| 1911 | B. L. Bremner | Locomotive, Carriage and Wagon Department | Accounts | — | — |
| 1912 | B. L. Bremner | Locomotive, Carriage and Wagon Department | Locomotive, Carriage and Wagon Department | — | — |
| 1913 | B. L. Bremner | Locomotive, Carriage and Wagon Department | Railway | — | — |

### Deterministic checks: `bremner_bruce-laing_e1894` vs `Bremner, B. L___Kenya___1910`

- [PASS] surname_gate: bio 'BREMNER' vs stint 'Bremner, B. L' (exact)
- [PASS] initials: bio ['B', 'L'] ~ stint ['B', 'L']
- [PASS] age_gate: stint starts 1910; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1913
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bremner, B. L___Kenya___1918`

- Staff-list name: **Bremner, B. L** | colony: **Kenya** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | B. L. Bremner | District Superintendent | Locomotive, Carriage and Wagon Department | — | — |
| 1919 | B. L. Bremner | District Superintendent | Locomotive, Carriage and Wagon Department | D.S.O. | — |

### Deterministic checks: `bremner_bruce-laing_e1894` vs `Bremner, B. L___Kenya___1918`

- [PASS] surname_gate: bio 'BREMNER' vs stint 'Bremner, B. L' (exact)
- [PASS] initials: bio ['B', 'L'] ~ stint ['B', 'L']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1919
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

