<!-- {"case_id": "case_nettleton_clement-ridgway_e1901", "bio_ids": ["nettleton_clement-ridgway_e1901"], "stint_ids": ["Nettleton, C. R___Basutoland___1899", "Nettleton, C. R___Bechuanaland___1921"]} -->
# Dossier case_nettleton_clement-ridgway_e1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Nettleton, C. R___Basutoland___1899` is also gate-compatible with biography(ies) outside this case: ['nettetton_clement-ridgway_e1901'] (already linked elsewhere or filtered).
- NOTE: stint `Nettleton, C. R___Bechuanaland___1921` is also gate-compatible with biography(ies) outside this case: ['nettetton_clement-ridgway_e1901'] (already linked elsewhere or filtered).

## Biography `nettleton_clement-ridgway_e1901`

- Printed name: **NETTLETON, CLEMENT RIDGWAY**
- Birth year: not printed
- Appears in editions: [1911, 1914, 1918, 1920, 1921, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1911-L46958.v` — printed in editions [1911, 1914, 1918, 1920, 1921, 1923, 1924]:**

> NETTLETON, CLEMENT RIDGWAY.—Inspr., Bechuanaland Prot. pol., May, 1901; seconded from Basutoland service.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | Inspr., Bechuanaland Prot. pol | Bechuanaland | [1911, 1914, 1918, 1920, 1921, 1923, 1924] |

## Candidate stint `Nettleton, C. R___Basutoland___1899`

- Staff-list name: **Nettleton, C. R** | colony: **Basutoland** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | C. R. Nettleton | Sub-Inspector of Police | Establishment | — | — |
| 1900 | C. R. Nettleton | Sub-Inspector of Police | Establishment | — | — |

### Deterministic checks: `nettleton_clement-ridgway_e1901` vs `Nettleton, C. R___Basutoland___1899`

- [PASS] surname_gate: bio 'NETTLETON' vs stint 'Nettleton, C. R' (exact)
- [PASS] initials: bio ['C', 'R'] ~ stint ['C', 'R']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Basutoland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Nettleton, C. R___Bechuanaland___1921`

- Staff-list name: **Nettleton, C. R** | colony: **Bechuanaland** | listed 1921–1922 | editions [1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | C. R. Nettleton | Resident Magistrate, Serowe | Establishment | — | — |
| 1922 | C. R. Nettleton | Resident Magistrate | Establishment | — | — |

### Deterministic checks: `nettleton_clement-ridgway_e1901` vs `Nettleton, C. R___Bechuanaland___1921`

- [PASS] surname_gate: bio 'NETTLETON' vs stint 'Nettleton, C. R' (exact)
- [PASS] initials: bio ['C', 'R'] ~ stint ['C', 'R']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Bechuanaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1922
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

