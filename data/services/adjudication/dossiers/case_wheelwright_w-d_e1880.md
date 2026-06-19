<!-- {"case_id": "case_wheelwright_w-d_e1880", "bio_ids": ["wheelwright_w-d_e1880"], "stint_ids": ["Wheelwright, W. D___Natal___1879"]} -->
# Dossier case_wheelwright_w-d_e1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wheelwright_w-d_e1880`

- Printed name: **WHEELWRIGHT, W. D**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1886-L36215.v` — printed in editions [1886, 1888, 1889, 1890, 1894]:**

> WHEELWRIGHT, W. D.—Resident magistrate, Umvoti county, Natal, 18th March, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Resident magistrate, Umvoti county | Natal | [1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Wheelwright, W. D___Natal___1879`

- Staff-list name: **Wheelwright, W. D** | colony: **Natal** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | W. D. Wheelwright | Administrator of Native Law | Magisterial Department and Staff | — | — |
| 1880 | W. D. Wheelwright | Administrator of Native Law | Magisterial Department and Staff | — | — |

### Deterministic checks: `wheelwright_w-d_e1880` vs `Wheelwright, W. D___Natal___1879`

- [PASS] surname_gate: bio 'WHEELWRIGHT' vs stint 'Wheelwright, W. D' (exact)
- [PASS] initials: bio ['W', 'D'] ~ stint ['W', 'D']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1880
- [FAIL] position_sim: best 40 vs bar 60: 'Resident magistrate, Umvoti county' ~ 'Administrator of Native Law'
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

