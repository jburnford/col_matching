<!-- {"case_id": "case_theron_h-s_e1896", "bio_ids": ["theron_h-s_e1896"], "stint_ids": ["Theron, Hendrik Schalk___Orange River Colony___1908"]} -->
# Dossier case_theron_h-s_e1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `theron_h-s_e1896`

- Printed name: **THERON, H. S**
- Birth year: not printed
- Appears in editions: [1914, 1915, 1917]

### Verbatim printed entry text (OCR)

**Version `col1914-L50307.v` — printed in editions [1914, 1915, 1917]:**

> THERON, Hon. H. S., R.A.—Inspr. of mines, Orange Free State, 1896; resident J.P., Koffyfontein, 1898; min. of lands, Union of South Africa, since 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | Inspr. of mines | Orange Free State | [1914, 1915, 1917] |
| 1 | 1898 | resident J.P., Koffyfontein | Orange Free State *(inherited from previous clause)* | [1914, 1915, 1917] |
| 2 | 1913 | min. of lands, Union of South Africa, since | Orange Free State *(inherited from previous clause)* | [1914, 1915, 1917] |

## Candidate stint `Theron, Hendrik Schalk___Orange River Colony___1908`

- Staff-list name: **Theron, Hendrik Schalk** | colony: **Orange River Colony** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | Hendrik Schalk Theron | Member | Electoral Division | — | — |
| 1909 | Hendrik Schalk Theron | Member | Electoral Division | — | — |

### Deterministic checks: `theron_h-s_e1896` vs `Theron, Hendrik Schalk___Orange River Colony___1908`

- [PASS] surname_gate: bio 'THERON' vs stint 'Theron, Hendrik Schalk' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Orange River Colony'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1908-1909
- [FAIL] position_sim: best 13 vs bar 60: 'resident J.P., Koffyfontein' ~ 'Member'
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

