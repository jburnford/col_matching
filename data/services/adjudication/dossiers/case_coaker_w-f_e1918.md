<!-- {"case_id": "case_coaker_w-f_e1918", "bio_ids": ["coaker_w-f_e1918"], "stint_ids": ["Coaker, W. F___Newfoundland___1920"]} -->
# Dossier case_coaker_w-f_e1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coaker_w-f_e1918`

- Printed name: **COAKER, W.F**
- Birth year: not printed
- Appears in editions: [1918]

### Verbatim printed entry text (OCR)

**Version `col1918-L49443.v` — printed in editions [1918]:**

> COAKER, HON. W.F.—Min. without portfolio, Newfoundland, Jan., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | Min. without portfolio | Newfoundland | [1918] |

## Candidate stint `Coaker, W. F___Newfoundland___1920`

- Staff-list name: **Coaker, W. F** | colony: **Newfoundland** | listed 1920–1921 | editions [1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Hon. W. F. Coaker | Minister of Marine and Fisheries | Department of Marine and Fisheries | — | — |
| 1921 | W. F. Coaker | Minister of Marine and Fisheries | Department of Marine and Fisheries | — | — |

### Deterministic checks: `coaker_w-f_e1918` vs `Coaker, W. F___Newfoundland___1920`

- [PASS] surname_gate: bio 'COAKER' vs stint 'Coaker, W. F' (exact)
- [PASS] initials: bio ['W', 'F'] ~ stint ['W', 'F']
- [PASS] age_gate: stint starts 1920; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Newfoundland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1920-1921
- [FAIL] position_sim: best 30 vs bar 60: 'Min. without portfolio' ~ 'Minister of Marine and Fisheries'
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

