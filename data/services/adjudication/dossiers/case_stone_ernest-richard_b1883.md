<!-- {"case_id": "case_stone_ernest-richard_b1883", "bio_ids": ["stone_ernest-richard_b1883"], "stint_ids": ["Stone, E. R___Straits Settlements___1925"]} -->
# Dossier case_stone_ernest-richard_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 45 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stone_ernest-richard_b1883`

- Printed name: **STONE, ERNEST RICHARD**
- Birth year: 1883 (attested in editions [1932, 1933, 1934, 1935])
- Honours: B.A, M.B
- Appears in editions: [1932, 1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `col1932-L64234.v` — printed in editions [1932, 1933, 1934, 1935]:**

> STONE, ERNEST RICHARD, B.A., M.B., B. Chir. (Cantab.), M.R.C.S. (Eng.), L.R.C.P. (Lond.), D.T.M. (Liverpool).—B. 1883; ast. med. supt., central mental hosp., Tanjong Rambutan, Apr., 1921; med. supt., lunatic asylum, Singa- pore, April, 1923; ditto, mental hosp., Jan., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | ast. med. supt., central mental hosp., Tanjong Rambutan | — | [1932, 1933, 1934, 1935] |
| 1 | 1923 | med. supt., lunatic asylum | Singa- pore | [1932, 1933, 1934, 1935] |
| 2 | 1928 | ditto, mental hosp | Singa- pore *(inherited from previous clause)* | [1932, 1933, 1934, 1935] |

## Candidate stint `Stone, E. R___Straits Settlements___1925`

- Staff-list name: **Stone, E. R** | colony: **Straits Settlements** | listed 1925–1934 | editions [1925, 1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | E. R. Stone | Medical Superintendent, Lunatic Asylum | SINGAPORE | — | — |
| 1931 | E. R. Stone | Medical Superintendent, Mental Hospital | Medical | — | — |
| 1933 | E. R. Stone | Medical Superintendent, Mental Hospital | Medical | — | — |
| 1934 | E. R. Stone | Medical Superintendent, Mental Hospital | Singapore | — | — |

### Deterministic checks: `stone_ernest-richard_b1883` vs `Stone, E. R___Straits Settlements___1925`

- [PASS] surname_gate: bio 'STONE' vs stint 'Stone, E. R' (exact)
- [PASS] initials: bio ['E', 'R'] ~ stint ['E', 'R']
- [PASS] age_gate: stint starts 1925, birth 1883 (age 42)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1934
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

