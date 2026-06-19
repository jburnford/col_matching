<!-- {"case_id": "case_hamilton_fredrick-lindsay_b1891", "bio_ids": ["hamilton_fredrick-lindsay_b1891"], "stint_ids": ["Hamilton, F. L___Gold Coast___1927"]} -->
# Dossier case_hamilton_fredrick-lindsay_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 105 official(s) with this surname in the graph's staff lists; 44 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hamilton_fredrick-lindsay_b1891`

- Printed name: **HAMILTON, FREDRICK LINDSAY**
- Birth year: 1891 (attested in editions [1937, 1940])
- Appears in editions: [1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L61522.v` — printed in editions [1937, 1940]:**

> HAMILTON, MAJOR FREDRICK LINDSAY, M.C.—B. 1891; B.E.F., France, 1914-18; N. Russia, 1919-20; dist. inspnr., R.I.C., 1921; asst. commnr., pol., Gold Coast, June, 1921; commnr., 1927; ag. senr. commnr., pol., 1933-1934; title changed to supt., 1937; ag. dep. commr., Apr., 1937; ag. commr., Apr., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1918 | B.E.F., France | — | [1937, 1940] |
| 1 | 1919–1920 | N. Russia | — | [1937, 1940] |
| 2 | 1921 | dist. inspnr., R.I.C | — | [1937, 1940] |
| 3 | 1921 | asst. commnr., pol. | Gold Coast | [1937, 1940] |
| 4 | 1927 | commnr | Gold Coast *(inherited from previous clause)* | [1937, 1940] |
| 5 | 1933–1934 | ag. senr. commnr., pol | Gold Coast *(inherited from previous clause)* | [1937, 1940] |
| 6 | 1937 | title changed to supt | Gold Coast *(inherited from previous clause)* | [1937, 1940] |
| 7 | 1938 | ag. commr | Gold Coast *(inherited from previous clause)* | [1937, 1940] |

## Candidate stint `Hamilton, F. L___Gold Coast___1927`

- Staff-list name: **Hamilton, F. L** | colony: **Gold Coast** | listed 1927–1936 | editions [1927, 1928, 1929, 1930, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | F. L. Hamilton | Commissioner/Assistant Commissioner of Police | Police Department | — | Major |
| 1928 | Major F. L. Hamilton | Commissioners and Assistant Commissioners of Police | Police Department | — | Major |
| 1929 | F. L. Hamilton | Commissioners and Assistant Commissioners of Police | Police Department | — | Major |
| 1930 | Major F. L. Hamilton | Commissioners and Assistant Commissioners of Police | Police Department | — | Major |
| 1932 | Major F. L. Hamilton | Commissioners and Assistant Commissioners of Police | Police Department | — | Major |
| 1934 | Major F. L. Hamilton | Commissioners and Assistant Commissioners of Police | Police Department | — | Major |
| 1936 | F. L. Hamilton | Commissioners and Assistant Commissioners of Police | Police Department | — | Major |

### Deterministic checks: `hamilton_fredrick-lindsay_b1891` vs `Hamilton, F. L___Gold Coast___1927`

- [PASS] surname_gate: bio 'HAMILTON' vs stint 'Hamilton, F. L' (exact)
- [PASS] initials: bio ['F', 'L'] ~ stint ['F', 'L']
- [PASS] age_gate: stint starts 1927, birth 1891 (age 36)
- [PASS] colony: 5 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1927-1936
- [FAIL] position_sim: best 58 vs bar 60: 'asst. commnr., pol.' ~ 'Commissioners and Assistant Commissioners of Police'
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

