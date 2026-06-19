<!-- {"case_id": "case_sutherland_p_e1850", "bio_ids": ["sutherland_p_e1850"], "stint_ids": ["Sutherland, P. C___Natal___1879", "Sutherland, P. E___Jamaica___1933"]} -->
# Dossier case_sutherland_p_e1850

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sutherland_p_e1850'] carry a single initial only — the namesake trap applies.

## Biography `sutherland_p_e1850`

- Printed name: **SUTHERLAND, P.**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L35899.v` — printed in editions [1886, 1888]:**

> SUTHERLAND, P. (C.M., M.D.), L.R.C.S.E.—Served in the Franklin Search Expedition under Penny and Inglefield, 1850, 1851, and 1852; wrote an account of the Penny Expedition (Longmans, 1852, 2 vols.); paper on "Physical Geography of Davis Straits and Baffin's Bay" (Transactions of Geographical Society of London, 1852); entered the civil service of Natal, as Government Geologist, 1854; appointed surveyor-general, May, 1866.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1850–1852 | — | — | [1886, 1888] |
| 1 | 1852–1852 | — | — | [1886, 1888] |
| 2 | 1852–1852 | — | — | [1886, 1888] |
| 3 | 1854–1854 | Government Geologist | Natal | [1886, 1888] |
| 4 | 1866 | surveyor-general | — | [1886, 1888] |

## Candidate stint `Sutherland, P. C___Natal___1879`

- Staff-list name: **Sutherland, P. C** | colony: **Natal** | listed 1879–1886 | editions [1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | P. C. Sutherland | Surveyor-General | Survey Department | — | — |
| 1880 | P. C. Sutherland | Surveyor-General | Survey Department | — | — |
| 1883 | P. C. Sutherland | Surveyor-General | Lands | — | — |
| 1886 | P. C. Sutherland | Surveyor-General | Lands | — | — |

### Deterministic checks: `sutherland_p_e1850` vs `Sutherland, P. C___Natal___1879`

- [PASS] surname_gate: bio 'SUTHERLAND' vs stint 'Sutherland, P. C' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P', 'C']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1886
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Sutherland, P. E___Jamaica___1933`

- Staff-list name: **Sutherland, P. E** | colony: **Jamaica** | listed 1933–1940 | editions [1933, 1934, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | P. E. Sutherland | Senior Superintendents' Clerks and Cashiers | Department of Public Works | — | — |
| 1934 | P. E. Sutherland | Senior Superintendents' Clerks and Cashiers | Department of Public Works | — | — |
| 1937 | P. E. Sutherland | Senior Superintendents' Clerks and Cashiers | Public Works | — | — |
| 1940 | P. E. Sutherland | Senior Superintendents' Clerks and Cashiers | Department of Public Works | — | — |

### Deterministic checks: `sutherland_p_e1850` vs `Sutherland, P. E___Jamaica___1933`

- [PASS] surname_gate: bio 'SUTHERLAND' vs stint 'Sutherland, P. E' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P', 'E']
- [PASS] age_gate: stint starts 1933; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1940
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

