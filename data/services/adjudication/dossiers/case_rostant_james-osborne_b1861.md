<!-- {"case_id": "case_rostant_james-osborne_b1861", "bio_ids": ["rostant_james-osborne_b1861"], "stint_ids": ["Rostant, J. O___Trinidad and Tobago___1910", "Rostant, J. O___Trinidad___1896"]} -->
# Dossier case_rostant_james-osborne_b1861

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rostant_james-osborne_b1861`

- Printed name: **ROSTANT, JAMES OSBORNE**
- Birth year: 1861 (attested in editions [1917])
- Appears in editions: [1917]

### Verbatim printed entry text (OCR)

**Version `col1917-L52853.v` — printed in editions [1917]:**

> ROSTANT, JAMES OSBORNE.—B. 1861; entd. pub. wks. dept., Trinidad, 15th Feb., 1884; dist. offr., 1st grade, P.W.D., 1st Jan., 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884 | entd. pub. wks. dept. | Trinidad | [1917] |
| 1 | 1897 | dist. offr., 1st grade, P.W.D | Trinidad *(inherited from previous clause)* | [1917] |

## Candidate stint `Rostant, J. O___Trinidad and Tobago___1910`

- Staff-list name: **Rostant, J. O** | colony: **Trinidad and Tobago** | listed 1910–1915 | editions [1910, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | J. O. Rostant | District Officer | District Officers | — | — |
| 1912 | J. O. Rostant | District Officer | District Officers | — | — |
| 1913 | J. O. Rostant | District Officer | District Officers | — | — |
| 1914 | J. O. Rostant | District Officer | District Officers | — | — |
| 1915 | J. O. Rostant | District Officer, Sangre Grande (N. Division) | District Officers | — | — |

### Deterministic checks: `rostant_james-osborne_b1861` vs `Rostant, J. O___Trinidad and Tobago___1910`

- [PASS] surname_gate: bio 'ROSTANT' vs stint 'Rostant, J. O' (exact)
- [PASS] initials: bio ['J', 'O'] ~ stint ['J', 'O']
- [PASS] age_gate: stint starts 1910, birth 1861 (age 49)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1915
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Rostant, J. O___Trinidad___1896`

- Staff-list name: **Rostant, J. O** | colony: **Trinidad** | listed 1896–1911 | editions [1896, 1898, 1908, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | J. O. Rostant | 2nd Assistant Engineer of Works | Public Works Department | — | — |
| 1898 | J. O. Rostant | District Officer | District Officers | — | — |
| 1908 | J. O. Rostant | District Officer | District Officers | — | — |
| 1911 | J. O. Rostant | District Officer | District Officers | — | — |

### Deterministic checks: `rostant_james-osborne_b1861` vs `Rostant, J. O___Trinidad___1896`

- [PASS] surname_gate: bio 'ROSTANT' vs stint 'Rostant, J. O' (exact)
- [PASS] initials: bio ['J', 'O'] ~ stint ['J', 'O']
- [PASS] age_gate: stint starts 1896, birth 1861 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1896-1911
- [FAIL] position_sim: best 51 vs bar 60: 'dist. offr., 1st grade, P.W.D' ~ 'District Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

