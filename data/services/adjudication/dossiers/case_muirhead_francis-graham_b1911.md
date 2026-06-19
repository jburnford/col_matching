<!-- {"case_id": "case_muirhead_francis-graham_b1911", "bio_ids": ["muirhead_francis-graham_b1911"], "stint_ids": ["Muirhead, F. G___High Commission Territories___1959"]} -->
# Dossier case_muirhead_francis-graham_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `muirhead_francis-graham_b1911`

- Printed name: **MUIRHEAD, FRANCIS GRAHAM**
- Birth year: 1911 (attested in editions [1940])
- Honours: O.B.E (1957)
- Appears in editions: [1940, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1940-L66949.v` — printed in editions [1940]:**

> MUIRHEAD, FRANCIS GRAHAM, B.Sc. (Lond.)—B. 1911; ed. Robert Gordon's Coll., Aberdeen and Univ. Coll., London Univ.; ast. dist. commr., (cadet) Basutoland, 1937; regir., res. commr.'s ct., 1938; ast. dist. commr., 1939.

**Version `col1957-L25869.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> MUIRHEAD, F. G., O.B.E. (1957).—b. 1911; ed. Gordon's Coll., Aberdeen, and Univ. Coll., London; mil. serv., 1941-43, capt.; D.O. Basuto., 1937; 1st asst. sec., 1956; sec., finance, 1960-63.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | ast. dist. commr., (cadet) Basutoland | — | [1940] |
| 1 | 1937 | D.O. Basuto | Dominions Office | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1938 | regir., res. commr.'s ct | — | [1940] |
| 3 | 1939 | ast. dist. commr | — | [1940] |
| 4 | 1956 | 1st asst. sec | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1960–1963 | sec., finance | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Muirhead, F. G___High Commission Territories___1959`

- Staff-list name: **Muirhead, F. G** | colony: **High Commission Territories** | listed 1959–1963 | editions [1959, 1960, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | F. G. Muirhead | First Assistant Secretary (Finance and Development) | BASUTOLAND | O.B.E. | — |
| 1960 | F. G. Muirhead | First Assistant Secretary (Finance and Development) | BASUTOLAND | O.B.E. | — |
| 1963 | F. G. Muirhead | Finance Secretary | Secretariat | O.B.E. | — |

### Deterministic checks: `muirhead_francis-graham_b1911` vs `Muirhead, F. G___High Commission Territories___1959`

- [PASS] surname_gate: bio 'MUIRHEAD' vs stint 'Muirhead, F. G' (exact)
- [PASS] initials: bio ['F', 'G'] ~ stint ['F', 'G']
- [PASS] age_gate: stint starts 1959, birth 1911 (age 48)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1963
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: O.B.E
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

