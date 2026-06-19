<!-- {"case_id": "case_mchattie_a-g_e1874", "bio_ids": ["mchattie_a-g_e1874"], "stint_ids": ["McHattie, A. G___Antigua___1888", "McHattie, A. G___Leeward Islands___1878"]} -->
# Dossier case_mchattie_a-g_e1874

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mchattie_a-g_e1874`

- Printed name: **MCHATTIE, A. G**
- Birth year: not printed
- Honours: M.D, M.R.C.S
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L28507.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894]:**

> MCHATTIE, A. G., M.D., M.R.C.S., England.—Medical officer, district No. 2, Antigua, June, 1874.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | Medical officer, district No. 2 | Antigua | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `McHattie, A. G___Antigua___1888`

- Staff-list name: **McHattie, A. G** | colony: **Antigua** | listed 1888–1896 | editions [1888, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | A. G. McHattie | — | Medical | — | — |
| 1890 | A. G. McHattie | — | Medical | — | — |
| 1894 | A. G. McHattie | — | Medical | — | — |
| 1896 | A. G. McHattie | — | Medical | — | — |

### Deterministic checks: `mchattie_a-g_e1874` vs `McHattie, A. G___Antigua___1888`

- [PASS] surname_gate: bio 'MCHATTIE' vs stint 'McHattie, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Antigua'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1896
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `McHattie, A. G___Leeward Islands___1878`

- Staff-list name: **McHattie, A. G** | colony: **Leeward Islands** | listed 1878–1889 | editions [1878, 1879, 1880, 1883, 1886, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | A. G. McHattie | — | Medical | — | — |
| 1879 | A. G. McHattie | — | Medical | — | — |
| 1880 | Dr. A. G. McHattie | Member | Legislative Council (Local) | — | — |
| 1880 | A. G. McHattie | — | Medical | — | — |
| 1883 | A. G. McHattie | — | Medical | — | — |
| 1886 | A. G. McHattie | Medical, District No. 1 and Public Institutions | Medical | — | — |
| 1889 | A. G. McHattie | Medical Officer | Medical | — | — |
| 1889 | A. G. McHattie | — | Legislative Council (Local) | — | — |

### Deterministic checks: `mchattie_a-g_e1874` vs `McHattie, A. G___Leeward Islands___1878`

- [PASS] surname_gate: bio 'MCHATTIE' vs stint 'McHattie, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1889
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

