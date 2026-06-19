<!-- {"case_id": "case_dryden_alexander-hunter-munro_b1899", "bio_ids": ["dryden_alexander-hunter-munro_b1899"], "stint_ids": ["Dryden, A. H. M___Tanganyika___1933"]} -->
# Dossier case_dryden_alexander-hunter-munro_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dryden_alexander-hunter-munro_b1899`

- Printed name: **DRYDEN, Alexander Hunter Munro**
- Birth year: 1899 (attested in editions [1951])
- Honours: C.P.M (1941), K.P.M (1949), O.B.E (1947)
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L37704.v` — printed in editions [1951]:**

> DRYDEN, Alexander Hunter Munro, O.B.E. (1947), K.P.M. (1949), C.P.M. (1941).—b. 1899; ed. in S. Africa; on mil. serv., 1939-45, maj.; asst. inspr., police, T.T., 1927; inspr., 1931; ch. inspr., Zanz., 1936; supt., 1939; senr., Uga., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | asst. inspr., police, T.T | — | [1951] |
| 1 | 1931 | inspr | — | [1951] |
| 2 | 1936 | ch. inspr. | Zanzibar | [1951] |
| 3 | 1939 | supt | Zanzibar *(inherited from previous clause)* | [1951] |
| 4 | 1949 | senr. | Uganda | [1951] |

## Candidate stint `Dryden, A. H. M___Tanganyika___1933`

- Staff-list name: **Dryden, A. H. M** | colony: **Tanganyika** | listed 1933–1934 | editions [1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | A. H. M. Dryden | Inspector | Police | — | — |
| 1934 | A. H. M. Dryden | Inspectors | Police | — | — |

### Deterministic checks: `dryden_alexander-hunter-munro_b1899` vs `Dryden, A. H. M___Tanganyika___1933`

- [PASS] surname_gate: bio 'DRYDEN' vs stint 'Dryden, A. H. M' (exact)
- [PASS] initials: bio ['A', 'H', 'M'] ~ stint ['A', 'H', 'M']
- [PASS] age_gate: stint starts 1933, birth 1899 (age 34)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1934
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

