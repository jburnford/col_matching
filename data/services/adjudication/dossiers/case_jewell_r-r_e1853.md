<!-- {"case_id": "case_jewell_r-r_e1853", "bio_ids": ["jewell_r-r_e1853"], "stint_ids": ["Jewell, R. R___Western Australia___1877"]} -->
# Dossier case_jewell_r-r_e1853

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Jewell, R. R___Western Australia___1877` is also gate-compatible with biography(ies) outside this case: ['jewell_rich-roach_e1854'] (already linked elsewhere or filtered).

## Biography `jewell_r-r_e1853`

- Printed name: **JEWELL, R. R**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34228.v` — printed in editions [1886]:**

> JEWELL, R. R.—Clark of works, works and railways department, Western Australia, Jan., 1853.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1853 | Clark of works, works and railways department | Western Australia | [1886] |

## Candidate stint `Jewell, R. R___Western Australia___1877`

- Staff-list name: **Jewell, R. R** | colony: **Western Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. R. Jewell | Clerk of Works | Civil Establishment | — | — |
| 1878 | R. R. Jewell | Clerk of Works | Civil Establishment | — | — |
| 1879 | R. R. Jewell | Clerk of Works | Office of Works | — | — |
| 1880 | R. R. Jewell | Clerk of Works | Works and Railways Department | — | — |

### Deterministic checks: `jewell_r-r_e1853` vs `Jewell, R. R___Western Australia___1877`

- [PASS] surname_gate: bio 'JEWELL' vs stint 'Jewell, R. R' (exact)
- [PASS] initials: bio ['R', 'R'] ~ stint ['R', 'R']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Western Australia'
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

