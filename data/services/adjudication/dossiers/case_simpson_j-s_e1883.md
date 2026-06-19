<!-- {"case_id": "case_simpson_j-s_e1883", "bio_ids": ["simpson_j-s_e1883"], "stint_ids": ["Simpson, S___Nyasaland___1908", "Simpson, S___Uganda___1913"]} -->
# Dossier case_simpson_j-s_e1883

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 73 official(s) with this surname in the graph's staff lists; 29 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Simpson, S___Nyasaland___1908` is also gate-compatible with biography(ies) outside this case: ['simpson_samuel_b1876'] (already linked elsewhere or filtered).
- NOTE: stint `Simpson, S___Uganda___1913` is also gate-compatible with biography(ies) outside this case: ['simpson_samuel_b1876'] (already linked elsewhere or filtered).

## Biography `simpson_j-s_e1883`

- Printed name: **SIMPSON, J. S**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1886-L35735.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1897, 1898]:**

> SIMPSON, J. S.—Resident magistrate, Woolwich Bay, Cape Colony, 3rd May, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Resident magistrate, Woolwich Bay | Cape of Good Hope | [1886, 1888, 1889, 1890, 1894, 1897, 1898] |

## Candidate stint `Simpson, S___Nyasaland___1908`

- Staff-list name: **Simpson, S** | colony: **Nyasaland** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | S. Simpson | Cotton Expert | Forestry and Botanic Department | — | — |
| 1909 | S. Simpson | Cotton Expert | Forestry, Botanic and Agricultural Department | — | — |

### Deterministic checks: `simpson_j-s_e1883` vs `Simpson, S___Nyasaland___1908`

- [PASS] surname_gate: bio 'SIMPSON' vs stint 'Simpson, S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Simpson, S___Uganda___1913`

- Staff-list name: **Simpson, S** | colony: **Uganda** | listed 1913–1929 | editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1914 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1915 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1917 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1918 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1919 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1920 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1921 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1922 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1923 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1924 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1925 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1927 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1928 | S. Simpson | Director of Agriculture | Agricultural Department | — | — |
| 1929 | S. Simpson | Director of Agriculture | Agricultural Department | C.M.G. | — |

### Deterministic checks: `simpson_j-s_e1883` vs `Simpson, S___Uganda___1913`

- [PASS] surname_gate: bio 'SIMPSON' vs stint 'Simpson, S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1929
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

