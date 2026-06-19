<!-- {"case_id": "case_sandberg_john-owen_b1892", "bio_ids": ["sandberg_john-owen_b1892"], "stint_ids": ["Sanders, J. O___Federation of Malaya___1949"]} -->
# Dossier case_sandberg_john-owen_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Sanders, J. O___Federation of Malaya___1949` is also gate-compatible with biography(ies) outside this case: ['sanders_john-owen_b1892'] (already linked elsewhere or filtered).

## Biography `sandberg_john-owen_b1892`

- Printed name: **SANDBERG, JOHN OWEN**
- Birth year: 1892 (attested in editions [1930])
- Honours: A.M.I.C.E
- Appears in editions: [1930]

### Verbatim printed entry text (OCR)

**Version `col1930-L67972.v` — printed in editions [1930]:**

> SANDBERG, JOHN OWEN, A.M.I.C.E.—B. 1892; ed. Elstow Sch. and Manchester Univ.; mil. ser., 1915-20; 2nd lieut., 1917; ag. capt., 1918; asst., Crewe loco. works, L.M.S.R., 1922; works man., F.M.S. Rly., 1924; run. supt., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1920 | mil. ser | — | [1930] |
| 1 | 1917 | 2nd lieut | — | [1930] |
| 2 | 1918 | ag. capt | — | [1930] |
| 3 | 1922 | asst., Crewe loco. works, L.M.S.R | — | [1930] |
| 4 | 1924 | works man., F.M.S. Rly | Federated Malay States | [1930] |
| 5 | 1927 | run. supt | Federated Malay States *(inherited from previous clause)* | [1930] |

## Candidate stint `Sanders, J. O___Federation of Malaya___1949`

- Staff-list name: **Sanders, J. O** | colony: **Federation of Malaya** | listed 1949–1952 | editions [1949, 1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. O. Sanders | General Manager, Malayan Railway | Civil Establishment | C.M.G. | — |
| 1950 | J. O. Sanders | General Manager, Malayan Railway | Civil Establishment | C.M.G. | — |
| 1952 | J. O. Sanders | Member for Railways and Ports | Civil Establishment | C.M.G. | — |

### Deterministic checks: `sandberg_john-owen_b1892` vs `Sanders, J. O___Federation of Malaya___1949`

- [PASS] surname_gate: bio 'SANDBERG' vs stint 'Sanders, J. O' (fuzzy:2)
- [PASS] initials: bio ['J', 'O'] ~ stint ['J', 'O']
- [PASS] age_gate: stint starts 1949, birth 1892 (age 57)
- [FAIL] colony: no placed event resolves to 'Federation of Malaya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1952
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

