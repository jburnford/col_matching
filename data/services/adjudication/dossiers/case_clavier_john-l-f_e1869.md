<!-- {"case_id": "case_clavier_john-l-f_e1869", "bio_ids": ["clavier_john-l-f_e1869"], "stint_ids": ["Clavier, J. L___Windward Islands___1877", "Clavier, L___British Guiana___1918"]} -->
# Dossier case_clavier_john-l-f_e1869

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `clavier_john-l-f_e1869`

- Printed name: **CLAVIER, JOHN L. F.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26870.v` — printed in editions [1883]:**

> CLAVIER, JOHN L. F.—Supernumerary clerk in the treasurer's office, St. Lucia, March, 1869; acted as clerk in that office from May, 1871, to July, 1872; transferred to the colonial secretary's office as fourth clerk; returned to the treasury as second clerk, in June, 1874; first clerk, March, 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Supernumerary clerk | St. Lucia | [1883] |
| 1 | 1871–1872 | clerk | — | [1883] |
| 2 | 1874 | second clerk | — | [1883] |
| 3 | 1875 | first clerk | — | [1883] |

## Candidate stint `Clavier, J. L___Windward Islands___1877`

- Staff-list name: **Clavier, J. L** | colony: **Windward Islands** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. L. Clavier | Clerk to Treasurer | Civil Establishment | — | — |
| 1878 | J. L. Clavier | Clerk to Treasurer | Civil Establishment | — | — |

### Deterministic checks: `clavier_john-l-f_e1869` vs `Clavier, J. L___Windward Islands___1877`

- [PASS] surname_gate: bio 'CLAVIER' vs stint 'Clavier, J. L' (exact)
- [PASS] initials: bio ['J', 'L', 'F'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Clavier, L___British Guiana___1918`

- Staff-list name: **Clavier, L** | colony: **British Guiana** | listed 1918–1929 | editions [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | L. Clavier | Surgeon, No. 1 Dispensary, Alms House and Orphan Asylum | Medical Department | — | — |
| 1919 | L. Clavier | Medical Officer | Poor | — | — |
| 1919 | L. Clavier | Surgeon, No. 1 Dispensary, Alms House and Orphan Asylum | Government Medical Officers | — | — |
| 1920 | L. Clavier | Surgeon, No. 1 Dispensary, Alms House and Orphan Asylum | Government Medical Officers | — | — |
| 1920 | L. Clavier | Medical Officer | Poor | — | — |
| 1921 | Dr. L. Clavier | Medical Officer | Poor | — | — |
| 1922 | L. Clavier | Surgeon | Medical Department | — | — |
| 1923 | L. Clavier | Surgeon, No. 1 Dispensary and Alms House | Government Medical Officers | — | — |
| 1923 | L. Clavier | Medical Officer | Poor | — | — |
| 1924 | L. Clavier | Surgeon, No. 1 Dispensary and Alms House | Medical Department | — | — |
| 1925 | L. Clavier | Medical Officer | Poor | — | — |
| 1927 | L. Clavier | Medical Officer | Poor | — | — |
| 1927 | L. Clavier | Surgeon | Government Medical Officers | — | — |
| 1928 | L. Clavier | Surgeon, No. 1 Dispensary and Alms House | Medical Department | — | — |
| 1928 | L. Clavier | Medical Officer | Poor | — | — |
| 1929 | L. Clavier | Surgeon, No. 1 Dispensary and Alms House | Medical Department | — | — |

### Deterministic checks: `clavier_john-l-f_e1869` vs `Clavier, L___British Guiana___1918`

- [PASS] surname_gate: bio 'CLAVIER' vs stint 'Clavier, L' (exact)
- [PASS] initials: bio ['J', 'L', 'F'] ~ stint ['L']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1929
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

