<!-- {"case_id": "case_price_mawrfryn_b1902", "bio_ids": ["price_mawrfryn_b1902"], "stint_ids": ["Price, R. M. R___British Honduras___1949", "Price, R. M. R___British Honduras___1957"]} -->
# Dossier case_price_mawrfryn_b1902

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 27 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['price_mawrfryn_b1902'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Price, R. M. R___British Honduras___1949` is also gate-compatible with biography(ies) outside this case: ['price_r-m-r_b1917'] (already linked elsewhere or filtered).
- NOTE: stint `Price, R. M. R___British Honduras___1957` is also gate-compatible with biography(ies) outside this case: ['price_r-m-r_b1917'] (already linked elsewhere or filtered).

## Biography `price_mawrfryn_b1902`

- Printed name: **PRICE, Mawrfryn**
- Birth year: 1902 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35336.v` — printed in editions [1948, 1949, 1950, 1951]:**

> PRICE, Mawrfryn.—b. 1902; ed. Brynmawr Interm. Sch.; mstr. mariner; apptd. col. serv., 1931; marine offr., T.T., 1932; Nig., 1934; prin. 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | apptd. col. serv | — | [1948, 1949, 1950, 1951] |
| 1 | 1932 | marine offr., T.T | — | [1948, 1949, 1950, 1951] |
| 2 | 1934 | marine offr., T.T | Nigeria | [1948, 1949, 1950, 1951] |
| 3 | 1950 | prin | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Price, R. M. R___British Honduras___1949`

- Staff-list name: **Price, R. M. R** | colony: **British Honduras** | listed 1949–1953 | editions [1949, 1950, 1951, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. M. R. Price | Assistant Superintendent | Police Department | — | — |
| 1950 | R. M. R. Price | Assistant Superintendent | Police Department | — | — |
| 1951 | R. M. R. Price | Assistant Superintendents | POLICE | — | — |
| 1953 | R. M. R. Price | Assistant Superintendent of Police | Civil Establishment | — | — |

### Deterministic checks: `price_mawrfryn_b1902` vs `Price, R. M. R___British Honduras___1949`

- [PASS] surname_gate: bio 'PRICE' vs stint 'Price, R. M. R' (exact)
- [PASS] initials: bio ['M'] ~ stint ['R', 'M', 'R']
- [PASS] age_gate: stint starts 1949, birth 1902 (age 47)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1953
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Price, R. M. R___British Honduras___1957`

- Staff-list name: **Price, R. M. R** | colony: **British Honduras** | listed 1957–1960 | editions [1957, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | R. M. R. Price | Deputy Superintendent | Civil Establishment | — | — |
| 1958 | R. M. R. Price | Superintendent of Police | Civil Establishment | — | — |
| 1959 | R. M. R. Price | Superintendent of Police | Civil Establishment | — | — |
| 1960 | R. M. R. Price | Superintendent of Police | Civil Establishment | — | — |

### Deterministic checks: `price_mawrfryn_b1902` vs `Price, R. M. R___British Honduras___1957`

- [PASS] surname_gate: bio 'PRICE' vs stint 'Price, R. M. R' (exact)
- [PASS] initials: bio ['M'] ~ stint ['R', 'M', 'R']
- [PASS] age_gate: stint starts 1957, birth 1902 (age 55)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1960
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

