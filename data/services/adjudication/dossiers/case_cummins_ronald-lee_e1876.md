<!-- {"case_id": "case_cummins_ronald-lee_e1876", "bio_ids": ["cummins_ronald-lee_e1876"], "stint_ids": ["Cummins, R. L___Windward Islands___1878"]} -->
# Dossier case_cummins_ronald-lee_e1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cummins_ronald-lee_e1876`

- Printed name: **CUMMINS, RONALD LEE**
- Birth year: not printed
- Appears in editions: [1886, 1889]

### Verbatim printed entry text (OCR)

**Version `col1886-L32896.v` — printed in editions [1886, 1889]:**

> CUMMINS, RONALD LEE.—As supernumerary, colonial secretary's office, Barbados, Feb., 1876; third clerk correspondence branch, March, 1879; second clerk, audit office, January, 1881; acting chief clerk, audit office, November, 1881, to December, 1882; second clerk correspondence branch colonial secretary's office, January, 1883; chief clerk and treasurer, petty debt court, Bridgetown, July, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | supernumerary, colonial secretary's office | Barbados | [1886, 1889] |
| 1 | 1879 | third clerk correspondence branch | — | [1886, 1889] |
| 2 | 1881 | second clerk, audit office | — | [1886, 1889] |
| 3 | 1883 | second clerk correspondence branch colonial secretary's office | — | [1886, 1889] |
| 4 | 1884 | chief clerk and treasurer, petty debt court | Bridgetown | [1886, 1889] |

## Candidate stint `Cummins, R. L___Windward Islands___1878`

- Staff-list name: **Cummins, R. L** | colony: **Windward Islands** | listed 1878–1883 | editions [1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | R. L. Cummins | Clerk | Colonial Secretary's Department | — | — |
| 1879 | R. L. Cummins | Clerk | Colonial Secretary's Office | — | — |
| 1880 | R. L. Cummins | 3rd Clerk | Correspondence Branch | — | — |
| 1883 | R. L. Cummins | 2nd Clerk | Audit Office | — | — |

### Deterministic checks: `cummins_ronald-lee_e1876` vs `Cummins, R. L___Windward Islands___1878`

- [PASS] surname_gate: bio 'CUMMINS' vs stint 'Cummins, R. L' (exact)
- [PASS] initials: bio ['R', 'L'] ~ stint ['R', 'L']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1883
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

