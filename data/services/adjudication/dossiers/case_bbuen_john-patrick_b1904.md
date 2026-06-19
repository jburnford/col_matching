<!-- {"case_id": "case_bbuen_john-patrick_b1904", "bio_ids": ["bbuen_john-patrick_b1904"], "stint_ids": ["Bruen, J. P___British Guiana___1949", "Bruen, J. P___Fiji___1950"]} -->
# Dossier case_bbuen_john-patrick_b1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Bruen, J. P___British Guiana___1949` is also gate-compatible with biography(ies) outside this case: ['bruen_john-patrick_b1904'] (already linked elsewhere or filtered).
- NOTE: stint `Bruen, J. P___Fiji___1950` is also gate-compatible with biography(ies) outside this case: ['bruen_john-patrick_b1904'] (already linked elsewhere or filtered).

## Biography `bbuen_john-patrick_b1904`

- Printed name: **BBUEN, JOHN PATRICK**
- Birth year: 1904 (attested in editions [1935])
- Appears in editions: [1935]

### Verbatim printed entry text (OCR)

**Version `dol1935-L57244.v` — printed in editions [1935]:**

> BBUEN, JOHN PATRICK, B.E. (Dub.).—B. 1904; asst. engrn., Br. Guiana, 1930; asst. engrn. to sea defence bd. of comsnrs., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | asst. engrn. | British Guiana | [1935] |
| 1 | 1934 | asst. engrn. to sea defence bd. of comsnrs | British Guiana *(inherited from previous clause)* | [1935] |

## Candidate stint `Bruen, J. P___British Guiana___1949`

- Staff-list name: **Bruen, J. P** | colony: **British Guiana** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. P. Bruen | Deputy Director Drainage, Irrigation and Sea Defences | Public Works Department | — | — |
| 1950 | J. P. Bruen | Deputy Director, Drainage, Irrigation and Sea Defences | Public Works Department | — | — |

### Deterministic checks: `bbuen_john-patrick_b1904` vs `Bruen, J. P___British Guiana___1949`

- [PASS] surname_gate: bio 'BBUEN' vs stint 'Bruen, J. P' (fuzzy:1)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J', 'P']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bruen, J. P___Fiji___1950`

- Staff-list name: **Bruen, J. P** | colony: **Fiji** | listed 1950–1953 | editions [1950, 1951, 1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | J. P. Bruen | Director of Public Works | Public Works | — | — |
| 1951 | J. P. Bruen | Director of Public Works | PUBLIC WORKS | — | — |
| 1952 | J. P. Bruen | Director of Public Works | Civil Establishment | — | — |
| 1953 | J. P. Bruen | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `bbuen_john-patrick_b1904` vs `Bruen, J. P___Fiji___1950`

- [PASS] surname_gate: bio 'BBUEN' vs stint 'Bruen, J. P' (fuzzy:1)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J', 'P']
- [PASS] age_gate: stint starts 1950, birth 1904 (age 46)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1953
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

