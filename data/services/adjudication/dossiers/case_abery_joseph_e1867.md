<!-- {"case_id": "case_abery_joseph_e1867", "bio_ids": ["abery_joseph_e1867"], "stint_ids": ["Abey, J. R___Australia___1913", "Abey, J. R___Tasmania___1894"]} -->
# Dossier case_abery_joseph_e1867

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['abery_joseph_e1867'] carry a single initial only — the namesake trap applies.

## Biography `abery_joseph_e1867`

- Printed name: **ABERY, JOSEPH**
- Birth year: not printed
- Honours: M.B.C.M
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L31192.v` — printed in editions [1897]:**

> ABERY, JOSEPH, M.B.C.M.—Assistant colonel surgeon, Ceylon, 1867.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1867 | Assistant colonel surgeon | Ceylon | [1897] |

## Candidate stint `Abey, J. R___Australia___1913`

- Staff-list name: **Abey, J. R** | colony: **Australia** | listed 1913–1918 | editions [1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | J. R. Abey | Stationmaster | Tasmanian Government Railways | — | — |
| 1918 | J. R. Abey | Stationmaster | Tasmanian Government Railways | — | — |

### Deterministic checks: `abery_joseph_e1867` vs `Abey, J. R___Australia___1913`

- [PASS] surname_gate: bio 'ABERY' vs stint 'Abey, J. R' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['J', 'R']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Abey, J. R___Tasmania___1894`

- Staff-list name: **Abey, J. R** | colony: **Tasmania** | listed 1894–1917 | editions [1894, 1896, 1897, 1898, 1899, 1905, 1906, 1907, 1908, 1909, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | J. R. Abey | Stationmaster | Tasmanian Government Railways | — | — |
| 1896 | J. R. Abey | Stationmaster | Tasmanian Government Railways | — | — |
| 1897 | J. R. Abey | Engineer, Launceston | Engineers | — | — |
| 1898 | J. R. Abey | Stationmaster | Tasmanian Government Railways | — | — |
| 1899 | J. R. Abey | Clerk | Tasmanian Government Railways. | — | — |
| 1905 | J. R. Abey | Stationmaster | Tasmanian Government Railways | — | — |
| 1906 | J. R. Abey | Stationmaster | Tasmanian Government Railways | — | — |
| 1907 | J. R. Abey | Stationmaster | Tasmanian Government Railways | — | — |
| 1908 | J. R. Abey | Stationmaster | Tasmanian Government Railways. | — | — |
| 1909 | J. R. Abey | Stationmaster | Tasmanian Government Railways | — | — |
| 1917 | J. R. Abey | Stationmaster | Tasmanian Government Railways | — | — |

### Deterministic checks: `abery_joseph_e1867` vs `Abey, J. R___Tasmania___1894`

- [PASS] surname_gate: bio 'ABERY' vs stint 'Abey, J. R' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['J', 'R']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Tasmania'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1917
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

