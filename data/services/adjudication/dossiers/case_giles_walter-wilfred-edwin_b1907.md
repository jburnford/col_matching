<!-- {"case_id": "case_giles_walter-wilfred-edwin_b1907", "bio_ids": ["giles_walter-wilfred-edwin_b1907"], "stint_ids": ["Giles, W. W. E___Seychelles___1946"]} -->
# Dossier case_giles_walter-wilfred-edwin_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `giles_walter-wilfred-edwin_b1907`

- Printed name: **GILES, Walter Wilfred Edwin**
- Birth year: 1907 (attested in editions [1948, 1949])
- Honours: F.R.G.S, M.R.S.T
- Appears in editions: [1937, 1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L32837.v` — printed in editions [1948, 1949]:**

> GILES, Walter Wilfred Edwin, M.R.S.T., F.R.G.S.—b. 1907; ed. Oxford, M.A. (Oxon), dip. educ. (Oxon); on mil. serv., 1939-41; asst. mstr., King's Sch., Canterbury, 1931; headmnr., Busoga Coll., Uga., 1933; supt., educ., T.T., 1935; dir., educ., Seychelles, 1944; M.L.C., 1944; M.E.C. and agric. bd., 1945; chmn., advsy. coun. for educ., 1944; jt. auth. of Better English; mem., royal socy. of S. Africa, 1942.

**Version `col1950-L35712.v` — printed in editions [1950]:**

> GILES, Walter Wilfred Edwin, M.R.S.T., F.R.G.S.—b. 1907; ed. Oxford, M.A. (Oxon), dip. educ. (Oxon); on mil. serv. 1939–41; asst. mstr., King's Sch., Canterbury, 1931; headmr., Bucoya Coll., Uga., 1933; supt., educ., T.T., 1935; dir., educ., Seychelles, 1944; M.L.C., 1944; M.E.C. and agric. bd., 1945.

**Version `col1937-L61183.v` — printed in editions [1937]:**

> GILES, WALTER WILFRED EDWIN, B.A. (Oxon).—B. 1907; ast. mast., King's Schl., Canterbury, 1930-32; headmast., Busoga Coll., Uganda, 1933; ast., educn., Tanganyika Territory, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930–1932 | ast. mast., King's Schl., Canterbury | — | [1937] |
| 1 | 1931 | asst. mstr., King's Sch., Canterbury | — | [1948, 1949, 1950] |
| 2 | 1933 | headmnr., Busoga Coll. | Uganda | [1937, 1948, 1949, 1950] |
| 3 | 1935 | supt., educ., T.T | Uganda *(inherited from previous clause)* | [1948, 1949, 1950] |
| 4 | 1935 | ast., educn., Tanganyika Territory | Tanganyika | [1937] |
| 5 | 1942 | mem., royal socy. of S. Africa | Seychelles *(inherited from previous clause)* | [1948, 1949] |
| 6 | 1944 | dir., educ. | Seychelles | [1948, 1949, 1950] |
| 7 | 1945 | M.E.C. and agric. bd | Seychelles *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Giles, W. W. E___Seychelles___1946`

- Staff-list name: **Giles, W. W. E** | colony: **Seychelles** | listed 1946–1949 | editions [1946, 1948, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1946 | W. W. E. Giles | official | Executive Council | — | — |
| 1948 | W. W. E. Giles | — | Executive Council | — | — |
| 1949 | W. W. E. Giles | Director of Education | Education | — | — |

### Deterministic checks: `giles_walter-wilfred-edwin_b1907` vs `Giles, W. W. E___Seychelles___1946`

- [PASS] surname_gate: bio 'GILES' vs stint 'Giles, W. W. E' (exact)
- [PASS] initials: bio ['W', 'W', 'E'] ~ stint ['W', 'W', 'E']
- [PASS] age_gate: stint starts 1946, birth 1907 (age 39)
- [PASS] colony: 3 placed event(s) resolve to 'Seychelles'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1946-1949
- [FAIL] position_sim: best 55 vs bar 60: 'dir., educ.' ~ 'Director of Education'
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

