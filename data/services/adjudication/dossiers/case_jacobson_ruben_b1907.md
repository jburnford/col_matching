<!-- {"case_id": "case_jacobson_ruben_b1907", "bio_ids": ["jacobson_ruben_b1907"], "stint_ids": ["Jacobson, R. R. E___Nigeria___1952", "Jacobson, R___High Commission Territories___1959"]} -->
# Dossier case_jacobson_ruben_b1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['jacobson_ruben_b1907'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Jacobson, R. R. E___Nigeria___1952` is also gate-compatible with biography(ies) outside this case: ['jacobson_reginald-ronald-eric_b1912'] (already linked elsewhere or filtered).
- NOTE: stint `Jacobson, R___High Commission Territories___1959` is also gate-compatible with biography(ies) outside this case: ['jacobson_reginald-ronald-eric_b1912'] (already linked elsewhere or filtered).

## Biography `jacobson_ruben_b1907`

- Printed name: **JACOBSON, RUBEN**
- Birth year: 1907 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961])
- Honours: M.B, O.B.E (1958)
- Appears in editions: [1940, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1953-L17922.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961]:**

> JACOBSON, R., O.B.E. (1958).—b. 1907; ed. King Edward VII Sch., Jo'burg, and Witwatersrand Univ.; temp. M.O., Basuto., 1935; M.O., 1936; D.M.S., 1952-60.

**Version `col1940-L65539.v` — printed in editions [1940]:**

> JACOBSON, RUBEN, M.B., Ch.B. (W.W. Rand).—B. 1907; temp. med. offr., Basutoland, 1935; med. offr., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | temp. M.O. | Basutoland | [1940, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1936 | M.O | Basutoland *(inherited from previous clause)* | [1940, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |
| 2 | 1952–1960 | D.M.S | Basutoland *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Jacobson, R. R. E___Nigeria___1952`

- Staff-list name: **Jacobson, R. R. E** | colony: **Nigeria** | listed 1952–1960 | editions [1952, 1956, 1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | R. R. E. Jacobson | Director of Geological Survey | Civil Establishment | — | — |
| 1956 | R. R. E. Jacobson | Director of Geological Survey | Civil Establishment | — | — |
| 1958 | R. R. E. Jacobson | Director of Geological Survey | Civil Establishment | — | — |
| 1960 | R. R. E. Jacobson | Director of Geological Survey | Civil Establishment | — | — |

### Deterministic checks: `jacobson_ruben_b1907` vs `Jacobson, R. R. E___Nigeria___1952`

- [PASS] surname_gate: bio 'JACOBSON' vs stint 'Jacobson, R. R. E' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R', 'R', 'E']
- [PASS] age_gate: stint starts 1952, birth 1907 (age 45)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1952-1960
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Jacobson, R___High Commission Territories___1959`

- Staff-list name: **Jacobson, R** | colony: **High Commission Territories** | listed 1959–1960 | editions [1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | R. Jacobson | Director of Medical Services | BASUTOLAND | O.B.E. | — |
| 1960 | R. Jacobson | Director of Medical Services | BASUTOLAND | O.B.E. | — |

### Deterministic checks: `jacobson_ruben_b1907` vs `Jacobson, R___High Commission Territories___1959`

- [PASS] surname_gate: bio 'JACOBSON' vs stint 'Jacobson, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1959, birth 1907 (age 52)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1960
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: O.B.E
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

