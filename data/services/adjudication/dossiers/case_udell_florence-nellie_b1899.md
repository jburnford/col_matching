<!-- {"case_id": "case_udell_florence-nellie_b1899", "bio_ids": ["udell_florence-nellie_b1899"], "stint_ids": ["O'Dell, F___Southern Rhodesia___1925"]} -->
# Dossier case_udell_florence-nellie_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `udell_florence-nellie_b1899`

- Printed name: **UDELL, Florence Nellie**
- Birth year: 1899 (attested in editions [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: C.B.E (1958), M.B.E
- Appears in editions: [1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1954-L22650.v` — printed in editions [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> UDELL, Miss F. N., C.B.E. (1958).—b. 1899; ed. private sch. and Radcliffe Infy., Oxford; ch. nurse, E.R.O., U.N.R.R.A., 1944-46; ch. nursing offr., C.O., 1946; D.T.C., 1961-64.

**Version `col1950-L40322.v` — printed in editions [1950, 1951, 1953]:**

> UDELL, Florence Nellie, M.B.E.—b. 1899; ed. private bdg. sch.; ch. nursing offr., U.N.R.R.A.; C.O., 1946; chmn., nurses panel, Scottish nurses' salaries comttee.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944–1946 | ch. nurse, E.R.O., U.N.R.R.A | — | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1946 | ch. nursing offr. | Colonial Office | [1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1961–1964 | D.T.C | Colonial Office *(inherited from previous clause)* | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `O'Dell, F___Southern Rhodesia___1925`

- Staff-list name: **O'Dell, F** | colony: **Southern Rhodesia** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | F. O'Dell | Staff Officer, War Records | Defence Department | — | Lieutenant |
| 1927 | F. O'Dell | Staff Officer, War Records | Defence Department | — | Capt. |

### Deterministic checks: `udell_florence-nellie_b1899` vs `O'Dell, F___Southern Rhodesia___1925`

- [PASS] surname_gate: bio 'UDELL' vs stint 'O'Dell, F' (fuzzy:1)
- [PASS] initials: bio ['F', 'N'] ~ stint ['F']
- [PASS] age_gate: stint starts 1925, birth 1899 (age 26)
- [FAIL] colony: no placed event resolves to 'Southern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1927
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

