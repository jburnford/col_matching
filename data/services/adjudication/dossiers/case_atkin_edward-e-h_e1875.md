<!-- {"case_id": "case_atkin_edward-e-h_e1875", "bio_ids": ["atkin_edward-e-h_e1875"], "stint_ids": ["Atkins, E___Falkland Islands___1930", "Watkin, H___Sierra Leone___1931"]} -->
# Dossier case_atkin_edward-e-h_e1875

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `atkin_edward-e-h_e1875`

- Printed name: **ATKIN, EDWARD E. H.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26256.v` — printed in editions [1883]:**

> ATKIN, EDWARD E. H.—Entered Civil Service, 1875; transferred from patent office to savings bank department, and to War Office, July, 1879; detached for service in Cyprus, Feb. 1880, now clerk in audit office.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Civil Service | — | [1883] |
| 1 | 1879 | clerk | — | [1883] |
| 2 | 1880 | — | Cyprus | [1883] |
| 3 | ? | clerk in audit office | — | [1883] |

## Candidate stint `Atkins, E___Falkland Islands___1930`

- Staff-list name: **Atkins, E** | colony: **Falkland Islands** | listed 1930–1931 | editions [1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | E. Atkins | Clerk | Post Office | — | — |
| 1931 | Miss E. Atkins | Clerk | Post Office | — | — |

### Deterministic checks: `atkin_edward-e-h_e1875` vs `Atkins, E___Falkland Islands___1930`

- [PASS] surname_gate: bio 'ATKIN' vs stint 'Atkins, E' (fuzzy:1)
- [PASS] initials: bio ['E', 'E', 'H'] ~ stint ['E']
- [PASS] age_gate: stint starts 1930; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1931
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Watkin, H___Sierra Leone___1931`

- Staff-list name: **Watkin, H** | colony: **Sierra Leone** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. Watkin | Assistant Electrical Engineer | Public Works Department | — | — |
| 1933 | H. Watkin | Chief Electrical Engineer | Public Works Department | — | — |

### Deterministic checks: `atkin_edward-e-h_e1875` vs `Watkin, H___Sierra Leone___1931`

- [PASS] surname_gate: bio 'ATKIN' vs stint 'Watkin, H' (fuzzy:1)
- [PASS] initials: bio ['E', 'E', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1931; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

