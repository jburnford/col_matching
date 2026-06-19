<!-- {"case_id": "case_docker_e-b_e1884-2", "bio_ids": ["docker_e-b_e1884-2"], "stint_ids": ["Docker, Ernest Brougham___New South Wales___1877"]} -->
# Dossier case_docker_e-b_e1884-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Docker, Ernest Brougham___New South Wales___1877` is also gate-compatible with biography(ies) outside this case: ['docker_e-b_e1884'] (already linked elsewhere or filtered).

## Biography `docker_e-b_e1884-2`

- Printed name: **DOCKER, E. B**
- Birth year: not printed
- Appears in editions: [1898, 1899, 1900, 1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1898-L33103.v` — printed in editions [1898, 1899, 1900, 1905, 1906]:**

> DOCKER, E. B.—Dist. court judge, N. S. Wales, June, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884 | Dist. court judge, N. S. Wales | Nova Scotia | [1898, 1899, 1900, 1905, 1906] |

## Candidate stint `Docker, Ernest Brougham___New South Wales___1877`

- Staff-list name: **Docker, Ernest Brougham** | colony: **New South Wales** | listed 1877–1917 | editions [1877, 1878, 1879, 1880, 1886, 1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. B. Docker | Crown Prosecutors | Attorney-General's Department | — | — |
| 1878 | E. B. Docker | Crown Prosecutors | Attorney-General's Department | — | — |
| 1879 | E. B. Docker | — | Attorney-General's Department | — | — |
| 1880 | E. B. Docker | Crown Prosecutors | Attorney-General's Department | — | — |
| 1886 | Ernest Brougaam Docker | District Court Judge (Western District) | Judicial and Legal Departments | — | — |
| 1888 | Ernest Brougham Docker | District Court Judge | Judicial and Legal Departments | — | — |
| 1889 | Ernest Brougham Docker | District Court Judge, Chairman of Quarter Sessions, Western District | Judicial and Legal Department | — | — |
| 1894 | Ernest Brougham Docker | District Court Judge, Western District | District Court Judges, and Chairmen of Quarter Sessions | — | — |
| 1896 | Ernest Brougham Docker | District Court Judge | Department of Justice and Subordinate Departments. | — | — |
| 1897 | Ernest Brougham Docker | District Court Judge, Western District | District Court Judges and Chairmen of Quarter Sessions. | — | — |
| 1898 | Ernest Brougham Docker | Western District | District Court Judges, and Chairmen of Quarter Sessions | — | — |
| 1899 | Ernest Brougham Docker | Western District | District Court Judges, and Chairmen of Quarter Sessions | — | — |
| 1900 | Ernest Brougham Docker | Western District | District Court Judges, and Chairmen of Quarter Sessions | — | — |
| 1905 | Ernest Brougham Docker | District Court Judge | Department of the Attorney-General and of Justice. | — | — |
| 1906 | Ernest Brougham Docker | District Court Judge | Department of the Attorney-General and of Justice | — | — |
| 1917 | E. B. Docker | Metropolitan District Judge | District Court Judges, and Chairmen of Quarter Sessions | — | — |

### Deterministic checks: `docker_e-b_e1884-2` vs `Docker, Ernest Brougham___New South Wales___1877`

- [PASS] surname_gate: bio 'DOCKER' vs stint 'Docker, Ernest Brougham' (exact)
- [PASS] initials: bio ['E', 'B'] ~ stint ['E', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1917
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

