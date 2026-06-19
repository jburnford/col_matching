<!-- {"case_id": "case_fowler_reginald-charles-stuchbery-fowler_b1897", "bio_ids": ["fowler_reginald-charles-stuchbery-fowler_b1897"], "stint_ids": ["Fowler, Robert___Canada___1917"]} -->
# Dossier case_fowler_reginald-charles-stuchbery-fowler_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Fowler, Robert___Canada___1917` is also gate-compatible with biography(ies) outside this case: ['fowler_james-robinson_b1875', 'fowler_robert_b1876'] (already linked elsewhere or filtered).

## Biography `fowler_reginald-charles-stuchbery-fowler_b1897`

- Printed name: **FOWLER, Reginald Charles Stuchbery Fowler**
- Birth year: 1897 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L32667.v` — printed in editions [1948]:**

> FOWLER, Reginald Charles Stuchbery Fowler.—b. 1897; ed. Cranbrook Sch.; foreman of wks., P.W.D., Nig., 1926; inspr., 1928; asst. wks man., 1937; wks. man., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | foreman of wks., P.W.D. | Nigeria | [1948] |
| 1 | 1928 | inspr | Nigeria *(inherited from previous clause)* | [1948] |
| 2 | 1937 | asst. wks man | Nigeria *(inherited from previous clause)* | [1948] |
| 3 | 1945 | wks. man | Nigeria *(inherited from previous clause)* | [1948] |

## Candidate stint `Fowler, Robert___Canada___1917`

- Staff-list name: **Fowler, Robert** | colony: **Canada** | listed 1917–1920 | editions [1917, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | Robert Fowler | Assistant Deputy Minister | Post Office Department | — | — |
| 1918 | Robert Fowler | Assistant Deputy Minister | Post Office Department | — | — |
| 1919 | Robert Fowler | Assistant Deputy Minister | Post Office Department | — | — |
| 1920 | Robert Fowler | Superintendent Dead Letter Branch | Post Office Department | — | — |

### Deterministic checks: `fowler_reginald-charles-stuchbery-fowler_b1897` vs `Fowler, Robert___Canada___1917`

- [PASS] surname_gate: bio 'FOWLER' vs stint 'Fowler, Robert' (exact)
- [PASS] initials: bio ['R', 'C', 'S', 'F'] ~ stint ['R']
- [PASS] age_gate: stint starts 1917, birth 1897 (age 20)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1920
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

