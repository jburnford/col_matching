<!-- {"case_id": "case_mankin_john-hender_b1897", "bio_ids": ["mankin_john-hender_b1897"], "stint_ids": ["Mankin, J. H___Palestine___1925"]} -->
# Dossier case_mankin_john-hender_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mankin_john-hender_b1897`

- Printed name: **MANKIN, John Hender**
- Birth year: 1897 (attested in editions [1949, 1950, 1951])
- Honours: F.R.C.S, F.R.I.C.S
- Appears in editions: [1949, 1950, 1951, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1949-L34138.v` — printed in editions [1949, 1950, 1951]:**

> MANKIN, John Hender, F.R.I.C.S., F.R.C.S.—b. 1897; ed. privately and at Holy Trinity, Cloudesley; on mil. serv., 1914-19; W.O., G.S.O. III, 1939-44; sub inspr., surveys, Pal., 1921; asst. inspr. of surveys, 1927; supt., 1938; senr. survr., Uga., 1946; asst. to dep. dir., directorate of col. surv., 1949; mem., boundary coms., Transjordan-Syria, 1932.

**Version `col1959-L25798.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964]:**

> MANKIN, J. H.—b. 1897; ed. privately and Holy Trinity, Cloudesley; mil. serv., 1914-19, 1939-44, W.O., G.S.O. III; sub-inspr., surveys, Pal., 1921; asst. inspr., 1927; supt., 1938; senr. surveyor, Uga., 1946; ret.; senr. surveyor, D.O.S., 1949; provisioning and investigt. offr., 1955; mem., boundary comsn., Transjordan-Syria, 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | sub inspr., surveys | Palestine | [1949, 1950, 1951, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1927 | asst. inspr. of surveys | Palestine *(inherited from previous clause)* | [1949, 1950, 1951, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1932 | mem., boundary coms., Transjordan-Syria | Uganda *(inherited from previous clause)* | [1949, 1950, 1951, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1938 | supt | Palestine *(inherited from previous clause)* | [1949, 1950, 1951, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1939–1944 | W.O., G.S.O. III | — | [1949, 1950, 1951] |
| 5 | 1946 | senr. survr. | Uganda | [1949, 1950, 1951, 1959, 1960, 1961, 1962, 1963, 1964] |
| 6 | 1949 | asst. to dep. dir., directorate of col. surv | Uganda *(inherited from previous clause)* | [1949, 1950, 1951, 1959, 1960, 1961, 1962, 1963, 1964] |
| 7 | 1955 | provisioning and investigt. offr | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Mankin, J. H___Palestine___1925`

- Staff-list name: **Mankin, J. H** | colony: **Palestine** | listed 1925–1940 | editions [1925, 1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | J. H. Mankin | Sub-Inspectors | Department of Surveys | — | — |
| 1927 | J. H. Mankin | Sub-Inspectors | Department of Surveys | — | — |
| 1928 | J. H. Mankin | Sub-Inspector | Department of Surveys | — | — |
| 1929 | J. H. Mankin | Assistant Inspector | Department of Surveys | — | — |
| 1930 | J. H. Mankin | Assistant Inspectors | Department of Surveys | — | — |
| 1931 | J. H. Mankin | Assistant Inspector | Department of Surveys | — | — |
| 1932 | J. H. Mankin | Assistant Inspector | Department of Surveys | — | — |
| 1940 | J. H. Mankin | Superintendents | Surveys | — | — |

### Deterministic checks: `mankin_john-hender_b1897` vs `Mankin, J. H___Palestine___1925`

- [PASS] surname_gate: bio 'MANKIN' vs stint 'Mankin, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1925, birth 1897 (age 28)
- [PASS] colony: 3 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1925-1940
- [FAIL] position_sim: best 59 vs bar 60: 'asst. inspr. of surveys' ~ 'Assistant Inspectors'
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

