<!-- {"case_id": "case_haynes_w-s_b1910", "bio_ids": ["haynes_w-s_b1910"], "stint_ids": ["Haynes, W. S___Kenya___1949"]} -->
# Dossier case_haynes_w-s_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 41 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `haynes_w-s_b1910`

- Printed name: **HAYNES, W. S**
- Birth year: 1910 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L23944.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> HAYNES, W. S.—b. 1910; ed. Uppingham Sch. and Clare Coll., Camb.; mil. serv., 1940-44, capt.; M.O., Ken., 1937; T.B. offr., 1952; pubns. Tuberculosis Survey, Kenya, 1949; Tuberculosis in Kenya. (B.M.J. 1951.)

**Version `col1962-L22122.v` — printed in editions [1962, 1963, 1964, 1965]:**

> HAYNES, W. S.—b. 1910; ed. Uppingham Sch. and Clare Coll., Camb.; mil. serv., 1940-44, capt.; M.O., Ken., 1937; T.B. offr., 1952. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | M.O. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1949 | pubns. Tuberculosis Survey | Kenya | [1957, 1958, 1959, 1960, 1961] |
| 2 | 1951 | Tuberculosis in Kenya. (B.M.J | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 3 | 1952 | T.B. offr | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Haynes, W. S___Kenya___1949`

- Staff-list name: **Haynes, W. S** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. S. Haynes | Medical Officer | Medical | — | — |
| 1950 | W. S. Haynes | Medical Officer | Medical | — | — |
| 1951 | W. S. Haynes | Medical Officer | Medical | — | — |

### Deterministic checks: `haynes_w-s_b1910` vs `Haynes, W. S___Kenya___1949`

- [PASS] surname_gate: bio 'HAYNES' vs stint 'Haynes, W. S' (exact)
- [PASS] initials: bio ['W', 'S'] ~ stint ['W', 'S']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 36 vs bar 60: 'T.B. offr' ~ 'Medical Officer'
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

