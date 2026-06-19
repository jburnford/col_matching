<!-- {"case_id": "case_powles_james_e1881", "bio_ids": ["powles_james_e1881"], "stint_ids": ["Bowles, J. H___British Guiana___1877"]} -->
# Dossier case_powles_james_e1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['powles_james_e1881'] carry a single initial only — the namesake trap applies.

## Biography `powles_james_e1881`

- Printed name: **POWLES, James**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L35593.v` — printed in editions [1888]:**

> POWLES, James.—Collector of customs, New South Wales, 1st Aug., 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Collector of customs | New South Wales | [1888] |

## Candidate stint `Bowles, J. H___British Guiana___1877`

- Staff-list name: **Bowles, J. H** | colony: **British Guiana** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. H. Bowles | Ordinary Marshal | Judicial Establishment | — | — |
| 1878 | J. H. Bowles | Ordinary Marshal | Ordinary Marshals | — | — |

### Deterministic checks: `powles_james_e1881` vs `Bowles, J. H___British Guiana___1877`

- [PASS] surname_gate: bio 'POWLES' vs stint 'Bowles, J. H' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
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

