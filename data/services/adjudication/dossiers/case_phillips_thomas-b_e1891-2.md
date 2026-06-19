<!-- {"case_id": "case_phillips_thomas-b_e1891-2", "bio_ids": ["phillips_thomas-b_e1891-2"], "stint_ids": ["Phillips, T. B___British Honduras___1894", "Phillips, T. B___Nigeria___1915"]} -->
# Dossier case_phillips_thomas-b_e1891-2

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 119 official(s) with this surname in the graph's staff lists; 54 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `phillips_thomas-b_e1891-2`

- Printed name: **PHILLIPS, THOMAS B**
- Birth year: not printed
- Appears in editions: [1914, 1915, 1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1914-L49166.v` — printed in editions [1914, 1915, 1917, 1918, 1919]:**

> PHILLIPS, THOMAS B.—Served in treasy., secretariat, customs, and post office, British Honduras, 1891 to 1900; assist. treas., N. Nigeria, 2nd Aug., 1900; has acted on several occasions as chief ass't. treas. and treas.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891–1900 | Served in treasy., secretariat, customs, and post office | British Honduras | [1914, 1915, 1917, 1918, 1919] |
| 1 | 1900 | assist. treas., N. Nigeria | British Honduras *(inherited from previous clause)* | [1914, 1915, 1917, 1918, 1919] |

## Candidate stint `Phillips, T. B___British Honduras___1894`

- Staff-list name: **Phillips, T. B** | colony: **British Honduras** | listed 1894–1900 | editions [1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | T. B. Phillips | 3rd and Registry Clerk | Colonial Secretary's Department | — | — |
| 1896 | T. B. Phillips | Third Clerk | Treasury and Customs Department, &c. | — | — |
| 1897 | T. B. Phillips | Third Clerk | Treasury and Customs Department, &c. | — | — |
| 1898 | T. B. Phillips | 3rd Clerk | Colonial Secretary's Department | — | — |
| 1899 | T. B. Phillips | 2nd Clerk | Colonial Secretary's Department | — | — |
| 1900 | T. B. Phillips | 2nd Clerk | Colonial Secretary's Department | — | — |

### Deterministic checks: `phillips_thomas-b_e1891-2` vs `Phillips, T. B___British Honduras___1894`

- [PASS] surname_gate: bio 'PHILLIPS' vs stint 'Phillips, T. B' (exact)
- [PASS] initials: bio ['T', 'B'] ~ stint ['T', 'B']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'British Honduras'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1894-1900
- [FAIL] position_sim: best 41 vs bar 60: 'assist. treas., N. Nigeria' ~ '3rd and Registry Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Phillips, T. B___Nigeria___1915`

- Staff-list name: **Phillips, T. B** | colony: **Nigeria** | listed 1915–1920 | editions [1915, 1917, 1918, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | T. B. Phillips | Treasury Assistant, 1st Grade | Treasury | — | — |
| 1917 | T. B. Phillips | Treasury Assistant, 1st Grade | Treasury | — | — |
| 1918 | T. B. Phillips | Treasury Assistant, 1st Grade | Treasury | — | — |
| 1920 | T. B. Phillips | Treasury Assistant, 1st Grade | Treasury | — | — |

### Deterministic checks: `phillips_thomas-b_e1891-2` vs `Phillips, T. B___Nigeria___1915`

- [PASS] surname_gate: bio 'PHILLIPS' vs stint 'Phillips, T. B' (exact)
- [PASS] initials: bio ['T', 'B'] ~ stint ['T', 'B']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1920
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

