<!-- {"case_id": "case_budge_william_e1862", "bio_ids": ["budge_william_e1862"], "stint_ids": ["Budge, William___Sierra Leone___1878"]} -->
# Dossier case_budge_william_e1862

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['budge_william_e1862'] carry a single initial only — the namesake trap applies.

## Biography `budge_william_e1862`

- Printed name: **BUDGE, WILLIAM**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26640.v` — printed in editions [1883]:**

> BUDGE, WILLIAM.—Chief clerk in the office of the registrar of courts, Trinidad, Feb., 1868; was acting clerk of the peace for the town of Port of Spain and western district of the county of St. George from March to November, 1862; acting clerk of the peace for the eastern district of the county of St. Patrick from November, 1862, to February, 1863; acting registrar of courts from April to June, 1865, and from July, 1866, to May, 1867; acting clerk to the legislative council, and confidential clerk to the colonial secretary from August, 1870, to May, 1871; manager and coroner of the second eastern and Quiah districts, Sierra Leone; police magistrate and commissioner of the court of requests; acted for a short time in 1876 as civil commandant of Sherbro.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862–1862 | acting clerk of the peace | — | [1883] |
| 1 | 1865–1867 | acting registrar of courts | — | [1883] |
| 2 | 1868 | Chief clerk in the office of the registrar of courts | Trinidad | [1883] |
| 3 | 1870–1871 | acting clerk to the legislative council, and confidential clerk to the colonial secretary | — | [1883] |
| 4 | 1876–1876 | civil commandant | Sherbro | [1883] |

## Candidate stint `Budge, William___Sierra Leone___1878`

- Staff-list name: **Budge, William** | colony: **Sierra Leone** | listed 1878–1883 | editions [1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | William Budge | Manager and Coroner | Rural Districts | — | — |
| 1879 | William Budge | Manager and Coroner | Rural Districts | — | — |
| 1880 | W. Budge | Manager | 2nd Eastern | — | — |
| 1883 | W. Budge | Manager | Rural Districts | — | — |

### Deterministic checks: `budge_william_e1862` vs `Budge, William___Sierra Leone___1878`

- [PASS] surname_gate: bio 'BUDGE' vs stint 'Budge, William' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1883
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

