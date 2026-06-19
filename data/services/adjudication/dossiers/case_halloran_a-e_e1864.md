<!-- {"case_id": "case_halloran_a-e_e1864", "bio_ids": ["halloran_a-e_e1864"], "stint_ids": ["Halloran, Arthur Edward___Queensland___1878"]} -->
# Dossier case_halloran_a-e_e1864

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `halloran_a-e_e1864`

- Printed name: **HALLORAN, A. E**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L33883.v` — printed in editions [1886, 1888, 1889, 1890]:**

> HALLORAN, A. E.—Sheriff, Queensland, 24th Feb., 1864.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864 | Sheriff | Queensland | [1886, 1888, 1889, 1890] |

## Candidate stint `Halloran, Arthur Edward___Queensland___1878`

- Staff-list name: **Halloran, Arthur Edward** | colony: **Queensland** | listed 1878–1888 | editions [1878, 1879, 1880, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | Arthur Edward Halloran | Sheriff | Attorney-General's Department | — | — |
| 1879 | Arthur Edward Halloran | Sheriff | Attorney-General's Department | — | — |
| 1880 | Arthur Edward Halloran | Sheriff | Attorney-General's Department | — | — |
| 1883 | Arthur Edward Halloran | Sheriff | Attorney-General's Department | — | — |
| 1886 | Arthur Edward Halloran | Sheriff | Attorney-General's Department | — | — |
| 1888 | Arthur Edward Halloran | Sheriff | Attorney-General's Department | — | — |

### Deterministic checks: `halloran_a-e_e1864` vs `Halloran, Arthur Edward___Queensland___1878`

- [PASS] surname_gate: bio 'HALLORAN' vs stint 'Halloran, Arthur Edward' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Queensland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1888
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

