<!-- {"case_id": "case_cherry_f_b1921", "bio_ids": ["cherry_f_b1921"], "stint_ids": ["Cherry, F___Western Pacific___1960"]} -->
# Dossier case_cherry_f_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cherry_f_b1921'] carry a single initial only — the namesake trap applies.

## Biography `cherry_f_b1921`

- Printed name: **CHERRY, F**
- Birth year: 1921 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Honours: E.M (1945)
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L20660.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> CHERRY, F., E.M. (1945).—b. 1921; ed. Queen Eliz. Gram. Sch., Darlington; mil. serv., 1939-46; asst. audr., Nig., 1951; audr., W. Nig., 1951; senr. audr., O.A.D., 1956; prin. audr., B.S.I.P., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | asst. audr. | Nigeria | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1956 | senr. audr., O.A.D | Western Nigeria *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1960 | prin. audr., B.S.I.P | Western Nigeria *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Cherry, F___Western Pacific___1960`

- Staff-list name: **Cherry, F** | colony: **Western Pacific** | listed 1960–1966 | editions [1960, 1961, 1962, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | F. Cherry | Principal Auditor | Civil Establishment | — | — |
| 1961 | F. Cherry | Principal Auditor | Civil Establishment | — | — |
| 1962 | F. Cherry | Principal Auditor | Civil Establishment | — | — |
| 1964 | F. Cherry | Principal Auditor | Civil Establishment | — | — |
| 1965 | F. Cherry | Principal Auditor | Civil Establishment | — | — |
| 1966 | F. Cherry | Principal Auditor | Civil Establishment | — | — |

### Deterministic checks: `cherry_f_b1921` vs `Cherry, F___Western Pacific___1960`

- [PASS] surname_gate: bio 'CHERRY' vs stint 'Cherry, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1960, birth 1921 (age 39)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1960-1966
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

