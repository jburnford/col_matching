<!-- {"case_id": "case_webbe_e-augustus_e1875", "bio_ids": ["webbe_e-augustus_e1875"], "stint_ids": ["Webbe, E. A___Leeward Islands___1880"]} -->
# Dossier case_webbe_e-augustus_e1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `webbe_e-augustus_e1875`

- Printed name: **WEBBE, E. AUGUSTUS**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L29940.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894]:**

> WEBBE, E. AUGUSTUS.—Appointed clerk in the registrar's and provost marshal's office, Nevis, 28th August, 1875; clerk in the treasury department of Montserrat, August, 1879; is treasury cashier and accountant.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Appointed clerk in the registrar's and provost marshal's office | Nevis | [1883, 1886, 1888, 1889, 1890, 1894] |
| 1 | 1879 | clerk in the treasury department of Montserrat | Nevis *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Webbe, E. A___Leeward Islands___1880`

- Staff-list name: **Webbe, E. A** | colony: **Leeward Islands** | listed 1880–1886 | editions [1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | E. A. Webbe | Clerk | Civil Establishment | — | — |
| 1883 | E. A. Webbe | First Clerk | Civil Establishment | — | — |
| 1886 | E. A. Webbe | First Clerk | Civil Establishment | — | — |

### Deterministic checks: `webbe_e-augustus_e1875` vs `Webbe, E. A___Leeward Islands___1880`

- [PASS] surname_gate: bio 'WEBBE' vs stint 'Webbe, E. A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1886
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

