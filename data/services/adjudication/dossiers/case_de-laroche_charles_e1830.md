<!-- {"case_id": "case_de-laroche_charles_e1830", "bio_ids": ["de-laroche_charles_e1830"], "stint_ids": ["de Laroche, C___Mauritius___1877"]} -->
# Dossier case_de-laroche_charles_e1830

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['de-laroche_charles_e1830'] carry a single initial only — the namesake trap applies.

## Biography `de-laroche_charles_e1830`

- Printed name: **DE LAROCHE, CHARLES**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27129.v` — printed in editions [1883]:**

> DE LAROCHE, CHARLES.—Clerk in the audit office, Mauritius, July, 1830; inspector of distilleries, Oct., 1845; superintendent of same, Oct., 1848, and chief clerk of internal revenue department, Oct. 1860.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1830 | Clerk in the audit office | Mauritius | [1883] |
| 1 | 1845 | inspector of distilleries | Mauritius *(inherited from previous clause)* | [1883] |
| 2 | 1848 | superintendent of same | Mauritius *(inherited from previous clause)* | [1883] |
| 3 | 1860 | chief clerk of internal revenue department | Mauritius *(inherited from previous clause)* | [1883] |

## Candidate stint `de Laroche, C___Mauritius___1877`

- Staff-list name: **de Laroche, C** | colony: **Mauritius** | listed 1877–1883 | editions [1877, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. de Laroche | Chief Clerk | General Branch | — | — |
| 1879 | C. de Laroche | Chief Clerk | General Branch | — | — |
| 1880 | C. de Laroche | Chief Clerk | General Branch | — | — |
| 1883 | C. de Laroche | Chief Clerk | General Branch | — | — |

### Deterministic checks: `de-laroche_charles_e1830` vs `de Laroche, C___Mauritius___1877`

- [PASS] surname_gate: bio 'DE LAROCHE' vs stint 'de Laroche, C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Mauritius'
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

