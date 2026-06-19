<!-- {"case_id": "case_steytler_john_e1877", "bio_ids": ["steytler_john_e1877"], "stint_ids": ["Steytler, J___Cape of Good Hope___1888"]} -->
# Dossier case_steytler_john_e1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['steytler_john_e1877'] carry a single initial only — the namesake trap applies.

## Biography `steytler_john_e1877`

- Printed name: **STEYTLER, JOHN**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L34121.v` — printed in editions [1894]:**

> STEYTLER, JOHN.—Accntt. (construction and working of rlyws, Cape), July, 1877; chief accntt., Western system, July, 1881; chief accntt. of railways (working and construction), May, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1877 | Accntt. (construction and working of rlyws | Cape of Good Hope | [1894] |
| 1 | 1881 | chief accntt., Western system | Cape of Good Hope *(inherited from previous clause)* | [1894] |
| 2 | 1884 | chief accntt. of railways (working and construction) | Cape of Good Hope *(inherited from previous clause)* | [1894] |

## Candidate stint `Steytler, J___Cape of Good Hope___1888`

- Staff-list name: **Steytler, J** | colony: **Cape of Good Hope** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | J. Steytler | Chief Accountant | General Manager's Department | — | — |
| 1889 | J. Steytler | Chief Accountant | General Manager's Department | — | — |
| 1890 | J. Steytler | Chief Accountant | General Manager's Department, Cape Town | — | — |

### Deterministic checks: `steytler_john_e1877` vs `Steytler, J___Cape of Good Hope___1888`

- [PASS] surname_gate: bio 'STEYTLER' vs stint 'Steytler, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1890
- [FAIL] position_sim: best 48 vs bar 60: 'chief accntt. of railways (working and construction)' ~ 'Chief Accountant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

