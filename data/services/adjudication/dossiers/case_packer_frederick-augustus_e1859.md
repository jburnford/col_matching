<!-- {"case_id": "case_packer_frederick-augustus_e1859", "bio_ids": ["packer_frederick-augustus_e1859"], "stint_ids": ["Packer, F. A___Tasmania___1888"]} -->
# Dossier case_packer_frederick-augustus_e1859

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `packer_frederick-augustus_e1859`

- Printed name: **PACKER, Frederick Augustus**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1888-L35386.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897]:**

> PACKER, Frederick Augustus.—Entered telegraph service, Tasmania, Jan., 1859; landing waiter, customs, Launceston, 1862; sessional clerk House of Assembly, 1862; clerk ordnance department, 1863; sessional clerk, legislative council, 1864, clerk R.E. department, 1865; chief clerk, telegraph department, 1866; superintendent of telegraphs, 1873; clerk assistant, House of Assembly, 1878; clerk of the House, and librarian to Parliament, 1882. Is a magistrate for the Colony.

**Version `col1898-L35275.v` — printed in editions [1898]:**

> PACKER, FREDERICK AUGUSTUS.—Entered telegraph service, Tasmania, Jan., 1859; landing waiter, customs, Launceston, 1862; sessional clk. house of assem., 1862; clk. ordnance dept., 1863; sessional clk., legis. coun., 1864; clk. R.E. dept., 1865; ch. clk., telegraph dept., 1866; supt. of telegraphs, 1873; clk. asst., house of assem., 1878; clk. of the house, and librarian to parlmt., 1882. Is a J.P. for the col.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1859 | telegraph service | Tasmania | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 1 | 1862 | landing waiter | Launceston | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 2 | 1862 | sessional clerk | — | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 3 | 1863 | clerk | — | [1888, 1889, 1890, 1894, 1896, 1897] |
| 4 | 1863 | clk. ordnance dept. | — | [1898] |
| 5 | 1864 | sessional clerk | — | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 6 | 1865 | clerk | — | [1888, 1889, 1890, 1894, 1896, 1897] |
| 7 | 1865 | clk. R.E. dept. | — | [1898] |
| 8 | 1866 | chief clerk | — | [1888, 1889, 1890, 1894, 1896, 1897] |
| 9 | 1866 | ch. clk., telegraph dept. | — | [1898] |
| 10 | 1873 | superintendent of telegraphs | — | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 11 | 1878 | clerk assistant | — | [1888, 1889, 1890, 1894, 1896, 1897] |
| 12 | 1878 | clk. asst., house of assem. | — | [1898] |
| 13 | 1882 | clerk of the House, and librarian to Parliament | — | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |

## Candidate stint `Packer, F. A___Tasmania___1888`

- Staff-list name: **Packer, F. A** | colony: **Tasmania** | listed 1888–1894 | editions [1888, 1889, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | F. A. Packer | Clerk to the House and Librarian | House of Assembly | — | — |
| 1889 | F. A. Packer | Clerk to the House and Librarian | House of Assembly | — | — |
| 1894 | Packer, F. A. | Clerk to the House and Librarian | House of Assembly | — | — |

### Deterministic checks: `packer_frederick-augustus_e1859` vs `Packer, F. A___Tasmania___1888`

- [PASS] surname_gate: bio 'PACKER' vs stint 'Packer, F. A' (exact)
- [PASS] initials: bio ['F', 'A'] ~ stint ['F', 'A']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tasmania'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1894
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

