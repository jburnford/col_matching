<!-- {"case_id": "case_tilney_thomas_e1855", "bio_ids": ["tilney_thomas_e1855"], "stint_ids": ["Tilney, T. S___Cape of Good Hope___1907"]} -->
# Dossier case_tilney_thomas_e1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['tilney_thomas_e1855'] carry a single initial only — the namesake trap applies.

## Biography `tilney_thomas_e1855`

- Printed name: **TILNEY, THOMAS**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29757.v` — printed in editions [1883]:**

> TILNEY, THOMAS.—Civil commissioner and resident magistrate, Beaufort West, Cape Colony, was shipping master Cape Town, from 1855 to 1867, was promoted, from Beaufort West, September, 1872, to division of Swellendam as civil commissioner and resident magistrate.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855–1867 | shipping master | Cape Colony | [1883] |
| 1 | 1872 | civil commissioner and resident magistrate | Cape Colony | [1883] |
| 2 | ? | Civil commissioner and resident magistrate | Cape Colony | [1883] |

## Candidate stint `Tilney, T. S___Cape of Good Hope___1907`

- Staff-list name: **Tilney, T. S** | colony: **Cape of Good Hope** | listed 1907–1908 | editions [1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | T. S. Tilney | Excise Officer | Excise Branch | — | — |
| 1908 | T. S. Tilney | Excise Officer | Excise Branch | — | — |

### Deterministic checks: `tilney_thomas_e1855` vs `Tilney, T. S___Cape of Good Hope___1907`

- [PASS] surname_gate: bio 'TILNEY' vs stint 'Tilney, T. S' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T', 'S']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1908
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

