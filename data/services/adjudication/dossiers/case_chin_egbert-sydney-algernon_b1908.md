<!-- {"case_id": "case_chin_egbert-sydney-algernon_b1908", "bio_ids": ["chin_egbert-sydney-algernon_b1908"], "stint_ids": ["Chin, E. S. A___Leeward Islands___1932"]} -->
# Dossier case_chin_egbert-sydney-algernon_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chin_egbert-sydney-algernon_b1908`

- Printed name: **CHIN, EGBERT SYDNEY ALGERNON**
- Birth year: 1908 (attested in editions [1933, 1935])
- Appears in editions: [1933, 1935]

### Verbatim printed entry text (OCR)

**Version `col1933-L58613.v` — printed in editions [1933, 1935]:**

> CHIN, EGBERT SYDNEY ALGERNON, Dip. Agr. (I.C.T.A.).—B. 1908; field offr., genetic dept., cotton research station, Trinidad, 1931; spl. agrl. ast., Montserrat, Mar., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | field offr., genetic dept., cotton research station | Trinidad | [1933, 1935] |
| 1 | 1931 | spl. agrl. ast. | Montserrat | [1933, 1935] |

## Candidate stint `Chin, E. S. A___Leeward Islands___1932`

- Staff-list name: **Chin, E. S. A** | colony: **Leeward Islands** | listed 1932–1933 | editions [1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | E. S. A. Chin | Agricultural Assistant | Agricultural Department | — | — |
| 1933 | E. S. A. Chin | Agricultural Assistant | Agricultural Department | — | — |

### Deterministic checks: `chin_egbert-sydney-algernon_b1908` vs `Chin, E. S. A___Leeward Islands___1932`

- [PASS] surname_gate: bio 'CHIN' vs stint 'Chin, E. S. A' (exact)
- [PASS] initials: bio ['E', 'S', 'A'] ~ stint ['E', 'S', 'A']
- [PASS] age_gate: stint starts 1932, birth 1908 (age 24)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1933
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

