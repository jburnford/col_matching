<!-- {"case_id": "case_kaine_john-charles_b1854", "bio_ids": ["kaine_john-charles_b1854"], "stint_ids": ["Kaine, John C___Canada___1917"]} -->
# Dossier case_kaine_john-charles_b1854

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kaine_john-charles_b1854`

- Printed name: **KAINE, JOHN CHARLES**
- Birth year: 1854 (attested in editions [1911, 1912, 1913, 1914, 1915, 1917, 1920, 1921, 1922, 1923])
- Appears in editions: [1911, 1912, 1913, 1914, 1915, 1917, 1920, 1921, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1911-L45911.v` — printed in editions [1911, 1912, 1913, 1914, 1915, 1917, 1920, 1921, 1922, 1923]:**

> KAINE, HON. JOHN CHARLES.—B. 1854; ed. Comm'l. Acad., Quebec; elec. mem. of exec. coun. for Quebec West, 1904; re-elec., 1908 and 1912; min. without portfolio, 8th Jan., 1906; app'd. to legis. coun., 1915.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904–1904 | mem. of exec. coun. | Quebec | [1911, 1912, 1913, 1914, 1915, 1917, 1920, 1921, 1922, 1923] |
| 1 | 1906–1906 | min. without portfolio | — | [1911, 1912, 1913, 1914, 1915, 1917, 1920, 1921, 1922, 1923] |
| 2 | 1908–1912 | re-elec. | — | [1911, 1912, 1913, 1914, 1915, 1917, 1920, 1921, 1922, 1923] |
| 3 | 1915–1915 | legis. coun. | — | [1911, 1912, 1913, 1914, 1915, 1917, 1920, 1921, 1922, 1923] |

## Candidate stint `Kaine, John C___Canada___1917`

- Staff-list name: **Kaine, John C** | colony: **Canada** | listed 1917–1922 | editions [1917, 1918, 1919, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | Hon. John C. Kaine | Minister without portfolio | Executive Council | — | — |
| 1918 | John C. Kaine | Minister without portfolio | Executive Council | — | — |
| 1919 | John C. Kaine | Minister without portfolio | Executive Council | — | — |
| 1922 | J. C. Kaine | Minister without portfolio | Executive Council | — | — |

### Deterministic checks: `kaine_john-charles_b1854` vs `Kaine, John C___Canada___1917`

- [PASS] surname_gate: bio 'KAINE' vs stint 'Kaine, John C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1917, birth 1854 (age 63)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1922
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

