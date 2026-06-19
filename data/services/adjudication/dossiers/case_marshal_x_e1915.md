<!-- {"case_id": "case_marshal_x_e1915", "bio_ids": ["marshal_x_e1915"], "stint_ids": ["Marshal, F. W___Lagos___1896", "Marshal, N___British Guiana___1890"]} -->
# Dossier case_marshal_x_e1915

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['marshal_x_e1915'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Marshal, F. W___Lagos___1896` is also gate-compatible with biography(ies) outside this case: ['marshal_fred-wm_e1892'] (already linked elsewhere or filtered).

## Biography `marshal_x_e1915`

- Printed name: **MARSHAL, (no given names printed)**
- Birth year: not printed
- Appears in editions: [1925]

### Verbatim printed entry text (OCR)

**Version `col1925-L54154.v` — printed in editions [1925]:**

> MARSHAL, H.B.M. Court for Zanzibar (in Prize), 26th Jan. to 15th Aug., 1915, and from 19th Dec., 1917; imigrn. offr., 23rd Sept., 1915; asst. compt., cust., Tanganyika Territory, 15th Oct., 1920; ag. compt., cust., 14th Feb. to 8th Dec., 1921, 26th Sept., 1922 to 17th Jan., 1923 and from 18th Oct., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | — | Zanzibar | [1925] |
| 1 | 1915–1915 | imigrn. offr. | — | [1925] |
| 2 | 1920–1920 | asst. compt., cust. | Tanganyika Territory | [1925] |
| 3 | 1921 | ag. compt., cust. | — | [1925] |

## Candidate stint `Marshal, F. W___Lagos___1896`

- Staff-list name: **Marshal, F. W** | colony: **Lagos** | listed 1896–1899 | editions [1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | F. W. Marshal | Local Auditor | Audit Office | — | — |
| 1897 | F. W. Marshal | Local Auditor | Audit Office | — | — |
| 1898 | F. W. Marshal | Local Auditor | Audit Office | — | — |
| 1899 | F. W. Marshal | Local Auditor | Audit Office | — | — |

### Deterministic checks: `marshal_x_e1915` vs `Marshal, F. W___Lagos___1896`

- [PASS] surname_gate: bio 'MARSHAL' vs stint 'Marshal, F. W' (exact)
- [PASS] initials: bio ['?'] ~ stint ['F', 'W']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Lagos'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1899
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Marshal, N___British Guiana___1890`

- Staff-list name: **Marshal, N** | colony: **British Guiana** | listed 1890–1900 | editions [1890, 1894, 1896, 1897, 1898, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | N. Marshal | Steward and Dispenser | Medical Institutions | — | — |
| 1894 | N. Marshal | Steward and Dispenser | Medical Institutions | — | — |
| 1896 | N. Marshal | Steward and Dispenser | Medical Institutions | — | — |
| 1897 | N. Marshal | Steward and Dispenser | Medical Institutions | — | — |
| 1898 | N. Marshal | Steward and Dispenser | Medical Institutions | — | — |
| 1900 | N. Marshal | Steward and Dispenser | Medical Institutions | — | — |

### Deterministic checks: `marshal_x_e1915` vs `Marshal, N___British Guiana___1890`

- [PASS] surname_gate: bio 'MARSHAL' vs stint 'Marshal, N' (exact)
- [PASS] initials: bio ['?'] ~ stint ['N']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1900
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

