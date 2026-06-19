<!-- {"case_id": "case_bagge_stephen-salisbury_e1894", "bio_ids": ["bagge_stephen-salisbury_e1894", "baggie_stephen-salsbury_e1894"], "stint_ids": ["Bagge, S. S___Kenya___1905"]} -->
# Dossier case_bagge_stephen-salisbury_e1894

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Bagge, S. S___Kenya___1905'] have more than one claimant biography in this case.

## Biography `bagge_stephen-salisbury_e1894`

- Printed name: **BAGGE, STEPHEN SALISBURY**
- Birth year: not printed
- Honours: C.M.G (1907)
- Appears in editions: [1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1919, 1920]

### Verbatim printed entry text (OCR)

**Version `col1908-L43002.v` — printed in editions [1908, 1909, 1910, 1917, 1919, 1920]:**

> BAGGE, STEPHEN SALISBURY, C.M.G. (1907).—2nd cls. asst., Uganda Prot., 8th Oct., 1894; sub. comntr., East Africa Prot., 1st Apr., 1902; ret., 1910.

**Version `col1912-L42335.v` — printed in editions [1912, 1913, 1914, 1915]:**

> BAGGE, STEPHEN SALISBURY, C.M.G. (1907).—2nd cls. asst., Uganda Prot., 8th Oct., 1894; sub. comsnnr., East Africa Prot., 1st Apr., 1902; ret., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | 2nd cls. asst. | Uganda | [1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1919, 1920] |
| 1 | 1902 | sub. comntr., East Africa Prot | Uganda *(inherited from previous clause)* | [1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1919, 1920] |
| 2 | 1910 | ret | Uganda *(inherited from previous clause)* | [1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1919, 1920] |

## Biography `baggie_stephen-salsbury_e1894`

- Printed name: **BAGGIE, STEPHEN SALSBURY**
- Birth year: not printed
- Honours: C.M.G (1907)
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L42923.v` — printed in editions [1911]:**

> BAGGIE, STEPHEN SALSBURY, C.M.G. (1907).—2nd cls. asst., Uganda Prot., 8th Oct., 1894; sub-comsnr., East Africa Prot., 1st Apr., 1902; ret., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | 2nd cls. asst. | Uganda | [1911] |
| 1 | 1902 | sub-comsnr., East Africa Prot | Uganda *(inherited from previous clause)* | [1911] |
| 2 | 1910 | ret | Uganda *(inherited from previous clause)* | [1911] |

## Candidate stint `Bagge, S. S___Kenya___1905`

- Staff-list name: **Bagge, S. S** | colony: **Kenya** | listed 1905–1909 | editions [1905, 1906, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | S. S. Bagge | Sub-Commissioner (Naivasha) | — | — | — |
| 1906 | S. S. Bagge | Sub-Commissioner (Kisumu) | — | — | — |
| 1908 | S. S. Bagge | Provincial Commissioner | Civil Establishment | C.M.G. | — |
| 1909 | S. S. Bagge | Provincial Commissioner | Provincial Administration | C.M.G. | — |

### Deterministic checks: `bagge_stephen-salisbury_e1894` vs `Bagge, S. S___Kenya___1905`

- [PASS] surname_gate: bio 'BAGGE' vs stint 'Bagge, S. S' (exact)
- [PASS] initials: bio ['S', 'S'] ~ stint ['S', 'S']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `baggie_stephen-salsbury_e1894` vs `Bagge, S. S___Kenya___1905`

- [PASS] surname_gate: bio 'BAGGIE' vs stint 'Bagge, S. S' (fuzzy:1)
- [PASS] initials: bio ['S', 'S'] ~ stint ['S', 'S']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G
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

