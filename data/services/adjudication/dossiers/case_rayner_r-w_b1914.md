<!-- {"case_id": "case_rayner_r-w_b1914", "bio_ids": ["rayner_r-w_b1914"], "stint_ids": ["Rayner, R. W___Kenya___1950"]} -->
# Dossier case_rayner_r-w_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rayner_r-w_b1914`

- Printed name: **RAYNER, R. W**
- Birth year: 1914 (attested in editions [1958, 1959, 1960])
- Appears in editions: [1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1958-L26264.v` — printed in editions [1958, 1959, 1960]:**

> RAYNER, R. W.—b. 1914; ed. Latymer Upper Sch., Hammersmith, King's Coll., Camb. and I.C.T.A.; plant pathol. and physiol., coffee services, Ken., 1940-59; publs. concerning larger fungi of Trinidad, coffee flowering, growth and diseases, especially "tonic" spraying and control of leaf rust.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940–1959 | plant pathol. and physiol., coffee services | Kenya | [1958, 1959, 1960] |

## Candidate stint `Rayner, R. W___Kenya___1950`

- Staff-list name: **Rayner, R. W** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. W. Rayner | Plant Pathologist | AGRICULTURE | — | — |
| 1951 | R. W. Rayner | Plant Pathologist | Agriculture | — | — |

### Deterministic checks: `rayner_r-w_b1914` vs `Rayner, R. W___Kenya___1950`

- [PASS] surname_gate: bio 'RAYNER' vs stint 'Rayner, R. W' (exact)
- [PASS] initials: bio ['R', 'W'] ~ stint ['R', 'W']
- [PASS] age_gate: stint starts 1950, birth 1914 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 53 vs bar 60: 'plant pathol. and physiol., coffee services' ~ 'Plant Pathologist'
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

