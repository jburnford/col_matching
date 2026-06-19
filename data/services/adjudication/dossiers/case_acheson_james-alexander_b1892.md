<!-- {"case_id": "case_acheson_james-alexander_b1892", "bio_ids": ["acheson_james-alexander_b1892"], "stint_ids": ["Acheson, J. A___Northern Rhodesia___1925"]} -->
# Dossier case_acheson_james-alexander_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `acheson_james-alexander_b1892`

- Printed name: **ACHESON, James Alexander**
- Birth year: 1892 (attested in editions [1940, 1948, 1949, 1950, 1951])
- Appears in editions: [1940, 1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1940-L61874.v` — printed in editions [1940, 1948, 1949, 1950, 1951]:**

> ACHESON, James Alexander.—b. 1892; ed. the Academy, Ballymena and Dublin Univ.; L.M. Rotunda, M.B., B.Ch., B.A.O. (Dublin), D.P.H., M.A., M.D.; war serv. 1915-18; 1941, Maj., M.O., N. Rhod., 1923; ag. D.M.S., 1936-37; S.M.O., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1918 | war serv. | — | [1940, 1948, 1949, 1950, 1951] |
| 1 | 1923 | M.O. | Northern Rhodesia | [1940, 1948, 1949, 1950, 1951] |
| 2 | 1936–1937 | ag. D.M.S. | — | [1940, 1948, 1949, 1950, 1951] |
| 3 | 1937 | S.M.O. | — | [1940, 1948, 1949, 1950, 1951] |
| 4 | 1941–1941 | Maj. | — | [1940, 1948, 1949, 1950, 1951] |

## Candidate stint `Acheson, J. A___Northern Rhodesia___1925`

- Staff-list name: **Acheson, J. A** | colony: **Northern Rhodesia** | listed 1925–1939 | editions [1925, 1927, 1928, 1929, 1931, 1933, 1934, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | J. A. Acheson | Medical Officer | Medical | — | — |
| 1927 | J. A. Acheson | Medical Officer | Medical | — | — |
| 1928 | J. A. Acheson | Medical Officer | Medical | — | — |
| 1929 | J. A. Acheson | Medical Officers | Health | — | — |
| 1931 | J. A. Acheson | Medical Officer | Health | — | — |
| 1933 | J. A. Acheson | Medical Officers | Health | — | — |
| 1934 | J. A. Acheson | Medical Officers | Health | — | — |
| 1936 | J. A. Acheson | Medical and Health Officer | Medical | — | — |
| 1937 | J. A. Acheson | Medical Officer | Medical | — | — |
| 1939 | J. A. Acheson | Senior Medical Officer | Medical | — | — |

### Deterministic checks: `acheson_james-alexander_b1892` vs `Acheson, J. A___Northern Rhodesia___1925`

- [PASS] surname_gate: bio 'ACHESON' vs stint 'Acheson, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1925, birth 1892 (age 33)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1925-1939
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

