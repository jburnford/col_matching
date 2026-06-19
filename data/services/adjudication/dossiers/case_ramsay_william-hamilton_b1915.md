<!-- {"case_id": "case_ramsay_william-hamilton_b1915", "bio_ids": ["ramsay_william-hamilton_b1915"], "stint_ids": ["Ramsay, W. H___Cyprus___1955", "Ramsay, W. H___Western Pacific___1937"]} -->
# Dossier case_ramsay_william-hamilton_b1915

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 25 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ramsay_william-hamilton_b1915`

- Printed name: **RAMSAY, William Hamilton**
- Birth year: 1915 (attested in editions [1955, 1956, 1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1949, 1950, 1951, 1955, 1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1955-L22364.v` — printed in editions [1955, 1956, 1957, 1958, 1959, 1960, 1961]:**

> RAMSAY, W. H.—b. 1915; ed. Fettes Coll. and Caius Coll., Camb.; mil. serv., 1939-42; cadet, Nig., 1938; admin. offr., cl. II, Cyp., 1952; cl. I, 1954; senr. admin. offr., 1954-60.

**Version `col1949-L35131.v` — printed in editions [1949, 1950, 1951]:**

> RAMSAY, William Hamilton.—b. 1915; ed. Fettes and Cambridge, B.A. (Cantab.); on mil. serv., 1939-42, lieut.; admin. cadet, Nig., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | cadet | Nigeria | [1949, 1950, 1951, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1952 | admin. offr., cl. II | Cyprus | [1955, 1956, 1957, 1958, 1959, 1960, 1961] |
| 2 | 1954 | cl. I | Cyprus *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Ramsay, W. H___Cyprus___1955`

- Staff-list name: **Ramsay, W. H** | colony: **Cyprus** | listed 1955–1959 | editions [1955, 1956, 1957, 1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | W. H. Ramsay | Commissioner | Civil Establishment | — | — |
| 1956 | W. H. Ramsay | Senior Administrative Officer | Civil Establishment | — | — |
| 1957 | W. H. Ramsay | Senior Assistant Secretary | Civil Establishment | — | — |
| 1958 | W. H. Ramsay | Under-Secretary (Internal Security) | Civil Establishment | — | — |
| 1959 | W. H. Ramsay | Senior Administrative Officer | Civil Establishment | — | — |

### Deterministic checks: `ramsay_william-hamilton_b1915` vs `Ramsay, W. H___Cyprus___1955`

- [PASS] surname_gate: bio 'RAMSAY' vs stint 'Ramsay, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1955, birth 1915 (age 40)
- [PASS] colony: 2 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1955-1959
- [FAIL] position_sim: best 53 vs bar 60: 'admin. offr., cl. II' ~ 'Senior Administrative Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Ramsay, W. H___Western Pacific___1937`

- Staff-list name: **Ramsay, W. H** | colony: **Western Pacific** | listed 1937–1939 | editions [1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | W. H. Ramsay | — | Treasury, Customs and Postal Departments | — | — |
| 1939 | W. H. Ramsay | Clerk | Treasury, Customs and Postal Departments | — | — |

### Deterministic checks: `ramsay_william-hamilton_b1915` vs `Ramsay, W. H___Western Pacific___1937`

- [PASS] surname_gate: bio 'RAMSAY' vs stint 'Ramsay, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1937, birth 1915 (age 22)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1939
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

