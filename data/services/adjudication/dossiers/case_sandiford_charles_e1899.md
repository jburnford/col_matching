<!-- {"case_id": "case_sandiford_charles_e1899", "bio_ids": ["sandiford_charles_e1899"], "stint_ids": ["Sandiford, C___Kenya___1907"]} -->
# Dossier case_sandiford_charles_e1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sandiford_charles_e1899'] carry a single initial only — the namesake trap applies.

## Biography `sandiford_charles_e1899`

- Printed name: **SANDIFORD, CHARLES**
- Birth year: not printed
- Honours: C.B (1903), M.I.A.E, M.I.M.E
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1908-L47186.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913]:**

> SANDIFORD, CHARLES, C.B. (1903), M.I.A.E., M.I.M.E.—Loco. supt., N.W. rly., India; loco. supt., Uganda rly., 1899.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | loco. supt., Uganda rly | Uganda | [1908, 1909, 1910, 1911, 1912, 1913] |

## Candidate stint `Sandiford, C___Kenya___1907`

- Staff-list name: **Sandiford, C** | colony: **Kenya** | listed 1907–1913 | editions [1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | C. Sandiford | Locomotive Superintendent | Uganda Railway | C.B. | — |
| 1908 | C. Sandiford | Locomotive Superintendent, Uganda Railway | Civil Establishment | C.B. | — |
| 1909 | C. Sandiford | Locomotive, Carriage and Wagon Department | Railway | C.B. | — |
| 1910 | C. Sandiford | Locomotive, Carriage and Wagon Department | Locomotive, Carriage and Wagon Department | C.B. | — |
| 1911 | C. Sandiford | Locomotive, Carriage and Wagon Department | Accounts | C.B. | — |
| 1912 | C. Sandiford | Locomotive, Carriage and Wagon Department | Locomotive, Carriage and Wagon Department | C.B. | — |
| 1913 | C. Sandiford | Locomotive, Carriage and Wagon Department | Railway | C.B. | — |

### Deterministic checks: `sandiford_charles_e1899` vs `Sandiford, C___Kenya___1907`

- [PASS] surname_gate: bio 'SANDIFORD' vs stint 'Sandiford, C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1913
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.B
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

