<!-- {"case_id": "case_ingleby_john_e1868", "bio_ids": ["ingleby_john_e1868"], "stint_ids": ["Ingleby, J___Ceylon___1878"]} -->
# Dossier case_ingleby_john_e1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['ingleby_john_e1868'] carry a single initial only — the namesake trap applies.

## Biography `ingleby_john_e1868`

- Printed name: **INGLEBY, John**
- Birth year: not printed
- Appears in editions: [1889, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1889-L33877.v` — printed in editions [1889, 1894, 1896, 1897, 1898]:**

> INGLEBY, John.—Articled to John Eddison, Leeds, 1868; assistant to the borough engineer, Leeds, Sept., 1872; appointed to the surveyor-general's department, Ceylon, Aug., 1875; district surveyor, Jan., 1877; and chief surveyor, North and North Central Provinces, Aug., 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1868 | Articled to John Eddison, Leeds | — | [1889, 1894, 1896, 1897, 1898] |
| 1 | 1872 | assistant to the borough engineer, Leeds | — | [1889, 1894, 1896, 1897, 1898] |
| 2 | 1875 | appointed to the surveyor-general's department | Ceylon | [1889, 1894, 1896, 1897, 1898] |
| 3 | 1877 | district surveyor | Ceylon *(inherited from previous clause)* | [1889, 1894, 1896, 1897, 1898] |
| 4 | 1886 | and chief surveyor, North and North Central Provinces | Ceylon *(inherited from previous clause)* | [1889, 1894, 1896, 1897, 1898] |

## Candidate stint `Ingleby, J___Ceylon___1878`

- Staff-list name: **Ingleby, J** | colony: **Ceylon** | listed 1878–1888 | editions [1878, 1879, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | J. Ingleby | District Surveyor | Survey Department | — | — |
| 1879 | J. Ingleby | District Surveyor | District Surveyors | — | — |
| 1883 | J. Ingleby | District Surveyor | Survey Department | — | — |
| 1886 | J. Ingleby | District Surveyor | Survey Department | — | — |
| 1888 | J. Ingleby | 5th Chief Surveyor | Survey Department | — | — |

### Deterministic checks: `ingleby_john_e1868` vs `Ingleby, J___Ceylon___1878`

- [PASS] surname_gate: bio 'INGLEBY' vs stint 'Ingleby, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1878-1888
- [PASS] position_sim: best 100 vs bar 60: 'district surveyor' ~ 'District Surveyor'
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

