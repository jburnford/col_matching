<!-- {"case_id": "case_linley_richard-philip_e1865", "bio_ids": ["linley_richard-philip_e1865"], "stint_ids": ["Linley, R. P___St Vincent___1879", "Linley, R. P___Windward Islands___1877"]} -->
# Dossier case_linley_richard-philip_e1865

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `linley_richard-philip_e1865`

- Printed name: **LINLEY, RICHARD PHILIP**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L28393.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> LINLEY, RICHARD PHILIP.—Harbour master, St. Vincent, 1865.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865 | Harbour master | St. Vincent | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Linley, R. P___St Vincent___1879`

- Staff-list name: **Linley, R. P** | colony: **St Vincent** | listed 1879–1888 | editions [1879, 1880, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | R. P. Linley | Harbour Master | Civil Establishment | — | — |
| 1880 | R. P. Linley | Harbour Master | Civil Establishment | — | — |
| 1888 | R. P. Linley | Harbour Master | Civil Establishment | — | — |

### Deterministic checks: `linley_richard-philip_e1865` vs `Linley, R. P___St Vincent___1879`

- [PASS] surname_gate: bio 'LINLEY' vs stint 'Linley, R. P' (exact)
- [PASS] initials: bio ['R', 'P'] ~ stint ['R', 'P']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'St Vincent'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1888
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Linley, R. P___Windward Islands___1877`

- Staff-list name: **Linley, R. P** | colony: **Windward Islands** | listed 1877–1889 | editions [1877, 1878, 1880, 1883, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. P. Linley | Harbour Master | Civil Establishment | — | — |
| 1878 | R. P. Linley | Harbour Master | Civil Establishment | — | — |
| 1880 | R. P. Linley | Harbour Master | Civil Establishment | — | — |
| 1883 | R. P. Linley | Harbour Master | Civil Establishment | — | — |
| 1889 | R. P. Linley | Harbour Master | Civil Establishment | — | — |

### Deterministic checks: `linley_richard-philip_e1865` vs `Linley, R. P___Windward Islands___1877`

- [PASS] surname_gate: bio 'LINLEY' vs stint 'Linley, R. P' (exact)
- [PASS] initials: bio ['R', 'P'] ~ stint ['R', 'P']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1889
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

