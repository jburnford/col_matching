<!-- {"case_id": "case_jenkins_trevor-westover_b1914", "bio_ids": ["jenkins_trevor-westover_b1914"], "stint_ids": ["Jenkins, T. W___Gold Coast___1949"]} -->
# Dossier case_jenkins_trevor-westover_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jenkins_trevor-westover_b1914`

- Printed name: **JENKINS, Trevor Westover**
- Birth year: 1914 (attested in editions [1960, 1961])
- Honours: C.P.M. (1953), Mentioned in Despatches (1957), Q.P.M. (1955)
- Appears in editions: [1950, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1960-L24619.v` — printed in editions [1960, 1961]:**

> JENKINS, T. W., Q.P.M. (1955), C.P.M. (1953). Mentioned in Despatches (1957).—b. 1914; ed. St. Peter's Sch., York; asst. inspr., police, Ken., 1935; asst. supt., G.C., 1947; supt., Ken., 1951; senr. supt., 1953; asst. comsnr., 1954; dir., intell. and security, Ken., 1952–53, 1954–55; dep. comsnr., police, Nig., 1956–60.

**Version `col1950-L36774.v` — printed in editions [1950]:**

> JENKINS, Trevor Westover.—b. 1914; ed. St. Peter’s Sch., York; asst. inspr., police, Ken., 1935; inspr., 1945; asst. supt., G.C., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | asst. inspr., police | Kenya | [1950, 1960, 1961] |
| 1 | 1945 | inspr | Kenya *(inherited from previous clause)* | [1950] |
| 2 | 1947 | asst. supt. | Gold Coast | [1950, 1960, 1961] |
| 3 | 1951 | supt. | Kenya | [1960, 1961] |
| 4 | 1952–1953 | dir., intell. and security | Kenya | [1960, 1961] |
| 5 | 1953 | senr. supt. | — | [1960, 1961] |
| 6 | 1954 | asst. comsnr. | — | [1960, 1961] |
| 7 | 1954–1955 | — | — | [1960, 1961] |
| 8 | 1956–1960 | dep. comsnr., police | Nigeria | [1960, 1961] |

## Candidate stint `Jenkins, T. W___Gold Coast___1949`

- Staff-list name: **Jenkins, T. W** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. W. Jenkins | Senior Assistant Superintendents and Assistant Superintendents | Police | — | — |
| 1951 | T. W. Jenkins | Senior Assistant Superintendent / Assistant Superintendent / Cadet | Police | — | — |

### Deterministic checks: `jenkins_trevor-westover_b1914` vs `Jenkins, T. W___Gold Coast___1949`

- [PASS] surname_gate: bio 'JENKINS' vs stint 'Jenkins, T. W' (exact)
- [PASS] initials: bio ['T', 'W'] ~ stint ['T', 'W']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 40 vs bar 60: 'asst. supt.' ~ 'Senior Assistant Superintendents and Assistant Superintendents'
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

