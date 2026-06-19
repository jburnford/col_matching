<!-- {"case_id": "case_egg_john-tyrer_e1859", "bio_ids": ["egg_john-tyrer_e1859"], "stint_ids": ["Egg, J. T___British Guiana___1877"]} -->
# Dossier case_egg_john-tyrer_e1859

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `egg_john-tyrer_e1859`

- Printed name: **EGG, JOHN TYRER**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33208.v` — printed in editions [1886]:**

> EGG, JOHN TYRER.—Was first clerk in the customs from Jan. to July, 1859; then transferred to the registrar's office in Aug., 1859, acting assistant sworn clerk 23rd Nov., 1864; assistant sworn clerk, registrar's office, Berbice, British Guiana, Feb., 1868.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1859–1859 | first clerk in the customs | — | [1886] |
| 1 | 1859–1859 | — | — | [1886] |
| 2 | 1864–1864 | acting assistant sworn clerk | — | [1886] |
| 3 | 1868–1868 | assistant sworn clerk | British Guiana | [1886] |

## Candidate stint `Egg, J. T___British Guiana___1877`

- Staff-list name: **Egg, J. T** | colony: **British Guiana** | listed 1877–1883 | editions [1877, 1878, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. T. Egg | Assistant Sworn Clerk | Judicial Establishment | — | — |
| 1878 | J. T. Egg | Assistant Sworn Clerk | Judicial Establishment | — | — |
| 1880 | J. T. Egg | Sworn Clerk and Notary Public | Judicial Establishment | — | — |
| 1883 | J. T. Egg | Sworn Clerk and Notary Public | Judicial Establishment | — | — |

### Deterministic checks: `egg_john-tyrer_e1859` vs `Egg, J. T___British Guiana___1877`

- [PASS] surname_gate: bio 'EGG' vs stint 'Egg, J. T' (exact)
- [PASS] initials: bio ['J', 'T'] ~ stint ['J', 'T']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

