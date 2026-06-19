<!-- {"case_id": "case_reynolds_f-g_b1914", "bio_ids": ["reynolds_f-g_b1914"], "stint_ids": ["Reynolds, F. G___Gold Coast___1949"]} -->
# Dossier case_reynolds_f-g_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `reynolds_f-g_b1914`

- Printed name: **REYNOLDS, F. G**
- Birth year: 1914 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1955, 1956, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L27329.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> REYNOLDS, F. G.—b. 1914; ed. King Edward VI Sch., Birmingham, and Birmingham Univ.; asst. acctnt., Nig., 1942; assessmt. offr., G.C., 1945; senr., 1946; asst. comsnt., income tax, 1948; dep. comsnt., 1952; retd., 1956; re-apptd. dep. comsnt., Nig., 1956; comsnt., 1958; chmn., fed. bd. of inland rev., 1959. (Nig. Govt. service.)

**Version `col1955-L22422.v` — printed in editions [1955, 1956]:**

> REYNOLDS, F. G.—b. 1914; ed. King Edward VI Sch. and Univ., Birm.; asst. acctnt., treasy., Nig., 1942; assessment offr., inc. tax dept., G.C., 1945; senr., 1946; asst. comsnr., 1948; dep comsnr., 1954 (G.C. local service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1942 | asst. acctnt. | Nigeria | [1955, 1956, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1945 | assessmt. offr. | Gold Coast | [1955, 1956, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1946 | senr | Gold Coast *(inherited from previous clause)* | [1955, 1956, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1948 | asst. comsnt., income tax | Gold Coast *(inherited from previous clause)* | [1955, 1956, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1952 | dep. comsnt | Gold Coast *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1954 | dep comsnr | Gold Coast *(inherited from previous clause)* | [1955, 1956] |
| 6 | 1956 | retd | Gold Coast *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 7 | 1956 | re-apptd. dep. comsnt. | Nigeria | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 8 | 1958 | comsnt | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 9 | 1959 | chmn., fed. bd. of inland rev | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Reynolds, F. G___Gold Coast___1949`

- Staff-list name: **Reynolds, F. G** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. G. Reynolds | Assistant Commissioner | Income Tax | — | — |
| 1950 | F. G. Reynolds | Assistant Commissioners | Income Tax | — | — |
| 1951 | F. G. Reynolds | Assistant Commissioner | Income Tax | — | — |

### Deterministic checks: `reynolds_f-g_b1914` vs `Reynolds, F. G___Gold Coast___1949`

- [PASS] surname_gate: bio 'REYNOLDS' vs stint 'Reynolds, F. G' (exact)
- [PASS] initials: bio ['F', 'G'] ~ stint ['F', 'G']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 6 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 55 vs bar 60: 'asst. comsnt., income tax' ~ 'Assistant Commissioner'
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

