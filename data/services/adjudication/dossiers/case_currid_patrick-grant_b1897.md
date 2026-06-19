<!-- {"case_id": "case_currid_patrick-grant_b1897", "bio_ids": ["currid_patrick-grant_b1897"], "stint_ids": ["Currid, P. G___Straits Settlements___1931"]} -->
# Dossier case_currid_patrick-grant_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `currid_patrick-grant_b1897`

- Printed name: **CURRID, PATRICK GRANT**
- Birth year: 1897 (attested in editions [1940])
- Honours: M.B
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63522.v` — printed in editions [1940]:**

> CURRID, PATRICK GRANT, M.B., Ch.B., M.A. (Aberd.), D.P.H. (Univ. Lond.) Certif. L.S.T.M. (with dist.).—B. 1897; war serv., 1916-19; M.O., Malaya, Mar., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | M.O. | Malaya | [1940] |

## Candidate stint `Currid, P. G___Straits Settlements___1931`

- Staff-list name: **Currid, P. G** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | P. G. Currid | Health Officer | Health Branch | — | — |
| 1933 | P. G. Currid | Health Officer | Health Branch | — | — |

### Deterministic checks: `currid_patrick-grant_b1897` vs `Currid, P. G___Straits Settlements___1931`

- [PASS] surname_gate: bio 'CURRID' vs stint 'Currid, P. G' (exact)
- [PASS] initials: bio ['P', 'G'] ~ stint ['P', 'G']
- [PASS] age_gate: stint starts 1931, birth 1897 (age 34)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
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

