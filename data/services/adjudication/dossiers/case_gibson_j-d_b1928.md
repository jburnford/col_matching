<!-- {"case_id": "case_gibson_j-d_b1928", "bio_ids": ["gibson_j-d_b1928"], "stint_ids": ["Gibson, J. L. D___Bermuda___1949"]} -->
# Dossier case_gibson_j-d_b1928

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 49 official(s) with this surname in the graph's staff lists; 36 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gibson_j-d_b1928`

- Printed name: **GIBSON, J. D**
- Birth year: 1928 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L14928.v` — printed in editions [1966]:**

> GIBSON, J. D.—b. 1928; ed. Marist Brothers' High Sch., Fiji, Teachers' Training Coll., Auckland, and Auckland Univ.; master, gr. C, Fiji, 1952; gr. B, 1954; gr. A, 1957; senr. master, 1960; educ. offr., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | master, gr. C | Fiji | [1966] |
| 1 | 1954 | gr. B | Fiji *(inherited from previous clause)* | [1966] |
| 2 | 1957 | gr. A | Fiji *(inherited from previous clause)* | [1966] |
| 3 | 1960 | senr. master | Fiji *(inherited from previous clause)* | [1966] |

## Candidate stint `Gibson, J. L. D___Bermuda___1949`

- Staff-list name: **Gibson, J. L. D** | colony: **Bermuda** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. L. D. Gibson | Collector of Customs, Hamilton | Revenue | — | — |
| 1950 | J. L. D. Gibson | Collector of Customs | Revenue | — | — |
| 1951 | J. L. D. Gibson | Collector of Customs | Revenue | — | — |

### Deterministic checks: `gibson_j-d_b1928` vs `Gibson, J. L. D___Bermuda___1949`

- [PASS] surname_gate: bio 'GIBSON' vs stint 'Gibson, J. L. D' (exact)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'L', 'D']
- [PASS] age_gate: stint starts 1949, birth 1928 (age 21)
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

