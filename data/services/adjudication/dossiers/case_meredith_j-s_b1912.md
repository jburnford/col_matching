<!-- {"case_id": "case_meredith_j-s_b1912", "bio_ids": ["meredith_j-s_b1912"], "stint_ids": ["Meredith, J___Kenya___1939"]} -->
# Dossier case_meredith_j-s_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `meredith_j-s_b1912`

- Printed name: **MEREDITH, J. S**
- Birth year: 1912 (attested in editions [1956, 1957, 1958, 1959, 1961, 1962])
- Honours: O.B.E (1956)
- Appears in editions: [1956, 1957, 1958, 1959, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L23034.v` — printed in editions [1956, 1957, 1958, 1959, 1961, 1962]:**

> MEREDITH, J. S., O.B.E. (1956).—b. 1912; ed. Stirling and Glasgow Univ.; mil. serv., 1939–44, maj.; M.O., N. Rhod., 1939; med. specialist, Tang., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | M.O. | Northern Rhodesia | [1956, 1957, 1958, 1959, 1961, 1962] |
| 1 | 1951 | med. specialist | Tanganyika | [1956, 1957, 1958, 1959, 1961, 1962] |

## Candidate stint `Meredith, J___Kenya___1939`

- Staff-list name: **Meredith, J** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | J. Meredith | Senior Postmaster | Posts and Telegraphs Department | — | — |
| 1940 | J. Meredith | Senior Postmaster | Posts and Telegraphs Department | — | — |

### Deterministic checks: `meredith_j-s_b1912` vs `Meredith, J___Kenya___1939`

- [PASS] surname_gate: bio 'MEREDITH' vs stint 'Meredith, J' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J']
- [PASS] age_gate: stint starts 1939, birth 1912 (age 27)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

