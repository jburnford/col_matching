<!-- {"case_id": "case_moahon_cecil_e1909", "bio_ids": ["moahon_cecil_e1909"], "stint_ids": ["Mahon, C. A___Jamaica___1949", "Mahon, C. A___Windward Islands___1922"]} -->
# Dossier case_moahon_cecil_e1909

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['moahon_cecil_e1909'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Mahon, C. A___Jamaica___1949` is also gate-compatible with biography(ies) outside this case: ['mahon_campbell-alleyne_b1916'] (already linked elsewhere or filtered).

## Biography `moahon_cecil_e1909`

- Printed name: **MOAHON, CECIL**
- Birth year: not printed
- Appears in editions: [1925]

### Verbatim printed entry text (OCR)

**Version `col1925-L57635.v` — printed in editions [1925]:**

> MOAHON, CECIL.—Knt. S. Rhodesia civ. serv., Nov., 1909; served S. African rebellion and German S.W. African campaign, 1914-15; served E. Africa campaign with 1st Rhodesian Regt., 1915-18; capt. and adjt., 8th S. African Inf. Regt.; "1914-15" Star and M.C.; astt. polit. offr., Tanganyika Territory, 6th Mar., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | civ. serv. | Southern Rhodesia | [1925] |
| 1 | 1914–1915 | served S. African rebellion and German S.W. African campaign | — | [1925] |
| 2 | 1915–1918 | served E. Africa campaign with 1st Rhodesian Regt. | East Africa | [1925] |
| 3 | 1918 | astt. polit. offr. | Tanganyika Territory | [1925] |

## Candidate stint `Mahon, C. A___Jamaica___1949`

- Staff-list name: **Mahon, C. A** | colony: **Jamaica** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. A. Mahon | Senior Assistant Superintendents of Police | POLICE | — | — |
| 1950 | C. A. Mahon | Senior Assistant Superintendent of Police | Police | — | — |
| 1951 | C. A. Mahon | Senior Assistant Superintendent of Police | POLICE | — | — |

### Deterministic checks: `moahon_cecil_e1909` vs `Mahon, C. A___Jamaica___1949`

- [PASS] surname_gate: bio 'MOAHON' vs stint 'Mahon, C. A' (fuzzy:1)
- [PASS] initials: bio ['C'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Mahon, C. A___Windward Islands___1922`

- Staff-list name: **Mahon, C. A** | colony: **Windward Islands** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | C. A. Mahon | Clerk, Guyana Revenue Office | Revenue Officers | — | — |
| 1923 | C. A. Mahon | Clerk, Goyave Revenue Office | Revenue Officers | — | — |

### Deterministic checks: `moahon_cecil_e1909` vs `Mahon, C. A___Windward Islands___1922`

- [PASS] surname_gate: bio 'MOAHON' vs stint 'Mahon, C. A' (fuzzy:1)
- [PASS] initials: bio ['C'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
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

