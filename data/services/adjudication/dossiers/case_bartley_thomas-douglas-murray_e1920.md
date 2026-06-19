<!-- {"case_id": "case_bartley_thomas-douglas-murray_e1920", "bio_ids": ["bartley_thomas-douglas-murray_e1920"], "stint_ids": ["Bartley, T. D. M___Kenya___1949", "Bartley, T. D. M___Tanganyika___1923"]} -->
# Dossier case_bartley_thomas-douglas-murray_e1920

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Bartley, T. D. M___Kenya___1949` is also gate-compatible with biography(ies) outside this case: ['bartley_thomas-douglas-murray_e1920-2'] (already linked elsewhere or filtered).
- NOTE: stint `Bartley, T. D. M___Tanganyika___1923` is also gate-compatible with biography(ies) outside this case: ['bartley_thomas-douglas-murray_e1920-2'] (already linked elsewhere or filtered).

## Biography `bartley_thomas-douglas-murray_e1920`

- Printed name: **BARTLEY, THOMAS DOUGLAS MURRAY**
- Birth year: not printed
- Honours: B.A, T.C.D
- Appears in editions: [1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1923-L52307.v` — printed in editions [1923, 1924, 1925]:**

> BARTLEY, THOMAS DOUGLAS MURRAY, B.A., T.C.D.—Administrative offir. (cadet), Tanganyika Territory, 28th May, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | Administrative offir. (cadet), Tanganyika Territory | Tanganyika | [1923, 1924, 1925] |

## Candidate stint `Bartley, T. D. M___Kenya___1949`

- Staff-list name: **Bartley, T. D. M** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. D. M. Bartley | Puisne Judges | Judicial | — | — |
| 1950 | T. D. M. Bartley | Puisne Judges | JUDICIAL | — | — |
| 1951 | T. D. M. Bartley | Puisne Judges | Inland Revenue Department | — | — |

### Deterministic checks: `bartley_thomas-douglas-murray_e1920` vs `Bartley, T. D. M___Kenya___1949`

- [PASS] surname_gate: bio 'BARTLEY' vs stint 'Bartley, T. D. M' (exact)
- [PASS] initials: bio ['T', 'D', 'M'] ~ stint ['T', 'D', 'M']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bartley, T. D. M___Tanganyika___1923`

- Staff-list name: **Bartley, T. D. M** | colony: **Tanganyika** | listed 1923–1925 | editions [1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | T. D. M. Bartley | Assistant Secretary | Secretariat | — | — |
| 1924 | T. D. M. Bartley | Assistant Secretary | Secretariat | — | — |
| 1925 | T. D. M. Bartley | Assistant Secretary | Secretariat | — | — |

### Deterministic checks: `bartley_thomas-douglas-murray_e1920` vs `Bartley, T. D. M___Tanganyika___1923`

- [PASS] surname_gate: bio 'BARTLEY' vs stint 'Bartley, T. D. M' (exact)
- [PASS] initials: bio ['T', 'D', 'M'] ~ stint ['T', 'D', 'M']
- [PASS] age_gate: stint starts 1923; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1925
- [FAIL] position_sim: best 39 vs bar 60: 'Administrative offir. (cadet), Tanganyika Territory' ~ 'Assistant Secretary'
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

