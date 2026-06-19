<!-- {"case_id": "case_noad_frederick-mitchell_b1895", "bio_ids": ["noad_frederick-mitchell_b1895"], "stint_ids": ["Noad, F. M___Bahamas___1953", "Noad, F. M___Leeward Islands___1949"]} -->
# Dossier case_noad_frederick-mitchell_b1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `noad_frederick-mitchell_b1895`

- Printed name: **NOAD, FREDERICK MITCHELL**
- Birth year: 1895 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69414.v` — printed in editions [1939, 1940]:**

> NOAD, FREDERICK MITCHELL.—B. 1895; ed. prvte. (Ascham Coll.) Berkhamsted and St. Lawrence; W.A.F.F., 1915-20; admtrv. offr., cls. III, Nigeria, 1930; do., cls. II, 1936; do., cls. I, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1920 | W.A.F.F | — | [1939, 1940] |
| 1 | 1930 | admtrv. offr., cls. III | Nigeria | [1939, 1940] |
| 2 | 1936 | do., cls. II | Nigeria *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1937 | do., cls. I | Nigeria *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Noad, F. M___Bahamas___1953`

- Staff-list name: **Noad, F. M** | colony: **Bahamas** | listed 1953–1958 | editions [1953, 1954, 1955, 1956, 1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | F. M. Noad | Deputy Colonial Secretary | Civil Establishment | — | — |
| 1954 | F. M. Noad | Deputy Colonial Secretary | Civil Establishment | — | — |
| 1955 | F. M. Noad. | Deputy Colonial Secretary | Civil Establishment | — | — |
| 1956 | F. M. Noad | Deputy Colonial Secretary | Civil Establishment | — | — |
| 1957 | F. M. Noad | Deputy Colonial Secretary | Civil Establishment | — | — |
| 1958 | F. M. Noad | Deputy Colonial Secretary | Civil Establishment | — | — |

### Deterministic checks: `noad_frederick-mitchell_b1895` vs `Noad, F. M___Bahamas___1953`

- [PASS] surname_gate: bio 'NOAD' vs stint 'Noad, F. M' (exact)
- [PASS] initials: bio ['F', 'M'] ~ stint ['F', 'M']
- [PASS] age_gate: stint starts 1953, birth 1895 (age 58)
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1958
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Noad, F. M___Leeward Islands___1949`

- Staff-list name: **Noad, F. M** | colony: **Leeward Islands** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. M. Noad | Administrator | ADMINISTRATION | — | — |
| 1951 | F. M. Noad | Administrator | Administrators | — | — |

### Deterministic checks: `noad_frederick-mitchell_b1895` vs `Noad, F. M___Leeward Islands___1949`

- [PASS] surname_gate: bio 'NOAD' vs stint 'Noad, F. M' (exact)
- [PASS] initials: bio ['F', 'M'] ~ stint ['F', 'M']
- [PASS] age_gate: stint starts 1949, birth 1895 (age 54)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

