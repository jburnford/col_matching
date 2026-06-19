<!-- {"case_id": "case_went_t-e_b1924", "bio_ids": ["went_t-e_b1924"], "stint_ids": ["Went, T. E___Barbados___1949"]} -->
# Dossier case_went_t-e_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `went_t-e_b1924`

- Printed name: **WENT, T. E**
- Birth year: 1924 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L18849.v` — printed in editions [1966]:**

> WENT, T. E.—b. 1924; ed. Harrison Coll., Barb., Reading Univ.; pilot trng. R.A.F.; air traffic contl. offr., Barb., 1957; senr., 1958; asst. dir. of civil aviat., 1962; dir., 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1957 | air traffic contl. offr. | Barbados | [1966] |
| 1 | 1958 | senr | Barbados *(inherited from previous clause)* | [1966] |
| 2 | 1962 | asst. dir. of civil aviat | Barbados *(inherited from previous clause)* | [1966] |
| 3 | 1965 | dir | Barbados *(inherited from previous clause)* | [1966] |

## Candidate stint `Went, T. E___Barbados___1949`

- Staff-list name: **Went, T. E** | colony: **Barbados** | listed 1949–1953 | editions [1949, 1950, 1951, 1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. E. Went | Assistant to the Colonial Engineer | PUBLIC WORKS | — | — |
| 1950 | T. E. Went | Assistant to the Colonial Engineer | PUBLIC WORKS | — | — |
| 1951 | T. E. Went | Colonial Engineer | PUBLIC WORKS | — | — |
| 1952 | T. E. Went | Colonial Engineer | Civil Establishment | — | — |
| 1953 | T. E. Went | Colonial Engineer | Civil Establishment | — | — |

### Deterministic checks: `went_t-e_b1924` vs `Went, T. E___Barbados___1949`

- [PASS] surname_gate: bio 'WENT' vs stint 'Went, T. E' (exact)
- [PASS] initials: bio ['T', 'E'] ~ stint ['T', 'E']
- [PASS] age_gate: stint starts 1949, birth 1924 (age 25)
- [PASS] colony: 4 placed event(s) resolve to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1953
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

