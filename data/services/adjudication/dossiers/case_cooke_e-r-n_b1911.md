<!-- {"case_id": "case_cooke_e-r-n_b1911", "bio_ids": ["cooke_e-r-n_b1911", "cooke_n_b1916"], "stint_ids": ["Cooke, E. R. N___Kenya___1949"]} -->
# Dossier case_cooke_e-r-n_b1911

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 46 official(s) with this surname in the graph's staff lists; 25 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cooke_n_b1916'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Cooke, E. R. N___Kenya___1949'] have more than one claimant biography in this case.

## Biography `cooke_e-r-n_b1911`

- Printed name: **COOKE, E. R. N**
- Birth year: 1911 (attested in editions [1957, 1958, 1959, 1960, 1961, 1964, 1965])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L22123.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1964, 1965]:**

> COOKE, E. R. N.—b. 1911; ed. Methodist Coll. and Queen's Univ., Belfast; mil. serv., E.A.A.M.C., capt.; M.O., Ken., 1939; pathologist, 1948; specialist pathologist, 1955; pubns. Observations on Brucellosis in Kenya; (jt.) First Year in Kenya.

**Version `col1962-L19950.v` — printed in editions [1962, 1963]:**

> COOKE, E. R. N.—b. 1911; ed. Methodist Coll. and Queen’s Univ., Belfast; mil. serv., E.A.A.M.C., capt.; M.O., Ken., 1939; pathologist, 1948; specialist pathologist, 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | M.O. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1948 | pathologist | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1955 | specialist pathologist | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Biography `cooke_n_b1916`

- Printed name: **COOKE, N**
- Birth year: 1916 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L20940.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> COOKE, N.—b. 1916; ed. Stretford Gram. Sch., and Coll. of Technology, Manchester; mil. serv., 1939-45, R.A.F., sgt.; rating and val. surveyor, H.K., 1948; asst. comsnr. rating and value, 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | rating and val. surveyor | Hong Kong | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1962 | asst. comsnr. rating and value | Hong Kong *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Cooke, E. R. N___Kenya___1949`

- Staff-list name: **Cooke, E. R. N** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. R. N. Cooke | Pathologists | Medical | — | — |
| 1950 | E. R. N. Cooke | Pathologists | Medical | — | — |
| 1951 | E. R. N. Cooke | Pathologist | Medical | — | — |

### Deterministic checks: `cooke_e-r-n_b1911` vs `Cooke, E. R. N___Kenya___1949`

- [PASS] surname_gate: bio 'COOKE' vs stint 'Cooke, E. R. N' (exact)
- [PASS] initials: bio ['E', 'R', 'N'] ~ stint ['E', 'R', 'N']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 100 vs bar 60: 'pathologist' ~ 'Pathologist'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `cooke_n_b1916` vs `Cooke, E. R. N___Kenya___1949`

- [PASS] surname_gate: bio 'COOKE' vs stint 'Cooke, E. R. N' (exact)
- [PASS] initials: bio ['N'] ~ stint ['E', 'R', 'N']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

