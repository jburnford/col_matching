<!-- {"case_id": "case_gisborne_hartley_e1876", "bio_ids": ["gisborne_hartley_e1876"], "stint_ids": ["Gisborne, F. H___Canada___1912"]} -->
# Dossier case_gisborne_hartley_e1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gisborne_hartley_e1876'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Gisborne, F. H___Canada___1912` is also gate-compatible with biography(ies) outside this case: ['gisborne_francis-hernaman_b1858'] (already linked elsewhere or filtered).

## Biography `gisborne_hartley_e1876`

- Printed name: **GISBORNE, HARTLEY**
- Birth year: not printed
- Honours: A.M, C.E, M.A.I.E.E
- Appears in editions: [1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1890-L34203.v` — printed in editions [1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906]:**

> GISBORNE, HARTLEY, A.M., Cam., C.E., M.A.I.E.E.—Ed. at Mercers school and Windsor Coll., Canada; asst. geological surveyor, Canada, 1876; telegraph engineer, 1880; dist. tel. superint., Manitoba, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | asst. geological surveyor | Canada | [1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906] |
| 1 | 1880 | telegraph engineer | Canada *(inherited from previous clause)* | [1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906] |
| 2 | 1882 | dist. tel. superint., Manitoba | Canada *(inherited from previous clause)* | [1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906] |

## Candidate stint `Gisborne, F. H___Canada___1912`

- Staff-list name: **Gisborne, F. H** | colony: **Canada** | listed 1912–1922 | editions [1912, 1913, 1914, 1915, 1917, 1919, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | F. H. Gisborne | Secretary | DEPARTMENT OF JUSTICE | — | — |
| 1913 | F. H. Gisborne | Assistant Deputy and Secretary | Department of Justice | — | — |
| 1914 | F. H. Gisborne | Chief Parliamentary Counsel | House of Commons | — | — |
| 1915 | F. H. Gisborne | Parliamentary Counsel | House of Commons | — | — |
| 1917 | F. H. Gisborne | Parliamentary Counsel | — | — | — |
| 1919 | F. H. Gisborne | Parliamentary Counsel | House of Commons | — | — |
| 1922 | F. H. Gisborne | Parliamentary Counsel | House of Commons | — | — |

### Deterministic checks: `gisborne_hartley_e1876` vs `Gisborne, F. H___Canada___1912`

- [PASS] surname_gate: bio 'GISBORNE' vs stint 'Gisborne, F. H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1922
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

