<!-- {"case_id": "case_coakes_c-j_e1851", "bio_ids": ["coakes_c-j_e1851"], "stint_ids": ["Coakes, C. J___Natal___1879"]} -->
# Dossier case_coakes_c-j_e1851

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coakes_c-j_e1851`

- Printed name: **COAKES, C. J**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L26886.v` — printed in editions [1883, 1886]:**

> COAKES, C. J.—Messenger to the magistrates' court, Pietermaritzburg, Natal, 1851; clerk to the resident magistrate, Upper Umcomas, 1859; and clerk in the post-office, 1861; and postmaster at D'Urban, March, 1863.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1851 | Messenger to the magistrates' court, Pietermaritzburg | Natal | [1883, 1886] |
| 1 | 1859 | clerk to the resident magistrate, Upper Umcomas | Natal *(inherited from previous clause)* | [1883, 1886] |
| 2 | 1861 | and clerk in the post-office | Natal *(inherited from previous clause)* | [1883, 1886] |
| 3 | 1863 | and postmaster at D'Urban | Natal *(inherited from previous clause)* | [1883, 1886] |

## Candidate stint `Coakes, C. J___Natal___1879`

- Staff-list name: **Coakes, C. J** | colony: **Natal** | listed 1879–1886 | editions [1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | C. J. Coakes | Postmaster | Post and Telegraph Department | — | — |
| 1880 | C. J. Coakes | Postmaster | Postal Department | — | — |
| 1883 | C. J. Coakes | Postmaster | Postal | — | — |
| 1886 | C. J. Coakes | Postmaster | Postal | — | — |

### Deterministic checks: `coakes_c-j_e1851` vs `Coakes, C. J___Natal___1879`

- [PASS] surname_gate: bio 'COAKES' vs stint 'Coakes, C. J' (exact)
- [PASS] initials: bio ['C', 'J'] ~ stint ['C', 'J']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1886
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

