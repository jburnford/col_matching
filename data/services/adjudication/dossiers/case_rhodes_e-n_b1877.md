<!-- {"case_id": "case_rhodes_e-n_b1877", "bio_ids": ["rhodes_e-n_b1877"], "stint_ids": ["Rhodes, Edgar N___Canada___1914"]} -->
# Dossier case_rhodes_e-n_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rhodes_e-n_b1877`

- Printed name: **RHODES, E. N**
- Birth year: 1877 (attested in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940])
- Honours: B.A, D.C.L, K.C
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1931-L67660.v` — printed in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]:**

> RHODES, HON. E. N., P.C. (Can.), K.C., B.A., LL.B., D.C.L.—B. 1877; ed. Amherst Acad., Acadia Univ. and Dalhousie Univ.; apptd. K.C., Nova Scotia, May, 1916; 1st lt. to H. of C. Canada at g.e., 1908; el. dep. speaker, H. of C., Feb., 1916; speaker, 1917; re-el. Mar., 1918; el. to legis., N.S., 1925; prov. premier and prov. sec., 1925; re-el. at g.e., 1928; joined Dom. cabinet of Bennett adminstr., as min. of fisheries, Aug., 1930; min. of finance, 1932; mem., senate, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | 1st lt. to H. of C. Canada at g.e | Nova Scotia *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 1 | 1916 | apptd. K.C. | Nova Scotia | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 2 | 1917 | speaker | Nova Scotia *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 3 | 1918 | re-el | Nova Scotia *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 4 | 1925 | el. to legis. | Nova Scotia | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 5 | 1928 | re-el. at g.e | Nova Scotia *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 6 | 1930 | joined Dom. cabinet of Bennett adminstr., as min. of fisheries | Nova Scotia *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 7 | 1932 | min. of finance | Nova Scotia *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 8 | 1935 | mem., senate | Nova Scotia *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |

## Candidate stint `Rhodes, Edgar N___Canada___1914`

- Staff-list name: **Rhodes, Edgar N** | colony: **Canada** | listed 1914–1922 | editions [1914, 1917, 1919, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | Edgar N. Rhodes | — | — | — | — |
| 1917 | Edgar N. Rhodes | Speaker | — | — | — |
| 1919 | Edgar N. Rhodes | Speaker | House of Commons | Hon. | — |
| 1919 | E. N. Rhodes | Member of Parliament | House of Commons | — | — |
| 1922 | Edgar N. Rhodes | Privy Councillor | Privy Council | — | — |

### Deterministic checks: `rhodes_e-n_b1877` vs `Rhodes, Edgar N___Canada___1914`

- [PASS] surname_gate: bio 'RHODES' vs stint 'Rhodes, Edgar N' (exact)
- [PASS] initials: bio ['E', 'N'] ~ stint ['E', 'N']
- [PASS] age_gate: stint starts 1914, birth 1877 (age 37)
- [PASS] colony: 9 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1914-1922
- [PASS] position_sim: best 100 vs bar 60: 'speaker' ~ 'Speaker'
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

