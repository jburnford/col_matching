<!-- {"case_id": "case_allen_a-d_b1922", "bio_ids": ["allen_a-d_b1922"], "stint_ids": ["Allen, A. D. W___Gold Coast___1949"]} -->
# Dossier case_allen_a-d_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 103 official(s) with this surname in the graph's staff lists; 49 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Allen, A. D. W___Gold Coast___1949` is also gate-compatible with biography(ies) outside this case: ['allen_arthur-dudley-william_b1905'] (already linked elsewhere or filtered).

## Biography `allen_a-d_b1922`

- Printed name: **ALLEN, A. D**
- Birth year: 1922 (attested in editions [1960, 1961, 1962])
- Appears in editions: [1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1960-L20001.v` — printed in editions [1960, 1961, 1962]:**

> ALLEN, A. D.—b. 1922; ed. Cheltenham Gram. Sch.; mil. serv., 1941-46; civ. instr., air min., 1947; radio offr., M.C.A., 1948; wireless offr., E.A.C.S.O., posts and tels. admin., 1949; radio supt., civ. aviation dept., 1954; asst. signals offr., Nig., 1955-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | civ. instr., air min | — | [1960, 1961, 1962] |
| 1 | 1948 | radio offr., M.C.A | — | [1960, 1961, 1962] |
| 2 | 1949 | wireless offr., E.A.C.S.O., posts and tels. admin | — | [1960, 1961, 1962] |
| 3 | 1954 | radio supt., civ. aviation dept | — | [1960, 1961, 1962] |
| 4 | 1955–1961 | asst. signals offr. | Nigeria | [1960, 1961, 1962] |

## Candidate stint `Allen, A. D. W___Gold Coast___1949`

- Staff-list name: **Allen, A. D. W** | colony: **Gold Coast** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. D. W. Allen | Senior Collectors | Customs and Excise | — | — |
| 1950 | A. D. W. Allen | Senior Collectors | Customs and Excise | — | — |

### Deterministic checks: `allen_a-d_b1922` vs `Allen, A. D. W___Gold Coast___1949`

- [PASS] surname_gate: bio 'ALLEN' vs stint 'Allen, A. D. W' (exact)
- [PASS] initials: bio ['A', 'D'] ~ stint ['A', 'D', 'W']
- [PASS] age_gate: stint starts 1949, birth 1922 (age 27)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

