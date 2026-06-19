<!-- {"case_id": "case_selby_francis-leslie-george_b1902", "bio_ids": ["selby_francis-leslie-george_b1902"], "stint_ids": ["Selby, F. G___Nigeria___1956"]} -->
# Dossier case_selby_francis-leslie-george_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Selby, F. G___Nigeria___1956` is also gate-compatible with biography(ies) outside this case: ['selby_f-g_b1910'] (already linked elsewhere or filtered).

## Biography `selby_francis-leslie-george_b1902`

- Printed name: **SELBY, Francis Leslie George**
- Birth year: 1902 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35788.v` — printed in editions [1948, 1949, 1950, 1951]:**

> SELBY, Francis Leslie George, M.R.C.S. (Eng.), L.R.C.P. (Lond.).—b. 1902; ed. Allhallows Sch., Honiton and St. Mary's Hosp., London; med. offr., Nig., 1927; S.M.O., 1945; asst. D.M.S., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | med. offr. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1945 | S.M.O | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1949 | asst. D.M.S | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Selby, F. G___Nigeria___1956`

- Staff-list name: **Selby, F. G** | colony: **Nigeria** | listed 1956–1958 | editions [1956, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | F. G. Selby | Commissioner of Income Tax | Civil Establishment | — | — |
| 1958 | F. G. Selby | Commissioner of Income Tax | Civil Establishment | C.B.E. | — |

### Deterministic checks: `selby_francis-leslie-george_b1902` vs `Selby, F. G___Nigeria___1956`

- [PASS] surname_gate: bio 'SELBY' vs stint 'Selby, F. G' (exact)
- [PASS] initials: bio ['F', 'L', 'G'] ~ stint ['F', 'G']
- [PASS] age_gate: stint starts 1956, birth 1902 (age 54)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1956-1958
- [FAIL] position_sim: best 24 vs bar 60: 'asst. D.M.S' ~ 'Commissioner of Income Tax'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

