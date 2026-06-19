<!-- {"case_id": "case_sutherland_reay-mackay_e1906", "bio_ids": ["sutherland_reay-mackay_e1906"], "stint_ids": ["Sutherland, R. M___Basutoland___1908"]} -->
# Dossier case_sutherland_reay-mackay_e1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sutherland_reay-mackay_e1906`

- Printed name: **SUTHERLAND, REAY MACKAY**
- Birth year: not printed
- Appears in editions: [1909, 1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1909-L49901.v` — printed in editions [1909, 1910, 1911]:**

> SUTHERLAND, REAY MACKAY.—Sub.-inspr., Bechuana land Prot. pol., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | Sub.-inspr., Bechuana land Prot. pol | Bechuana land | [1909, 1910, 1911] |

## Candidate stint `Sutherland, R. M___Basutoland___1908`

- Staff-list name: **Sutherland, R. M** | colony: **Basutoland** | listed 1908–1910 | editions [1908, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | R. M. Sutherland | Sub-Inspector | Establishment | — | — |
| 1910 | R. M. Sutherland | Sub-Inspector of Police | Civil Establishment | — | — |

### Deterministic checks: `sutherland_reay-mackay_e1906` vs `Sutherland, R. M___Basutoland___1908`

- [PASS] surname_gate: bio 'SUTHERLAND' vs stint 'Sutherland, R. M' (exact)
- [PASS] initials: bio ['R', 'M'] ~ stint ['R', 'M']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Basutoland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1910
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

