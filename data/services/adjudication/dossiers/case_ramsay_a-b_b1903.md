<!-- {"case_id": "case_ramsay_a-b_b1903", "bio_ids": ["ramsay_a-b_b1903"], "stint_ids": ["Ramsay, A. B___Federation of Malaya___1949"]} -->
# Dossier case_ramsay_a-b_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 25 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ramsay_a-b_b1903`

- Printed name: **RAMSAY, A. B**
- Birth year: 1903 (attested in editions [1949, 1950, 1951, 1953, 1954])
- Appears in editions: [1949, 1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1949-L35129.v` — printed in editions [1949, 1950, 1951, 1953, 1954]:**

> RAMSAY, A. B.—b. 1903; ed. Sherborne Sch. and Sidney Sussex Coll., Camb.; M.C.S., 1927; cl. V, 1930; cl. IV, 1934; cl. III, 1939; cl. II, 1944; cl. IB, 1947; ag. Br. advr., Kedah, 1951; staff gr. A, 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | M.C.S | — | [1949, 1950, 1951, 1953, 1954] |
| 1 | 1930 | cl. V | — | [1949, 1950, 1951, 1953, 1954] |
| 2 | 1934 | cl. IV | — | [1949, 1950, 1951, 1953, 1954] |
| 3 | 1939 | cl. III | — | [1949, 1950, 1951, 1953, 1954] |
| 4 | 1944 | cl. II | — | [1949, 1950, 1951, 1953, 1954] |
| 5 | 1947 | cl. IB | — | [1949, 1950, 1951, 1953, 1954] |
| 6 | 1951 | ag. Br. advr. | Kedah | [1949, 1950, 1951, 1953, 1954] |
| 7 | 1953 | staff gr. A | Kedah *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954] |

## Candidate stint `Ramsay, A. B___Federation of Malaya___1949`

- Staff-list name: **Ramsay, A. B** | colony: **Federation of Malaya** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. B. Ramsay | British Adviser, Kedah | Civil Establishment | — | — |
| 1951 | A. B. Ramsay | Class I | Administrative Service | — | — |

### Deterministic checks: `ramsay_a-b_b1903` vs `Ramsay, A. B___Federation of Malaya___1949`

- [PASS] surname_gate: bio 'RAMSAY' vs stint 'Ramsay, A. B' (exact)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1949, birth 1903 (age 46)
- [PASS] colony: 2 placed event(s) resolve to 'Federation of Malaya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 45 vs bar 60: 'ag. Br. advr.' ~ 'British Adviser, Kedah'
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

