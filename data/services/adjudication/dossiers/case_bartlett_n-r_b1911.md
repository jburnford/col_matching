<!-- {"case_id": "case_bartlett_n-r_b1911", "bio_ids": ["bartlett_n-r_b1911"], "stint_ids": ["Bartlett, N. R___Nyasaland___1949"]} -->
# Dossier case_bartlett_n-r_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 27 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bartlett_n-r_b1911`

- Printed name: **BARTLETT, N. R**
- Birth year: 1911 (attested in editions [1965, 1966])
- Honours: M.B.E (1965)
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L13458.v` — printed in editions [1965, 1966]:**

> BARTLETT, N. R., M.B.E. (1965).—b. 1911; ed. Brighton Coll.; mil. serv., 1939-43; sec., med. dept., Nyasa., 1947; acctnt., 1952; senr. acctnt., 1956; prov. acctnt., 1960; senr. estab. offr., P.W.D., 1960. (Malawi Govt. service.)

**Version `col1961-L19554.v` — printed in editions [1961, 1962, 1963, 1964]:**

> BARTLETT, N. R.—b. 1911; ed. Brighton Coll.; mil. serv., 1942-45; sec., med. dept., Nyasa., 1947; acctnt., agric. dept., 1952; senr. estab. offr., P.W.D., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | sec., med. dept. | Nyasaland | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1952 | acctnt | Nyasaland *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1956 | senr. acctnt | Nyasaland *(inherited from previous clause)* | [1965, 1966] |
| 3 | 1960 | prov. acctnt | Nyasaland *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Bartlett, N. R___Nyasaland___1949`

- Staff-list name: **Bartlett, N. R** | colony: **Nyasaland** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | N. R. Bartlett | Secretary | Medical | — | — |
| 1950 | N. R. Bartlett | Secretary | Medical | — | — |
| 1951 | N. R. Bartlett | Secretary | MEDICAL | — | — |

### Deterministic checks: `bartlett_n-r_b1911` vs `Bartlett, N. R___Nyasaland___1949`

- [PASS] surname_gate: bio 'BARTLETT' vs stint 'Bartlett, N. R' (exact)
- [PASS] initials: bio ['N', 'R'] ~ stint ['N', 'R']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 4 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 29 vs bar 60: 'sec., med. dept.' ~ 'Secretary'
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

