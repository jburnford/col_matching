<!-- {"case_id": "case_henkel_c-c-ii_e1889", "bio_ids": ["henkel_c-c-ii_e1889"], "stint_ids": ["Henkel, C. C___Cape of Good Hope___1877", "Henkel, C. C___Cape of Good Hope___1889"]} -->
# Dossier case_henkel_c-c-ii_e1889

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `henkel_c-c-ii_e1889`

- Printed name: **HENKEL, C. C. II**
- Birth year: not printed
- Appears in editions: [1898, 1899, 1900, 1905, 1906, 1907]

### Verbatim printed entry text (OCR)

**Version `col1898-L33891.v` — printed in editions [1898, 1899, 1900, 1905, 1906, 1907]:**

> HENKEL, C. C. II.—Conservator of forests, Transkeian territories, Cape Col., July, 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | Conservator of forests, Transkeian territories | Cape of Good Hope | [1898, 1899, 1900, 1905, 1906, 1907] |

## Candidate stint `Henkel, C. C___Cape of Good Hope___1877`

- Staff-list name: **Henkel, C. C** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. Henkel | Assistant Compiler of Index Maps | Surveyor-General's Office | — | — |
| 1878 | C. Henkel | Assistant Compiler of Index Maps | Surveyor-General's Office | — | — |
| 1879 | C. Henkel | Assistant Compiler of Index Maps | Surveyor-General's Office | — | — |
| 1880 | C. Henkel | Assistant Compiler of Index Maps | Surveyor-General's Office | — | — |

### Deterministic checks: `henkel_c-c-ii_e1889` vs `Henkel, C. C___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'HENKEL' vs stint 'Henkel, C. C' (exact)
- [PASS] initials: bio ['C', 'C', 'I'] ~ stint ['C', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Henkel, C. C___Cape of Good Hope___1889`

- Staff-list name: **Henkel, C. C** | colony: **Cape of Good Hope** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | C. C. Henkel | Clerk and Ranger | Crown Forests and Plantations | — | — |
| 1890 | C. C. Henkel | Chief Forest Ranger | Crown Forests and Plantations | — | — |

### Deterministic checks: `henkel_c-c-ii_e1889` vs `Henkel, C. C___Cape of Good Hope___1889`

- [PASS] surname_gate: bio 'HENKEL' vs stint 'Henkel, C. C' (exact)
- [PASS] initials: bio ['C', 'C', 'I'] ~ stint ['C', 'C']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1890
- [FAIL] position_sim: best 44 vs bar 60: 'Conservator of forests, Transkeian territories' ~ 'Chief Forest Ranger'
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

