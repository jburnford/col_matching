<!-- {"case_id": "case_hulse_b-m_b1911", "bio_ids": ["hulse_b-m_b1911"], "stint_ids": ["Hulse, B. M___British Honduras___1949"]} -->
# Dossier case_hulse_b-m_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hulse_b-m_b1911`

- Printed name: **HULSE, B. M**
- Birth year: 1911 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L23544.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> HULSE, Miss B. M.—b. 1911; ed. St. Hilda's Coll., Belize, London Univ., and Welsh Nat. Sch. of Medicine; M.O., B. Hond., 1944; chest physician, 1957; i/c T.B. control, B. Hond. since 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | M.O. | British Honduras | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1953 | i/c T.B. control, B. Hond. since | British Honduras | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1957 | chest physician | British Honduras *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Hulse, B. M___British Honduras___1949`

- Staff-list name: **Hulse, B. M** | colony: **British Honduras** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | B. M. Hulse | Medical Officer | MEDICAL | — | — |
| 1950 | B. M. Hulse | Medical Officer | Medical | — | — |
| 1951 | B. M. Hulse | Medical Officer | MEDICAL | — | — |

### Deterministic checks: `hulse_b-m_b1911` vs `Hulse, B. M___British Honduras___1949`

- [PASS] surname_gate: bio 'HULSE' vs stint 'Hulse, B. M' (exact)
- [PASS] initials: bio ['B', 'M'] ~ stint ['B', 'M']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 3 placed event(s) resolve to 'British Honduras'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

