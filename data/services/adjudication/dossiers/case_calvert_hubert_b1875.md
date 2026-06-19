<!-- {"case_id": "case_calvert_hubert_b1875", "bio_ids": ["calvert_hubert_b1875"], "stint_ids": ["Calvert, G. H___Hong Kong___1949", "Calvert, J. E. H___Uganda___1933"]} -->
# Dossier case_calvert_hubert_b1875

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['calvert_hubert_b1875'] carry a single initial only — the namesake trap applies.

## Biography `calvert_hubert_b1875`

- Printed name: **CALVERT, HUBERT**
- Birth year: 1875 (attested in editions [1937, 1939, 1940])
- Honours: C.I.E, C.S.I
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L59433.v` — printed in editions [1937, 1939, 1940]:**

> CALVERT, HUBERT, C.S.I., C.I.E., I.C.S. (ret.), B.Sc.—B. 1875; registr., co-op. socs., Ceylon, Mar., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | registr., co-op. socs. | Ceylon | [1937, 1939, 1940] |

## Candidate stint `Calvert, G. H___Hong Kong___1949`

- Staff-list name: **Calvert, G. H** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. H. Calvert | Corps Quartermaster | Hong Kong Volunteer Defence Corps | — | Captain |
| 1950 | G. H. Calvert | Administrative Officer | HONG KONG DEFENCE FORCE | — | Captain |
| 1951 | G. H. Calvert | Administrative Officer | HONG KONG DEFENCE FORCE | — | Captain |

### Deterministic checks: `calvert_hubert_b1875` vs `Calvert, G. H___Hong Kong___1949`

- [PASS] surname_gate: bio 'CALVERT' vs stint 'Calvert, G. H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1949, birth 1875 (age 74)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Calvert, J. E. H___Uganda___1933`

- Staff-list name: **Calvert, J. E. H** | colony: **Uganda** | listed 1933–1940 | editions [1933, 1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | J. E. H. Calvert | Assistant Factories Inspector | Public Works Department | — | — |
| 1936 | J. E. H. Calvert | Assistant Factories Inspector | Public Works Department | — | — |
| 1939 | J. E. H. Calvert | Assistant Factories Inspector | Public Works Department | — | — |
| 1940 | J. E. H. Calvert | Assistant Factories Inspector | Public Works Department | — | — |

### Deterministic checks: `calvert_hubert_b1875` vs `Calvert, J. E. H___Uganda___1933`

- [PASS] surname_gate: bio 'CALVERT' vs stint 'Calvert, J. E. H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['J', 'E', 'H']
- [PASS] age_gate: stint starts 1933, birth 1875 (age 58)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1940
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

