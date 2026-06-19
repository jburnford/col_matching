<!-- {"case_id": "case_blanc_reginald-norris-o-connell_b1898", "bio_ids": ["blanc_reginald-norris-o-connell_b1898"], "stint_ids": ["Blanc, N. O'C___Trinidad and Tobago___1927"]} -->
# Dossier case_blanc_reginald-norris-o-connell_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blanc_reginald-norris-o-connell_b1898`

- Printed name: **BLANC, Reginald Norris O'Connell**
- Birth year: 1898 (attested in editions [1948, 1949, 1950, 1951])
- Honours: B.A.O, M.B, N.U.I
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31241.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BLANC, Reginald Norris O'Connell, M.B., B.Ch., B.A.O., N.U.I.—b. 1898; ed. St. Mary's Coll., Trin. (Island Schol.) and Univ. Coll., Dublin, 1st cl. hons., 1st place final M.B., B.Ch., B.A.O. (medallist); med. offr., Trin., 1923; dist. med. offr., 1926; gr. C., 1939; gr. B., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | med. offr. | Trinidad | [1948, 1949, 1950, 1951] |
| 1 | 1926 | dist. med. offr | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1939 | gr. C | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1945 | gr. B | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Blanc, N. O'C___Trinidad and Tobago___1927`

- Staff-list name: **Blanc, N. O'C** | colony: **Trinidad and Tobago** | listed 1927–1934 | editions [1927, 1928, 1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | N. O'C. Blanc | Medical Officer | Government Medical Officers | — | — |
| 1928 | N. O'C. Blanc | — | Government Medical Officers | — | — |
| 1931 | N. O'C. Blanc | — | Government Medical Officers | — | — |
| 1933 | N. O'C. Blanc | Medical Officer | Medical Establishment | — | — |
| 1934 | N. O'C. Blanc | Medical Officer | Government Medical Officers | — | — |

### Deterministic checks: `blanc_reginald-norris-o-connell_b1898` vs `Blanc, N. O'C___Trinidad and Tobago___1927`

- [PASS] surname_gate: bio 'BLANC' vs stint 'Blanc, N. O'C' (exact)
- [PASS] initials: bio ['R', 'N', 'O'] ~ stint ['N', 'O']
- [PASS] age_gate: stint starts 1927, birth 1898 (age 29)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1934
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

