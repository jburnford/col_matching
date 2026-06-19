<!-- {"case_id": "case_brewer_j-s_e1872", "bio_ids": ["brewer_j-s_e1872", "brewer_j-s_e1881"], "stint_ids": ["Brewer, J. S___Hong Kong___1883", "Brewer, J___Southern Nigeria___1909", "Brewer, Jane___Lagos___1905"]} -->
# Dossier case_brewer_j-s_e1872

## Case context

- 2 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Brewer, J. S___Hong Kong___1883'] have more than one claimant biography in this case.
- Phase 1 found `brewer_j-s_e1872` ↔ `Brewer, J. S___Hong Kong___1883` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `brewer_j-s_e1881` ↔ `Brewer, J. S___Hong Kong___1883` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `brewer_j-s_e1872`

- Printed name: **BREWER, J. S**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L32296.v` — printed in editions [1888, 1889, 1890]:**

> BREWER, J. S.—Employed as surveyor under the Board of Trade, 1872 to 1876; marine surveyor, Hong Kong, 11th Feb., 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872–1876 | Employed as surveyor under the Board of Trade | — | [1888, 1889, 1890] |
| 1 | 1881 | marine surveyor | Hong Kong | [1888, 1889, 1890] |

## Biography `brewer_j-s_e1881`

- Printed name: **BREWER, J. S**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L32328.v` — printed in editions [1886]:**

> BREWER, J. S.—Marine surveyor, Hong Kong, 11th Feb., 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Marine surveyor | Hong Kong | [1886] |

## Candidate stint `Brewer, J. S___Hong Kong___1883`

- Staff-list name: **Brewer, J. S** | colony: **Hong Kong** | listed 1883–1890 | editions [1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | J. S. Brewer | Marine Surveyor | Government Marine Surveyor's Department | — | — |
| 1886 | J. S. Brewer | Assistant Superintendents | Fire Brigade | — | — |
| 1888 | J. S. Brewer | Assistant Superintendent | Fire Brigade | — | — |
| 1888 | J. S. Brewer | Marine Surveyor | Marine Surveyor's (Sub-Department) | — | — |
| 1889 | J. S. Brewer | Assistant Superintendents | Fire Brigade | — | — |
| 1889 | J. S. Brewer | Marine Surveyor | Marine Surveyor's (Sub-Department) | — | — |
| 1890 | J. S. Brewer | Assistant Superintendent | Fire Brigade | — | — |
| 1890 | J. S. Brewer | Marine Surveyor | Marine Surveyor's (Sub-Department) | — | — |

### Deterministic checks: `brewer_j-s_e1872` vs `Brewer, J. S___Hong Kong___1883`

- [PASS] surname_gate: bio 'BREWER' vs stint 'Brewer, J. S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1890
- [PASS] position_sim: best 100 vs bar 60: 'marine surveyor' ~ 'Marine Surveyor'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 3 agreeing edition-year(s) [1888, 1889, 1890] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `brewer_j-s_e1881` vs `Brewer, J. S___Hong Kong___1883`

- [PASS] surname_gate: bio 'BREWER' vs stint 'Brewer, J. S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1890
- [PASS] position_sim: best 100 vs bar 60: 'Marine surveyor' ~ 'Marine Surveyor'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Brewer, J___Southern Nigeria___1909`

- Staff-list name: **Brewer, J** | colony: **Southern Nigeria** | listed 1909–1911 | editions [1909, 1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | J. Brewer | European Nurse | Medical Department | — | — |
| 1910 | J. Brewer | European Nurse | Medical Department | — | — |
| 1911 | J. Brewer | European Nurses | Medical | — | — |

### Deterministic checks: `brewer_j-s_e1881` vs `Brewer, J___Southern Nigeria___1909`

- [PASS] surname_gate: bio 'BREWER' vs stint 'Brewer, J' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Southern Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1911
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Brewer, Jane___Lagos___1905`

- Staff-list name: **Brewer, Jane** | colony: **Lagos** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | Miss Jane Brewer | Nurse | Medical | — | — |
| 1906 | Jane Brewer | Nurse | Medical | — | — |

### Deterministic checks: `brewer_j-s_e1881` vs `Brewer, Jane___Lagos___1905`

- [PASS] surname_gate: bio 'BREWER' vs stint 'Brewer, Jane' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Lagos'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
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

