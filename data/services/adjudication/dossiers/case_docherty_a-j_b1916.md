<!-- {"case_id": "case_docherty_a-j_b1916", "bio_ids": ["docherty_a-j_b1916"], "stint_ids": ["Docherty, A. J___Uganda___1949"]} -->
# Dossier case_docherty_a-j_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `docherty_a-j_b1916`

- Printed name: **DOCHERTY, A. J**
- Birth year: 1916 (attested in editions [1959, 1960, 1961, 1962, 1963])
- Honours: C.P.M (1960)
- Appears in editions: [1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1959-L22460.v` — printed in editions [1959, 1960, 1961, 1962, 1963]:**

> DOCHERTY, A. J., C.P.M. (1960).—b. 1916; ed. St. Andrews Sch., Rothesay; police constable, Pal., 1939; asst. supt., police, Uga., 1947; supt., 1954; senr. supt., 1957-62. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | police constable | Palestine | [1959, 1960, 1961, 1962, 1963] |
| 1 | 1947 | asst. supt., police | Uganda | [1959, 1960, 1961, 1962, 1963] |
| 2 | 1954 | supt | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963] |
| 3 | 1957–1962 | senr. supt | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Docherty, A. J___Uganda___1949`

- Staff-list name: **Docherty, A. J** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. J. Docherty | Superintendents, Assistants and Cadets | Police | — | — |
| 1951 | A. J. Docherty | Superintendents, Assistants and Cadets | Police | — | — |

### Deterministic checks: `docherty_a-j_b1916` vs `Docherty, A. J___Uganda___1949`

- [PASS] surname_gate: bio 'DOCHERTY' vs stint 'Docherty, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 45 vs bar 60: 'asst. supt., police' ~ 'Superintendents, Assistants and Cadets'
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

