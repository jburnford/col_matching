<!-- {"case_id": "case_ross_david-alexander_e1848", "bio_ids": ["ross_david-alexander_e1848"], "stint_ids": ["Ross, Donald A___Canada___1905"]} -->
# Dossier case_ross_david-alexander_e1848

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 140 official(s) with this surname in the graph's staff lists; 64 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ross_david-alexander_e1848`

- Printed name: **ROSS, DAVID ALEXANDER**
- Birth year: not printed
- Honours: Q.C. (1873)
- Appears in editions: [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1889-L35424.v` — printed in editions [1889, 1890, 1894, 1896, 1897]:**

> ROSS, DAVID ALEXANDER.—Admitted to the bar, Quebec, 1848; Q.C., 1873; in 1878-9 member legislative assembly for county of Quebec; member of the executive council, attorney-general, and in 1887-8 member legislative council, and member executive council (without portfolio).

**Version `col1898-L35683.v` — printed in editions [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]:**

> ROSS, DAVID ALEXANDER.—Admitted to the bar, Quebec, 1884; Q.C., 1873; in 1878-9 mem. legis. assem. for co. of Quebec; mem. of the exec. coun., atty.-gen., and in 1887-8, mem. legis. coun.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1848–1848 | Admitted to the bar | Quebec | [1889, 1890, 1894, 1896, 1897] |
| 1 | 1873–1873 | Q.C. | — | [1889, 1890, 1894, 1896, 1897] |
| 2 | 1878–1879 | member legislative assembly for county of Quebec | Quebec | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 3 | 1884–1884 | Admitted to the bar | Quebec | [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 4 | 1887–1888 | member legislative council, and member executive council (without portfolio) | — | [1889, 1890, 1894, 1896, 1897] |
| 5 | 1887–1888 | mem. legis. coun. | — | [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |

## Candidate stint `Ross, Donald A___Canada___1905`

- Staff-list name: **Ross, Donald A** | colony: **Canada** | listed 1905–1915 | editions [1905, 1906, 1907, 1908, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | Duncan Ross | — | — | — | — |
| 1906 | Duncan Ross | — | — | — | — |
| 1907 | Duncan Ross | — | British Columbia | — | — |
| 1908 | D. A. Ross | Member | Legislative Assembly | — | — |
| 1908 | Duncan Ross | — | — | — | — |
| 1913 | D. A. Ross | Member of Legislative Assembly | Members | — | — |
| 1914 | D. A. Ross | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1915 | Donald A. Ross | Member for St. Clements | — | — | — |

### Deterministic checks: `ross_david-alexander_e1848` vs `Ross, Donald A___Canada___1905`

- [PASS] surname_gate: bio 'ROSS' vs stint 'Ross, Donald A' (exact)
- [PASS] initials: bio ['D', 'A'] ~ stint ['D', 'A']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1915
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

