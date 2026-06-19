<!-- {"case_id": "case_gratiaen_e_e1858", "bio_ids": ["gratiaen_e_e1858"], "stint_ids": ["Gratiaen, E___Ceylon___1877", "Gratiaen, E___Ceylon___1888"]} -->
# Dossier case_gratiaen_e_e1858

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gratiaen_e_e1858'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Gratiaen, E___Ceylon___1877` is also gate-compatible with biography(ies) outside this case: ['gratiaen_e_e1868'] (already linked elsewhere or filtered).
- NOTE: stint `Gratiaen, E___Ceylon___1888` is also gate-compatible with biography(ies) outside this case: ['gratiaen_e_e1868'] (already linked elsewhere or filtered).

## Biography `gratiaen_e_e1858`

- Printed name: **GRATIAEN, E**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1883-L27745.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1896, 1897]:**

> GRATIAEN, E.—Assistant colonial surgeon, Ceylon, 1858.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858 | Assistant colonial surgeon | Ceylon | [1883, 1886, 1888, 1889, 1890, 1896, 1897] |

## Candidate stint `Gratiaen, E___Ceylon___1877`

- Staff-list name: **Gratiaen, E** | colony: **Ceylon** | listed 1877–1880 | editions [1877, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. Gratiaen | Assistant Colonial Surgeons | Medical Department | — | — |
| 1879 | E. Gratiaen | Assistant Colonial Surgeons | Medical Department | — | — |
| 1880 | E. Gratiaen | Assistant Colonial Surgeons | Medical Department | — | — |

### Deterministic checks: `gratiaen_e_e1858` vs `Gratiaen, E___Ceylon___1877`

- [PASS] surname_gate: bio 'GRATIAEN' vs stint 'Gratiaen, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Gratiaen, E___Ceylon___1888`

- Staff-list name: **Gratiaen, E** | colony: **Ceylon** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | E. Gratiaen | Assistant Colonial Surgeon | Medical Department | — | — |
| 1889 | E. Gratiaen | Assistant Colonial Surgeon | Medical Department | — | — |

### Deterministic checks: `gratiaen_e_e1858` vs `Gratiaen, E___Ceylon___1888`

- [PASS] surname_gate: bio 'GRATIAEN' vs stint 'Gratiaen, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1889
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

