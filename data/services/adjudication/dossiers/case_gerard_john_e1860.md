<!-- {"case_id": "case_gerard_john_e1860", "bio_ids": ["gerard_john_e1860"], "stint_ids": ["Gerard, J. S___Jamaica___1888"]} -->
# Dossier case_gerard_john_e1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gerard_john_e1860'] carry a single initial only — the namesake trap applies.

## Biography `gerard_john_e1860`

- Printed name: **GERARD, JOHN**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27620.v` — printed in editions [1883]:**

> GERARD, JOHN.—Second clerk in the registrar-general's office, Hong Kong, 1860.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860 | Second clerk in the registrar-general's office | Hong Kong | [1883] |

## Candidate stint `Gerard, J. S___Jamaica___1888`

- Staff-list name: **Gerard, J. S** | colony: **Jamaica** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | J. S. Gerard | District Medical Officer | Medical Department | — | — |
| 1889 | J. S. Gerard | District Medical Officer | Medical Department | — | — |
| 1890 | J. S. Gerard | District Medical Officer | Medical Department | — | — |

### Deterministic checks: `gerard_john_e1860` vs `Gerard, J. S___Jamaica___1888`

- [PASS] surname_gate: bio 'GERARD' vs stint 'Gerard, J. S' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1890
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

