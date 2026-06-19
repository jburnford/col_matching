<!-- {"case_id": "case_wendt_henry-lorenz_e1895", "bio_ids": ["wendt_henry-lorenz_e1895"], "stint_ids": ["Wendt, H. L___Ceylon___1905", "Wendt, H. L___Ceylon___1936"]} -->
# Dossier case_wendt_henry-lorenz_e1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wendt_henry-lorenz_e1895`

- Printed name: **WENDT, HENRY LORENZ**
- Birth year: not printed
- Appears in editions: [1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1899-L37862.v` — printed in editions [1899, 1900]:**

> WENDT, HENRY LORENZ.—Mem. of legis. coun., Ceylon, 1895; advce. of sup. ct.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | Mem. of legis. coun. | Ceylon | [1899, 1900] |

## Candidate stint `Wendt, H. L___Ceylon___1905`

- Staff-list name: **Wendt, H. L** | colony: **Ceylon** | listed 1905–1911 | editions [1905, 1906, 1907, 1908, 1909, 1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. L. Wendt | Junior Puisne Judge | Judicial Establishment | — | — |
| 1906 | H. L. Wendt | Senior Puisne Judge | Judicial Establishment | — | — |
| 1907 | H. L. Wendt | Senior Puisne Judge | Judicial Establishment | — | — |
| 1908 | H. L. Wendt | Senior Puisne Judge | Judicial Establishment | — | — |
| 1909 | H. L. Wendt | Senior Puisne Judge | Judicial Establishment | — | — |
| 1910 | H. L. Wendt | Senior Puine Judge | Judicial Establishment | — | — |
| 1911 | H. L. Wendt | Senior Puisne Judge | Judicial Establishment | — | — |

### Deterministic checks: `wendt_henry-lorenz_e1895` vs `Wendt, H. L___Ceylon___1905`

- [PASS] surname_gate: bio 'WENDT' vs stint 'Wendt, H. L' (exact)
- [PASS] initials: bio ['H', 'L'] ~ stint ['H', 'L']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1911
- [FAIL] position_sim: best 39 vs bar 60: 'Mem. of legis. coun.' ~ 'Senior Puisne Judge'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Wendt, H. L___Ceylon___1936`

- Staff-list name: **Wendt, H. L** | colony: **Ceylon** | listed 1936–1940 | editions [1936, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | H. L. Wendt | Crown Counsel | Crown Counsel | — | — |
| 1940 | H. L. Wendt | Second Assistant Legal Draftsman | Legal Draftsman's Department | — | — |

### Deterministic checks: `wendt_henry-lorenz_e1895` vs `Wendt, H. L___Ceylon___1936`

- [PASS] surname_gate: bio 'WENDT' vs stint 'Wendt, H. L' (exact)
- [PASS] initials: bio ['H', 'L'] ~ stint ['H', 'L']
- [PASS] age_gate: stint starts 1936; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

