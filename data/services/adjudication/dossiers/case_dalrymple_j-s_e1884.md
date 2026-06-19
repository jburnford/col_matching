<!-- {"case_id": "case_dalrymple_j-s_e1884", "bio_ids": ["dalrymple_j-s_e1884"], "stint_ids": ["Dalrymple, J___Ceylon___1922"]} -->
# Dossier case_dalrymple_j-s_e1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dalrymple_j-s_e1884`

- Printed name: **DALRYMPLE, J. S**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L32940.v` — printed in editions [1888]:**

> DALRYMPLE, J. S.—Served in Methuen's Horse, "Bechuanaland Field Force," 1884-5; assistant inspector, Gold Coast constabulary, Mar., 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884–1885 | Served in Methuen's Horse, "Bechuanaland Field Force," | — | [1888] |
| 1 | 1886 | assistant inspector, Gold Coast constabulary | Gold Coast | [1888] |

## Candidate stint `Dalrymple, J___Ceylon___1922`

- Staff-list name: **Dalrymple, J** | colony: **Ceylon** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | J. Dalrymple | Temporary Irrigation Engineer | Irrigation Department | — | — |
| 1923 | J. Dalrymple | Temporary Irrigation Engineer | Irrigation Department | — | — |

### Deterministic checks: `dalrymple_j-s_e1884` vs `Dalrymple, J___Ceylon___1922`

- [PASS] surname_gate: bio 'DALRYMPLE' vs stint 'Dalrymple, J' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
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

