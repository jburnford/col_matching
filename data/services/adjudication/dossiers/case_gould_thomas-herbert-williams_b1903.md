<!-- {"case_id": "case_gould_thomas-herbert-williams_b1903", "bio_ids": ["gould_thomas-herbert-williams_b1903"], "stint_ids": ["Gould, H. W___Kenya___1922", "Gould, H. W___Uganda___1922"]} -->
# Dossier case_gould_thomas-herbert-williams_b1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gould_thomas-herbert-williams_b1903`

- Printed name: **GOULD, Thomas Herbert Williams**
- Birth year: 1903 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L32385.v` — printed in editions [1949, 1950, 1951]:**

> GOULD, Thomas Herbert Williams.—b. 1903; ed. Elliot Sch., London; C.A., 1921; admin. clk., T.T., 1925; tax offr., 1930; acctnt., 1932; asst. treas., 1938; senr. acctnt., Nyasa., 1943; treas. and ch. of cust., Som., 1946; fin. sec., 1947; acctnt.-gen., G.C., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | C.A | — | [1949, 1950, 1951] |
| 1 | 1925 | admin. clk., T.T | — | [1949, 1950, 1951] |
| 2 | 1930 | tax offr | — | [1949, 1950, 1951] |
| 3 | 1932 | acctnt | — | [1949, 1950, 1951] |
| 4 | 1938 | asst. treas | — | [1949, 1950, 1951] |
| 5 | 1943 | senr. acctnt. | Nyasaland | [1949, 1950, 1951] |
| 6 | 1946 | treas. and ch. of cust. | Somaliland | [1949, 1950, 1951] |
| 7 | 1947 | fin. sec | Somaliland *(inherited from previous clause)* | [1949, 1950, 1951] |
| 8 | 1949 | acctnt.-gen. | Gold Coast | [1949, 1950, 1951] |

## Candidate stint `Gould, H. W___Kenya___1922`

- Staff-list name: **Gould, H. W** | colony: **Kenya** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | H. W. Gould | Assistant Traffic Managers | Traffic | — | — |
| 1923 | H. W. Gould | Assistant Traffic Managers | Traffic | — | — |
| 1924 | H. W. Gould | Assistant Traffic Manager | Traffic | — | — |
| 1925 | H. W. Gould | Assistant Superintendents | Transportation | — | — |

### Deterministic checks: `gould_thomas-herbert-williams_b1903` vs `Gould, H. W___Kenya___1922`

- [PASS] surname_gate: bio 'GOULD' vs stint 'Gould, H. W' (exact)
- [PASS] initials: bio ['T', 'H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1922, birth 1903 (age 19)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Gould, H. W___Uganda___1922`

- Staff-list name: **Gould, H. W** | colony: **Uganda** | listed 1922–1924 | editions [1922, 1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | H. W. Gould | Superintendent | Port Bell—Kampala Railway | — | — |
| 1923 | H. W. Gould | Superintendent | Port Bell—Kampala Railway | — | — |
| 1924 | H. W. Gould | Superintendent | Port Bell—Kampala Railway | — | — |

### Deterministic checks: `gould_thomas-herbert-williams_b1903` vs `Gould, H. W___Uganda___1922`

- [PASS] surname_gate: bio 'GOULD' vs stint 'Gould, H. W' (exact)
- [PASS] initials: bio ['T', 'H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1922, birth 1903 (age 19)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1924
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

