<!-- {"case_id": "case_fichat_j_e1882", "bio_ids": ["fichat_j_e1882"], "stint_ids": ["Fichat, James___Cape of Good Hope___1877"]} -->
# Dossier case_fichat_j_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['fichat_j_e1882'] carry a single initial only — the namesake trap applies.

## Biography `fichat_j_e1882`

- Printed name: **FICHAT, J**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33351.v` — printed in editions [1886]:**

> FICHAT, J.—Civil commissioner and resident magistrate, division of Worcester, Cape of Good Hope, 1st March, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Civil commissioner and resident magistrate, division of Worcester | Cape of Good Hope | [1886] |

## Candidate stint `Fichat, James___Cape of Good Hope___1877`

- Staff-list name: **Fichat, James** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | James Fichat | Civil Commissioner and Resident Magistrate | Police Branch | — | — |
| 1878 | James Fichat | Civil Commissioner and Resident Magistrate | DIVISION OF GEORGE | — | — |
| 1880 | James Fichat | Civil Commissioner and Resident Magistrate | DIVISION OF GEORGE | — | — |

### Deterministic checks: `fichat_j_e1882` vs `Fichat, James___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'FICHAT' vs stint 'Fichat, James' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

