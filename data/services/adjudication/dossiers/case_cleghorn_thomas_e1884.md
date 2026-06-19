<!-- {"case_id": "case_cleghorn_thomas_e1884", "bio_ids": ["cleghorn_thomas_e1884"], "stint_ids": ["Cleghorn, T___Leeward Islands___1886"]} -->
# Dossier case_cleghorn_thomas_e1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cleghorn_thomas_e1884'] carry a single initial only — the namesake trap applies.

## Biography `cleghorn_thomas_e1884`

- Printed name: **CLEGHORN, Thomas**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1888-L32674.v` — printed in editions [1888, 1889, 1890, 1894, 1896]:**

> CLEGHORN, Thomas.—Clark, public library, Antigua, Aug., 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884 | Clark, public library | Antigua | [1888, 1889, 1890, 1894, 1896] |

## Candidate stint `Cleghorn, T___Leeward Islands___1886`

- Staff-list name: **Cleghorn, T** | colony: **Leeward Islands** | listed 1886–1889 | editions [1886, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | T. Cleghorn | Clerk to the Public Library | Civil Establishment | — | — |
| 1889 | T. Cleghorn | Clerk to the Public Library | Civil Establishment | — | — |

### Deterministic checks: `cleghorn_thomas_e1884` vs `Cleghorn, T___Leeward Islands___1886`

- [PASS] surname_gate: bio 'CLEGHORN' vs stint 'Cleghorn, T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1889
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

