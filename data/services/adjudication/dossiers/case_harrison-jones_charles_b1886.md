<!-- {"case_id": "case_harrison-jones_charles_b1886", "bio_ids": ["harrison-jones_charles_b1886"], "stint_ids": ["Harrison-Jones, C___Ceylon___1921"]} -->
# Dossier case_harrison-jones_charles_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['harrison-jones_charles_b1886'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Harrison-Jones, C___Ceylon___1921` is also gate-compatible with biography(ies) outside this case: ['harrison-jones_charles_b1884'] (already linked elsewhere or filtered).

## Biography `harrison-jones_charles_b1886`

- Printed name: **HARRISON-JONES, CHARLES**
- Birth year: 1886 (attested in editions [1937])
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L61623.v` — printed in editions [1937]:**

> HARRISON-JONES, CHARLES.—B. 1886; Reading and St. John's Coll., Oxford; cadet, Ceylon civ. ser., Nov., 1907; asst. gov't. Colombo and Negombodists., July, 1909; Matara, May, 1912; on military duty, dist. judge Tangalla, Dec., 1919; asst. g. Matale, June, 1920; do., Nuwara Eliya, 1924; gov't. agt., E.P. Jan., 1929; gov't. & P. Nov., 1932; do., S.P., Nov., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | cadet, Ceylon civ. ser | Ceylon | [1937] |
| 1 | 1909 | asst. gov't. Colombo and Negombodists | Ceylon *(inherited from previous clause)* | [1937] |
| 2 | 1912 | Matara | Ceylon *(inherited from previous clause)* | [1937] |
| 3 | 1919 | on military duty, dist. judge Tangalla | Ceylon *(inherited from previous clause)* | [1937] |
| 4 | 1920 | asst. g. Matale | Ceylon *(inherited from previous clause)* | [1937] |
| 5 | 1924 | do., Nuwara Eliya | Ceylon *(inherited from previous clause)* | [1937] |
| 6 | 1929 | gov't. agt., E.P | Ceylon *(inherited from previous clause)* | [1937] |
| 7 | 1932 | gov't. & P | Ceylon *(inherited from previous clause)* | [1937] |
| 8 | 1935 | do., S.P | Ceylon *(inherited from previous clause)* | [1937] |

## Candidate stint `Harrison-Jones, C___Ceylon___1921`

- Staff-list name: **Harrison-Jones, C** | colony: **Ceylon** | listed 1921–1937 | editions [1921, 1922, 1925, 1928, 1931, 1934, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | C. Harrison-Jones | Assistant Government Agent | CENTRAL PROVINCE | — | — |
| 1922 | C. Harrison-Jones | Assistant Government Agent | Government Agencies | — | — |
| 1925 | C. Harrison-Jones | Assistant Government Agent | Central Province | — | — |
| 1928 | C. Harrison-Jones | Collector | Eastern Province | — | — |
| 1931 | C. Harrison-Jones | Collector | Eastern Province | — | — |
| 1931 | C. Harrison-Jones | Government Agent | Government Agencies | — | — |
| 1934 | C. Harrison-Jones | Government Agent | North Western Province | — | — |
| 1937 | C. Harrison-Jones | Collector | Southern Province | — | — |

### Deterministic checks: `harrison-jones_charles_b1886` vs `Harrison-Jones, C___Ceylon___1921`

- [PASS] surname_gate: bio 'HARRISON-JONES' vs stint 'Harrison-Jones, C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1921, birth 1886 (age 35)
- [PASS] colony: 9 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 6 event tenure(s) overlap stint years 1921-1937
- [FAIL] position_sim: best 59 vs bar 60: 'gov't. agt., E.P' ~ 'Government Agent'
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

