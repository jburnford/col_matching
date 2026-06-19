<!-- {"case_id": "case_falls_william-t-b_e1877", "bio_ids": ["falls_william-t-b_e1877"], "stint_ids": ["Falls, W. T. B___Straits Settlements___1880"]} -->
# Dossier case_falls_william-t-b_e1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `falls_william-t-b_e1877`

- Printed name: **FALLS, WILLIAM T. B.**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L27398.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> FALLS, WILLIAM T. B., L.R.C.S.I., L.K.Q.C.P.I., L.M., Dublin Lying-in Hospital, formerly in the P. & O. service. Held the appointment of assistant colonial surgeon, Province Wellesley, Jan., 1877, to Feb., 1879; assistant colonial surgeon, Malacca, April, 1879; colonial surgeon, April, 1879, health officer, municipality, Feb., 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1877–1879 | assistant colonial surgeon | Province Wellesley | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1879 | assistant colonial surgeon | Malacca | [1883, 1886, 1888, 1889, 1890] |
| 2 | 1888 | health officer, municipality | — | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Falls, W. T. B___Straits Settlements___1880`

- Staff-list name: **Falls, W. T. B** | colony: **Straits Settlements** | listed 1880–1889 | editions [1880, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | W. T. B. Falls | Colonial Surgeon | Medical | — | — |
| 1888 | W. T. B. Falls | Colonial Surgeon | Malacca | — | — |
| 1889 | W. T. B. Falls | Official | Malacca | — | — |

### Deterministic checks: `falls_william-t-b_e1877` vs `Falls, W. T. B___Straits Settlements___1880`

- [PASS] surname_gate: bio 'FALLS' vs stint 'Falls, W. T. B' (exact)
- [PASS] initials: bio ['W', 'T', 'B'] ~ stint ['W', 'T', 'B']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1889
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

