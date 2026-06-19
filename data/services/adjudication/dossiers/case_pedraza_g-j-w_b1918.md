<!-- {"case_id": "case_pedraza_g-j-w_b1918", "bio_ids": ["pedraza_g-j-w_b1918"], "stint_ids": ["Pedraza, G. J. W___Kenya___1950"]} -->
# Dossier case_pedraza_g-j-w_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pedraza_g-j-w_b1918`

- Printed name: **PEDRAZA, G. J. W**
- Birth year: 1918 (attested in editions [1960, 1961, 1962, 1963, 1964])
- Honours: M.B.E
- Appears in editions: [1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1960-L26848.v` — printed in editions [1960, 1961, 1962, 1963, 1964]:**

> PEDRAZA, G. J. W., M.B.E., M.C.—b. 1918; ed. Wellington Coll., and R.M.C., Sandhurst; mil. serv., 1938-48; dist. offr., Ken., 1949; senr., 1961-63. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | dist. offr. | Kenya | [1960, 1961, 1962, 1963, 1964] |
| 1 | 1961–1963 | senr | Kenya *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Pedraza, G. J. W___Kenya___1950`

- Staff-list name: **Pedraza, G. J. W** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | G. J. W. Pedraza | Assistant Secretary | Secretariat | — | — |
| 1951 | G. J. W. Pedraza | Assistant Secretary | Secretariat | — | — |

### Deterministic checks: `pedraza_g-j-w_b1918` vs `Pedraza, G. J. W___Kenya___1950`

- [PASS] surname_gate: bio 'PEDRAZA' vs stint 'Pedraza, G. J. W' (exact)
- [PASS] initials: bio ['G', 'J', 'W'] ~ stint ['G', 'J', 'W']
- [PASS] age_gate: stint starts 1950, birth 1918 (age 32)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 36 vs bar 60: 'dist. offr.' ~ 'Assistant Secretary'
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

