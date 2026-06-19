<!-- {"case_id": "case_davidson_m-n_b1922", "bio_ids": ["davidson_m-n_b1922"], "stint_ids": ["Davidson, M. N___Cyprus___1949"]} -->
# Dossier case_davidson_m-n_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 65 official(s) with this surname in the graph's staff lists; 29 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `davidson_m-n_b1922`

- Printed name: **DAVIDSON, M. N**
- Birth year: 1922 (attested in editions [1956, 1957, 1958])
- Appears in editions: [1956, 1957, 1958]

### Verbatim printed entry text (OCR)

**Version `col1956-L20722.v` — printed in editions [1956, 1957, 1958]:**

> DAVIDSON, M. N.—b. 1922; ed. Tonbridge Sch. and St. John's Coll., Camb.; mil. serv., 1941-43, capt.; admin. offr., Cyp., 1944; p.s. to gov., 1945; clk., ex. co., 1948; cl. I, 1954; dist. offr., Tang., 1954; asst. sec. and clk., assembly, E.A.H.C., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | admin. offr. | Cyprus | [1956, 1957, 1958] |
| 1 | 1945 | p.s. to gov | Cyprus *(inherited from previous clause)* | [1956, 1957, 1958] |
| 2 | 1948 | clk., ex. co | Cyprus *(inherited from previous clause)* | [1956, 1957, 1958] |
| 3 | 1954 | cl. I | Cyprus *(inherited from previous clause)* | [1956, 1957, 1958] |
| 4 | 1954 | dist. offr. | Tanganyika | [1956, 1957, 1958] |
| 5 | 1955 | asst. sec. and clk., assembly, E.A.H.C | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958] |

## Candidate stint `Davidson, M. N___Cyprus___1949`

- Staff-list name: **Davidson, M. N** | colony: **Cyprus** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | M. N. Davidson | Assistant Secretaries (Administrative Officers) | Secretariat | — | — |
| 1951 | M. N. Davidson | Assistant Commissioner of Paphos | District Administration | — | — |

### Deterministic checks: `davidson_m-n_b1922` vs `Davidson, M. N___Cyprus___1949`

- [PASS] surname_gate: bio 'DAVIDSON' vs stint 'Davidson, M. N' (exact)
- [PASS] initials: bio ['M', 'N'] ~ stint ['M', 'N']
- [PASS] age_gate: stint starts 1949, birth 1922 (age 27)
- [PASS] colony: 4 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 20 vs bar 60: 'p.s. to gov' ~ 'Assistant Commissioner of Paphos'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

