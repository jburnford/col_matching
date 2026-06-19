<!-- {"case_id": "case_methley_f-h_e1875", "bio_ids": ["methley_f-h_e1875"], "stint_ids": ["Methley, F___Natal___1879"]} -->
# Dossier case_methley_f-h_e1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `methley_f-h_e1875`

- Printed name: **METHLEY, F. H.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28688.v` — printed in editions [1883]:**

> METHLEY, F. H.—Clerk and interpreter in the resident magistrate's office, Natal, May, 1875, Umgeni Division; acting government interpreter, and interpreter to the native high court, 1st Jan., 1877; clerk and interpreter to the resident magistrate, Umgeni Division, March, 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Clerk and interpreter in the resident magistrate's office | Natal | [1883] |
| 1 | 1877 | acting government interpreter, and interpreter to the native high court | — | [1883] |
| 2 | 1878 | clerk and interpreter to the resident magistrate | — | [1883] |

## Candidate stint `Methley, F___Natal___1879`

- Staff-list name: **Methley, F** | colony: **Natal** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | F. Methley | Clerk and Zulu Interpreter | Magisterial Department and Staff | — | — |
| 1880 | F. Methley | Clerk and Zulu Interpreter | Magisterial Department and Staff | — | — |

### Deterministic checks: `methley_f-h_e1875` vs `Methley, F___Natal___1879`

- [PASS] surname_gate: bio 'METHLEY' vs stint 'Methley, F' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
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

