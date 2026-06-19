<!-- {"case_id": "case_de-silva_walwin-arnold_b1905", "bio_ids": ["de-silva_walwin-arnold_b1905"], "stint_ids": ["de Silva, W. A___Ceylon___1927"]} -->
# Dossier case_de-silva_walwin-arnold_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-silva_walwin-arnold_b1905`

- Printed name: **DE SILVA, Walwin Arnold**
- Birth year: 1905 (attested in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1929-L59608.v` — printed in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> DE SILVA, Walwin Arnold, B.Sc. (Lond.)—B. 1905; cadet, Ceylon civ. serv., Dec., 1927; astt., Kegalle kach., Jan. and Sept., 1928; astt., Jaffna kach., June, 1928; astt., Kegalle kach., Sept., 1928; astt., Matara kach., Nov., 1928; office astt., Galle kach., Oct., 1932; astt. govt. agt., Badulla, Dec., 1934; astt. comnr. of lands, Apr., 1936; sec., min. for commuens, and works, Aug., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | cadet, Ceylon civ. serv | Ceylon | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1928 | astt., Kegalle kach., Jan. and | Ceylon *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1932 | office astt., Galle kach | Ceylon *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1934 | astt. govt. agt., Badulla | Ceylon *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1936 | astt. comnr. of lands | Ceylon *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1937 | sec., min. for commuens, and works | Ceylon *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `de Silva, W. A___Ceylon___1927`

- Staff-list name: **de Silva, W. A** | colony: **Ceylon** | listed 1927–1940 | editions [1927, 1929, 1931, 1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | W. de Silva | 1st Grade Medical Officer | Medical Department | — | — |
| 1929 | W. A. de Silva | Office Assistant | PROVINCE OF SABARAGAMUWA | — | — |
| 1931 | W. A. de Silva | Office Assistant | Government Agencies | — | — |
| 1934 | W. A. de Silva | Office Assistant | Southern Province | — | — |
| 1934 | W. A. de Silva | — | Local Administration | — | — |
| 1936 | W. A. de Silva | Assistant Government Agent (Land) | PROVINCE OF UVA | — | — |
| 1936 | W. A. de Silva | — | Local Administration | — | — |
| 1936 | W. A. de Silva | Assistant Irrigation Engineer | Irrigation Department | — | — |
| 1937 | W. A. de Silva | Assistant Irrigation Engineer | Irrigation Department | — | — |
| 1937 | W. A. de Silva | Assistant Land Commissioner | Land Commissioner's Office | — | — |
| 1940 | W. A. de Silva | Irrigation Engineer | Irrigation Department | — | — |

### Deterministic checks: `de-silva_walwin-arnold_b1905` vs `de Silva, W. A___Ceylon___1927`

- [PASS] surname_gate: bio 'DE SILVA' vs stint 'de Silva, W. A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1927, birth 1905 (age 22)
- [PASS] colony: 6 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 6 event tenure(s) overlap stint years 1927-1940
- [PASS] position_sim: best 65 vs bar 60: 'astt. comnr. of lands' ~ 'Assistant Land Commissioner'
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

