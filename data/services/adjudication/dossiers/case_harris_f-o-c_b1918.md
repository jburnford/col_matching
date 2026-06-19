<!-- {"case_id": "case_harris_f-o-c_b1918", "bio_ids": ["harris_f-o-c_b1918"], "stint_ids": ["Harris, F. O. C___West Indies Federation___1961"]} -->
# Dossier case_harris_f-o-c_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 90 official(s) with this surname in the graph's staff lists; 35 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harris_f-o-c_b1918`

- Printed name: **HARRIS, F. O. C**
- Birth year: 1918 (attested in editions [1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1958-L23376.v` — printed in editions [1958, 1959, 1960, 1961, 1962]:**

> HARRIS, F. O. C.—b. 1918; ed. Dominica Gram. Sch. and St. Peter's Hall, Oxford; barrister-at-law, Middle Temple; M.E.C., Dominica; crown atty. and mag. (registr. and provost-marshal), Montserrat, 1956; asst. legal dftsman., W. Indies, 1958; legal dftsman., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1956 | crown atty. and mag. (registr. and provost-marshal) | Montserrat | [1958, 1959, 1960, 1961, 1962] |
| 1 | 1958 | asst. legal dftsman., W. Indies | Montserrat *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |
| 2 | 1959 | legal dftsman | Montserrat *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Harris, F. O. C___West Indies Federation___1961`

- Staff-list name: **Harris, F. O. C** | colony: **West Indies Federation** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | F. O. C. Harris | Legal Draftsmen | Law Officers | — | — |
| 1962 | F. O. C. Harris | Legal Draftsmen | Law Officers | — | — |

### Deterministic checks: `harris_f-o-c_b1918` vs `Harris, F. O. C___West Indies Federation___1961`

- [PASS] surname_gate: bio 'HARRIS' vs stint 'Harris, F. O. C' (exact)
- [PASS] initials: bio ['F', 'O', 'C'] ~ stint ['F', 'O', 'C']
- [PASS] age_gate: stint starts 1961, birth 1918 (age 43)
- [FAIL] colony: no placed event resolves to 'West Indies Federation'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
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

