<!-- {"case_id": "case_dunn_dermot-john_b1915", "bio_ids": ["dunn_dermot-john_b1915"], "stint_ids": ["Dunn, D. J___Cyprus___1955"]} -->
# Dossier case_dunn_dermot-john_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dunn_dermot-john_b1915`

- Printed name: **DUNN, Dermot John**
- Birth year: 1915 (attested in editions [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Honours: A.M.I.C.E, B.A.I, O.B.E (1960)
- Appears in editions: [1951, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1955-L20495.v` — printed in editions [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> DUNN, D. J., O.B.E. (1960).—b. 1915; ed. Presentation Coll. and Univ. of Dublin (T.C.D.); asst. engrn., Mal., 1941; S.L., 1942; exec. engrn., Tang., 1946; asst. D.P.W., Cyp., 1953; D.D.P.W., 1954; D.P.W., 1959.

**Version `col1951-L37757.v` — printed in editions [1951]:**

> DUNN, Dermot John, M.A. (Dub.), B.A.I., A.M.I.C.E., A.M.I.Struct.E.—b. 1915; ed. Presentation Coll., Dublin and Rosse Coll.; l.s., Swahili; exec. engr., Mal., 1941; S.L., 1942; gr. II, T.T., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | asst. engrn. | Malaya | [1951, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1942 | asst. engrn. | Sierra Leone | [1951, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1946 | exec. engrn. | Tanganyika | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1946 | gr. II, T.T | Sierra Leone *(inherited from previous clause)* | [1951] |
| 4 | 1953 | asst. D.P.W. | Cyprus | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 5 | 1954 | D.D.P.W | Cyprus *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 6 | 1959 | D.P.W | Cyprus *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Dunn, D. J___Cyprus___1955`

- Staff-list name: **Dunn, D. J** | colony: **Cyprus** | listed 1955–1959 | editions [1955, 1956, 1957, 1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | D. J. Dunn | Deputy Director of Public Works | Civil Establishment | — | — |
| 1956 | D. J. Dunn | Deputy Director of Public Works | Civil Establishment | — | — |
| 1957 | D. J. Dunn | Deputy Director of Public Works | Civil Establishment | — | — |
| 1958 | D. J. Dunn | Deputy Director of Public Works | Civil Establishment | — | — |
| 1959 | D. J. Dunn | Deputy Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `dunn_dermot-john_b1915` vs `Dunn, D. J___Cyprus___1955`

- [PASS] surname_gate: bio 'DUNN' vs stint 'Dunn, D. J' (exact)
- [PASS] initials: bio ['D', 'J'] ~ stint ['D', 'J']
- [PASS] age_gate: stint starts 1955, birth 1915 (age 40)
- [PASS] colony: 3 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1955-1959
- [FAIL] position_sim: best 26 vs bar 60: 'asst. D.P.W.' ~ 'Deputy Director of Public Works'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

