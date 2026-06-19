<!-- {"case_id": "case_dow_john-lamont_e1886", "bio_ids": ["dow_john-lamont_e1886", "dow_john-lamont_e1886-2", "dow_john-lamont_e1886-3"], "stint_ids": ["Dow, J. L___Victoria___1889", "Dow, J___Uganda___1927"]} -->
# Dossier case_dow_john-lamont_e1886

## Case context

- 3 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Dow, J. L___Victoria___1889', 'Dow, J___Uganda___1927'] have more than one claimant biography in this case.
- Phase 1 found `dow_john-lamont_e1886` ↔ `Dow, J. L___Victoria___1889` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `dow_john-lamont_e1886-2` ↔ `Dow, J. L___Victoria___1889` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `dow_john-lamont_e1886`

- Printed name: **DOW, JOHN LAMONT**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L33143.v` — printed in editions [1888]:**

> DOW, JOHN LAMONT.—President board of land, commissioner of crown lands and survey, and minister of mines and agriculture, Victoria, Feb., 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1886 | President board of land, commissioner of crown lands and survey, and minister of mines and agriculture | Victoria | [1888] |

## Biography `dow_john-lamont_e1886-2`

- Printed name: **DOW, JOHN LAMONT**
- Birth year: not printed
- Appears in editions: [1889, 1890, 1894, 1896, 1897, 1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1889-L32824.v` — printed in editions [1889, 1890, 1894, 1896, 1897, 1905, 1906]:**

> DOW, THE HON. JOHN LAMONT.—Minister of lands and agriculture, president board of lands and works, Victoria, Feb., 1886-90.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1886–1890 | Minister of lands and agriculture, president board of lands and works | Victoria | [1889, 1890, 1894, 1896, 1897, 1905, 1906] |

## Biography `dow_john-lamont_e1886-3`

- Printed name: **DOW, JOHN LAMONT**
- Birth year: not printed
- Appears in editions: [1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1898-L33125.v` — printed in editions [1898, 1899, 1900]:**

> DOW, THE HON. JOHN LAMONT.—Min. of lands and agricul., pres. bd. of lands and wks., Victoria, Feb., 1886-90.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1886–1890 | Min. of lands and agricul., pres. bd. of lands and wks. | Victoria | [1898, 1899, 1900] |

## Candidate stint `Dow, J. L___Victoria___1889`

- Staff-list name: **Dow, J. L** | colony: **Victoria** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | J. L. Dow | Minister of Agriculture | Department of Agriculture | — | — |
| 1890 | J. L. Dow | Minister of Agriculture | Department of Agriculture | — | — |
| 1890 | J. L. Dow | President of the Board of Land and Works, and Commissioner Crown Lands and Survey | Crown Lands and Survey Division | — | — |

### Deterministic checks: `dow_john-lamont_e1886` vs `Dow, J. L___Victoria___1889`

- [PASS] surname_gate: bio 'DOW' vs stint 'Dow, J. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1890
- [PASS] position_sim: best 100 vs bar 60: 'President board of land, commissioner of crown lands and survey, and minister of mines and agriculture' ~ 'Minister of Agriculture'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `dow_john-lamont_e1886-2` vs `Dow, J. L___Victoria___1889`

- [PASS] surname_gate: bio 'DOW' vs stint 'Dow, J. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1890
- [PASS] position_sim: best 100 vs bar 60: 'Minister of lands and agriculture, president board of lands and works' ~ 'Minister of Agriculture'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1889, 1890] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `dow_john-lamont_e1886-3` vs `Dow, J. L___Victoria___1889`

- [PASS] surname_gate: bio 'DOW' vs stint 'Dow, J. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1890
- [FAIL] position_sim: best 55 vs bar 60: 'Min. of lands and agricul., pres. bd. of lands and wks.' ~ 'President of the Board of Land and Works, and Commissioner Crown Lands and Survey'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Dow, J___Uganda___1927`

- Staff-list name: **Dow, J** | colony: **Uganda** | listed 1927–1930 | editions [1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | J. Dow | Assistant Manager, Government Timber Supply | Government Timber Supply | — | — |
| 1928 | J. Dow | Assistant Manager | Government Timber Supply | — | — |
| 1929 | J. Dow | Assistant Manager, Government Timber Supply | Government Timber Supply | — | — |
| 1930 | J. Dow | Assistant Manager | Government Timber Supply | — | — |

### Deterministic checks: `dow_john-lamont_e1886` vs `Dow, J___Uganda___1927`

- [PASS] surname_gate: bio 'DOW' vs stint 'Dow, J' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J']
- [PASS] age_gate: stint starts 1927; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1930
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `dow_john-lamont_e1886-3` vs `Dow, J___Uganda___1927`

- [PASS] surname_gate: bio 'DOW' vs stint 'Dow, J' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J']
- [PASS] age_gate: stint starts 1927; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1930
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

