<!-- {"case_id": "case_mitchell_o_e1905", "bio_ids": ["mitchell_o_e1905"], "stint_ids": ["Mitchell, O___Gold Coast___1911", "Mitchell, O___Northern Rhodesia___1949", "Mitchell, O___Sierra Leone___1917"]} -->
# Dossier case_mitchell_o_e1905

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 118 official(s) with this surname in the graph's staff lists; 46 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mitchell_o_e1905'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Mitchell, O___Gold Coast___1911` is also gate-compatible with biography(ies) outside this case: ['mitchell_owen_e1905'] (already linked elsewhere or filtered).
- NOTE: stint `Mitchell, O___Northern Rhodesia___1949` is also gate-compatible with biography(ies) outside this case: ['mitchell_owen_b1908', 'mitchell_owen_e1905'] (already linked elsewhere or filtered).
- NOTE: stint `Mitchell, O___Sierra Leone___1917` is also gate-compatible with biography(ies) outside this case: ['mitchell_owen_e1905'] (already linked elsewhere or filtered).

## Biography `mitchell_o_e1905`

- Printed name: **MITCHELL, O**
- Birth year: not printed
- Appears in editions: [1910]

### Verbatim printed entry text (OCR)

**Version `col1910-L47607.v` — printed in editions [1910]:**

> MITCHELL, O. — Customs asst., E.A.P., 9th Jan., 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1905 | Customs asst. | East Africa Protectorate | [1910] |

## Candidate stint `Mitchell, O___Gold Coast___1911`

- Staff-list name: **Mitchell, O** | colony: **Gold Coast** | listed 1911–1919 | editions [1911, 1913, 1914, 1915, 1917, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | O. Mitchell | Assistant Comptroller | Customs | — | — |
| 1913 | O. Mitchell | Assistant Comptroller | Customs | — | — |
| 1914 | O. Mitchell | Assistant Comptroller | Customs | — | — |
| 1915 | O. Mitchell | Assistant Comptroller | Customs Department | — | — |
| 1917 | O. Mitchell | Assistant Comptroller | Customs Department | — | — |
| 1919 | O. Mitchell | Comptroller | Customs Department | — | — |

### Deterministic checks: `mitchell_o_e1905` vs `Mitchell, O___Gold Coast___1911`

- [PASS] surname_gate: bio 'MITCHELL' vs stint 'Mitchell, O' (exact)
- [PASS] initials: bio ['O'] ~ stint ['O']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Mitchell, O___Northern Rhodesia___1949`

- Staff-list name: **Mitchell, O** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | O. Mitchell | Senior Assistant Superintendents and Assistant Superintendents of Police | POLICE | — | — |
| 1951 | O. Mitchell | Superintendent | Police | — | — |

### Deterministic checks: `mitchell_o_e1905` vs `Mitchell, O___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'MITCHELL' vs stint 'Mitchell, O' (exact)
- [PASS] initials: bio ['O'] ~ stint ['O']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Mitchell, O___Sierra Leone___1917`

- Staff-list name: **Mitchell, O** | colony: **Sierra Leone** | listed 1917–1918 | editions [1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | O. Mitchell | Comptroller of Customs | Customs Department | — | — |
| 1918 | O. Mitchell | Comptroller of Customs | Customs Department | — | — |

### Deterministic checks: `mitchell_o_e1905` vs `Mitchell, O___Sierra Leone___1917`

- [PASS] surname_gate: bio 'MITCHELL' vs stint 'Mitchell, O' (exact)
- [PASS] initials: bio ['O'] ~ stint ['O']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1918
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

