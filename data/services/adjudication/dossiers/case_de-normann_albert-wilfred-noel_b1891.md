<!-- {"case_id": "case_de-normann_albert-wilfred-noel_b1891", "bio_ids": ["de-normann_albert-wilfred-noel_b1891"], "stint_ids": ["de Normann, A. W. N___Nigeria___1936"]} -->
# Dossier case_de-normann_albert-wilfred-noel_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-normann_albert-wilfred-noel_b1891`

- Printed name: **DE NORMANN, Albert Wilfred Noel**
- Birth year: 1891 (attested in editions [1932, 1933, 1937, 1939, 1940])
- Appears in editions: [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L59637.v` — printed in editions [1932, 1933, 1937, 1939, 1940]:**

> DE NORMANN, Capt. Albert Wilfred Noel.—B. 1891; ed. United Services Coll. and Chateau du Rosey, Switzerland; Canadian Exped. Force, 1914; lieut., Royal Fusiliers, 1915; West African Forces, 1916-20; survr., Nigeria survey, 1921; astt. survr.-gen., 1930; ag. survr.-gen., Apr., Sept., 1933; ag. comnr., lands and survr.-gen., Mar.-Sept., 1935 and Mar.-May, 1936; comnr., lands and survr.-gen., 1936; M.L.C.; chmn., Lagos exec. development bd., 1937; comnr., lands and dir. of surveys, 1939.

**Version `col1934-L58371.v` — printed in editions [1934, 1935, 1936]:**

> DE NORMAN, ALBERT WILFRED NOEL.—B. 1891; ed. United Services Coll. and Chateau du Rosey, Switzerland; Canadian Expedy. Force, 1914; lieut., Royal Fusiliers, 1915; West African Forces, 1916-20; survr., Nigeria survey, 1921; asst. survr.gen., 1930; ag. survr.gen., Apr., Sept., 1933; ag. commnr., lands and survr.gen., Mar.-Sept., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | Canadian Exped. Force | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1915 | lieut., Royal Fusiliers | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1916–1920 | West African Forces | — | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1921 | survr., Nigeria survey | Nigeria | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1930 | astt. survr.-gen | Nigeria *(inherited from previous clause)* | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1933 | ag. survr.-gen., Apr | Nigeria *(inherited from previous clause)* | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1935 | ag. comnr., lands and survr.-gen., Mar.- | Nigeria *(inherited from previous clause)* | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 7 | 1936 | Mar.- | Nigeria *(inherited from previous clause)* | [1932, 1933, 1937, 1939, 1940] |
| 8 | 1937 | chmn., Lagos exec. development bd | Lagos | [1932, 1933, 1937, 1939, 1940] |
| 9 | 1939 | comnr., lands and dir. of surveys | Lagos *(inherited from previous clause)* | [1932, 1933, 1937, 1939, 1940] |

## Candidate stint `de Normann, A. W. N___Nigeria___1936`

- Staff-list name: **de Normann, A. W. N** | colony: **Nigeria** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | Capt. A. W. N. de Normann | Assistant Surveyor-General | Land and Survey | — | Captain |
| 1939 | A. W. N. de Normann | Commissioner of Lands and Surveyor-General | Land and Survey | — | Capt. |

### Deterministic checks: `de-normann_albert-wilfred-noel_b1891` vs `de Normann, A. W. N___Nigeria___1936`

- [PASS] surname_gate: bio 'DE NORMANN' vs stint 'de Normann, A. W. N' (exact)
- [PASS] initials: bio ['A', 'W', 'N'] ~ stint ['A', 'W', 'N']
- [PASS] age_gate: stint starts 1936, birth 1891 (age 45)
- [PASS] colony: 5 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1936-1939
- [PASS] position_sim: best 69 vs bar 60: 'ag. comnr., lands and survr.-gen., Mar.-' ~ 'Commissioner of Lands and Surveyor-General'
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

