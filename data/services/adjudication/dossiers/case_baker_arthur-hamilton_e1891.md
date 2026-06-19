<!-- {"case_id": "case_baker_arthur-hamilton_e1891", "bio_ids": ["baker_arthur-hamilton_e1891"], "stint_ids": ["Baker, A. H___British Guiana___1894", "Baker, A. H___Falkland Islands___1961"]} -->
# Dossier case_baker_arthur-hamilton_e1891

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 91 official(s) with this surname in the graph's staff lists; 52 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `baker_arthur-hamilton_e1891`

- Printed name: **BAKER, ARTHUR HAMILTON**
- Birth year: not printed
- Appears in editions: [1915]

### Verbatim printed entry text (OCR)

**Version `col1915-L45010.v` — printed in editions [1915]:**

> BAKER, ARTHUR HAMILTON.—Ag. sub-inspr. of police, B. Guiana, Oct., 1891; sub-inspr., Oct., 1892; ag. dist. inspr., June, 1894; dist. inspr., Dec., 1895; ag. county inspr., Mar., 1900; county inspr., Apr., 1903; ag. deputy inspr.-gen. and inspr. of prisons, Dec., 1909; county inspr., Apr., 1910; ag. deputy inspr.-gen. and supt. of Georgetown fire brigade, Mar., 1914; sen. inspr. of constabulary and supt. of Port-of-Spain fire brigade, Trinidad, 7th July, 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | Ag. sub-inspr. of police, B. Guiana | — | [1915] |
| 1 | 1892 | sub-inspr | — | [1915] |
| 2 | 1894 | ag. dist. inspr | — | [1915] |
| 3 | 1895 | dist. inspr | — | [1915] |
| 4 | 1900 | ag. county inspr | — | [1915] |
| 5 | 1903 | county inspr | — | [1915] |
| 6 | 1909 | ag. deputy inspr.-gen. and inspr. of prisons | — | [1915] |
| 7 | 1910 | county inspr | — | [1915] |
| 8 | 1914 | ag. deputy inspr.-gen. and supt. of Georgetown fire brigade | — | [1915] |
| 9 | 1914 | sen. inspr. of constabulary and supt. of Port-of-Spain fire brigade | Trinidad | [1915] |

## Candidate stint `Baker, A. H___British Guiana___1894`

- Staff-list name: **Baker, A. H** | colony: **British Guiana** | listed 1894–1914 | editions [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1911, 1912, 1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | A. H. Baker | Sub-Inspector | Police | — | — |
| 1896 | A. H. Baker | Sub-Inspectors | Police | — | — |
| 1897 | A. H. Baker | District Inspector | Police | — | — |
| 1898 | A. H. Baker | District Inspector | Police | — | — |
| 1899 | A. H. Baker | District Inspector | Police | — | — |
| 1900 | A. H. Baker | District Inspector | Police | — | — |
| 1905 | A. H. Baker | County Inspector | Police | — | — |
| 1906 | A. H. Baker | County Inspector | Police | — | — |
| 1907 | A. H. Baker | County Inspector | Police | — | — |
| 1908 | A. H. Baker | County Inspector | Police | — | — |
| 1909 | A. H. Baker | County Inspector | Police | — | — |
| 1911 | A. H. Baker | County Inspectors | Police | — | — |
| 1912 | A. H. Baker | County Inspector | Police | — | — |
| 1913 | A. H. Baker | County Inspector | Police | — | — |
| 1914 | A. H. Baker | County Inspector | Police | — | — |

### Deterministic checks: `baker_arthur-hamilton_e1891` vs `Baker, A. H___British Guiana___1894`

- [PASS] surname_gate: bio 'BAKER' vs stint 'Baker, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1914
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Baker, A. H___Falkland Islands___1961`

- Staff-list name: **Baker, A. H** | colony: **Falkland Islands** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | A. H. Baker | Chief Constable | Civil Establishment | — | — |
| 1962 | A. H. Baker | Chief Constable | Civil Establishment | — | — |

### Deterministic checks: `baker_arthur-hamilton_e1891` vs `Baker, A. H___Falkland Islands___1961`

- [PASS] surname_gate: bio 'BAKER' vs stint 'Baker, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1961; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
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

