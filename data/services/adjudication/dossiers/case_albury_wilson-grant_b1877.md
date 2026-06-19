<!-- {"case_id": "case_albury_wilson-grant_b1877", "bio_ids": ["albury_wilson-grant_b1877"], "stint_ids": ["Albury, William G___Bahamas___1918"]} -->
# Dossier case_albury_wilson-grant_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Albury, William G___Bahamas___1918` is also gate-compatible with biography(ies) outside this case: ['albury_wilton-grant_b1877'] (already linked elsewhere or filtered).

## Biography `albury_wilson-grant_b1877`

- Printed name: **ALBURY, WILSON GRANT**
- Birth year: 1877 (attested in editions [1927])
- Appears in editions: [1927]

### Verbatim printed entry text (OCR)

**Version `col1927-L56760.v` — printed in editions [1927]:**

> ALBURY, WILSON GRANT.—B. 1877; public school teacher, Bahamas, 1896; resigned, 1906; re-apttd., 1909; head-master, boys' central school, 1914; inspr. of schools, 1915; ag. S. and C. mag., 8th June to 5th July and from 17th July, 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | public school teacher | Bahamas | [1927] |
| 1 | 1906 | resigned | Bahamas *(inherited from previous clause)* | [1927] |
| 2 | 1909 | re-apttd | Bahamas *(inherited from previous clause)* | [1927] |
| 3 | 1914 | head-master, boys' central school | Bahamas *(inherited from previous clause)* | [1927] |
| 4 | 1915 | inspr. of schools | Bahamas *(inherited from previous clause)* | [1927] |
| 5 | 1926 | ag. S. and C. mag., 8th June to 5th July and from | Bahamas *(inherited from previous clause)* | [1927] |

## Candidate stint `Albury, William G___Bahamas___1918`

- Staff-list name: **Albury, William G** | colony: **Bahamas** | listed 1918–1940 | editions [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | W. G. Albury | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1919 | W. G. Albury | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1920 | W. G. Albury | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1921 | W. G. Albury | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1922 | W. G. Albury | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1923 | W. G. Albury | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1923 | W. G. Albury, junr. | Cadet | Colonial Secretary's Office | — | — |
| 1924 | W. G. Albury | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1924 | W. G. Albury | Cadet | Colonial Secretary's Office | — | — |
| 1925 | W. G. Albury, junr. | Cadets | Colonial Secretary's Office | — | — |
| 1925 | W. G. Albury | Inspector and General Superintendent of Schools | Education Department | — | — |
| 1927 | W. G. Albury | Inspector and General Superintendent | Educational Department | — | — |
| 1928 | William G. Albury | Inspector and General Superintendent | Educational Department | — | — |
| 1929 | W. G. Albury | Inspector and General Superintendent | Educational Department | — | — |
| 1930 | W. G. Albury | Inspector and General Superintendent | Educational Department | — | — |
| 1931 | W. G. Albury | Inspector and General Superintendent | Educational Department | — | — |
| 1932 | W. G. Albury | Inspector and General Superintendent | Educational Department | — | — |
| 1933 | W. G. Albury | Inspector and General Superintendent | Educational Department | — | — |
| 1934 | W. G. Albury | Inspector and General Superintendent | Educational Department | — | — |
| 1936 | W. G. Albury | Inspector and General Superintendent | Educational Department | — | — |
| 1937 | W. G. Albury | Inspector and General Superintendent | Educational Department | — | — |
| 1940 | W. G. Albury | Inspector and General Superintendent | Educational Department | — | — |

### Deterministic checks: `albury_wilson-grant_b1877` vs `Albury, William G___Bahamas___1918`

- [PASS] surname_gate: bio 'ALBURY' vs stint 'Albury, William G' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1918, birth 1877 (age 41)
- [PASS] colony: 6 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1918-1940
- [PASS] position_sim: best 77 vs bar 60: 'inspr. of schools' ~ 'Inspector and General Superintendent of Schools'
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

