<!-- {"case_id": "case_gawthorne_james_e1855", "bio_ids": ["gawthorne_james_e1855"], "stint_ids": ["Gawthorne, J___Straits Settlements___1877"]} -->
# Dossier case_gawthorne_james_e1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gawthorne_james_e1855'] carry a single initial only — the namesake trap applies.

## Biography `gawthorne_james_e1855`

- Printed name: **GAWTHORNE, JAMES**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27616.v` — printed in editions [1883]:**

> GAWTHORNE, JAMES.—Clerk in survey office, 2nd January, 1862; promoted in April, 1855, to post-office, Penang; 28th February, 1869, to 30th May, 1870, acting as assistant post-master.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855 | post-office | Penang | [1883] |
| 1 | 1862 | Clerk in survey office | — | [1883] |
| 2 | 1869–1870 | acting as assistant post-master | — | [1883] |

## Candidate stint `Gawthorne, J___Straits Settlements___1877`

- Staff-list name: **Gawthorne, J** | colony: **Straits Settlements** | listed 1877–1879 | editions [1877, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Gawthorne | Chief Clerk | Post Office | — | — |
| 1879 | J. Gawthorne | Chief Clerk | Post Office | — | — |

### Deterministic checks: `gawthorne_james_e1855` vs `Gawthorne, J___Straits Settlements___1877`

- [PASS] surname_gate: bio 'GAWTHORNE' vs stint 'Gawthorne, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
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

