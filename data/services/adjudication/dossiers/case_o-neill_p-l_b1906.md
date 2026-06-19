<!-- {"case_id": "case_o-neill_p-l_b1906", "bio_ids": ["o-neill_p-l_b1906"], "stint_ids": ["O\u2019Neill, P. L___North Borneo___1949"]} -->
# Dossier case_o-neill_p-l_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `o-neill_p-l_b1906`

- Printed name: **O'NEILL, P. L**
- Birth year: 1906 (attested in editions [1959, 1960, 1961, 1962])
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L26532.v` — printed in editions [1959, 1960, 1961, 1962]:**

> O'NEILL, P. L.—b. 1906; ed. Clongowes Wood Coll., and Trinity Coll., Dublin; mil. serv., Burma rebellion, 1931, Wa States exped., 1934, and 1939-46, R.A.M.C.; M.O., N. Borneo, 1948-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948–1961 | M.O. | North Borneo | [1959, 1960, 1961, 1962] |

## Candidate stint `O’Neill, P. L___North Borneo___1949`

- Staff-list name: **O’Neill, P. L** | colony: **North Borneo** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. L. O’Neill | Health Officer | MEDICAL | — | Colonel |
| 1950 | P. L. O’Neill | Health Officer | MEDICAL | — | — |
| 1951 | P. L. O’Neill | Health Officer | MEDICAL | — | — |

### Deterministic checks: `o-neill_p-l_b1906` vs `O’Neill, P. L___North Borneo___1949`

- [PASS] surname_gate: bio 'O'NEILL' vs stint 'O’Neill, P. L' (exact)
- [PASS] initials: bio ['P', 'L'] ~ stint ['P', 'L']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [PASS] colony: 1 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 12 vs bar 60: 'M.O.' ~ 'Health Officer'
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

