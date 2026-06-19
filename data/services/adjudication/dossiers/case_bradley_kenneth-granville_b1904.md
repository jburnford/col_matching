<!-- {"case_id": "case_bradley_kenneth-granville_b1904", "bio_ids": ["bradley_kenneth-granville_b1904"], "stint_ids": ["Bradley, K. G___Northern Rhodesia___1936"]} -->
# Dossier case_bradley_kenneth-granville_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bradley_kenneth-granville_b1904`

- Printed name: **BRADLEY, Kenneth Granville**
- Birth year: 1904 (attested in editions [1948, 1949, 1950, 1951])
- Honours: C.M.G (1946)
- Appears in editions: [1932, 1933, 1934, 1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31333.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BRADLEY, Kenneth Granville, C.M.G. (1946).—b. 1904; ed. Wellington Coll. and Univ. Coll., Oxford, B.A.; apptd. prob., N. Rhod., 1926; dist. offr., 1928; seconded to C.O., 1928-29; inf. offr., 1939-1942; col. sec. and fin. sec., Falk. Is., 1942; und.-sec., G.C., 1946; edr., coll. serv. jour., C.O., 1948.

**Version `col1932-L58611.v` — printed in editions [1932, 1934]:**

> BRADLEY, KENNETH GRANVILLE, B.A.—B. 1904; ed. Wellington Coll., Berkshire, and Univ. Coll., Oxford; prob., N. Rhodesia, 1926; asst. native comsnr., Jan., 1928; dist. offr., grade III, Apr., 1929; seconded as ag. asst. prin., C.O., Nov. 1928 to May, 1929; asst. sec., N. Rhodesia, June, 1930.

**Version `col1933-L58170.v` — printed in editions [1933]:**

> BRADLEY, KENNETH GRANVILLE, B.A.— B. 1904; ed. Wellington Coll., Berkshire, and Univ. Coll., Oxford; prob., N. Rhodesia, 1926; astt. native comsrr., Jan., 1928; dist. offr., grade

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | apptd. prob. | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 1 | 1926 | prob., N. Rhodesia | — | [1932, 1933, 1934] |
| 2 | 1928 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1928 | asst. native comsnr | — | [1932, 1933, 1934] |
| 4 | 1928–1929 | seconded as ag. asst. prin. | Colonial Office | [1932, 1934] |
| 5 | 1929 | dist. offr., grade III | — | [1932, 1934] |
| 6 | 1930 | asst. sec., N. Rhodesia | Colonial Office *(inherited from previous clause)* | [1932, 1934] |
| 7 | 1939–1942 | inf. offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 8 | 1942 | col. sec. and fin. sec. | Falkland Islands | [1948, 1949, 1950, 1951] |
| 9 | 1946 | und.-sec. | Gold Coast | [1948, 1949, 1950, 1951] |
| 10 | 1948 | edr., coll. serv. jour. | Colonial Office | [1948, 1949, 1950, 1951] |

## Candidate stint `Bradley, K. G___Northern Rhodesia___1936`

- Staff-list name: **Bradley, K. G** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | K. G. Bradley | District Officers | District Administration | — | — |
| 1939 | K. G. Bradley | District Officer | District Administration | — | — |
| 1940 | K. G. Bradley | District Officer | District Administration | — | — |

### Deterministic checks: `bradley_kenneth-granville_b1904` vs `Bradley, K. G___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'BRADLEY' vs stint 'Bradley, K. G' (exact)
- [PASS] initials: bio ['K', 'G'] ~ stint ['K', 'G']
- [PASS] age_gate: stint starts 1936, birth 1904 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 50 vs bar 60: 'inf. offr' ~ 'District Officer'
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

