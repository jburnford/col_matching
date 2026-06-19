<!-- {"case_id": "case_foxton_j-f-g_e1906", "bio_ids": ["foxton_j-f-g_e1906"], "stint_ids": ["Foxton, Justin F. G___Queensland___1898"]} -->
# Dossier case_foxton_j-f-g_e1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `foxton_j-f-g_e1906`

- Printed name: **FOXTON, J. F. G.**
- Birth year: not printed
- Honours: C.M.G. (1903), V.D.
- Appears in editions: [1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1914-L46403.v` — printed in editions [1914, 1915]:**

> FOXTON, Hon. J. F. G., C.M.G. (1903); V.D.; for many years minister of the Crown, Queensland; mem. of H. of R., Commonwealth of Australia, 1906-1910; hon. min., June, 1909.

**Version `col1910-L45810.v` — printed in editions [1910, 1911, 1912, 1913]:**

> FOXTON, HON. J. F. G., C.M.G. (1903); V.D.; mem. of H. of R., Commonwealth of Australia, 1906-1910; hon. min., June, 1909.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906–1910 | mem. of H. of R. | Australia | [1910, 1911, 1912, 1913, 1914, 1915] |
| 1 | 1909 | hon. min. | — | [1910, 1911, 1912, 1913, 1914, 1915] |
| 2 | ? | minister of the Crown | Queensland | [1914, 1915] |

## Candidate stint `Foxton, Justin F. G___Queensland___1898`

- Staff-list name: **Foxton, Justin F. G** | colony: **Queensland** | listed 1898–1900 | editions [1898, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | Hon. Justin F. G. Foxton | Member for Carnarvon | Legislative Assembly | — | — |
| 1900 | J. F. G. Foxton | Home Secretary | Civil Establishment | — | — |

### Deterministic checks: `foxton_j-f-g_e1906` vs `Foxton, Justin F. G___Queensland___1898`

- [PASS] surname_gate: bio 'FOXTON' vs stint 'Foxton, Justin F. G' (exact)
- [PASS] initials: bio ['J', 'F', 'G'] ~ stint ['J', 'F', 'G']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Queensland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1900
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

