<!-- {"case_id": "case_clemmay_a-v_b1901", "bio_ids": ["clemmay_a-v_b1901"], "stint_ids": ["Clemmey, A. V___Tanganyika___1940"]} -->
# Dossier case_clemmay_a-v_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Clemmey, A. V___Tanganyika___1940` is also gate-compatible with biography(ies) outside this case: ['clemmy_a-v_b1901'] (already linked elsewhere or filtered).

## Biography `clemmay_a-v_b1901`

- Printed name: **CLEMMAY, A.V**
- Birth year: 1901 (attested in editions [1939])
- Honours: L.R.C.P, M.A, M.B, M.M.S.A, M.R.C.S
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L65597.v` — printed in editions [1939]:**

> CLEMMAY, A.V., M.A., M.B., B.Ch. (Oxf.), M.R.C.S., L.R.C.P., M.M.S.A.—B. 1901; med. offr., Tanganyika Territory, July, 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | med. offr., Tanganyika Territory | Tanganyika | [1939] |

## Candidate stint `Clemmey, A. V___Tanganyika___1940`

- Staff-list name: **Clemmey, A. V** | colony: **Tanganyika** | listed 1940–1949 | editions [1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | A. V. Clemmey | Medical Officer | Medical Department | — | — |
| 1949 | A. V. Clemmey | Specialist | Medical and Sanitation | — | — |

### Deterministic checks: `clemmay_a-v_b1901` vs `Clemmey, A. V___Tanganyika___1940`

- [PASS] surname_gate: bio 'CLEMMAY' vs stint 'Clemmey, A. V' (fuzzy:1)
- [PASS] initials: bio ['A', 'V'] ~ stint ['A', 'V']
- [PASS] age_gate: stint starts 1940, birth 1901 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1940-1949
- [FAIL] position_sim: best 45 vs bar 60: 'med. offr., Tanganyika Territory' ~ 'Medical Officer'
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

