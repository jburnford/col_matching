<!-- {"case_id": "case_marillier_eric-stanley_b1890", "bio_ids": ["marillier_eric-stanley_b1890"], "stint_ids": ["Marillier, E. S___Northern Rhodesia___1925", "Marillier, E. S___Northern Rhodesia___1933"]} -->
# Dossier case_marillier_eric-stanley_b1890

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `marillier_eric-stanley_b1890`

- Printed name: **MARILLIER, ERIC STANLEY**
- Birth year: 1890 (attested in editions [1937])
- Honours: O.B.E (1935)
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L63041.v` — printed in editions [1937]:**

> MARILLIER, ERIC STANLEY, O.B.E.—B. 1890; clk., oust., N. Rhodesia, Apr., 1915; collr., cust., Apr., 1915; senr. collr., 1926; contr. cust., Mar., 1928; mem. leg. MARITZ, G. J.—B. 1889; ed. Victoria, Stellenbosch and Trinity Coll., Oxford; bar, Middle Temple, 1912; pres., sp. income appl. ct., 1926; judge, sup. ct., Transvaal divn., 1930; mem., delimitation comm., 1932.

**Version `col1931-L66532.v` — printed in editions [1931, 1932, 1933, 1934, 1935, 1936]:**

> MARILLIER, ERIC STANLEY, O.B.E. (1935).—B. 1890; olk., cust., N. Rhodesia, Apr., 1912; collr., cust., Apr., 1915; senr. collr., cust., Oct., 1926; contr. cust., Mar., 1928; mem., leg. coun.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | olk., cust., N. Rhodesia | — | [1931, 1932, 1933, 1934, 1935, 1936] |
| 1 | 1915–1915 | clk., oust. | Northern Rhodesia | [1937] |
| 2 | 1915–1915 | collr., cust. | — | [1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 3 | 1926–1926 | senr. collr. | — | [1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 4 | 1928–1928 | contr. cust. | — | [1931, 1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Marillier, E. S___Northern Rhodesia___1925`

- Staff-list name: **Marillier, E. S** | colony: **Northern Rhodesia** | listed 1925–1928 | editions [1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | E. S. Marillier | Collectors | Customs | — | — |
| 1927 | E. S. Marillier | Senior Collector | Customs | — | — |
| 1928 | E. S. Marillier | Senior Collector | Customs | — | — |

### Deterministic checks: `marillier_eric-stanley_b1890` vs `Marillier, E. S___Northern Rhodesia___1925`

- [PASS] surname_gate: bio 'MARILLIER' vs stint 'Marillier, E. S' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1925, birth 1890 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1928
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Marillier, E. S___Northern Rhodesia___1933`

- Staff-list name: **Marillier, E. S** | colony: **Northern Rhodesia** | listed 1933–1937 | editions [1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | E. S. Marillier | Controller of Customs | Customs | — | — |
| 1934 | E. S. Marillier | Controller of Customs | Customs | — | — |
| 1936 | E. S. Marillier | Controller of Customs | Customs | — | — |
| 1937 | E. S. Marillier | Controller of Customs | Customs | — | — |

### Deterministic checks: `marillier_eric-stanley_b1890` vs `Marillier, E. S___Northern Rhodesia___1933`

- [PASS] surname_gate: bio 'MARILLIER' vs stint 'Marillier, E. S' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1933, birth 1890 (age 43)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1937
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

