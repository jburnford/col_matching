<!-- {"case_id": "case_o-malley_king_e1901", "bio_ids": ["o-malley_king_e1901"], "stint_ids": ["O'Malley, King___Commonwealth Of Australia___1905"]} -->
# Dossier case_o-malley_king_e1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['o-malley_king_e1901'] carry a single initial only — the namesake trap applies.

## Biography `o-malley_king_e1901`

- Printed name: **O'MALLEY, KING**
- Birth year: not printed
- Terminal: resigned 1916 — “resigned, 14th Nov., 1916.”
- Appears in editions: [1917]

### Verbatim printed entry text (OCR)

**Version `col1917-L52230.v` — printed in editions [1917]:**

> O'MALLEY, Hon. KING.—Formerly M.H.A., S. Australia; elec. to first H. of R., C. of A., 1901; re-elec., 1903 and 1906; min. for home affairs, C. of A., Apr., 1910 to June, 1913, and from 27th Oct., 1915; resigned, 14th Nov., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1901 | first H. of R. | Commonwealth of Australia | [1917] |
| 1 | 1903–1906 | re-elec. | — | [1917] |
| 2 | 1910–1913 | min. for home affairs | Commonwealth of Australia | [1917] |
| 3 | 1915 | min. for home affairs | — | [1917] |
| 4 | ? | M.H.A. | South Australia | [1917] |

## Candidate stint `O'Malley, King___Commonwealth Of Australia___1905`

- Staff-list name: **O'Malley, King** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | King O'Malley | Member for Darwin | — | — | — |
| 1907 | Hon. King O'Malley | — | TASMANIA | — | — |

### Deterministic checks: `o-malley_king_e1901` vs `O'Malley, King___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'O'MALLEY' vs stint 'O'Malley, King' (exact)
- [PASS] initials: bio ['K'] ~ stint ['K']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Commonwealth Of Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

