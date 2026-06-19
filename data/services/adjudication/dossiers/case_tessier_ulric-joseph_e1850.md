<!-- {"case_id": "case_tessier_ulric-joseph_e1850", "bio_ids": ["tessier_ulric-joseph_e1850"], "stint_ids": ["Tessier, Jules___Canada___1900", "Tessier, Ulric J___Canada___1877"]} -->
# Dossier case_tessier_ulric-joseph_e1850

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tessier_ulric-joseph_e1850`

- Printed name: **TESSIER, Ulric Joseph**
- Birth year: not printed
- Appears in editions: [1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L35934.v` — printed in editions [1889, 1890]:**

> TESSIER, Ulric Joseph, I.L.D.—Justice, Court of Queen's Bench and Appeal Province Quebec, 1873; he was mayor of his native city, Quebec, in 1851; sat in the Canadian Parliament for the county of Portneuf, 1850-53; afterwards in the legislative council, 1859-66; was a member of the provincial cabinet in 1861 and 1862; president of the legislative council from 1859 to 1866, when the confederation was proclaimed; was then appointed one of the senators of the Dominion, which position he held until he was named a judge of the superior court; he has been since 1871 dean of the law faculty of the Laval university.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1850–1853 | sat in the Canadian Parliament for the county of Portneuf | Canada | [1889, 1890] |
| 1 | 1851–1851 | mayor | Quebec | [1889, 1890] |
| 2 | 1859–1866 | member of the legislative council | — | [1889, 1890] |
| 3 | 1861–1862 | member of the provincial cabinet | — | [1889, 1890] |
| 4 | 1871 | dean of the law faculty of the Laval university | — | [1889, 1890] |
| 5 | 1873 | Justice, Court of Queen's Bench and Appeal | Quebec | [1889, 1890] |

## Candidate stint `Tessier, Jules___Canada___1900`

- Staff-list name: **Tessier, Jules** | colony: **Canada** | listed 1900–1922 | editions [1900, 1905, 1907, 1908, 1913, 1914, 1915, 1917, 1918, 1919, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | Hon. Jules Tessier | Speaker | Legislative Assembly | — | — |
| 1905 | Jules Tessier | Senator | Senate of Canada | — | — |
| 1907 | Jules Tessier | Senator | Senate | — | — |
| 1908 | Jules Tessier | Senator | Senate of Canada | — | — |
| 1913 | Jules Tessier | Senator | Senate | — | — |
| 1914 | Jules Tessier | Senator | Senate of Canada | — | — |
| 1915 | Jules Tessier | — | Senate | — | — |
| 1917 | Hon. J. A. Tessier | Roads Department | Executive Council | — | — |
| 1918 | Jules Tessier | Senator | Senate | — | — |
| 1918 | J. A. Tessier | Roads Department | Executive Council | — | — |
| 1919 | J. A. Tessier | Roads Department | Executive Council | — | — |
| 1922 | Jules Tessier | Senator | Senators | — | — |

### Deterministic checks: `tessier_ulric-joseph_e1850` vs `Tessier, Jules___Canada___1900`

- [PASS] surname_gate: bio 'TESSIER' vs stint 'Tessier, Jules' (exact)
- [PASS] initials: bio ['U', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1900; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1922
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Tessier, Ulric J___Canada___1877`

- Staff-list name: **Tessier, Ulric J** | colony: **Canada** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | U. J. Tessier | Puisne Judge, Queen's Bench | Judicial and Legal Departments | — | — |
| 1878 | U. J. Tessier | Puisne Judges, Queen's Bench | JUDICIAL AND LEGAL DEPARTMENTS | — | — |

### Deterministic checks: `tessier_ulric-joseph_e1850` vs `Tessier, Ulric J___Canada___1877`

- [PASS] surname_gate: bio 'TESSIER' vs stint 'Tessier, Ulric J' (exact)
- [PASS] initials: bio ['U', 'J'] ~ stint ['U', 'J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
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

