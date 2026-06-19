<!-- {"case_id": "case_archibald_william-oliver_e1914-2", "bio_ids": ["archibald_william-oliver_e1914-2"], "stint_ids": ["Archibald, W. O___South Australia___1898"]} -->
# Dossier case_archibald_william-oliver_e1914-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `archibald_william-oliver_e1914-2`

- Printed name: **ARCHIBALD, WILLIAM OLIVER**
- Birth year: not printed
- Appears in editions: [1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1917-L47348.v` — printed in editions [1917, 1918, 1919]:**

> ARCHIBALD, HON. WILLIAM OLIVER.—Mem. for Hindmarsh, S. Australia, in H. of R., C. of A.; min. of home affirs., C. of A., Sept., 1914, to Oct., 1915; min. for trade and customs, 14th Nov., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1915 | min. of home affirs. | Commonwealth of Australia | [1917, 1918, 1919] |
| 1 | 1916 | min. for trade and customs | — | [1917, 1918, 1919] |
| 2 | ? | Mem. for Hindmarsh | South Australia | [1917, 1918, 1919] |

## Candidate stint `Archibald, W. O___South Australia___1898`

- Staff-list name: **Archibald, W. O** | colony: **South Australia** | listed 1898–1906 | editions [1898, 1900, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | W. O. Archibald | Member | House of Assembly | — | — |
| 1900 | W. O. Archibald | Member, House of Assembly (Port Adelaide) | House of Assembly | — | — |
| 1906 | W. O. Archibald | Member | House of Assembly | — | — |

### Deterministic checks: `archibald_william-oliver_e1914-2` vs `Archibald, W. O___South Australia___1898`

- [PASS] surname_gate: bio 'ARCHIBALD' vs stint 'Archibald, W. O' (exact)
- [PASS] initials: bio ['W', 'O'] ~ stint ['W', 'O']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1906
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

