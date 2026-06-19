<!-- {"case_id": "case_bray_j-p-m_b1917", "bio_ids": ["bray_j-p-m_b1917"], "stint_ids": ["Bray, J. P. M___Gambia___1964"]} -->
# Dossier case_bray_j-p-m_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bray_j-p-m_b1917`

- Printed name: **BRAY, J. P. M**
- Birth year: 1917 (attested in editions [1964, 1965, 1966])
- Honours: C.P.M (1959), Q.P.M (1965)
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L15014.v` — printed in editions [1964, 1965, 1966]:**

> BRAY, J. P. M., Q.P.M. (1965), C.P.M. (1959).—b. 1917; ed. St. Brendans Coll., Bristol; U.K. police, 1937–50; asst. supt. police, G.C., 1950; sup. police, Gam., 1956; senr. supt., 1960; asst. comsnr., 1961; comsnr., 1963. (Gambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937–1950 | U.K. police | — | [1964, 1965, 1966] |
| 1 | 1950 | asst. supt. police | Gold Coast | [1964, 1965, 1966] |
| 2 | 1956 | sup. police, Gam | Gold Coast *(inherited from previous clause)* | [1964, 1965, 1966] |
| 3 | 1960 | senr. supt | Gold Coast *(inherited from previous clause)* | [1964, 1965, 1966] |
| 4 | 1961 | asst. comsnr | Gold Coast *(inherited from previous clause)* | [1964, 1965, 1966] |
| 5 | 1963 | comsnr | Gold Coast *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Bray, J. P. M___Gambia___1964`

- Staff-list name: **Bray, J. P. M** | colony: **Gambia** | listed 1964–1965 | editions [1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | J. P. M. Bray | Commissioner of Police | Office of the Prime Minister | — | — |
| 1965 | J. P. M. Bray | Commissioner of Police | Civil Establishment | — | — |

### Deterministic checks: `bray_j-p-m_b1917` vs `Bray, J. P. M___Gambia___1964`

- [PASS] surname_gate: bio 'BRAY' vs stint 'Bray, J. P. M' (exact)
- [PASS] initials: bio ['J', 'P', 'M'] ~ stint ['J', 'P', 'M']
- [PASS] age_gate: stint starts 1964, birth 1917 (age 47)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1965
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

