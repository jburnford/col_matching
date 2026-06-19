<!-- {"case_id": "case_bond-taylor_r-f_b1906", "bio_ids": ["bond-taylor_r-f_b1906"], "stint_ids": ["Bond-Taylor, R. F___St Helena___1960"]} -->
# Dossier case_bond-taylor_r-f_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bond-taylor_r-f_b1906`

- Printed name: **BOND-TAYLOR, R. F**
- Birth year: 1906 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1956-L19893.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> BOND-TAYLOR, R. F.—b. 1906; ed. Gram. Sch., Tottenham; min. of war transp. port, 1940; higher accnty. asst., 1941; senr., 1941; acctnt., P.W.D., G.C., 1949; chief stores acctnt., 1955; chief stores supt., Ghana rlyw., 1956; col. treas. and collr., customs, St. H., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | min. of war transp. port | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1941 | higher accnty. asst | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1941 | senr | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1949 | acctnt., P.W.D. | Gold Coast | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 4 | 1955 | chief stores acctnt | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 5 | 1956 | chief stores supt., Ghana rlyw | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 6 | 1959 | col. treas. and collr., customs, St. H | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Bond-Taylor, R. F___St Helena___1960`

- Staff-list name: **Bond-Taylor, R. F** | colony: **St Helena** | listed 1960–1962 | editions [1960, 1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | R. F. Bond-Taylor | Colonial Treasurer and Collector of Customs | Civil Establishment | — | — |
| 1961 | R. F. Bond-Taylor | Colonial Treasurer and Collector of Customs | Civil Establishment | — | — |
| 1962 | R. F. Bond-Taylor | Colonial Treasurer and Collector of Customs | Civil Establishment | — | — |

### Deterministic checks: `bond-taylor_r-f_b1906` vs `Bond-Taylor, R. F___St Helena___1960`

- [PASS] surname_gate: bio 'BOND-TAYLOR' vs stint 'Bond-Taylor, R. F' (exact)
- [PASS] initials: bio ['R', 'F'] ~ stint ['R', 'F']
- [PASS] age_gate: stint starts 1960, birth 1906 (age 54)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1960-1962
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

