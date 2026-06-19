<!-- {"case_id": "case_gibbe_john_b1881", "bio_ids": ["gibbe_john_b1881"], "stint_ids": ["Gibbe, H. J___Straits Settlements___1913"]} -->
# Dossier case_gibbe_john_b1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gibbe_john_b1881'] carry a single initial only — the namesake trap applies.

## Biography `gibbe_john_b1881`

- Printed name: **GIBBE, JOHN**
- Birth year: 1881 (attested in editions [1929])
- Appears in editions: [1929]

### Verbatim printed entry text (OCR)

**Version `col1929-L60483.v` — printed in editions [1929]:**

> GIBBE, JOHN.—B. 1881; supervisor of warehouses, govt. stores, Ceylon, Oct., 1914; col. storekeeper, Sept., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | supervisor of warehouses, govt. stores | Ceylon | [1929] |
| 1 | 1916 | col. storekeeper | Ceylon *(inherited from previous clause)* | [1929] |

## Candidate stint `Gibbe, H. J___Straits Settlements___1913`

- Staff-list name: **Gibbe, H. J** | colony: **Straits Settlements** | listed 1913–1915 | editions [1913, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | H. J. Gibbe | Medical Superintendent, Lunatic Asylum | Medical | — | — |
| 1915 | H. J. Gibbe | Medical Superintendent, Lunatic Asylum | Medical | — | — |

### Deterministic checks: `gibbe_john_b1881` vs `Gibbe, H. J___Straits Settlements___1913`

- [PASS] surname_gate: bio 'GIBBE' vs stint 'Gibbe, H. J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1913, birth 1881 (age 32)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1915
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

