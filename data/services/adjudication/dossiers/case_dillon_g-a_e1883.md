<!-- {"case_id": "case_dillon_g-a_e1883", "bio_ids": ["dillon_g-a_e1883"], "stint_ids": ["Dillon, G. A___Windward Islands___1878"]} -->
# Dossier case_dillon_g-a_e1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dillon_g-a_e1883`

- Printed name: **DILLON, G. A**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33079.v` — printed in editions [1886]:**

> DILLON, G. A.—Colonial registrar, Grenada, 1st January, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Colonial registrar | Grenada | [1886] |

## Candidate stint `Dillon, G. A___Windward Islands___1878`

- Staff-list name: **Dillon, G. A** | colony: **Windward Islands** | listed 1878–1883 | editions [1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | G. A. Dillon | Clerk | Colonial Secretary's Department | — | — |
| 1879 | G. A. Dillon | Clerk | Colonial Secretary's Office | — | — |
| 1880 | G. A. Dillon | Clerk | Record Branch | — | — |
| 1883 | G. A. Dillon | Clerk | Record Branch | — | — |

### Deterministic checks: `dillon_g-a_e1883` vs `Dillon, G. A___Windward Islands___1878`

- [PASS] surname_gate: bio 'DILLON' vs stint 'Dillon, G. A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
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

