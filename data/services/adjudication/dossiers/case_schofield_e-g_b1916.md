<!-- {"case_id": "case_schofield_e-g_b1916", "bio_ids": ["schofield_e-g_b1916"], "stint_ids": ["Schofield, E. G___Uganda___1949"]} -->
# Dossier case_schofield_e-g_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `schofield_e-g_b1916`

- Printed name: **SCHOFIELD, E. G**
- Birth year: 1916 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L27087.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> SCHOFIELD, E. G.—b. 1916; mil. serv., 1940-45, R.A.F.; asst. press supt., Uga., 1947; press supt., 1954. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | asst. press supt. | Uganda | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1954 | press supt | Uganda *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Schofield, E. G___Uganda___1949`

- Staff-list name: **Schofield, E. G** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. G. Schofield | Machine Section Superintendent | Printing | — | — |
| 1951 | E. G. Schofield | Machine Section Superintendent | PRINTING | — | — |

### Deterministic checks: `schofield_e-g_b1916` vs `Schofield, E. G___Uganda___1949`

- [PASS] surname_gate: bio 'SCHOFIELD' vs stint 'Schofield, E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['E', 'G']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 36 vs bar 60: 'asst. press supt.' ~ 'Machine Section Superintendent'
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

