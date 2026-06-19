<!-- {"case_id": "case_hatteley_e-b_e1874", "bio_ids": ["hatteley_e-b_e1874"], "stint_ids": ["Hartley, Edmund Baron___Cape of Good Hope___1879", "Hartley, Edmund Baron___Cape of Good Hope___1897"]} -->
# Dossier case_hatteley_e-b_e1874

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `hatteley_e-b_e1874` ↔ `Hartley, Edmund Baron___Cape of Good Hope___1879` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Hartley, Edmund Baron___Cape of Good Hope___1879` is also gate-compatible with biography(ies) outside this case: ['hartley_e-b_e1874'] (already linked elsewhere or filtered).
- NOTE: stint `Hartley, Edmund Baron___Cape of Good Hope___1897` is also gate-compatible with biography(ies) outside this case: ['hartley_e-b_e1874'] (already linked elsewhere or filtered).

## Biography `hatteley_e-b_e1874`

- Printed name: **HATTELEY, E. B.**
- Birth year: not printed
- Appears in editions: [1896]

### Verbatim printed entry text (OCR)

**Version `col1896-L39362.v` — printed in editions [1896]:**

> HATTELEY, E. B.—Surgeon-Major, Cape Mounted Riflemen; created D.C. for gallantry in the operations against the stronghold of the Basuto chief Morosi; principal medical officer, Cape colonial forces, 1878; served through the Gaika, Morosi, and Basuto wars, 1878-9-80-1; was government medical officer, Basutoland, 1874-7.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874–1877 | government medical officer | Basutoland | [1896] |
| 1 | 1878–1878 | principal medical officer | Cape Colony | [1896] |
| 2 | 1878–1881 | — | — | [1896] |

## Candidate stint `Hartley, Edmund Baron___Cape of Good Hope___1879`

- Staff-list name: **Hartley, Edmund Baron** | colony: **Cape of Good Hope** | listed 1879–1883 | editions [1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | E. B. Hartley | Surgeon | Cape Mounted Riflemen (Act No. 9 of 1878) | — | — |
| 1880 | E. B. Hartley | Surgeon | Cape Mounted Riflemen | — | — |
| 1883 | Edmund Baron Hartley | Surgeon-Major and Senior Medical Officer | Late Left Wing | — | — |

### Deterministic checks: `hatteley_e-b_e1874` vs `Hartley, Edmund Baron___Cape of Good Hope___1879`

- [PASS] surname_gate: bio 'HATTELEY' vs stint 'Hartley, Edmund Baron' (fuzzy:2)
- [PASS] initials: bio ['E', 'B'] ~ stint ['E', 'B']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1883
- [PASS] position_sim: best 75 vs bar 60: 'principal medical officer' ~ 'Surgeon-Major and Senior Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Hartley, Edmund Baron___Cape of Good Hope___1897`

- Staff-list name: **Hartley, Edmund Baron** | colony: **Cape of Good Hope** | listed 1897–1900 | editions [1897, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | Edmund Baron Hartley | Surgeon-Lt.-Col. and Principal Medical Officer, Colonial Forces | Defence Department | — | Lt.-Col. |
| 1899 | Edmund Bayo Hartley | Surgeon-Lt.-Col. and Principal Medical Officer, Colonial Forces | Cape Mounted Riflemen | — | Lt.-Col. |
| 1900 | Edmund Baron Hartley | Surgeon-Lt.-Col | Cape Mounted Riflemens | — | Lt.-Col. |

### Deterministic checks: `hatteley_e-b_e1874` vs `Hartley, Edmund Baron___Cape of Good Hope___1897`

- [PASS] surname_gate: bio 'HATTELEY' vs stint 'Hartley, Edmund Baron' (fuzzy:2)
- [PASS] initials: bio ['E', 'B'] ~ stint ['E', 'B']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1900
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

