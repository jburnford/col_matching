<!-- {"case_id": "case_macdougall_patrick-leonard_e1836", "bio_ids": ["macdougall_patrick-leonard_e1836"], "stint_ids": ["MacDougall, Patrick___Canada___1880"]} -->
# Dossier case_macdougall_patrick-leonard_e1836

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `macdougall_patrick-leonard_e1836`

- Printed name: **MACDOUGALL, PATRICK LEONARD**
- Birth year: not printed
- Honours: K.C.M.G. (1877)
- Appears in editions: [1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1886-L34602.v` — printed in editions [1886, 1888, 1889, 1890, 1894]:**

> MACDOUGALL, GENERAL SIR PATRICK LEONARD, K.C.M.G. (1877).—Entered the army in the 78th Highlanders in 1836, and served afterwards in the 36th regiment and royal Canadian rifles; was major and superintendent of studies at the royal military college; was appointed commandant of the staff college at its formation; was adjutant general of the Canadian militia during the Fenian raids; appointed deputy inspector-general of reserve forces (England), during which period he was president of the committee on the localization of the forces; organized the intelligence branch of the quartermaster-general's department, on its first formation; served on the quarter-master general's staff in the Crimea, during the siege of Sebastopol and the capture of Kerch; promoted lieutenant-colonel; medal and clasp for Sebastopol, and Turkish medal; stationed at Halifax since 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1836 | Entered the army in the 78th Highlanders | — | [1886, 1888, 1889, 1890, 1894] |
| 1 | 1878 | stationed | Halifax | [1886, 1888, 1889, 1890, 1894] |

## Candidate stint `MacDougall, Patrick___Canada___1880`

- Staff-list name: **MacDougall, Patrick** | colony: **Canada** | listed 1880–1883 | editions [1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | Sir Patrick MacDougall | General Commanding Her Majesty's Forces | Military Establishment | K.C.M.G. | — |
| 1883 | Patrick MacDougall | General Commanding Her Majesty's Forces | Imperial Military Establishment | K.C.M.G. | — |

### Deterministic checks: `macdougall_patrick-leonard_e1836` vs `MacDougall, Patrick___Canada___1880`

- [PASS] surname_gate: bio 'MACDOUGALL' vs stint 'MacDougall, Patrick' (exact)
- [PASS] initials: bio ['P', 'L'] ~ stint ['P']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: K.C.M.G.
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

