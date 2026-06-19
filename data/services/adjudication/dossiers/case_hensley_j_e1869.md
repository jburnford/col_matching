<!-- {"case_id": "case_hensley_j_e1869", "bio_ids": ["hensley_j_e1869"], "stint_ids": ["Hensley, Joseph___Canada___1877"]} -->
# Dossier case_hensley_j_e1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hensley_j_e1869'] carry a single initial only — the namesake trap applies.

## Biography `hensley_j_e1869`

- Printed name: **HENSLEY, J**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L27963.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> HENSLEY, J.—Vice-chancellor and assistant judge of the supreme court, Prince Edward Island, 1869.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Vice-chancellor and assistant judge of the supreme court | Prince Edward Island | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Hensley, Joseph___Canada___1877`

- Staff-list name: **Hensley, Joseph** | colony: **Canada** | listed 1877–1888 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Joseph Hensley | Vice-Chancellor and Assistant Judge of the Supreme Court | Judicial Establishment, Supreme Court | — | — |
| 1878 | Joseph Hensley | Vice-Chancellor and Assistant Judge of the Supreme Court | — | — | — |
| 1879 | Joseph Hensley | Vice-Chancellor and Assistant Judge of the Supreme Court | — | — | — |
| 1880 | Joseph Hensley | Vice-Chancellor and Assistant Judge of the Supreme Court | — | — | — |
| 1883 | Hon. Joseph Hensley | Vice-Chancellor and Assistant Judge of the Supreme Court | Judicial Establishment, Supreme Court | — | — |
| 1886 | Joseph Hensley | Vice-Chancellor and Assistant Judge of the Supreme Court | Judicial Establishment, Supreme Court | — | — |
| 1888 | Hon. Joseph Hensley | Vice-Chancellor and Assistant Judge of the Supreme Court | Judicial Establishment, Supreme Court | — | — |

### Deterministic checks: `hensley_j_e1869` vs `Hensley, Joseph___Canada___1877`

- [PASS] surname_gate: bio 'HENSLEY' vs stint 'Hensley, Joseph' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1888
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

