<!-- {"case_id": "case_fosbery_e_e1874-2", "bio_ids": ["fosbery_e_e1874-2"], "stint_ids": ["Fosbery, Edmund___New South Wales___1877"]} -->
# Dossier case_fosbery_e_e1874-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['fosbery_e_e1874-2'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Fosbery, Edmund___New South Wales___1877` is also gate-compatible with biography(ies) outside this case: ['fosbery_e_e1874'] (already linked elsewhere or filtered).

## Biography `fosbery_e_e1874-2`

- Printed name: **FOSBERY, E**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L33396.v` — printed in editions [1898]:**

> FOSBERY, E.—Inspr.-gen. of pol., N.S. Wales, Oct., 1874.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | Inspr.-gen. of pol., N.S. Wales | Nova Scotia | [1898] |

## Candidate stint `Fosbery, Edmund___New South Wales___1877`

- Staff-list name: **Fosbery, Edmund** | colony: **New South Wales** | listed 1877–1900 | editions [1877, 1878, 1880, 1886, 1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |
| 1878 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |
| 1880 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |
| 1886 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |
| 1888 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |
| 1889 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |
| 1894 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |
| 1896 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |
| 1897 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |
| 1898 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |
| 1899 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |
| 1900 | Edmund Fosbery | Inspector-General of Police | Police Department | — | — |

### Deterministic checks: `fosbery_e_e1874-2` vs `Fosbery, Edmund___New South Wales___1877`

- [PASS] surname_gate: bio 'FOSBERY' vs stint 'Fosbery, Edmund' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1900
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

