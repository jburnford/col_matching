<!-- {"case_id": "case_lagaite_charles-tristan_b1892", "bio_ids": ["lagaite_charles-tristan_b1892"], "stint_ids": ["Lagait\u00e9, T___Mauritius___1936"]} -->
# Dossier case_lagaite_charles-tristan_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lagaite_charles-tristan_b1892`

- Printed name: **LAGAITE, Charles Tristan**
- Birth year: 1892 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L37090.v` — printed in editions [1950, 1951]:**

> LAGAITE, Charles Tristan.—b. 1892; ed. 2nd cl. teacher of prim. schs.; apptd., Maur., 1913; pay and Q.M., police, 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | apptd. | Mauritius | [1950, 1951] |
| 1 | 1932 | pay and Q.M., police | Mauritius *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Lagaité, T___Mauritius___1936`

- Staff-list name: **Lagaité, T** | colony: **Mauritius** | listed 1936–1937 | editions [1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | T. Lagaité | Pay and Quarter Master | Police Department | — | — |
| 1937 | T. Lagaité | Pay and Quarter Master | Police Department | — | — |

### Deterministic checks: `lagaite_charles-tristan_b1892` vs `Lagaité, T___Mauritius___1936`

- [PASS] surname_gate: bio 'LAGAITE' vs stint 'Lagaité, T' (fuzzy:1)
- [PASS] initials: bio ['C', 'T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1936, birth 1892 (age 44)
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1937
- [FAIL] position_sim: best 58 vs bar 60: 'pay and Q.M., police' ~ 'Pay and Quarter Master'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

