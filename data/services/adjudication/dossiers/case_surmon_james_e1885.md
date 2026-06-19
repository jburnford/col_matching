<!-- {"case_id": "case_surmon_james_e1885", "bio_ids": ["surmon_james_e1885"], "stint_ids": ["Surmon, J___Cape of Good Hope___1877"]} -->
# Dossier case_surmon_james_e1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['surmon_james_e1885'] carry a single initial only — the namesake trap applies.

## Biography `surmon_james_e1885`

- Printed name: **SURMON, JAMES**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L35897.v` — printed in editions [1886, 1888, 1889, 1890]:**

> SURMON, JAMES, E.—Resident magistrate, Mafeking, British Bechuanaland, Oct., 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885 | Resident magistrate, Mafeking | British Bechuanaland | [1886, 1888, 1889, 1890] |

## Candidate stint `Surmon, J___Cape of Good Hope___1877`

- Staff-list name: **Surmon, J** | colony: **Cape of Good Hope** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Surmon | Inspector | Armed Mounted Police Force | — | — |
| 1878 | J. Surmon | Inspector | Armed Mounted Police Force | — | — |
| 1879 | J. Surmon | Clerk to Magistrate, Cornet Spruit | Basutoland | — | — |
| 1879 | J. Surmon | Captain | Cape Mounted Riflemen (Act No. 9 of 1878) | — | — |

### Deterministic checks: `surmon_james_e1885` vs `Surmon, J___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'SURMON' vs stint 'Surmon, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
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

