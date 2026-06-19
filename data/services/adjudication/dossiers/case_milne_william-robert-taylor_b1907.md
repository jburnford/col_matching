<!-- {"case_id": "case_milne_william-robert-taylor_b1907", "bio_ids": ["milne_william-robert-taylor_b1907"], "stint_ids": ["Milne, R___Sierra Leone___1955", "Milne, R___Uganda___1922"]} -->
# Dossier case_milne_william-robert-taylor_b1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `milne_william-robert-taylor_b1907`

- Printed name: **MILNE, William Robert Taylor**
- Birth year: 1907 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L34331.v` — printed in editions [1949, 1950, 1951]:**

> MILNE, William Robert Taylor.—b. 1907; ed. Eltham Coll., Madras Coll., St. Andrews and St. Andrews Univ., M.A.; cadet, Nig., 1930; asst. sec., Trin., 1942-44; asst. civ. serv. comsnr., Nig., 1948; dep., 1950; mem., comtce. on unestab. and daily rated gov. servants.

**Version `col1948-L34679.v` — printed in editions [1948]:**

> MILNE, William Robert Taylor.—b. 1907; ed. Madras Coll., St. Andrew's, St. Andrew's Univ., M.A. (St. Andrew's); admin. offr., Nig., 1930; asst. sec., Trin., 1942-44.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | cadet | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1942–1944 | asst. sec. | Trinidad | [1948, 1949, 1950, 1951] |
| 2 | 1948 | asst. civ. serv. comsnr. | Nigeria | [1949, 1950, 1951] |
| 3 | 1950 | dep | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Milne, R___Sierra Leone___1955`

- Staff-list name: **Milne, R** | colony: **Sierra Leone** | listed 1955–1960 | editions [1955, 1956, 1957, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | R. Milne | Assistant Director of Public Works | Civil Establishment | — | — |
| 1956 | R. Milne | Deputy Director | Civil Establishment | — | — |
| 1957 | R. Milne | Deputy Director | Civil Establishment | — | — |
| 1958 | R. Milne | Deputy Director | Civil Establishment | — | — |
| 1959 | R. Milne | Deputy Director | Civil Establishment | — | — |
| 1960 | R. Milne | Deputy Director | Civil Establishment | — | — |

### Deterministic checks: `milne_william-robert-taylor_b1907` vs `Milne, R___Sierra Leone___1955`

- [PASS] surname_gate: bio 'MILNE' vs stint 'Milne, R' (exact)
- [PASS] initials: bio ['W', 'R', 'T'] ~ stint ['R']
- [PASS] age_gate: stint starts 1955, birth 1907 (age 48)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1960
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Milne, R___Uganda___1922`

- Staff-list name: **Milne, R** | colony: **Uganda** | listed 1922–1933 | editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | R. Milne | Overseer | Public Works | — | — |
| 1923 | R. Milne | Overseer | Public Works | — | — |
| 1924 | R. Milne | Overseer | Public Works | — | — |
| 1925 | R. Milne | Overseer | Public Works | — | — |
| 1927 | R. Milne | Overseer | Public Works | — | — |
| 1928 | R. Milne | Overseer | Public Works | — | — |
| 1929 | R. Milne | Overseer | Public Works | — | — |
| 1930 | R. Milne | Overseer | Police and Prisons | — | — |
| 1933 | R. Milne | Overseer | Public Works Department | — | — |

### Deterministic checks: `milne_william-robert-taylor_b1907` vs `Milne, R___Uganda___1922`

- [PASS] surname_gate: bio 'MILNE' vs stint 'Milne, R' (exact)
- [PASS] initials: bio ['W', 'R', 'T'] ~ stint ['R']
- [PASS] age_gate: stint starts 1922, birth 1907 (age 15)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1933
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

