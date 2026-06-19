<!-- {"case_id": "case_fowler_w_b1907", "bio_ids": ["fowler_w_b1907"], "stint_ids": ["Fowler, W___Western Pacific___1930"]} -->
# Dossier case_fowler_w_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['fowler_w_b1907'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Fowler, W___Western Pacific___1930` is also gate-compatible with biography(ies) outside this case: ['fowler_chas-w_e1896', 'fowler_i-w_e1876', 'fowler_j-w_e1876'] (already linked elsewhere or filtered).

## Biography `fowler_w_b1907`

- Printed name: **FOWLER, W**
- Birth year: 1907 (attested in editions [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957])
- Appears in editions: [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1948-L32669.v` — printed in editions [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957]:**

> FOWLER, W.—b. 1907; ed. Barry, Glam., and Univ. of Wales; mil. serv., 1940-45, major; cadet, B.S.I.P., 1929; admin. offr., Nig., 1936; cl. II, 1947; cl. I, 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | cadet, B.S.I.P | — | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957] |
| 1 | 1936 | admin. offr. | Nigeria | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957] |
| 2 | 1947 | cl. II | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957] |
| 3 | 1953 | cl. I | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957] |

## Candidate stint `Fowler, W___Western Pacific___1930`

- Staff-list name: **Fowler, W** | colony: **Western Pacific** | listed 1930–1937 | editions [1930, 1933, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | W. Fowler | Cadet | General | — | — |
| 1933 | W. Fowler | Cadet | District Administration | — | — |
| 1936 | W. Fowler | District Officer | District Administration | — | — |
| 1937 | W. Fowler | District Officer | District Administration | — | — |

### Deterministic checks: `fowler_w_b1907` vs `Fowler, W___Western Pacific___1930`

- [PASS] surname_gate: bio 'FOWLER' vs stint 'Fowler, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1930, birth 1907 (age 23)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1937
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

