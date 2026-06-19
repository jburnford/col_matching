<!-- {"case_id": "case_mckenna_w_e1879", "bio_ids": ["mckenna_w_e1879"], "stint_ids": ["McKenna, W. J___Western Australia___1905", "McKenna, William___Griqualand West___1877"]} -->
# Dossier case_mckenna_w_e1879

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mckenna_w_e1879'] carry a single initial only — the namesake trap applies.

## Biography `mckenna_w_e1879`

- Printed name: **McKENNA, W**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L34635.v` — printed in editions [1886, 1888, 1889, 1890]:**

> McKENNA, W.—Police magistrate, Kimberley, Cape Colony, 10 March, 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | Police magistrate, Kimberley | Cape of Good Hope | [1886, 1888, 1889, 1890] |

## Candidate stint `McKenna, W. J___Western Australia___1905`

- Staff-list name: **McKenna, W. J** | colony: **Western Australia** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | W. J. McKenna | Sub-collector of Customs | Customs Department | — | — |
| 1906 | W. J. McKenna | Sub-collector of Customs | Customs Department | — | — |

### Deterministic checks: `mckenna_w_e1879` vs `McKenna, W. J___Western Australia___1905`

- [PASS] surname_gate: bio 'McKENNA' vs stint 'McKenna, W. J' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `McKenna, William___Griqualand West___1877`

- Staff-list name: **McKenna, William** | colony: **Griqualand West** | listed 1877–1879 | editions [1877, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. McKenna | Sub-Inspector | Police | — | — |
| 1879 | William McKenna | Clerk to the Attorney-General and Clerk of the Peace for the Province | Attorney-General's Office | — | — |

### Deterministic checks: `mckenna_w_e1879` vs `McKenna, William___Griqualand West___1877`

- [PASS] surname_gate: bio 'McKENNA' vs stint 'McKenna, William' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Griqualand West'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
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

