<!-- {"case_id": "case_real_patrick_b1847", "bio_ids": ["real_patrick_b1847"], "stint_ids": ["Real, P___Australia___1912", "Real, P___Queensland___1894"]} -->
# Dossier case_real_patrick_b1847

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['real_patrick_b1847'] carry a single initial only — the namesake trap applies.

## Biography `real_patrick_b1847`

- Printed name: **REAL, PATRICK**
- Birth year: 1847 (attested in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922])
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Verbatim printed entry text (OCR)

**Version `col1908-L46918.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]:**

> REAL, HON. PATRICK.—B. 1847; called to the bar, Queensland, 1874; frequently acted as dist. ct. judge, and for some years was Crown proscr. in cent. dist.; mem. of Royal coman. on establishment of a Queensland Univ., 1891; judge of sup. ct., Queensland, 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | called to the bar | Queensland | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922] |
| 1 | 1890 | judge of sup. ct. | Queensland | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922] |
| 2 | 1891 | mem. of Royal coman. on establishment of a Queensland Univ | Queensland *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922] |

## Candidate stint `Real, P___Australia___1912`

- Staff-list name: **Real, P** | colony: **Australia** | listed 1912–1918 | editions [1912, 1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | P. Real | Senior Puisne Judge | Supreme Court Bench | — | — |
| 1913 | P. Real | Senior Puisne Judge | Supreme Court Bench | — | — |
| 1918 | P. Real | Senior Puisne Judge | Supreme Court Bench | — | — |

### Deterministic checks: `real_patrick_b1847` vs `Real, P___Australia___1912`

- [PASS] surname_gate: bio 'REAL' vs stint 'Real, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1912, birth 1847 (age 65)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Real, P___Queensland___1894`

- Staff-list name: **Real, P** | colony: **Queensland** | listed 1894–1917 | editions [1894, 1896, 1897, 1899, 1905, 1906, 1907, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | P. Real | 2nd Puisne Judge | Department of Justice | — | — |
| 1896 | P. Real | 2nd Judge | Department of Justice | — | — |
| 1897 | P. Real | 2nd Puisne Judge | Supreme Court Bench | — | — |
| 1899 | P. Real | 2nd puisne Judge | Supreme Court Bench | — | — |
| 1905 | P. Real | Senior Puisne Judge | Supreme Court Bench | — | — |
| 1906 | P. Real | Senior Puisne Judge | Supreme Court Bench | — | — |
| 1907 | P. Real | Senior Puisne Judge | Supreme Court Bench | — | — |
| 1917 | P. Real | Senior Puisne Judge | Supreme Court Bench | — | — |

### Deterministic checks: `real_patrick_b1847` vs `Real, P___Queensland___1894`

- [PASS] surname_gate: bio 'REAL' vs stint 'Real, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1894, birth 1847 (age 47)
- [PASS] colony: 3 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1894-1917
- [FAIL] position_sim: best 25 vs bar 60: 'mem. of Royal coman. on establishment of a Queensland Univ' ~ 'Senior Puisne Judge'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

