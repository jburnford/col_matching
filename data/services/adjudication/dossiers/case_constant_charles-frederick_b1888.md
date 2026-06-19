<!-- {"case_id": "case_constant_charles-frederick_b1888", "bio_ids": ["constant_charles-frederick_b1888"], "stint_ids": ["Constant, C. F___Straits Settlements___1931"]} -->
# Dossier case_constant_charles-frederick_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `constant_charles-frederick_b1888`

- Printed name: **CONSTANT, CHARLES FREDERICK**
- Birth year: 1888 (attested in editions [1935, 1936])
- Appears in editions: [1932, 1933, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `dol1935-L57728.v` — printed in editions [1935, 1936]:**

> CONSTANT, CHARLES FREDERICK, M.R.C.S. (Eng.), L.R.C.P. (Lond.).—B. 1888; radiologist, F.M.S., Apr., 1924; do., col. hosp., Port-of-Spain, Trinidad, Jan., 1934.

**Version `col1932-L59267.v` — printed in editions [1932, 1933]:**

> CONSTANT, CHARLES FREDERICK, M.R.C.S. (Eng.), L.R.C.P. (Lond.).—B. 1888; radiologist, F.M.S., Apr., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | radiologist | Federated Malay States | [1932, 1933, 1935, 1936] |
| 1 | 1934 | do., col. hosp., Port-of-Spain | Trinidad | [1935, 1936] |

## Candidate stint `Constant, C. F___Straits Settlements___1931`

- Staff-list name: **Constant, C. F** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | C. F. Constant | Radiologist | Medical | — | — |
| 1932 | C. F. Constant | Radiologist | Medical | — | — |
| 1933 | C. F. Constant | Radiologist | Medical | — | — |

### Deterministic checks: `constant_charles-frederick_b1888` vs `Constant, C. F___Straits Settlements___1931`

- [PASS] surname_gate: bio 'CONSTANT' vs stint 'Constant, C. F' (exact)
- [PASS] initials: bio ['C', 'F'] ~ stint ['C', 'F']
- [PASS] age_gate: stint starts 1931, birth 1888 (age 43)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

