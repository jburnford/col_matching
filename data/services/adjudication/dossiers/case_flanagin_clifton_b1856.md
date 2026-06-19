<!-- {"case_id": "case_flanagin_clifton_b1856", "bio_ids": ["flanagin_clifton_b1856"], "stint_ids": ["Flanagin, C. S___Trinidad___1880", "Flanagin, C___Trinidad and Tobago___1899"]} -->
# Dossier case_flanagin_clifton_b1856

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['flanagin_clifton_b1856'] carry a single initial only — the namesake trap applies.

## Biography `flanagin_clifton_b1856`

- Printed name: **FLANAGIN, CLIFTON**
- Birth year: 1856 (attested in editions [1917])
- Appears in editions: [1917]

### Verbatim printed entry text (OCR)

**Version `col1917-L49559.v` — printed in editions [1917]:**

> FLANAGIN, CLIFTON.—B. 1856; entd. civ. serv., Trinidad, 1st June, 1875; warden, Arima, 1st Apr., 1909.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | entd. civ. serv. | Trinidad | [1917] |
| 1 | 1909 | warden, Arima | Trinidad *(inherited from previous clause)* | [1917] |

## Candidate stint `Flanagin, C. S___Trinidad___1880`

- Staff-list name: **Flanagin, C. S** | colony: **Trinidad** | listed 1880–1911 | editions [1880, 1883, 1886, 1888, 1890, 1896, 1898, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | C. S. Flanagin | 4th Clerk | Receiver-General's Department | — | — |
| 1883 | C. Flanagin | 2nd Clerk | Auditor-General's Department | — | — |
| 1886 | C. Flanagin | 2nd Clerk | Auditor-General's Department | — | — |
| 1888 | C. Flanagin | 2nd Clerk | Auditor-General's Department | — | — |
| 1890 | C. Flanagin | Montserrat | Wardens (who are also Savings Bank Managers and Sanitary Inspectors) | — | — |
| 1896 | C. Flanagin | Warden | Northern Province | — | — |
| 1898 | C. Flanagin | Warden | Northern Province | — | — |
| 1911 | C. Flanagin | Warden | Clerks of the Peace | — | — |

### Deterministic checks: `flanagin_clifton_b1856` vs `Flanagin, C. S___Trinidad___1880`

- [PASS] surname_gate: bio 'FLANAGIN' vs stint 'Flanagin, C. S' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C', 'S']
- [PASS] age_gate: stint starts 1880, birth 1856 (age 24)
- [PASS] colony: 2 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1880-1911
- [PASS] position_sim: best 100 vs bar 60: 'warden, Arima' ~ 'Warden'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Flanagin, C___Trinidad and Tobago___1899`

- Staff-list name: **Flanagin, C** | colony: **Trinidad and Tobago** | listed 1899–1913 | editions [1899, 1905, 1906, 1910, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | C. Flanagin | Warden | Northern Province | — | — |
| 1905 | C. Flanagin | Warden | Miscellaneous | — | — |
| 1906 | C. Flanagin | Warden | Clerks of the Peace | — | — |
| 1910 | C. Flanagin | Warden | Warden | — | — |
| 1912 | C. Flanagin | Warden | Clerks of the Peace | — | — |
| 1913 | C. Flanagin | Warden | Wardens | — | — |

### Deterministic checks: `flanagin_clifton_b1856` vs `Flanagin, C___Trinidad and Tobago___1899`

- [PASS] surname_gate: bio 'FLANAGIN' vs stint 'Flanagin, C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1899, birth 1856 (age 43)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1913
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

