<!-- {"case_id": "case_jenks_stuart-dixon_b1869", "bio_ids": ["jenks_stuart-dixon_b1869"], "stint_ids": ["Jenks, Stuart___Canada___1912"]} -->
# Dossier case_jenks_stuart-dixon_b1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jenks_stuart-dixon_b1869`

- Printed name: **JENKS, STUART DIXON**
- Birth year: 1869 (attested in editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919])
- Appears in editions: [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1911-L45821.v` — printed in editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919]:**

> JENKS, STUART DIXON, LL.B., K.C.—B. 1869; ed. Picton Acad., Dalhousie Univ., and Cornell Univ.; called to the bar, 1896; practised law in Amherst, Nova Scotia, 1896-1908; K.C., 1908; dep. atty.-gen., Nova Scotia, 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | called to the bar | — | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 1 | 1896–1908 | practised law in Amherst | Nova Scotia | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 2 | 1908 | K.C | Nova Scotia | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |

## Candidate stint `Jenks, Stuart___Canada___1912`

- Staff-list name: **Jenks, Stuart** | colony: **Canada** | listed 1912–1918 | editions [1912, 1913, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Stuart Jenks | Deputy Attorney-General | Departmental Chiefs and Officers | — | — |
| 1913 | Stuart Jenks | Deputy Attorney-General | Departmental Chiefs and Officers | — | — |
| 1914 | Stuart Jenks | Deputy Attorney-General | Departmental Chiefs and Officers | — | — |
| 1915 | Stuart Jenks | Deputy Attorney-General | Departmental Chiefs and Officers | — | — |
| 1917 | Stuart Jenks | Deputy Attorney-General | Departmental Chiefs and Officers | — | — |
| 1918 | Stuart Jenks | Deputy Attorney-General | Departmental Chiefs and Officers | — | — |

### Deterministic checks: `jenks_stuart-dixon_b1869` vs `Jenks, Stuart___Canada___1912`

- [PASS] surname_gate: bio 'JENKS' vs stint 'Jenks, Stuart' (exact)
- [PASS] initials: bio ['S', 'D'] ~ stint ['S']
- [PASS] age_gate: stint starts 1912, birth 1869 (age 43)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

