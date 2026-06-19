<!-- {"case_id": "case_dallow_j-c_b1902", "bio_ids": ["dallow_j-c_b1902"], "stint_ids": ["Dallow, J. C___Singapore___1954"]} -->
# Dossier case_dallow_j-c_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dallow_j-c_b1902`

- Printed name: **DALLOW, J. C**
- Birth year: 1902 (attested in editions [1955, 1956, 1957])
- Appears in editions: [1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1955-L20352.v` — printed in editions [1955, 1956, 1957]:**

> DALLOW, J. C.—b. 1902; ed. Regent St. Polytechnic, Lond.; mil. serv., 1942–45; secon. from Br. P.O. as engrn., P. and T., S.S. and F.M.S., 1934; S.O. II, telecoms., B.M.A., Penang, 1945; asst. contrlr., telecoms., Kedah, 1946; contrlr., K.L., 1949; dir., telecoms. dept., S'pore, 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | secon. from Br. P.O. as engrn., P. and T., S.S. and F.M.S | Straits Settlements | [1955, 1956, 1957] |
| 1 | 1945 | S.O. II, telecoms., B.M.A., Penang | Straits Settlements *(inherited from previous clause)* | [1955, 1956, 1957] |
| 2 | 1946 | asst. contrlr., telecoms. | Kedah | [1955, 1956, 1957] |
| 3 | 1949 | contrlr., K.L | Kedah *(inherited from previous clause)* | [1955, 1956, 1957] |
| 4 | 1953 | dir., telecoms. dept., S'pore | Kedah *(inherited from previous clause)* | [1955, 1956, 1957] |

## Candidate stint `Dallow, J. C___Singapore___1954`

- Staff-list name: **Dallow, J. C** | colony: **Singapore** | listed 1954–1956 | editions [1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | J. C. Dallow | Director of Telecommunications | Civil Establishment | — | — |
| 1955 | J. C. Dallow | Director of Telecommunications | Civil Establishment | — | — |
| 1956 | J. C. Dallow | Director of Telecommunications | Civil Establishment | — | — |

### Deterministic checks: `dallow_j-c_b1902` vs `Dallow, J. C___Singapore___1954`

- [PASS] surname_gate: bio 'DALLOW' vs stint 'Dallow, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1954, birth 1902 (age 52)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1956
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

