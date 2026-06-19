<!-- {"case_id": "case_mckenzie_campbell-grant_b1894", "bio_ids": ["mckenzie_campbell-grant_b1894"], "stint_ids": ["McKenzie, Cuthbert___Australia___1912"]} -->
# Dossier case_mckenzie_campbell-grant_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mckenzie_campbell-grant_b1894`

- Printed name: **McKENZIE, Campbell Grant**
- Birth year: 1894 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L34345.v` — printed in editions [1948, 1949, 1950]:**

> McKENZIE, Campbell Grant.—b. 1894; ed. Aberdeen Gram. Sch. and Univ.; on mil. serv. 1914-18, maj.; cadet, Nig., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | cadet | Nigeria | [1948, 1949, 1950] |

## Candidate stint `McKenzie, Cuthbert___Australia___1912`

- Staff-list name: **McKenzie, Cuthbert** | colony: **Australia** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Cuthbert McKenzie | Member of Legislative Council | Legislative Council | — | — |
| 1913 | Cuthbert McKenzie | Member | Legislative Council | — | — |

### Deterministic checks: `mckenzie_campbell-grant_b1894` vs `McKenzie, Cuthbert___Australia___1912`

- [PASS] surname_gate: bio 'McKENZIE' vs stint 'McKenzie, Cuthbert' (exact)
- [PASS] initials: bio ['C', 'G'] ~ stint ['C']
- [PASS] age_gate: stint starts 1912, birth 1894 (age 18)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1913
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

