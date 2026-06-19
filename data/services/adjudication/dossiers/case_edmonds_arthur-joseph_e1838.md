<!-- {"case_id": "case_edmonds_arthur-joseph_e1838", "bio_ids": ["edmonds_arthur-joseph_e1838"], "stint_ids": ["Edmonds, J___Leeward Islands___1877"]} -->
# Dossier case_edmonds_arthur-joseph_e1838

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `edmonds_arthur-joseph_e1838`

- Printed name: **EDMONDS, ARTHUR JOSEPH**
- Birth year: not printed
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L32906.v` — printed in editions [1889]:**

> EDMONDS, ARTHUR JOSEPH.—Emigrated to South Australia 1838; barrister, supreme court, 1860, and practised for 16 years; appointed stipendiary magistrate, Port Pirie, Jan., 1877, and also returning officer, northern electoral district, in 1883, and still holds both offices.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1838–1838 | — | South Australia | [1889] |
| 1 | 1860–1876 | barrister, supreme court | — | [1889] |
| 2 | 1877 | stipendiary magistrate | — | [1889] |
| 3 | 1883 | returning officer | — | [1889] |

## Candidate stint `Edmonds, J___Leeward Islands___1877`

- Staff-list name: **Edmonds, J** | colony: **Leeward Islands** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Edmonds | No. 2 | Medical Officers | — | — |
| 1878 | J. Edmonds | No. 2 | Medical Officers | — | — |

### Deterministic checks: `edmonds_arthur-joseph_e1838` vs `Edmonds, J___Leeward Islands___1877`

- [PASS] surname_gate: bio 'EDMONDS' vs stint 'Edmonds, J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
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

