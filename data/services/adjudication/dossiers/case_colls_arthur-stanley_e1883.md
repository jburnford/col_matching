<!-- {"case_id": "case_colls_arthur-stanley_e1883", "bio_ids": ["colls_arthur-stanley_e1883"], "stint_ids": ["Colls, A. Stanley___Ceylon___1899"]} -->
# Dossier case_colls_arthur-stanley_e1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `colls_arthur-stanley_e1883`

- Printed name: **COLLS, ARTHUR STANLEY**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1905-L42600.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]:**

> COLLS, ARTHUR STANLEY.—Ed. Rugby; asst. engineer, Midland Rly., 1883 to 1886; dist. engrnr., P.W.D., Ceylon, 1886; dist. engrnr., Pretoria dist., Transvaal, 1892; ch. engrnr. of buildings, 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883–1886 | asst. engineer, Midland Rly | — | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 1 | 1886 | dist. engrnr., P.W.D. | Ceylon | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 2 | 1892 | dist. engrnr., Pretoria dist. | Transvaal | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 3 | 1905 | ch. engrnr. of buildings | Transvaal *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |

## Candidate stint `Colls, A. Stanley___Ceylon___1899`

- Staff-list name: **Colls, A. Stanley** | colony: **Ceylon** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | A. Stanley Colls | District Engineer (1st Grade) | District Engineers | — | — |
| 1900 | A. Stanley Colls | District Engineer, 1st Grade | Public Work Department | — | — |

### Deterministic checks: `colls_arthur-stanley_e1883` vs `Colls, A. Stanley___Ceylon___1899`

- [PASS] surname_gate: bio 'COLLS' vs stint 'Colls, A. Stanley' (exact)
- [PASS] initials: bio ['A', 'S'] ~ stint ['A', 'S']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1900
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

