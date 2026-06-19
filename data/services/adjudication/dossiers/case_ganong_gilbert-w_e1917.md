<!-- {"case_id": "case_ganong_gilbert-w_e1917", "bio_ids": ["ganong_gilbert-w_e1917"], "stint_ids": ["Ganong, Gilbert W___Canada___1897"]} -->
# Dossier case_ganong_gilbert-w_e1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ganong_gilbert-w_e1917`

- Printed name: **GANONG, GILBERT W**
- Birth year: not printed
- Appears in editions: [1918]

### Verbatim printed entry text (OCR)

**Version `col1918-L50683.v` — printed in editions [1918]:**

> GANONG, GILBERT W.—Lieut.-gov., New Brunswick, 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | Lieut.-gov. | New Brunswick | [1918] |

## Candidate stint `Ganong, Gilbert W___Canada___1897`

- Staff-list name: **Ganong, Gilbert W** | colony: **Canada** | listed 1897–1908 | editions [1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | Gilbert W. Ganong | Member for Charlotte | Province of New Brunswick | — | — |
| 1898 | Gilbert W. Ganong | — | — | — | — |
| 1899 | Gilbert W. Ganong | — | — | — | — |
| 1900 | Gilbert W. Ganong | — | Members | — | — |
| 1905 | Gilbert W. Ganong | — | — | — | — |
| 1906 | Gilbert W. Ganong | — | — | — | — |
| 1907 | Gilbert W. Ganong | — | Province of New Brunswick | — | — |
| 1908 | Gilbert W. Ganong | — | — | — | — |

### Deterministic checks: `ganong_gilbert-w_e1917` vs `Ganong, Gilbert W___Canada___1897`

- [PASS] surname_gate: bio 'GANONG' vs stint 'Ganong, Gilbert W' (exact)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G', 'W']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1908
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

