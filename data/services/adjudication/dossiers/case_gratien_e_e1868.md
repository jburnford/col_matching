<!-- {"case_id": "case_gratien_e_e1868", "bio_ids": ["gratien_e_e1868"], "stint_ids": ["Gratien, E___Ceylon___1883", "Gratien, E___Ceylon___1890"]} -->
# Dossier case_gratien_e_e1868

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gratien_e_e1868'] carry a single initial only — the namesake trap applies.

## Biography `gratien_e_e1868`

- Printed name: **GRATIEN, E**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L31800.v` — printed in editions [1894]:**

> GRATIEN, E.—Assistant colonial surgeon, Ceylon, 1868.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1868 | Assistant colonial surgeon | Ceylon | [1894] |

## Candidate stint `Gratien, E___Ceylon___1883`

- Staff-list name: **Gratien, E** | colony: **Ceylon** | listed 1883–1886 | editions [1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | E. Gratien | Assistant Colonial Surgeon | Medical Department | — | — |
| 1886 | E. Gratien | Assistant Colonial Surgeon | Medical Department | — | — |

### Deterministic checks: `gratien_e_e1868` vs `Gratien, E___Ceylon___1883`

- [PASS] surname_gate: bio 'GRATIEN' vs stint 'Gratien, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1886
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Gratien, E___Ceylon___1890`

- Staff-list name: **Gratien, E** | colony: **Ceylon** | listed 1890–1894 | editions [1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | E. Gratien | Assistant Colonial Surgeon | Medical Department | — | — |
| 1894 | E. Gratien | Assistant Colonial Surgeon | Medical Department | — | — |

### Deterministic checks: `gratien_e_e1868` vs `Gratien, E___Ceylon___1890`

- [PASS] surname_gate: bio 'GRATIEN' vs stint 'Gratien, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1894
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

