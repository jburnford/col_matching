<!-- {"case_id": "case_jack_r-l_e1867", "bio_ids": ["jack_r-l_e1867"], "stint_ids": ["Jack, R. L___Australia___1918"]} -->
# Dossier case_jack_r-l_e1867

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jack_r-l_e1867`

- Printed name: **JACK, R. L**
- Birth year: not printed
- Appears in editions: [1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1897-L32687.v` — printed in editions [1897, 1898]:**

> JACK, R. L.—Ed. Edin. Univ.; employed on Geological Survey, Scotland, 1867-77; govt. geologist, Queensland, 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1867–1877 | employed on Geological Survey, Scotland | — | [1897, 1898] |
| 1 | 1877 | govt. geologist | Queensland | [1897, 1898] |

## Candidate stint `Jack, R. L___Australia___1918`

- Staff-list name: **Jack, R. L** | colony: **Australia** | listed 1918–1927 | editions [1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | R. L. Jack | Assistant Government Geologist | Mines Department | — | — |
| 1927 | R. L. Jack | Deputy Government Geologist | MINES | — | — |

### Deterministic checks: `jack_r-l_e1867` vs `Jack, R. L___Australia___1918`

- [PASS] surname_gate: bio 'JACK' vs stint 'Jack, R. L' (exact)
- [PASS] initials: bio ['R', 'L'] ~ stint ['R', 'L']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1927
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

