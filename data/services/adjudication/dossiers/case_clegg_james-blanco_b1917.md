<!-- {"case_id": "case_clegg_james-blanco_b1917", "bio_ids": ["clegg_james-blanco_b1917"], "stint_ids": ["Clegg, J. B___Jamaica___1949", "Clegg, J. B___Singapore___1954"]} -->
# Dossier case_clegg_james-blanco_b1917

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Clegg, J. B___Jamaica___1949` is also gate-compatible with biography(ies) outside this case: ['clegg_j-b_b1910'] (already linked elsewhere or filtered).
- NOTE: stint `Clegg, J. B___Singapore___1954` is also gate-compatible with biography(ies) outside this case: ['clegg_j-b_b1910'] (already linked elsewhere or filtered).

## Biography `clegg_james-blanco_b1917`

- Printed name: **CLEGG, James Blanco**
- Birth year: 1917 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1951, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1957-L21984.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962]:**

> CLEGG, J. B.—b. 1917; ed. Prince of Wales Sch., Ken., and Lincoln Coll., Oxford; mil. serv., 1939-46, lieut.; agric. offr., Tang., 1946; senr., 1959-61.

**Version `col1951-L37012.v` — printed in editions [1951]:**

> CLEGG, James Blanco, B.A. (agric.) (Oxon.).—b. 1917; ed. Prince of Wales Sch., Kenya; on mil. serv., 1939-46; agric. offr., T.T., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | agric. offr. | Tanganyika | [1951, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1959–1961 | senr | Tanganyika *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Clegg, J. B___Jamaica___1949`

- Staff-list name: **Clegg, J. B** | colony: **Jamaica** | listed 1949–1953 | editions [1949, 1950, 1951, 1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. B. Clegg | Secretary for Economic Affairs | Secretariat | — | — |
| 1950 | J. B. Clegg | Secretary for Economic Affairs | Secretariat | — | — |
| 1951 | J. B. Clegg | Under Secretary (Economic) | Secretariat | — | — |
| 1952 | J. B. Clegg | Under Secretary (Economic) | Civil Establishment | — | — |
| 1953 | J. B. Clegg | Under Secretary (Economics) | Civil Establishment | — | — |

### Deterministic checks: `clegg_james-blanco_b1917` vs `Clegg, J. B___Jamaica___1949`

- [PASS] surname_gate: bio 'CLEGG' vs stint 'Clegg, J. B' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1949, birth 1917 (age 32)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1953
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Clegg, J. B___Singapore___1954`

- Staff-list name: **Clegg, J. B** | colony: **Singapore** | listed 1954–1957 | editions [1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | J. B. Clegg | Deputy Financial Secretary (Economic) | Civil Establishment | — | — |
| 1955 | J. B. Clegg | Deputy Financial Secretary (Economics) | Civil Establishment | — | — |
| 1956 | J. B. Clegg | Permanent Secretary to Ministry of Commerce and Industry | Civil Establishment | — | — |
| 1957 | J. B. Clegg | Permanent Secretary to Ministry of Commerce and Industry | Civil Establishment | — | — |

### Deterministic checks: `clegg_james-blanco_b1917` vs `Clegg, J. B___Singapore___1954`

- [PASS] surname_gate: bio 'CLEGG' vs stint 'Clegg, J. B' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1954, birth 1917 (age 37)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1957
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

