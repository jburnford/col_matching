<!-- {"case_id": "case_doberck_w_e1874", "bio_ids": ["doberck_w_e1874"], "stint_ids": ["Doberck, W___Hong Kong___1894", "Doberck, W___Hong Kong___1905"]} -->
# Dossier case_doberck_w_e1874

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['doberck_w_e1874'] carry a single initial only — the namesake trap applies.

## Biography `doberck_w_e1874`

- Printed name: **DOBERCK, W**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]

### Verbatim printed entry text (OCR)

**Version `col1905-L42918.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]:**

> DOBERCK, DR. W.—Astronomer in charge of Markree Observ., co. Sligo, 1874-1883; dir. Hong Kong Observ., since 1883; has published twenty volumes of observations and researches in Hong Kong, a pamphlet "On the Law of Storms in the Eastern Seas," and over 200 papers on scientific subjects in transactions of learned societies and scientific periodicals in Europe and America.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874–1883 | Astronomer in charge of Markree Observ., co. Sligo | Colonial Office | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 1 | 1883 | dir. Hong Kong Observ., since | Colonial Office *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |

## Candidate stint `Doberck, W___Hong Kong___1894`

- Staff-list name: **Doberck, W** | colony: **Hong Kong** | listed 1894–1896 | editions [1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | W. Doberck | Director | Hong Kong Observatory | — | — |
| 1896 | W. Doberck | Director | Hong Kong Observatory | — | — |

### Deterministic checks: `doberck_w_e1874` vs `Doberck, W___Hong Kong___1894`

- [PASS] surname_gate: bio 'DOBERCK' vs stint 'Doberck, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1896
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Doberck, W___Hong Kong___1905`

- Staff-list name: **Doberck, W** | colony: **Hong Kong** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | Dr. W. Doberck | Director | Observatory Department | — | — |
| 1907 | W. Doberck | Director of the Observatory | Observatory | — | — |

### Deterministic checks: `doberck_w_e1874` vs `Doberck, W___Hong Kong___1905`

- [PASS] surname_gate: bio 'DOBERCK' vs stint 'Doberck, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

