<!-- {"case_id": "case_lawton_john-gilbert_b1887", "bio_ids": ["lawton_john-gilbert_b1887"], "stint_ids": ["Lawton, J. G___Nigeria___1915"]} -->
# Dossier case_lawton_john-gilbert_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lawton_john-gilbert_b1887`

- Printed name: **LAWTON, JOHN GILBERT**
- Birth year: 1887 (attested in editions [1931])
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L66048.v` — printed in editions [1931]:**

> LAWTON, JOHN GILBERT.—B. 1887; ed. Harrow and Christ Church, Oxford; astt. dist. commr., S. Nigeria, 1911; cls. I, grade I, admstve. serv., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | astt. dist. commr. | Southern Nigeria | [1931] |
| 1 | 1928 | cls. I, grade I, admstve. serv | Southern Nigeria *(inherited from previous clause)* | [1931] |

## Candidate stint `Lawton, J. G___Nigeria___1915`

- Staff-list name: **Lawton, J. G** | colony: **Nigeria** | listed 1915–1919 | editions [1915, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | J. G. Lawton | Sixty Assistant District Officers | NORTHERN PROVINCES | — | — |
| 1918 | J. G. Lawton | Assistant District Officer | Southern Provinces | — | — |
| 1919 | J. G. Lawton | Sixty Assistant District Officers | SOUTHERN PROVINCES | — | — |

### Deterministic checks: `lawton_john-gilbert_b1887` vs `Lawton, J. G___Nigeria___1915`

- [PASS] surname_gate: bio 'LAWTON' vs stint 'Lawton, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1915, birth 1887 (age 28)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1915-1919
- [FAIL] position_sim: best 46 vs bar 60: 'astt. dist. commr.' ~ 'Sixty Assistant District Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

