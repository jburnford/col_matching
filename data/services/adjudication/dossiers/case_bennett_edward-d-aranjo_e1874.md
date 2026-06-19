<!-- {"case_id": "case_bennett_edward-d-aranjo_e1874", "bio_ids": ["bennett_edward-d-aranjo_e1874"], "stint_ids": ["Bennett, E___Zanzibar___1929"]} -->
# Dossier case_bennett_edward-d-aranjo_e1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 86 official(s) with this surname in the graph's staff lists; 34 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bennett_edward-d-aranjo_e1874`

- Printed name: **BENNETT, EDWARD D'ARANJO**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L32062.v` — printed in editions [1888, 1889, 1890]:**

> BENNETT, EDWARD D'ARANJO.—Educated at the government provincial college, Calicut; judicial clerk, subordinate judge's court, South Malabar, June, 1874; teacher in the government English branch school, Straits Settlements, Aug., 1878; had also charge of the Tamil school for a short time; chief clerk, medical department, Feb., 1879; compiler of "Regulations and Orders of the Medical Department."

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | judicial clerk, subordinate judge's court, South Malabar | — | [1888, 1889, 1890] |
| 1 | 1878 | teacher in the government English branch school | Straits Settlements | [1888, 1889, 1890] |
| 2 | 1879 | chief clerk, medical department | Straits Settlements *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Bennett, E___Zanzibar___1929`

- Staff-list name: **Bennett, E** | colony: **Zanzibar** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | E. Bennett | Nursing Sister | Medical Department | — | — |
| 1930 | E. Bennett | Nursing Sister | Medical Department | — | — |

### Deterministic checks: `bennett_edward-d-aranjo_e1874` vs `Bennett, E___Zanzibar___1929`

- [PASS] surname_gate: bio 'BENNETT' vs stint 'Bennett, E' (exact)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E']
- [PASS] age_gate: stint starts 1929; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Zanzibar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1930
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

