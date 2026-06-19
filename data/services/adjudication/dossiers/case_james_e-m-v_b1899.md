<!-- {"case_id": "case_james_e-m-v_b1899", "bio_ids": ["james_e-m-v_b1899"], "stint_ids": ["James, E. M. V___Leeward Islands___1954", "James, E. M. V___Palestine___1927"]} -->
# Dossier case_james_e-m-v_b1899

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 79 official(s) with this surname in the graph's staff lists; 42 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `james_e-m-v_b1899`

- Printed name: **JAMES, E. M. V**
- Birth year: 1899 (attested in editions [1954, 1955, 1956, 1957])
- Honours: C.P.M (1940), K.P.M (1945), O.B.E (1956)
- Appears in editions: [1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1954-L21020.v` — printed in editions [1954, 1955, 1956, 1957]:**

> JAMES, E. M. V., O.B.E. (1956), K.P.M. (1945), C.P.M. (1940), R.N. (Retd.)—b. 1899; ed. King Edward VI Sch., Southampton and R.N.C., Keyham; lieut., R.N., 1917-20; R.I.C., 1921; Pal. gendarmerie, 1922; Pal. police, supt., 1926; senr. supt., St. L. (secon.), 1948; Grenada, 1951; comsnr. Leeward Is., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1920 | lieut., R.N | — | [1954, 1955, 1956, 1957] |
| 1 | 1921 | R.I.C | — | [1954, 1955, 1956, 1957] |
| 2 | 1922 | Pal. gendarmerie | Palestine | [1954, 1955, 1956, 1957] |
| 3 | 1926 | Pal. police, supt | Palestine *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |
| 4 | 1948 | senr. supt., St. L. (secon.) | St. Lucia | [1954, 1955, 1956, 1957] |
| 5 | 1951 | senr. supt., St. L. (secon.) | Grenada | [1954, 1955, 1956, 1957] |
| 6 | 1953 | comsnr. Leeward Is | Grenada *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |

## Candidate stint `James, E. M. V___Leeward Islands___1954`

- Staff-list name: **James, E. M. V** | colony: **Leeward Islands** | listed 1954–1955 | editions [1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | E. M. V. James | Commissioner of Police | Civil Establishment | — | — |
| 1955 | E. M. V. James | Commissioner of Police | Civil Establishment | — | — |

### Deterministic checks: `james_e-m-v_b1899` vs `James, E. M. V___Leeward Islands___1954`

- [PASS] surname_gate: bio 'JAMES' vs stint 'James, E. M. V' (exact)
- [PASS] initials: bio ['E', 'M', 'V'] ~ stint ['E', 'M', 'V']
- [PASS] age_gate: stint starts 1954, birth 1899 (age 55)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1955
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `James, E. M. V___Palestine___1927`

- Staff-list name: **James, E. M. V** | colony: **Palestine** | listed 1927–1940 | editions [1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | E. M. V. James | Assistant Superintendents | Department of Police and Prisons | — | — |
| 1928 | E. M. V. James | Assistant Superintendents | Department of Police and Prisons | — | — |
| 1929 | E. M. V. James | Assistant Superintendents | Department of Police and Prisons | — | — |
| 1930 | E. M. V. James | Assistant Superintendents | Department of Police and Prisons | — | — |
| 1931 | E. M. V. James | Assistant Superintendents | Department of Police and Prisons. | — | — |
| 1932 | E. M. V. James | Assistant Superintendents | Department of Police and Prisons | — | — |
| 1940 | E. M. V. James | Deputy Superintendent | Department of Police and Prisons. | — | — |

### Deterministic checks: `james_e-m-v_b1899` vs `James, E. M. V___Palestine___1927`

- [PASS] surname_gate: bio 'JAMES' vs stint 'James, E. M. V' (exact)
- [PASS] initials: bio ['E', 'M', 'V'] ~ stint ['E', 'M', 'V']
- [PASS] age_gate: stint starts 1927, birth 1899 (age 28)
- [PASS] colony: 2 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1927-1940
- [FAIL] position_sim: best 35 vs bar 60: 'Pal. police, supt' ~ 'Assistant Superintendents'
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

