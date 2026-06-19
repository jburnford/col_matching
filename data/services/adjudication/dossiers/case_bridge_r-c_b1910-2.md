<!-- {"case_id": "case_bridge_r-c_b1910-2", "bio_ids": ["bridge_r-c_b1910-2"], "stint_ids": ["Bridge, R. C___Jamaica___1937", "Bridge, R. C___Jamaica___1953"]} -->
# Dossier case_bridge_r-c_b1910-2

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Bridge, R. C___Jamaica___1937` is also gate-compatible with biography(ies) outside this case: ['bridge_r-c_b1910'] (already linked elsewhere or filtered).
- NOTE: stint `Bridge, R. C___Jamaica___1953` is also gate-compatible with biography(ies) outside this case: ['bridge_r-c_b1910'] (already linked elsewhere or filtered).

## Biography `bridge_r-c_b1910-2`

- Printed name: **BRIDGE, R. C**
- Birth year: 1910 (attested in editions [1955])
- Appears in editions: [1955]

### Verbatim printed entry text (OCR)

**Version `col1955-L19893.v` — printed in editions [1955]:**

> BRIDGE, R. C.—b. 1910; ed. Charterhouse and Oxford Univ.; barrister-at-law, Inner Temple; mil. serv., 1940-46, wing cdr. (desps.); adv. and solr., Mal. and Sp'ore; C.L.S., 1947; regist., sup. ct., Mal., 1948; puisne judge, 1949; just. of appeal, E.A. ct. of appeal, 1953; chmn. Mal. armed local forces trib., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | C.L.S | — | [1955] |
| 1 | 1948 | regist., sup. ct. | Malaya | [1955] |
| 2 | 1949 | puisne judge | Malaya *(inherited from previous clause)* | [1955] |
| 3 | 1953 | just. of appeal, E.A. ct. of appeal | Malaya *(inherited from previous clause)* | [1955] |

## Candidate stint `Bridge, R. C___Jamaica___1937`

- Staff-list name: **Bridge, R. C** | colony: **Jamaica** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | R. C. Bridge | Junior Agricultural Officers | Department of Science and Agriculture | — | — |
| 1940 | R. C. Bridge | Marketing Officers | Marketing Department | — | — |

### Deterministic checks: `bridge_r-c_b1910-2` vs `Bridge, R. C___Jamaica___1937`

- [PASS] surname_gate: bio 'BRIDGE' vs stint 'Bridge, R. C' (exact)
- [PASS] initials: bio ['R', 'C'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1937, birth 1910 (age 27)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bridge, R. C___Jamaica___1953`

- Staff-list name: **Bridge, R. C** | colony: **Jamaica** | listed 1953–1956 | editions [1953, 1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | R. C. Bridge | Deputy Commissioner of Commerce and Industries | Civil Establishment | — | — |
| 1954 | R. C. Bridge | Marketing Administrator | Civil Establishment | — | — |
| 1955 | R. C. Bridge | Marketing Administrator | Civil Establishment | — | — |
| 1956 | R. C. Bridge | Marketing Administrator | Civil Establishment | — | — |

### Deterministic checks: `bridge_r-c_b1910-2` vs `Bridge, R. C___Jamaica___1953`

- [PASS] surname_gate: bio 'BRIDGE' vs stint 'Bridge, R. C' (exact)
- [PASS] initials: bio ['R', 'C'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1953, birth 1910 (age 43)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1956
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

