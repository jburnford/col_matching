<!-- {"case_id": "case_sheffield_william_b1915", "bio_ids": ["sheffield_william_b1915"], "stint_ids": ["Sheffield, W. R___Gold Coast___1930"]} -->
# Dossier case_sheffield_william_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sheffield_william_b1915'] carry a single initial only — the namesake trap applies.

## Biography `sheffield_william_b1915`

- Printed name: **SHEFFIELD, William**
- Birth year: 1915 (attested in editions [1957])
- Honours: C.P.H, M.B
- Appears in editions: [1951, 1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L27135.v` — printed in editions [1957]:**

> SHEFFIELD, W.—b. 1915; ed. Pocklington Sch. and Leeds Univ.; mil. serv., 1940-46, maj.; M.O., N. Rhod., 1946; S.M.O., 1953; secon., fedl. gov't.

**Version `col1951-L42438.v` — printed in editions [1951]:**

> SHEFFIELD, William, M.B., Ch.B., C.P.H.—b. 1915; ed. Pocklington Sch. and Leeds Univ.; on mil. serv., 1940-46, maj.; med. offr., N. Rhod., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O. | Northern Rhodesia | [1951, 1957] |
| 1 | 1953 | S.M.O | Northern Rhodesia *(inherited from previous clause)* | [1957] |

## Candidate stint `Sheffield, W. R___Gold Coast___1930`

- Staff-list name: **Sheffield, W. R** | colony: **Gold Coast** | listed 1930–1936 | editions [1930, 1932, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | W. R. Sheffield | Public Health Engineers | III. Public Health Engineering Staff | — | — |
| 1932 | W. R. Sheffield | Public Health Engineer | Public Works Department | — | — |
| 1936 | W. R. Sheffield | Public Health Engineer | Public Works Department | — | — |

### Deterministic checks: `sheffield_william_b1915` vs `Sheffield, W. R___Gold Coast___1930`

- [PASS] surname_gate: bio 'SHEFFIELD' vs stint 'Sheffield, W. R' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1930, birth 1915 (age 15)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1936
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

