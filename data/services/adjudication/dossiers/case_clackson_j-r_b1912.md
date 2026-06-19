<!-- {"case_id": "case_clackson_j-r_b1912", "bio_ids": ["clackson_j-r_b1912"], "stint_ids": ["Clackson, J. R___Nigeria___1949"]} -->
# Dossier case_clackson_j-r_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `clackson_j-r_b1912`

- Printed name: **CLACKSON, J. R**
- Birth year: 1912 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1953-L16878.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> CLACKSON, J. R.—b. 1912; ed. City of London Sch., Birkbeck Coll. and Imp. Coll. Sci. (London); mil. serv., 1943-46, R.A.F.V.R., flt. lieut.; meteorologist, B.E.A., 1936; senr. met., Nig., 1947; dir., B.W.A. met. serv., 1950; Fed. of Nig. 1954-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | meteorologist, B.E.A | — | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1947 | senr. met. | Nigeria | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1950 | dir., B.W.A. met. serv | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1954–1961 | Fed. of Nig | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Clackson, J. R___Nigeria___1949`

- Staff-list name: **Clackson, J. R** | colony: **Nigeria** | listed 1949–1960 | editions [1949, 1952, 1956, 1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. R. Clackson | Senior Meteorologist | METEOROLOGICAL SERVICE | — | — |
| 1952 | J. R. Clackson | Director of British West African Meteorological Services | Civil Establishment | — | — |
| 1956 | J. R. Clackson | Director of Meteorological Services | Civil Establishment | — | — |
| 1958 | J. R. Clackson | Director of Meteorological Department | Civil Establishment | — | — |
| 1960 | J. R. Clackson | Director of Meteorological Department | Civil Establishment | — | — |

### Deterministic checks: `clackson_j-r_b1912` vs `Clackson, J. R___Nigeria___1949`

- [PASS] surname_gate: bio 'CLACKSON' vs stint 'Clackson, J. R' (exact)
- [PASS] initials: bio ['J', 'R'] ~ stint ['J', 'R']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1949-1960
- [FAIL] position_sim: best 57 vs bar 60: 'senr. met.' ~ 'Senior Meteorologist'
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

