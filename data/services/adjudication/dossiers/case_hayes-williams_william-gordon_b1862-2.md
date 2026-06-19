<!-- {"case_id": "case_hayes-williams_william-gordon_b1862-2", "bio_ids": ["hayes-williams_william-gordon_b1862-2"], "stint_ids": ["Hayes-Williams, W. G___New South Wales___1905"]} -->
# Dossier case_hayes-williams_william-gordon_b1862-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hayes-Williams, W. G___New South Wales___1905` is also gate-compatible with biography(ies) outside this case: ['hayes-williams_william-gordon_b1862'] (already linked elsewhere or filtered).

## Biography `hayes-williams_william-gordon_b1862-2`

- Printed name: **HAYES-WILLIAMS, WILLIAM GORDON**
- Birth year: 1862 (attested in editions [1911])
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L45376.v` — printed in editions [1911]:**

> HAYES-WILLIAMS, WILLIAM GORDON.—B. 1862; registr.-gen., New South Wales, 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1888 | registr.-gen. | New South Wales | [1911] |

## Candidate stint `Hayes-Williams, W. G___New South Wales___1905`

- Staff-list name: **Hayes-Williams, W. G** | colony: **New South Wales** | listed 1905–1917 | editions [1905, 1906, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | W. G. Hayes-Williams | Registrar-General and Examiner of Patents | Statistician's Department | — | — |
| 1906 | W. G. Hayes-Williams | Registrar-General and Examiner of Patents | Statistician's Department | — | — |
| 1917 | W. G. Hayes-Williams | Registrar-General | Department of the Attorney-General and of Justice | — | — |

### Deterministic checks: `hayes-williams_william-gordon_b1862-2` vs `Hayes-Williams, W. G___New South Wales___1905`

- [PASS] surname_gate: bio 'HAYES-WILLIAMS' vs stint 'Hayes-Williams, W. G' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1905, birth 1862 (age 43)
- [PASS] colony: 1 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1917
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

