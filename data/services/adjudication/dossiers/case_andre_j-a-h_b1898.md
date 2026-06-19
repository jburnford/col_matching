<!-- {"case_id": "case_andre_j-a-h_b1898", "bio_ids": ["andre_j-a-h_b1898"], "stint_ids": ["Andre, H___Mauritius___1936", "Andre, H___Trinidad___1918", "Andre, J. A. H___Mauritius___1953"]} -->
# Dossier case_andre_j-a-h_b1898

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `andre_j-a-h_b1898`

- Printed name: **ANDRE, J. A. H**
- Birth year: 1898 (attested in editions [1953, 1954, 1955, 1956, 1957])
- Honours: M.B.E
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L16352.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> ANDRE, J. A. H., M.B.E.—b. 1898 ; ed. Primary Sch., Maur., Royal Coll., Maur., and Lond. Sch. of Trop. Med.; govt. med. offr., 1924 ; D.D.M.S., Maur., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | govt. med. offr | — | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1951 | D.D.M.S. | Mauritius | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Andre, H___Mauritius___1936`

- Staff-list name: **Andre, H** | colony: **Mauritius** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | H. Andre | Medical Officer | Medical and Health Department | — | — |
| 1937 | H. Andre | Medical Officer | Medical and Health Department | — | — |
| 1939 | H. Andre | Medical Officer | Medical and Health Department | — | — |

### Deterministic checks: `andre_j-a-h_b1898` vs `Andre, H___Mauritius___1936`

- [PASS] surname_gate: bio 'ANDRE' vs stint 'Andre, H' (exact)
- [PASS] initials: bio ['J', 'A', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1936, birth 1898 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Andre, H___Trinidad___1918`

- Staff-list name: **Andre, H** | colony: **Trinidad** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | H. Andre | Clerk | Department of Agriculture | — | — |
| 1919 | H. Andre | 8th Class Clerk | Department of Agriculture | — | — |

### Deterministic checks: `andre_j-a-h_b1898` vs `Andre, H___Trinidad___1918`

- [PASS] surname_gate: bio 'ANDRE' vs stint 'Andre, H' (exact)
- [PASS] initials: bio ['J', 'A', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1918, birth 1898 (age 20)
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Andre, J. A. H___Mauritius___1953`

- Staff-list name: **Andre, J. A. H** | colony: **Mauritius** | listed 1953–1957 | editions [1953, 1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | J. A. H. Andre | Deputy Directors of Medical Services | Civil Establishment | — | — |
| 1954 | J. A. H. Andre | Deputy Directors of Medical Services | Civil Establishment | — | — |
| 1955 | J. A. H. Andre | Deputy Directors of Medical Services | Civil Establishment | — | — |
| 1956 | J. A. H. Andre | Deputy Director of Medical Services | Civil Establishment | — | — |
| 1957 | J. A. H. Andre | Deputy Directors of Medical Services | Civil Establishment | — | — |

### Deterministic checks: `andre_j-a-h_b1898` vs `Andre, J. A. H___Mauritius___1953`

- [PASS] surname_gate: bio 'ANDRE' vs stint 'Andre, J. A. H' (exact)
- [PASS] initials: bio ['J', 'A', 'H'] ~ stint ['J', 'A', 'H']
- [PASS] age_gate: stint starts 1953, birth 1898 (age 55)
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1953-1957
- [FAIL] position_sim: best 21 vs bar 60: 'D.D.M.S.' ~ 'Deputy Director of Medical Services'
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

