<!-- {"case_id": "case_ells_p-r_b1918", "bio_ids": ["ells_p-r_b1918"], "stint_ids": ["Ells, P. R___Montserrat___1964"]} -->
# Dossier case_ells_p-r_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ells_p-r_b1918`

- Printed name: **ELLS, P. R**
- Birth year: 1918 (attested in editions [1955, 1956, 1957, 1958, 1959, 1960])
- Appears in editions: [1955, 1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1955-L20549.v` — printed in editions [1955, 1956, 1957, 1958, 1959, 1960]:**

> ELLS, P. R.—b. 1918; ed. Solihull, Warwicks, and Coll. of Accountancy and Econ., Glasgow; mil. serv., 1940-46, capt.; asst. audr., Wind. Is., 1947-50; treas., St. V., 1953; fin. sec., St. K., 1956; senr. asst. sec., W. Indies, 1958-59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947–1950 | asst. audr., Wind. Is | — | [1955, 1956, 1957, 1958, 1959, 1960] |
| 1 | 1953 | treas. | St. Vincent | [1955, 1956, 1957, 1958, 1959, 1960] |
| 2 | 1956 | fin. sec. | St. Kitts | [1955, 1956, 1957, 1958, 1959, 1960] |
| 3 | 1958–1959 | senr. asst. sec., W. Indies | St. Kitts *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960] |

## Candidate stint `Ells, P. R___Montserrat___1964`

- Staff-list name: **Ells, P. R** | colony: **Montserrat** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | P. R. Ells | Financial Secretary | Civil Establishment | — | — |
| 1965 | P. R. Ells | Financial Secretary | Civil Establishment | — | — |
| 1966 | P. R. Ells | Financial Secretary | Civil Establishment | — | — |

### Deterministic checks: `ells_p-r_b1918` vs `Ells, P. R___Montserrat___1964`

- [PASS] surname_gate: bio 'ELLS' vs stint 'Ells, P. R' (exact)
- [PASS] initials: bio ['P', 'R'] ~ stint ['P', 'R']
- [PASS] age_gate: stint starts 1964, birth 1918 (age 46)
- [FAIL] colony: no placed event resolves to 'Montserrat'
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

