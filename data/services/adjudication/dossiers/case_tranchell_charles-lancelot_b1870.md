<!-- {"case_id": "case_tranchell_charles-lancelot_b1870", "bio_ids": ["tranchell_charles-lancelot_b1870"], "stint_ids": ["Tranchell, C. L___Ceylon___1894"]} -->
# Dossier case_tranchell_charles-lancelot_b1870

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tranchell_charles-lancelot_b1870`

- Printed name: **TRANCHELL, CHARLES LANCELOT**
- Birth year: 1870 (attested in editions [1920, 1921])
- Appears in editions: [1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1920-L57682.v` — printed in editions [1920, 1921]:**

> TRANCHELL, CHARLES LANCELOT.—B. 1870; asst. supt. of police, Ceylon, Aug., 1892; supt. of police, Sept., 1902; deputy inspr.-gen. of police (Provinces), Oct., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892 | asst. supt. of police | Ceylon | [1920, 1921] |
| 1 | 1902 | supt. of police | Ceylon *(inherited from previous clause)* | [1920, 1921] |
| 2 | 1918 | deputy inspr.-gen. of police (Provinces) | Ceylon *(inherited from previous clause)* | [1920, 1921] |

## Candidate stint `Tranchell, C. L___Ceylon___1894`

- Staff-list name: **Tranchell, C. L** | colony: **Ceylon** | listed 1894–1920 | editions [1894, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1915, 1917, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | C. L. Tranchell | Assistant Superintendent | Police | — | — |
| 1896 | C. L. Tranchell | Assistant Superintendent | Police | — | — |
| 1898 | C. L. Tranchell | Assistant Superintendent | Police and Prisons | — | — |
| 1899 | C. L. Tranchell | Assistant Superintendent | Police and Prisons | — | — |
| 1900 | C. L. Tranchell | Assistant Superintendent | Police and Prisons | — | — |
| 1905 | C. L. Tranchell | Superintendent | Police and Prisons | — | — |
| 1906 | C. L. Tranchell | Superintendent | Police | — | — |
| 1907 | C. L. Tranchell | Superintendent | Police | — | — |
| 1908 | C. L. Tranchell | Superintendent | Police | — | — |
| 1909 | C. L. Tranchell | Superintendent | Police | — | — |
| 1910 | C. L. Tranchell | Superintendent | Police | — | — |
| 1911 | C. L. Tranchell | Superintendent | Police | — | — |
| 1912 | C. L. Tranchell | Superintendent | Police | — | — |
| 1913 | C. L. Tranchell | Superintendent | Police | — | — |
| 1915 | C. L. Tranchell | Superintendent | Police | — | — |
| 1917 | C. L. Tranchell | Superintendent | Police | — | — |
| 1919 | C. L. Tranchell | Deputy Inspector-General | Police | — | — |
| 1920 | C. L. Tranchell | Deputy Inspector-General | Police | — | — |

### Deterministic checks: `tranchell_charles-lancelot_b1870` vs `Tranchell, C. L___Ceylon___1894`

- [PASS] surname_gate: bio 'TRANCHELL' vs stint 'Tranchell, C. L' (exact)
- [PASS] initials: bio ['C', 'L'] ~ stint ['C', 'L']
- [PASS] age_gate: stint starts 1894, birth 1870 (age 24)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1894-1920
- [FAIL] position_sim: best 59 vs bar 60: 'deputy inspr.-gen. of police (Provinces)' ~ 'Deputy Inspector-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1920] pos~59 (bar: >=2)
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

