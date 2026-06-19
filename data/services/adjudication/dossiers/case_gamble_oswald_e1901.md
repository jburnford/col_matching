<!-- {"case_id": "case_gamble_oswald_e1901", "bio_ids": ["gamble_oswald_e1901"], "stint_ids": ["Gamble, O___Kenya___1909"]} -->
# Dossier case_gamble_oswald_e1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 19 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gamble_oswald_e1901'] carry a single initial only — the namesake trap applies.

## Biography `gamble_oswald_e1901`

- Printed name: **GAMBLE, OSWALD**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1908-L44598.v` — printed in editions [1908, 1909, 1910]:**

> GAMBLE, OSWALD.—Asst. paymaster to the forces, Brit. Cent. Africa, 30th July, 1901; paymaster, Somaliland field force, 1902 to 1904; African gen. serv. medal; paymaster, 1st King's African rifles, E. Africa Prot., 1st May, 1906; pay and qtrmr., E.A. Pol., Aug., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | Asst. paymaster to the forces, Brit. Cent. Africa | — | [1908, 1909, 1910] |
| 1 | 1902–1904 | paymaster, Somaliland field force | Somaliland | [1908, 1909, 1910] |
| 2 | 1906 | paymaster, 1st King's African rifles, E. Africa Prot | Somaliland *(inherited from previous clause)* | [1908, 1909, 1910] |
| 3 | 1907 | pay and qtrmr., E.A. Pol | Somaliland *(inherited from previous clause)* | [1908, 1909, 1910] |

## Candidate stint `Gamble, O___Kenya___1909`

- Staff-list name: **Gamble, O** | colony: **Kenya** | listed 1909–1910 | editions [1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | O. Gamble | Pay and Quartermaster | Police | — | — |
| 1910 | O. Gamble | Pay and Quartermaster | Police | — | — |

### Deterministic checks: `gamble_oswald_e1901` vs `Gamble, O___Kenya___1909`

- [PASS] surname_gate: bio 'GAMBLE' vs stint 'Gamble, O' (exact)
- [PASS] initials: bio ['O'] ~ stint ['O']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1910
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

