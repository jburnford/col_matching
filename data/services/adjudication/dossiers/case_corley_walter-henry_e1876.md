<!-- {"case_id": "case_corley_walter-henry_e1876", "bio_ids": ["corley_walter-henry_e1876"], "stint_ids": ["Corley, W. H___Fiji___1917"]} -->
# Dossier case_corley_walter-henry_e1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `corley_walter-henry_e1876`

- Printed name: **CORLEY, WALTER HENRY**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L32710.v` — printed in editions [1898]:**

> CORLEY, WALTER HENRY, A.M.I.C.E.—Asst. engrnr., Natal rly., Feb., 1876; ag. maintenance engrnr., Jan. 1880, to 1881; maintenance engrnr., 1882; dist. engrnr., 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | Asst. engrnr. | Natal | [1898] |
| 1 | 1880–1881 | ag. maintenance engrnr. | — | [1898] |
| 2 | 1882 | maintenance engrnr. | — | [1898] |
| 3 | 1883 | dist. engrnr. | — | [1898] |

## Candidate stint `Corley, W. H___Fiji___1917`

- Staff-list name: **Corley, W. H** | colony: **Fiji** | listed 1917–1921 | editions [1917, 1918, 1919, 1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | W. H. Corley | Marine Board Surveyor | Works Department | — | — |
| 1918 | W. H. Corley | Marine Board Surveyor | Works Department | — | — |
| 1919 | W. H. Corley | Marine Board Surveyor | Works Department | — | — |
| 1920 | W. H. Corley | Foreman of Works; Marine Board Surveyor | Works Department | — | — |
| 1921 | W. H. Corley | Marine Board Surveyor | Works Department | — | — |

### Deterministic checks: `corley_walter-henry_e1876` vs `Corley, W. H___Fiji___1917`

- [PASS] surname_gate: bio 'CORLEY' vs stint 'Corley, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1921
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

