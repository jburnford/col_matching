<!-- {"case_id": "case_oorloff_cedric-james_b1906", "bio_ids": ["oorloff_cedric-james_b1906"], "stint_ids": ["Oorloff, C. J___Ceylon___1934"]} -->
# Dossier case_oorloff_cedric-james_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Oorloff, C. J___Ceylon___1934` is also gate-compatible with biography(ies) outside this case: ['oorloof_charles-james_b1906'] (already linked elsewhere or filtered).

## Biography `oorloff_cedric-james_b1906`

- Printed name: **OORLOFF, CEDRIC JAMES**
- Birth year: 1906 (attested in editions [1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L67368.v` — printed in editions [1940]:**

> OORLOFF, CEDRIC JAMES, B.A. (Lond.)—B. 1906; cadet, Ceylon civ. serv., Oct., 1930; attd., secretariat, Oct., 1930; attd., Kalutara kach., July, 1931; office asst., Hambantota kach., Oct., 1932; do., Nawara Eliya kach., Apr., 1935; pol. mag., Puttalam, Nov., 1937; asst. commntr., lands, July, 1938.

**Version `col1939-L69545.v` — printed in editions [1939]:**

> ORLOFF, CEDRIC JAMES, B.A. (Lond.).—B. 1906; cadet, Ceylon civ. serv., Oct., 1930; attd., secretariat, Oct., 1930; attd., Kalutara kach., July, 1931; office asst., Hambantota kach., Oct., 1932; do., Nuwara Eliya kach., Apr., 1936; pol. mag., Puttalam, Nov., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | cadet, Ceylon civ. serv | Ceylon | [1939, 1940] |
| 1 | 1931 | attd., Kalutara kach | Ceylon *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1932 | office asst., Hambantota kach | Ceylon *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1935 | do., Nawara Eliya kach | Ceylon *(inherited from previous clause)* | [1940] |
| 4 | 1936 | do., Nuwara Eliya kach | Ceylon *(inherited from previous clause)* | [1939] |
| 5 | 1937 | pol. mag., Puttalam | Ceylon *(inherited from previous clause)* | [1939, 1940] |
| 6 | 1938 | asst. commntr., lands | Ceylon *(inherited from previous clause)* | [1940] |

## Candidate stint `Oorloff, C. J___Ceylon___1934`

- Staff-list name: **Oorloff, C. J** | colony: **Ceylon** | listed 1934–1940 | editions [1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | C. J. Oorloff | Office Assistant | Southern Province | — | — |
| 1936 | C. J. Oorloff | Office Assistant | Central Province | — | — |
| 1937 | C. J. Oorloff | Office Assistant | CENTRAL PROVINCE | — | — |
| 1940 | C. J. Oorloff | Landing Surveyor | Customs Department | — | — |

### Deterministic checks: `oorloff_cedric-james_b1906` vs `Oorloff, C. J___Ceylon___1934`

- [PASS] surname_gate: bio 'OORLOFF' vs stint 'Oorloff, C. J' (exact)
- [PASS] initials: bio ['C', 'J'] ~ stint ['C', 'J']
- [PASS] age_gate: stint starts 1934, birth 1906 (age 28)
- [PASS] colony: 7 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1934-1940
- [PASS] position_sim: best 65 vs bar 60: 'office asst., Hambantota kach' ~ 'Office Assistant'
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

