<!-- {"case_id": "case_mclellan_david_b1904", "bio_ids": ["mclellan_david_b1904"], "stint_ids": ["McLellan, D___Hong Kong___1949", "McLellan, D___Singapore___1954"]} -->
# Dossier case_mclellan_david_b1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mclellan_david_b1904'] carry a single initial only — the namesake trap applies.

## Biography `mclellan_david_b1904`

- Printed name: **McLELLAN, David**
- Birth year: 1904 (attested in editions [1956, 1957, 1959])
- Appears in editions: [1948, 1949, 1950, 1951, 1955, 1956, 1957, 1959]

### Verbatim printed entry text (OCR)

**Version `col1956-L22809.v` — printed in editions [1956, 1957, 1959]:**

> McLELLAN, D., E.D.—b. 1904; ed. King Edward VII Sch., Lytham, and Queens' Coll., Camb.; mil. serv., lieut. (p.o.w.), 1941-45; master, educ. dept., H.K., 1931; senr. educ. offr., 1951; dep. dir., educ., S'pore, 1953; perm. sec., min. of educ., and dir., educ., 1955.

**Version `col1955-L21790.v` — printed in editions [1955]:**

> McLELLAN, D., E.D.—b. 1904; ed. King Edward VII Sch., Lytham and Queens’ Coll., Camb.; mil. serv., lieut. (p.o.w.), 1941–45; master, educ. dept., H.K., 1931; senr. inspr., schools, 1951; dep. dir., educ., S’pore, 1953.

**Version `col1948-L34384.v` — printed in editions [1948, 1949, 1950, 1951]:**

> McLELLAN, David.—b. 1904; ed. King Edward VII Sch., Lytham and Queens' Coll., Camb. (open schol.), M.A. (Cantab.); on mil. serv., lieut. (p.o.w.), 1941-45; mstr., educ. dept., H.K., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | master, educ. dept. | Hong Kong | [1948, 1949, 1950, 1951, 1955, 1956, 1957, 1959] |
| 1 | 1951 | senr. educ. offr | Hong Kong *(inherited from previous clause)* | [1955, 1956, 1957, 1959] |
| 2 | 1953 | dep. dir., educ., S'pore | Hong Kong *(inherited from previous clause)* | [1955, 1956, 1957, 1959] |
| 3 | 1955 | perm. sec., min. of educ., and dir., educ | Hong Kong *(inherited from previous clause)* | [1956, 1957, 1959] |

## Candidate stint `McLellan, D___Hong Kong___1949`

- Staff-list name: **McLellan, D** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. McLellan | Masters | Education Department | — | — |
| 1950 | D. McLellan | Masters | Education | — | — |
| 1951 | D. McLellan | Masters | Education | — | — |

### Deterministic checks: `mclellan_david_b1904` vs `McLellan, D___Hong Kong___1949`

- [PASS] surname_gate: bio 'McLELLAN' vs stint 'McLellan, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [PASS] colony: 4 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 52 vs bar 60: 'master, educ. dept.' ~ 'Masters'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `McLellan, D___Singapore___1954`

- Staff-list name: **McLellan, D** | colony: **Singapore** | listed 1954–1958 | editions [1954, 1955, 1956, 1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | D. McLellan | Deputy Director of Education | Civil Establishment | — | — |
| 1955 | D. McLellan | Deputy Director of Education | Civil Establishment | — | — |
| 1956 | D. McLellan | Permanent Secretary to Ministry of Education and Director of Education | Civil Establishment | — | — |
| 1957 | D. McLellan | Permanent Secretary to Ministry of Education and Director of Education | Civil Establishment | — | — |
| 1958 | D. McLellan | Director of Education | Civil Establishment | C.M.G. | — |

### Deterministic checks: `mclellan_david_b1904` vs `McLellan, D___Singapore___1954`

- [PASS] surname_gate: bio 'McLELLAN' vs stint 'McLellan, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1954, birth 1904 (age 50)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1958
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

