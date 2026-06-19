<!-- {"case_id": "case_winston_j-h_e1874-2", "bio_ids": ["winston_j-h_e1874-2"], "stint_ids": ["Winston, J. H___Dominica___1886"]} -->
# Dossier case_winston_j-h_e1874-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Winston, J. H___Dominica___1886` is also gate-compatible with biography(ies) outside this case: ['winston_j-h_e1874'] (already linked elsewhere or filtered).

## Biography `winston_j-h_e1874-2`

- Printed name: **WINSTON, J. H**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908]

### Verbatim printed entry text (OCR)

**Version `col1888-L36845.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908]:**

> WINSTON, J. H.—Sub-inspector of roads, Dominica, Mar., 1874; inspector of roads and ranger of crown lands, Sept., 1882; is now district government officer.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | Sub-inspector of roads | Dominica | [1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908] |
| 1 | 1882 | inspector of roads and ranger of crown lands | Dominica *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908] |

## Candidate stint `Winston, J. H___Dominica___1886`

- Staff-list name: **Winston, J. H** | colony: **Dominica** | listed 1886–1888 | editions [1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | J. H. Winston | Sub-Inspector of Roads | Civil Establishment | — | — |
| 1888 | J. H. Winston | Sub-Inspector of Roads | Sub-Inspector of Roads | — | — |

### Deterministic checks: `winston_j-h_e1874-2` vs `Winston, J. H___Dominica___1886`

- [PASS] surname_gate: bio 'WINSTON' vs stint 'Winston, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Dominica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1888
- [FAIL] position_sim: best 58 vs bar 60: 'inspector of roads and ranger of crown lands' ~ 'Sub-Inspector of Roads'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1888] pos~58 (bar: >=2)
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

