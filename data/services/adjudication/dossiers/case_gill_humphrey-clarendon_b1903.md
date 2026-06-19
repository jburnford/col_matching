<!-- {"case_id": "case_gill_humphrey-clarendon_b1903", "bio_ids": ["gill_humphrey-clarendon_b1903"], "stint_ids": ["Gill, H. C___Palestine___1930", "Gill, H. S. C___Tanganyika___1949"]} -->
# Dossier case_gill_humphrey-clarendon_b1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 47 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Gill, H. C___Palestine___1930` is also gate-compatible with biography(ies) outside this case: ['gill_henry-sewell-currier_b1903'] (already linked elsewhere or filtered).
- NOTE: stint `Gill, H. S. C___Tanganyika___1949` is also gate-compatible with biography(ies) outside this case: ['gill_henry-sewell-currier_b1903'] (already linked elsewhere or filtered).

## Biography `gill_humphrey-clarendon_b1903`

- Printed name: **GILL, Humphrey Clarendon**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955])
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1948-L32842.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955]:**

> GILL, Humphrey Clarendon.—b. 1903; ed. Charterhouse and Christ Church, Oxford, B.A. (hons.) (Oxon); barrister-at-law; cadet, Nig., 1925; senr. dist. offr., 1945; admin. offr., cl. I, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | cadet | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1945 | senr. dist. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 2 | 1948 | admin. offr., cl. I | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |

## Candidate stint `Gill, H. C___Palestine___1930`

- Staff-list name: **Gill, H. C** | colony: **Palestine** | listed 1930–1940 | editions [1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | H. C. Gill | Assistant Engineer | Public Works | — | — |
| 1931 | H. C. Gill | Assistant Engineer | Public Works | — | — |
| 1932 | H. C. Gill | Assistant Engineer | Public Works | — | — |
| 1940 | H. C. Gill | Assistant Engineer | Department of Public Works | — | — |

### Deterministic checks: `gill_humphrey-clarendon_b1903` vs `Gill, H. C___Palestine___1930`

- [PASS] surname_gate: bio 'GILL' vs stint 'Gill, H. C' (exact)
- [PASS] initials: bio ['H', 'C'] ~ stint ['H', 'C']
- [PASS] age_gate: stint starts 1930, birth 1903 (age 27)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Gill, H. S. C___Tanganyika___1949`

- Staff-list name: **Gill, H. S. C** | colony: **Tanganyika** | listed 1949–1956 | editions [1949, 1952, 1953, 1954, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | H. S. C. Gill | Deputy Provincial Commissioners | Administrative | — | — |
| 1952 | H. S. C. Gill | Provincial Commissioner | Civil Establishment | — | — |
| 1953 | H. S. C. Gill | Provincial Commissioners | Civil Establishment | — | — |
| 1954 | H. S. C. Gill | Provincial Commissioners | Civil Establishment | — | — |
| 1956 | H. S. C. Gill | Senior Provincial Commissioner | Civil Establishment | — | — |

### Deterministic checks: `gill_humphrey-clarendon_b1903` vs `Gill, H. S. C___Tanganyika___1949`

- [PASS] surname_gate: bio 'GILL' vs stint 'Gill, H. S. C' (exact)
- [PASS] initials: bio ['H', 'C'] ~ stint ['H', 'S', 'C']
- [PASS] age_gate: stint starts 1949, birth 1903 (age 46)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1956
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

