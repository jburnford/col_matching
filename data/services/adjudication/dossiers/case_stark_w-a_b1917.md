<!-- {"case_id": "case_stark_w-a_b1917", "bio_ids": ["stark_w-a_b1917"], "stint_ids": ["Stark, W. A___Sierra Leone___1950"]} -->
# Dossier case_stark_w-a_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stark_w-a_b1917`

- Printed name: **STARK, W. A**
- Birth year: 1917 (attested in editions [1959])
- Appears in editions: [1959]

### Verbatim printed entry text (OCR)

**Version `col1959-L28207.v` — printed in editions [1959]:**

> STARK, W. A.—b. 1917; ed. Berwick-on-Tweed Gram. Sch.; admin. sec., medical dept., S. Leone, 1947-51; gen. sec., medical dept., Gold Coast 1951 (Ghana civil serv.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947–1951 | admin. sec., medical dept., S. Leone | — | [1959] |
| 1 | 1951 | gen. sec., medical dept. | Gold Coast | [1959] |

## Candidate stint `Stark, W. A___Sierra Leone___1950`

- Staff-list name: **Stark, W. A** | colony: **Sierra Leone** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | W. A. Stark | Secretary | Medical | — | — |
| 1951 | W. A. Stark | Secretary | Medical | — | — |

### Deterministic checks: `stark_w-a_b1917` vs `Stark, W. A___Sierra Leone___1950`

- [PASS] surname_gate: bio 'STARK' vs stint 'Stark, W. A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1950, birth 1917 (age 33)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

