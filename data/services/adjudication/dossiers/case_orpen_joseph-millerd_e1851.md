<!-- {"case_id": "case_orpen_joseph-millerd_e1851", "bio_ids": ["orpen_joseph-millerd_e1851"], "stint_ids": ["Orpen, Joseph M___Cape of Good Hope___1896"]} -->
# Dossier case_orpen_joseph-millerd_e1851

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `orpen_joseph-millerd_e1851`

- Printed name: **ORPEN, Joseph Millerd**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28967.v` — printed in editions [1883]:**

> ORPEN, Major Joseph Millerd.—Served as lieutenant of volunteers in the Kaffir war, 1851; elected member for Queenstown in the Cape house of assembly in 1871; in 1873 he was appointed British resident to the native tribes between the Umtata and Natal, for the defence of which he organized and conducted a military expedition on the occasion of the Langalibalele outbreak; was engaged on the trigonometrical survey of Griqualand West in 1878, when the Griqua rebellion broke out, in the suppression of which he took an active part, as chief of the intelligence department, receiving a commission as major, and the civil and military command of the district of Griquatown; elected member for Alivai North in 1878; and vacated his seat in 1881, on being appointed governor's agent in Basutoland.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1851–1851 | lieutenant of volunteers | — | [1883] |
| 1 | 1871–1871 | member for Queenstown | Cape Colony | [1883] |
| 2 | 1873 | British resident | Natal | [1883] |
| 3 | 1878–1878 | chief of the intelligence department | Griqualand West | [1883] |
| 4 | 1878–1878 | member | — | [1883] |
| 5 | 1881 | governor's agent | Basutoland | [1883] |

## Candidate stint `Orpen, Joseph M___Cape of Good Hope___1896`

- Staff-list name: **Orpen, Joseph M** | colony: **Cape of Good Hope** | listed 1896–1897 | editions [1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | Joseph M. Orpen | — | House of Assembly | — | — |
| 1897 | Joseph M. Orpen | — | Members | — | — |

### Deterministic checks: `orpen_joseph-millerd_e1851` vs `Orpen, Joseph M___Cape of Good Hope___1896`

- [PASS] surname_gate: bio 'ORPEN' vs stint 'Orpen, Joseph M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1897
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

