<!-- {"case_id": "case_coxhead_g-s_b1911", "bio_ids": ["coxhead_g-s_b1911"], "stint_ids": ["Coxhead, G. S___Hong Kong___1949"]} -->
# Dossier case_coxhead_g-s_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coxhead_g-s_b1911`

- Printed name: **COXHEAD, G. S**
- Birth year: 1911 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L20597.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> COXHEAD, G. S.—b. 1911; ed. Oundle Sch., L'pool and London Univs.; mil. serv., 1941-45; master, educ. dept., H.K., 1939; educ. offr., 1960; senr., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | master, educ. dept. | Hong Kong | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1961 | senr | Hong Kong *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Coxhead, G. S___Hong Kong___1949`

- Staff-list name: **Coxhead, G. S** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. S. Coxhead | Masters | Education Department | — | — |
| 1950 | G. S. Coxhead | Masters | Education | — | — |
| 1951 | G. S. Coxhead | Masters | Education | — | — |

### Deterministic checks: `coxhead_g-s_b1911` vs `Coxhead, G. S___Hong Kong___1949`

- [PASS] surname_gate: bio 'COXHEAD' vs stint 'Coxhead, G. S' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G', 'S']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 52 vs bar 60: 'master, educ. dept.' ~ 'Masters'
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

