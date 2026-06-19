<!-- {"case_id": "case_alves_a-f_e1855", "bio_ids": ["alves_a-f_e1855"], "stint_ids": ["Alves, A. F___Hong Kong___1877"]} -->
# Dossier case_alves_a-f_e1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `alves_a-f_e1855`

- Printed name: **ALVES, A. F**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L26176.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> ALVES, A. F.—Clerk and Draftsman in the Surveyor General's Office, Hong Kong, 1855; Accountant in the Treasury, 1863.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855 | Clerk and Draftsman in the Surveyor General's Office | Hong Kong | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1863 | Accountant in the Treasury | Hong Kong *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Alves, A. F___Hong Kong___1877`

- Staff-list name: **Alves, A. F** | colony: **Hong Kong** | listed 1877–1890 | editions [1877, 1878, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. F. Alves | 2nd Clerk and Accountant | Treasurer's Department | — | — |
| 1878 | A. F. Alves | 2nd Clerk and Accountant | Treasurer's Department | — | — |
| 1880 | A. F. Alves | 2nd Clerk and Accountant | Treasurer's Department | — | — |
| 1883 | A. F. Alves | 2nd Clerk and Accountant | Treasurer's Department | — | — |
| 1886 | A. F. Alves | 2nd Clerk and Cashier, Accountant | Treasurer's Department | — | — |
| 1888 | A. F. Alves | 2nd Clerk and Accountant | Treasurer's Department | — | — |
| 1889 | A. F. Alves | 2nd Clerk and Accountant | Treasurer's Department | — | — |
| 1890 | A. F. Alves | Clerk and Cashier | Treasurer's Department | — | — |

### Deterministic checks: `alves_a-f_e1855` vs `Alves, A. F___Hong Kong___1877`

- [PASS] surname_gate: bio 'ALVES' vs stint 'Alves, A. F' (exact)
- [PASS] initials: bio ['A', 'F'] ~ stint ['A', 'F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1890
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

