<!-- {"case_id": "case_farrell_gerald-hildebrand_b1891", "bio_ids": ["farrell_gerald-hildebrand_b1891"], "stint_ids": ["Farrell, G. H___Ceylon___1912", "Farrell, G. H___Nigeria___1927"]} -->
# Dossier case_farrell_gerald-hildebrand_b1891

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `farrell_gerald-hildebrand_b1891`

- Printed name: **FARRELL, GERALD HILDEBRAND**
- Birth year: 1891 (attested in editions [1939])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L66648.v` — printed in editions [1939]:**

> FARRELL, GERALD HILDEBRAND.—B. 1891; ed. abroad and Cranbrook Sch.; Ceylon pol., 1911; N. Nigeria pol., 1914; attd. Nigeria Regiment, 1917-18; Nigeria pol., 1930; ag. asst. inspr. gen., various periods 1931-34 and 1936; ag. dep. do., 1935-36; senr. supt., pol., 1936; ag. asst. commr., various periods 1937-38.

**Version `col1940-L64164.v` — printed in editions [1940]:**

> FARRELLI, GERALD HILDEBRAND.—B. 1891; ed. abroad and Cranbrook Schl.; Ceylon pol., 1911; N. Nigeria pol., 1914; attd. Nigeria Regiment, 1917-18; Nigeria pol., 1930; ag. astt. inspr. gen., various periods 1931-34 and 1936; ag. dep. do., 1935-36; senr. supt., pol., 1936; ag. astt. commr., various periods 1937-38.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911–1911 | pol. | Ceylon | [1939, 1940] |
| 1 | 1914–1914 | pol. | Northern Nigeria | [1939, 1940] |
| 2 | 1917–1918 | attd. Nigeria Regiment | Nigeria | [1939, 1940] |
| 3 | 1930–1930 | pol. | Nigeria | [1939, 1940] |
| 4 | 1931–1936 | ag. asst. inspr. gen. | — | [1939, 1940] |
| 5 | 1935–1936 | ag. dep. do. | — | [1939, 1940] |
| 6 | 1936–1936 | senr. supt., pol. | — | [1939, 1940] |
| 7 | 1937–1938 | ag. asst. commr. | — | [1939, 1940] |

## Candidate stint `Farrell, G. H___Ceylon___1912`

- Staff-list name: **Farrell, G. H** | colony: **Ceylon** | listed 1912–1914 | editions [1912, 1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | G. H. Farrell | Probationer | Police | — | — |
| 1913 | G. H. Farrell | Probationer | Police | — | — |
| 1914 | G. H. Farrell | Probationer | Police | — | — |

### Deterministic checks: `farrell_gerald-hildebrand_b1891` vs `Farrell, G. H___Ceylon___1912`

- [PASS] surname_gate: bio 'FARRELL' vs stint 'Farrell, G. H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1912, birth 1891 (age 21)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1912-1914
- [FAIL] position_sim: best 29 vs bar 60: 'pol.' ~ 'Probationer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Farrell, G. H___Nigeria___1927`

- Staff-list name: **Farrell, G. H** | colony: **Nigeria** | listed 1927–1939 | editions [1927, 1929, 1930, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | G. H. Farrell | Commissioner | Police, Northern Provinces | — | Lieutenant |
| 1929 | Lieut. G. H. Farrell | Commissioners and Assistant Commissioners | Marine | M.C., D.S.O., M.C., D.S.O., M.C., D.C.M., M.C. | — |
| 1930 | Lieut. G. H. Farrell | Commissioners and Assistant Commissioners | Police | — | — |
| 1933 | G. H. Farrell | Commissioner/Assistant Commissioner | Police | — | — |
| 1934 | G. H. Farrell | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | G. H. Farrell | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | G. H. Farrell | Senior Superintendent of Police | Police | — | — |

### Deterministic checks: `farrell_gerald-hildebrand_b1891` vs `Farrell, G. H___Nigeria___1927`

- [PASS] surname_gate: bio 'FARRELL' vs stint 'Farrell, G. H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1927, birth 1891 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1939
- [FAIL] position_sim: best 18 vs bar 60: 'pol.' ~ 'Senior Superintendent of Police'
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

