<!-- {"case_id": "case_blanc_edwin-gerald_b1864", "bio_ids": ["blanc_edwin-gerald_b1864"], "stint_ids": ["Blanc, E. G___Tobago___1888", "Blanc, E. G___Trinidad and Tobago___1900", "Blanc, E. G___Trinidad___1896"]} -->
# Dossier case_blanc_edwin-gerald_b1864

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blanc_edwin-gerald_b1864`

- Printed name: **BLANC, EDWIN GERALD**
- Birth year: 1864 (attested in editions [1917, 1918])
- Honours: M.B
- Appears in editions: [1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1917-L47721.v` — printed in editions [1917, 1918]:**

> BLANC, EDWIN GERALD, M.B., C.M.—B. 1864; med. offr., Trinidad, 12th Apr., 1887; dist. med. offr. and health offr., Scarborough, Tobago.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1887 | med. offr. | Trinidad | [1917, 1918] |

## Candidate stint `Blanc, E. G___Tobago___1888`

- Staff-list name: **Blanc, E. G** | colony: **Tobago** | listed 1888–1909 | editions [1888, 1889, 1890, 1894, 1897, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | E. G. Blanc | District Medical Officer | Medical Department | — | — |
| 1889 | E. G. Blanc | District Medical Officer | Medical Department | — | — |
| 1890 | E. G. Blanc | District Medical Officer | Medical Department | — | — |
| 1894 | E. G. Blanc | District Medical Officer | Medical Department | — | — |
| 1897 | E. G. Blanc | District Medical Officer | Medical Department | — | — |
| 1909 | E. G. Blanc | — | Government Medical Officers | — | — |

### Deterministic checks: `blanc_edwin-gerald_b1864` vs `Blanc, E. G___Tobago___1888`

- [PASS] surname_gate: bio 'BLANC' vs stint 'Blanc, E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['E', 'G']
- [PASS] age_gate: stint starts 1888, birth 1864 (age 24)
- [FAIL] colony: no placed event resolves to 'Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Blanc, E. G___Trinidad and Tobago___1900`

- Staff-list name: **Blanc, E. G** | colony: **Trinidad and Tobago** | listed 1900–1913 | editions [1900, 1905, 1906, 1907, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | E. G. Blanc | Medical Officer | Government Medical Officers | — | — |
| 1905 | E. G. Blanc | — | Medical Establishment | — | — |
| 1906 | E. G. Blanc | Medical Officer | Medical Establishment | — | — |
| 1907 | E. G. Blanc | — | Government Medical Officers | — | — |
| 1912 | E. G. Blanc | — | Department of Agriculture | — | — |
| 1913 | E. G. Blanc | — | Government Medical Officers | — | — |

### Deterministic checks: `blanc_edwin-gerald_b1864` vs `Blanc, E. G___Trinidad and Tobago___1900`

- [PASS] surname_gate: bio 'BLANC' vs stint 'Blanc, E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['E', 'G']
- [PASS] age_gate: stint starts 1900, birth 1864 (age 36)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1913
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Blanc, E. G___Trinidad___1896`

- Staff-list name: **Blanc, E. G** | colony: **Trinidad** | listed 1896–1898 | editions [1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | E. G. Blanc | District Medical Officer | Medical Department | — | — |
| 1898 | E. G. Blanc | District Medical Officer | Medical Department | — | — |

### Deterministic checks: `blanc_edwin-gerald_b1864` vs `Blanc, E. G___Trinidad___1896`

- [PASS] surname_gate: bio 'BLANC' vs stint 'Blanc, E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['E', 'G']
- [PASS] age_gate: stint starts 1896, birth 1864 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1896-1898
- [FAIL] position_sim: best 50 vs bar 60: 'med. offr.' ~ 'District Medical Officer'
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

