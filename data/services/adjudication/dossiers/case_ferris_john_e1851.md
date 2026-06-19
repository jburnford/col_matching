<!-- {"case_id": "case_ferris_john_e1851", "bio_ids": ["ferris_john_e1851"], "stint_ids": ["Ferris, James M___Canada___1880"]} -->
# Dossier case_ferris_john_e1851

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['ferris_john_e1851'] carry a single initial only — the namesake trap applies.

## Biography `ferris_john_e1851`

- Printed name: **FERRIS, John**
- Birth year: not printed
- Terminal: retired 1887 — “retired July, 1887.”
- Appears in editions: [1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L33066.v` — printed in editions [1889, 1890]:**

> FERRIS, John.—Govt. printer, Victoria, Nov., 1851; J.P., 1857; was several years chairman of Tender Bd.; in 1882 received honour of "Officer of Public Instruction of France;" retired July, 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1851 | Govt. printer | Victoria | [1889, 1890] |
| 1 | 1857 | J.P. | — | [1889, 1890] |
| 2 | 1882 | — | — | [1889, 1890] |

## Candidate stint `Ferris, James M___Canada___1880`

- Staff-list name: **Ferris, James M** | colony: **Canada** | listed 1880–1886 | editions [1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | James M. Ferris | — | — | — | — |
| 1883 | James M. Ferris | — | — | — | — |
| 1886 | James M. Ferris | — | — | — | — |

### Deterministic checks: `ferris_john_e1851` vs `Ferris, James M___Canada___1880`

- [PASS] surname_gate: bio 'FERRIS' vs stint 'Ferris, James M' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1886
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

