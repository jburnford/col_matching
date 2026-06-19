<!-- {"case_id": "case_usher_e-m_b1924", "bio_ids": ["usher_e-m_b1924"], "stint_ids": ["Usher, Miss E. M___Kenya___1950"]} -->
# Dossier case_usher_e-m_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `usher_e-m_b1924`

- Printed name: **USHER, E. M**
- Birth year: 1924 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: O.B.E (1964)
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L27750.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> USHER, Miss E. M., O.B.E. (1964).—b. 1924; ed. St. Paul's Girls' Sch., Rosebery County Sch., Epsom, and Newnham Coll., Camb.; clk., Ken., 1947; tech. offr., survey dept., 1948; asst. sec., 1954; under-sec., 1962. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | clk. | Kenya | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1948 | tech. offr., survey dept | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1954 | asst. sec | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1962 | under-sec | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Usher, Miss E. M___Kenya___1950`

- Staff-list name: **Usher, Miss E. M** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | Miss E. M. Usher | Technical Officer | Survey of Kenya | — | — |
| 1951 | Miss E. M. Usher | Technical Officer | Survey of Kenya | — | — |

### Deterministic checks: `usher_e-m_b1924` vs `Usher, Miss E. M___Kenya___1950`

- [PASS] surname_gate: bio 'USHER' vs stint 'Usher, Miss E. M' (exact)
- [PASS] initials: bio ['E', 'M'] ~ stint ['M', 'E', 'M']
- [PASS] age_gate: stint starts 1950, birth 1924 (age 26)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 47 vs bar 60: 'tech. offr., survey dept' ~ 'Technical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

