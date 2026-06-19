<!-- {"case_id": "case_wiltshire_robert-charles-blair_b1906", "bio_ids": ["wiltshire_robert-charles-blair_b1906"], "stint_ids": ["Wiltshire, R. C. B___Singapore___1949"]} -->
# Dossier case_wiltshire_robert-charles-blair_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wiltshire_robert-charles-blair_b1906`

- Printed name: **WILTSHIRE, Robert Charles Blair**
- Birth year: 1906 (attested in editions [1950, 1951])
- Honours: K.P.M (1949)
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L40863.v` — printed in editions [1950, 1951]:**

> WILTSHIRE, Robert Charles Blair, K.P.M. (1949).—b. 1906; ed. Edgeborough, Guildford; with H.M. forces, 1925-28; interned, 1942-45; police probr., S.S., 1928; asst. supt., 1931; supt., 1946; asst. comsnt., S'pore., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925–1928 | with H.M. forces | — | [1950, 1951] |
| 1 | 1928 | police probr. | Straits Settlements | [1950, 1951] |
| 2 | 1931 | asst. supt | Straits Settlements *(inherited from previous clause)* | [1950, 1951] |
| 3 | 1942–1945 | interned | — | [1950, 1951] |
| 4 | 1946 | supt | Straits Settlements *(inherited from previous clause)* | [1950, 1951] |
| 5 | 1948 | asst. comsnt., S'pore | Straits Settlements *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Wiltshire, R. C. B___Singapore___1949`

- Staff-list name: **Wiltshire, R. C. B** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. C. B. Wiltshire | Assistant Commissioner of Police | Police | — | — |
| 1951 | R. C. B. Wiltshire | Deputy Commissioners of Police | Police | — | — |

### Deterministic checks: `wiltshire_robert-charles-blair_b1906` vs `Wiltshire, R. C. B___Singapore___1949`

- [PASS] surname_gate: bio 'WILTSHIRE' vs stint 'Wiltshire, R. C. B' (exact)
- [PASS] initials: bio ['R', 'C', 'B'] ~ stint ['R', 'C', 'B']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [FAIL] colony: no placed event resolves to 'Singapore'
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

