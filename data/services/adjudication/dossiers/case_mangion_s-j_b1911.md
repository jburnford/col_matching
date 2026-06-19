<!-- {"case_id": "case_mangion_s-j_b1911", "bio_ids": ["mangion_s-j_b1911"], "stint_ids": ["Mangion, S. J___Malta___1955"]} -->
# Dossier case_mangion_s-j_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mangion_s-j_b1911`

- Printed name: **MANGION, S. J**
- Birth year: 1911 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: O.B.E (1960)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L22901.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> MANGION, S. J., O.B.E. (1960).—b. 1911; ed. St. Aloysius Coll. and Royal Univ. of Malta; engrnr., P.W.D., Malta, 1938; senr. engrnr., 1948; D.P.W., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | engrnr., P.W.D. | Malta | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1948 | senr. engrnr | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1954 | D.P.W | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Mangion, S. J___Malta___1955`

- Staff-list name: **Mangion, S. J** | colony: **Malta** | listed 1955–1964 | editions [1955, 1956, 1957, 1958, 1960, 1961, 1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | S. Mangion | Director of Public Works | THE MALTESE GOVERNMENT | — | — |
| 1956 | S. J. Mangion | Director of Public Works | The Maltese Government | — | — |
| 1957 | S. J. Mangion | Director of Public Works | The Maltese Government | — | — |
| 1958 | S. J. Mangion | Director of Public Works | The Maltese Government | — | — |
| 1960 | S. J. Mangion | Director of Public Works | Judiciary | — | — |
| 1961 | S. J. Mangion | Director of Public Works | Civil Establishment | O.B.E. | — |
| 1962 | S. J. Mangion | Director of Public Works | Civil Establishment | — | — |
| 1963 | S. J. Mangion | Director of Public Works | Civil Establishment | — | — |
| 1964 | S. J. Mangion | Director of Public Works | Law Officers | — | — |

### Deterministic checks: `mangion_s-j_b1911` vs `Mangion, S. J___Malta___1955`

- [PASS] surname_gate: bio 'MANGION' vs stint 'Mangion, S. J' (exact)
- [PASS] initials: bio ['S', 'J'] ~ stint ['S', 'J']
- [PASS] age_gate: stint starts 1955, birth 1911 (age 44)
- [PASS] colony: 3 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1955-1964
- [FAIL] position_sim: best 23 vs bar 60: 'senr. engrnr' ~ 'Director of Public Works'
- [PASS] honour: shared: O.B.E
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

