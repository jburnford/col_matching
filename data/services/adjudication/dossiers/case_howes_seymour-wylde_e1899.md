<!-- {"case_id": "case_howes_seymour-wylde_e1899", "bio_ids": ["howes_seymour-wylde_e1899"], "stint_ids": ["Howes, S. W___Leeward Islands___1925"]} -->
# Dossier case_howes_seymour-wylde_e1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `howes_seymour-wylde_e1899`

- Printed name: **HOWES, SEYMOUR WYLDE**
- Birth year: not printed
- Appears in editions: [1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1905-L43871.v` — printed in editions [1905, 1906]:**

> HOWES, SEYMOUR WYLDE.—Ag. 2nd treasy. offr., Montserrat, Nov., 1899; temp. offr., treasy. dept., May, 1900.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | Ag. 2nd treasy. offr. | Montserrat | [1905, 1906] |
| 1 | 1900 | temp. offr., treasy. dept | Montserrat *(inherited from previous clause)* | [1905, 1906] |

## Candidate stint `Howes, S. W___Leeward Islands___1925`

- Staff-list name: **Howes, S. W** | colony: **Leeward Islands** | listed 1925–1928 | editions [1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | S. W. Howes | Executive Council | Executive Council | — | — |
| 1927 | S. W. Howes | Member | Executive Council | — | — |
| 1928 | S. W. Howes | Executive Council Member | Executive Council | — | — |

### Deterministic checks: `howes_seymour-wylde_e1899` vs `Howes, S. W___Leeward Islands___1925`

- [PASS] surname_gate: bio 'HOWES' vs stint 'Howes, S. W' (exact)
- [PASS] initials: bio ['S', 'W'] ~ stint ['S', 'W']
- [PASS] age_gate: stint starts 1925; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1928
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

