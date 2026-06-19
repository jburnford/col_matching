<!-- {"case_id": "case_powles_mary_b1894", "bio_ids": ["powles_mary_b1894"], "stint_ids": ["Fowles, C. M___Australia___1913", "Powley, D. M___South Africa___1912", "Powley, D. M___Southern Rhodesia___1911"]} -->
# Dossier case_powles_mary_b1894

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['powles_mary_b1894'] carry a single initial only — the namesake trap applies.

## Biography `powles_mary_b1894`

- Printed name: **POWLES, Mary**
- Birth year: 1894 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L35025.v` — printed in editions [1949, 1950, 1951]:**

> POWLES, Mary.—b. 1894; ed. C. of E. Sch., Ross, Herefordshire and privately; nursing sister, Ken., 1929; senr., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | nursing sister | Kenya | [1949, 1950, 1951] |
| 1 | 1944 | senr | Kenya *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Fowles, C. M___Australia___1913`

- Staff-list name: **Fowles, C. M** | colony: **Australia** | listed 1913–1927 | editions [1913, 1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | C. M. Fowles | Chief Clerk | Irrigation and Reclamation Works | — | — |
| 1918 | C. M. Fowles | Secretary | Irrigation and Reclamation Works | — | — |
| 1927 | C. M. Fowles | Secretary | Administrative Officers | — | — |

### Deterministic checks: `powles_mary_b1894` vs `Fowles, C. M___Australia___1913`

- [PASS] surname_gate: bio 'POWLES' vs stint 'Fowles, C. M' (fuzzy:1)
- [PASS] initials: bio ['M'] ~ stint ['C', 'M']
- [PASS] age_gate: stint starts 1913, birth 1894 (age 19)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Powley, D. M___South Africa___1912`

- Staff-list name: **Powley, D. M** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | D. M. Powley | Native Commissioner | Native Affairs Department | — | — |
| 1914 | D. M. Powley | Native Commissioner, Mashonaland | Native Affairs Department | — | — |
| 1918 | D. M. Powley | Native Commissioner | Native Affairs Department | — | — |

### Deterministic checks: `powles_mary_b1894` vs `Powley, D. M___South Africa___1912`

- [PASS] surname_gate: bio 'POWLES' vs stint 'Powley, D. M' (fuzzy:1)
- [PASS] initials: bio ['M'] ~ stint ['D', 'M']
- [PASS] age_gate: stint starts 1912, birth 1894 (age 18)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Powley, D. M___Southern Rhodesia___1911`

- Staff-list name: **Powley, D. M** | colony: **Southern Rhodesia** | listed 1911–1927 | editions [1911, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | D. M. Powley | Native Commissioner | Native Affairs Department | — | — |
| 1925 | D. M. Powley | Native Commissioner | Native Commissioners | — | — |
| 1927 | D. M. Powley | Native Commissioner | Chief Native Commissioner's Department | — | — |

### Deterministic checks: `powles_mary_b1894` vs `Powley, D. M___Southern Rhodesia___1911`

- [PASS] surname_gate: bio 'POWLES' vs stint 'Powley, D. M' (fuzzy:1)
- [PASS] initials: bio ['M'] ~ stint ['D', 'M']
- [PASS] age_gate: stint starts 1911, birth 1894 (age 17)
- [FAIL] colony: no placed event resolves to 'Southern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1927
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

