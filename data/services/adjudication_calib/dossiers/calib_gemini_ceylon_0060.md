<!-- {"case_id": "calib_gemini_ceylon_0060", "bio_ids": ["harward_john_e1892"], "stint_ids": ["Harward, J___Ceylon___1894"]} -->
# Dossier calib_gemini_ceylon_0060

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['harward_john_e1892'] carry a single initial only — the namesake trap applies.

## Biography `harward_john_e1892`

- Printed name: **HARWARD, JOHN**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1914-L47014.v` — printed in editions [1914, 1915]:**

> HARWARD, JOHN.—Principal, Royal Coll., Ceylon, 1st Apr., 1892; dir. of pub. instrn., 23rd June, 1903; designation of office changed to dir. of educn., Aug., 1913.

**Version `col1910-L46347.v` — printed in editions [1910]:**

> HARWOOD, JOHN.—Principal, Royal Coll., Ceylon, 1st Apr., 1892; dir. of pub. instrn., 25th June, 1903.

**Version `col1905-L43711.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1911, 1912, 1913]:**

> HARWARD, JOHN.—Principal, Royal Coll., Ceylon, 1st Apl., 1892; dir. of pub. instrn., 23rd June, 1903.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892 | Principal, Royal Coll. | Ceylon | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 1 | 1903 | dir. of pub. instrn | Ceylon *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 2 | 1913 | designation of office changed to dir. of educn | Ceylon *(inherited from previous clause)* | [1914, 1915] |

## Candidate stint `Harward, J___Ceylon___1894`

- Staff-list name: **Harward, J** | colony: **Ceylon** | listed 1894–1915 | editions [1894, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | J. Harward | Principal of the Royal College | Department of Public Instruction | — | — |
| 1896 | J. Harward | Principal of the Royal College | Public Instruction | — | — |
| 1898 | J. Harward | Principal of the Royal College | Department of Public Instruction | — | — |
| 1899 | J. Harward | Principal of the Royal College | Public Instructor | — | — |
| 1900 | J. Harward | Principal of the Royal College | Department of Public Instruction | — | — |
| 1905 | J. Harward | Director | Department of Public Instruction | — | — |
| 1906 | J. Harward | Director | Department of Public Instruction | — | — |
| 1907 | J. Harward | Director | Department of Public Instruction | — | — |
| 1908 | J. Harward | Director | Department of Public Instruction | — | — |
| 1909 | J. Harward | Director | Department of Public Instruction | — | — |
| 1910 | J. Harward | Director | Department of Public Instruction | — | — |
| 1911 | J. Harward | Director | Department of Public Instruction | — | — |
| 1912 | J. Harward | Director | Department of Public Instruction | — | — |
| 1913 | J. Harward | Director | Department of Public Instruction | — | — |
| 1914 | J. Harward | Director | Education Department | — | — |
| 1915 | J. Harward | Director | Education Department | — | — |

### Deterministic checks: `harward_john_e1892` vs `Harward, J___Ceylon___1894`

- [PASS] surname_gate: bio 'HARWARD' vs stint 'Harward, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1894-1915
- [PASS] position_sim: best 100 vs bar 60: 'dir. of pub. instrn' ~ 'Director'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 11 agreeing edition-year(s) [1905, 1906, 1907, 1908, 1909, 1910] pos~100 (bar: >=2)
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

