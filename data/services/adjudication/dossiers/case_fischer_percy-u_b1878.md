<!-- {"case_id": "case_fischer_percy-u_b1878", "bio_ids": ["fischer_percy-u_b1878", "fischer_philip-u_b1878"], "stint_ids": ["Fischer, P. U___Orange River Colony___1908"]} -->
# Dossier case_fischer_percy-u_b1878

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Fischer, P. U___Orange River Colony___1908'] have more than one claimant biography in this case.

## Biography `fischer_percy-u_b1878`

- Printed name: **FISCHER, PERCY U**
- Birth year: 1878 (attested in editions [1940])
- Honours: B.A
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L64243.v` — printed in editions [1940]:**

> FISCHER, PERCY U., B.A., LL.B.—B. 1878; ED. GREY COLL., BLOEMFONTEIN, S.A. COLL., CAPE TOWN, TRINITY HALL, CAMBRIDGE; JUDGE, SUP. CT., SOUTH AFRICA, 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | JUDGE, SUP. CT. | SOUTH AFRICA | [1940] |

## Biography `fischer_philip-u_b1878`

- Printed name: **FISCHER, PHILIP U**
- Birth year: 1878 (attested in editions [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937])
- Honours: B.A, L.L.B
- Appears in editions: [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1930-L64399.v` — printed in editions [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]:**

> FISCHER, PHILIP U., B.A., L.L.B.—B. 1878; ed. Grey Coll., Bloemfontien, S.A. Coll., Cape Town, Trinity Hall, Camb.; judge, sup. ct., South Africa, 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | judge, sup. ct. | South Africa | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Fischer, P. U___Orange River Colony___1908`

- Staff-list name: **Fischer, P. U** | colony: **Orange River Colony** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | P. U. Fischer | Lecturer in Law | Education Department | — | — |
| 1909 | P. U. Fischer | Lecturer in Law | Grey University College | — | — |

### Deterministic checks: `fischer_percy-u_b1878` vs `Fischer, P. U___Orange River Colony___1908`

- [PASS] surname_gate: bio 'FISCHER' vs stint 'Fischer, P. U' (exact)
- [PASS] initials: bio ['P', 'U'] ~ stint ['P', 'U']
- [PASS] age_gate: stint starts 1908, birth 1878 (age 30)
- [FAIL] colony: no placed event resolves to 'Orange River Colony'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `fischer_philip-u_b1878` vs `Fischer, P. U___Orange River Colony___1908`

- [PASS] surname_gate: bio 'FISCHER' vs stint 'Fischer, P. U' (exact)
- [PASS] initials: bio ['P', 'U'] ~ stint ['P', 'U']
- [PASS] age_gate: stint starts 1908, birth 1878 (age 30)
- [FAIL] colony: no placed event resolves to 'Orange River Colony'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
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

