<!-- {"case_id": "case_ondaatje_s-d-j_e1840", "bio_ids": ["ondaatje_s-d-j_e1840"], "stint_ids": ["Ondaatje, S___Ceylon___1877"]} -->
# Dossier case_ondaatje_s-d-j_e1840

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ondaatje_s-d-j_e1840`

- Printed name: **ONDAATJE, S. D. J**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28939.v` — printed in editions [1883]:**

> ONDAATJE, REV. S. D. J.—Colonial chaplain of Jaffna, Ceylon, Dec. 1840; resigned that appointment, September, 1842; colonial chaplain of St. Thomas' Church, Colombo, in that colony, Dec. 1861.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1840 | Colonial chaplain of Jaffna | Ceylon | [1883] |
| 1 | 1842 | resigned that appointment | Ceylon *(inherited from previous clause)* | [1883] |
| 2 | 1861 | colonial chaplain of St. Thomas' Church, Colombo, in that colony | Ceylon *(inherited from previous clause)* | [1883] |

## Candidate stint `Ondaatje, S___Ceylon___1877`

- Staff-list name: **Ondaatje, S** | colony: **Ceylon** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | S. Ondaatje | Colonial Chaplain | Colonial Chaplains | — | — |
| 1878 | S. Ondaatje | — | Ecclesiastical Department | — | — |
| 1879 | S. Ondaatje | Colonial Chaplain | Ecclesiastical Department | — | — |
| 1880 | S. Ondaatje | Colonial Chaplain | Ecclesiastical Department | — | — |
| 1883 | S. Ondaatje | Colonial Chaplain | Ecclesiastical Department | — | — |

### Deterministic checks: `ondaatje_s-d-j_e1840` vs `Ondaatje, S___Ceylon___1877`

- [PASS] surname_gate: bio 'ONDAATJE' vs stint 'Ondaatje, S' (exact)
- [PASS] initials: bio ['S', 'D', 'J'] ~ stint ['S']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

