<!-- {"case_id": "case_spence_william-guthrie_e1914-2", "bio_ids": ["spence_william-guthrie_e1914-2"], "stint_ids": ["Spence, W. G___Commonwealth Of Australia___1905"]} -->
# Dossier case_spence_william-guthrie_e1914-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `spence_william-guthrie_e1914-2`

- Printed name: **SPENCE, WILLIAM GUTHRIE**
- Birth year: not printed
- Appears in editions: [1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1917-L53327.v` — printed in editions [1917, 1918, 1919]:**

> SPENCE, HON. WILLIAM GUTHRIE.—P.M.G., C. of A., 17th Sept., 1914, to 27th Oct., 1915; vice-pres. of exec. coun., 14th Nov., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1915 | P.M.G. | Commonwealth of Australia | [1917, 1918, 1919] |
| 1 | 1916 | vice-pres. of exec. coun. | — | [1917, 1918, 1919] |

## Candidate stint `Spence, W. G___Commonwealth Of Australia___1905`

- Staff-list name: **Spence, W. G** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | W. G. Spence | — | — | — | — |
| 1907 | W. G. Spence | Member | Legislative Assembly | — | — |

### Deterministic checks: `spence_william-guthrie_e1914-2` vs `Spence, W. G___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'SPENCE' vs stint 'Spence, W. G' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Commonwealth Of Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

