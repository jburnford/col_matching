<!-- {"case_id": "case_bateson_edward_e1888", "bio_ids": ["bateson_edward_e1888"], "stint_ids": ["Bateson, E___North Borneo___1933", "Bateson, E___Windward Islands___1905"]} -->
# Dossier case_bateson_edward_e1888

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bateson_edward_e1888'] carry a single initial only — the namesake trap applies.

## Biography `bateson_edward_e1888`

- Printed name: **BATESON, EDWARD**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907]

### Verbatim printed entry text (OCR)

**Version `col1905-L41921.v` — printed in editions [1905, 1906, 1907]:**

> BATESON, EDWARD.—Ed. at Rugby and King's Coll., Camb.; exhibnr., 1888; schlr., 1889; sen. in the historical tripos, 1890; editor of vols. i. and ii. of a "History of Northumberland," issued under the direction of a comtee., 1891-4; called to the bar (Lincoln's Inn), 1896; dist. and stip. mag. in Mauritius, 1901; att.-gen., St. Lucia, 1903.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1888 | exhibnr | — | [1905, 1906, 1907] |
| 1 | 1889 | schlr | — | [1905, 1906, 1907] |
| 2 | 1890 | sen. in the historical tripos | — | [1905, 1906, 1907] |
| 3 | 1891–1894 | editor of vols. i. and ii. of a "History of Northumberland," issued under the direction of a comtee | — | [1905, 1906, 1907] |
| 4 | 1896 | called to the bar (Lincoln's Inn) | — | [1905, 1906, 1907] |
| 5 | 1901 | dist. and stip. mag. in Mauritius | — | [1905, 1906, 1907] |
| 6 | 1903 | att.-gen. | St. Lucia | [1905, 1906, 1907] |

## Candidate stint `Bateson, E___North Borneo___1933`

- Staff-list name: **Bateson, E** | colony: **North Borneo** | listed 1933–1936 | editions [1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | E. Bateson | Mycologist and Agricultural Adviser | Staff | — | — |
| 1936 | E. Bateson | Inspector of Prisons, The Commandant, Mycologist and Agricultural Adviser | Civil Service | — | — |

### Deterministic checks: `bateson_edward_e1888` vs `Bateson, E___North Borneo___1933`

- [PASS] surname_gate: bio 'BATESON' vs stint 'Bateson, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1933; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1936
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bateson, E___Windward Islands___1905`

- Staff-list name: **Bateson, E** | colony: **Windward Islands** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | E. Bateson | Attorney-General | Judicial | — | — |
| 1906 | E. Bateson | Attorney-General | Judicial | — | — |

### Deterministic checks: `bateson_edward_e1888` vs `Bateson, E___Windward Islands___1905`

- [PASS] surname_gate: bio 'BATESON' vs stint 'Bateson, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
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

