<!-- {"case_id": "case_volonterio_l-r_b1908", "bio_ids": ["volonterio_l-r_b1908"], "stint_ids": ["Volonterio, L. R___Leeward Islands___1952"]} -->
# Dossier case_volonterio_l-r_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `volonterio_l-r_b1908`

- Printed name: **VOLONTERIO, L. R**
- Birth year: 1908 (attested in editions [1954, 1955])
- Appears in editions: [1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1954-L22697.v` — printed in editions [1954, 1955]:**

> VOLONTERIO, L. R.—b. 1908; ed. privately; mil. serv., 1940-41, sapper cadet; arch. and town plan. advr., Gam., 1946; supt., publ. wks., St. Kitts, 1951; author of Hospital Design and Planning, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | author of Hospital Design and Planning | St. Kitts *(inherited from previous clause)* | [1954, 1955] |
| 1 | 1946 | arch. and town plan. advr., Gam | — | [1954, 1955] |
| 2 | 1951 | supt., publ. wks. | St. Kitts | [1954, 1955] |

## Candidate stint `Volonterio, L. R___Leeward Islands___1952`

- Staff-list name: **Volonterio, L. R** | colony: **Leeward Islands** | listed 1952–1955 | editions [1952, 1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | L. Volonterio | Superintendent of Public Works | Civil Establishment | — | — |
| 1953 | L. R. Volonterio | Superintendent of Public Works | Civil Establishment | — | — |
| 1954 | L. R. Volonterio | Superintendent of Public Works | Civil Establishment | — | — |
| 1955 | L. R. Volonterio | Superintendent of Public Works | Civil Establishment | — | — |

### Deterministic checks: `volonterio_l-r_b1908` vs `Volonterio, L. R___Leeward Islands___1952`

- [PASS] surname_gate: bio 'VOLONTERIO' vs stint 'Volonterio, L. R' (exact)
- [PASS] initials: bio ['L', 'R'] ~ stint ['L', 'R']
- [PASS] age_gate: stint starts 1952, birth 1908 (age 44)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1952-1955
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

