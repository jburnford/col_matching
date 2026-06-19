<!-- {"case_id": "case_downer_j-w_e1881", "bio_ids": ["downer_j-w_e1881", "downer_j-w_e1881-2"], "stint_ids": ["Downer, John William___South Australia___1898"]} -->
# Dossier case_downer_j-w_e1881

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Downer, John William___South Australia___1898'] have more than one claimant biography in this case.
- NOTE: stint `Downer, John William___South Australia___1898` is also gate-compatible with biography(ies) outside this case: ['downer_j-w_b1844'] (already linked elsewhere or filtered).
- NOTE: stint `Downer, John William___South Australia___1898` is also gate-compatible with biography(ies) outside this case: ['downer_j-w_b1844'] (already linked elsewhere or filtered).

## Biography `downer_j-w_e1881`

- Printed name: **DOWNER, J. W**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27240.v` — printed in editions [1883]:**

> DOWNER, HON. J. W., Q.C.—Attorney-general, South Australia, 24 June, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Attorney-general | South Australia | [1883] |

## Biography `downer_j-w_e1881-2`

- Printed name: **DOWNER, J. W.**
- Birth year: not printed
- Honours: Q.C.
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33124.v` — printed in editions [1886]:**

> DOWNER, Hon. J. W., Q.C.—Attorney-general, South Australia, 24 June, 1881, to 16 June, 1884, and again 16 June, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881–1884 | Attorney-general | South Australia | [1886] |
| 1 | 1885 | Attorney-general | — | [1886] |

## Candidate stint `Downer, John William___South Australia___1898`

- Staff-list name: **Downer, John William** | colony: **South Australia** | listed 1898–1906 | editions [1898, 1900, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | Hon. Sir John William Downer, K.C.M.G. | Member | House of Assembly | K.C.M.G. | — |
| 1900 | Sir John William Downer | Member, House of Assembly | House of Assembly | K.C.M.G. | — |
| 1906 | Sir J. W. Downer | Member | Legislative Council | K.C.M.G. | — |

### Deterministic checks: `downer_j-w_e1881` vs `Downer, John William___South Australia___1898`

- [PASS] surname_gate: bio 'DOWNER' vs stint 'Downer, John William' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1906
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `downer_j-w_e1881-2` vs `Downer, John William___South Australia___1898`

- [PASS] surname_gate: bio 'DOWNER' vs stint 'Downer, John William' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1906
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

