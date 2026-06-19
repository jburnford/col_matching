<!-- {"case_id": "case_davis_d-r_b1928", "bio_ids": ["davis_d-r_b1928"], "stint_ids": ["Davis, D. R___Western Pacific___1964"]} -->
# Dossier case_davis_d-r_b1928

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 130 official(s) with this surname in the graph's staff lists; 42 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `davis_d-r_b1928`

- Printed name: **DAVIS, D. R**
- Birth year: 1928 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L16289.v` — printed in editions [1964, 1965, 1966]:**

> DAVIS, D. R.—b. 1928; ed. Prince of Wales Sch., Nairobi and Wadhams Coll., Oxon.; cr. coun., Ken., 1956; asst. atty-gen., B.S.I.P., 1962; legal advr., W.Pac.H.C. and atty-gen., B.S.I.P., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1956 | cr. coun. | Kenya | [1964, 1965, 1966] |
| 1 | 1962 | asst. atty-gen., B.S.I.P | Kenya *(inherited from previous clause)* | [1964, 1965, 1966] |
| 2 | 1963 | legal advr., W.Pac.H.C. and atty-gen., B.S.I.P | Kenya *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Davis, D. R___Western Pacific___1964`

- Staff-list name: **Davis, D. R** | colony: **Western Pacific** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | D. R. Davis | Legal Adviser | Civil Establishment | — | — |
| 1965 | D. R. Davis | Legal Adviser | Civil Establishment | — | — |
| 1966 | D. R. Davis | Legal Adviser | Civil Establishment | — | — |

### Deterministic checks: `davis_d-r_b1928` vs `Davis, D. R___Western Pacific___1964`

- [PASS] surname_gate: bio 'DAVIS' vs stint 'Davis, D. R' (exact)
- [PASS] initials: bio ['D', 'R'] ~ stint ['D', 'R']
- [PASS] age_gate: stint starts 1964, birth 1928 (age 36)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1966
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

