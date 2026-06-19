<!-- {"case_id": "case_maddison_v-a_b1915", "bio_ids": ["maddison_v-a_b1915"], "stint_ids": ["Maddison, V. A___Kenya___1949"]} -->
# Dossier case_maddison_v-a_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `maddison_v-a_b1915`

- Printed name: **MADDISON, V. A**
- Birth year: 1915 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: C.M.G (1961)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L22854.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> MADDISON, V. A., C.M.G. (1961).—b. 1915; ed. Wellingborough Sch. and Downing Coll., Camb.; mil. serv., 1939-45; dist. offr., Ken., 1947; secon., sect., 1948; dir., trade and supplies, 1953; sec., commerce and industry, 1954; perm. sec., 1957. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | dist. offr. | Kenya | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1948 | secon., sect | Kenya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1953 | dir., trade and supplies | Kenya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1954 | sec., commerce and industry | Kenya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1957 | perm. sec | Kenya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Maddison, V. A___Kenya___1949`

- Staff-list name: **Maddison, V. A** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | V. A. Maddison | Assistant Secretary | Secretariat | — | — |
| 1950 | V. A. Maddison | Assistant Secretary | Secretariat | — | — |
| 1951 | V. A. Maddison | Assistant Secretary | Secretariat | — | — |

### Deterministic checks: `maddison_v-a_b1915` vs `Maddison, V. A___Kenya___1949`

- [PASS] surname_gate: bio 'MADDISON' vs stint 'Maddison, V. A' (exact)
- [PASS] initials: bio ['V', 'A'] ~ stint ['V', 'A']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [PASS] colony: 5 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 48 vs bar 60: 'secon., sect' ~ 'Assistant Secretary'
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

