<!-- {"case_id": "case_kannangara_charles-henry-wilkokon_b1889", "bio_ids": ["kannangara_charles-henry-wilkokon_b1889"], "stint_ids": ["Kannangara, C. H. W___Ceylon___1931"]} -->
# Dossier case_kannangara_charles-henry-wilkokon_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kannangara_charles-henry-wilkokon_b1889`

- Printed name: **KANNANGARA, CHARLES HENRY WILKOKON**
- Birth year: 1889 (attested in editions [1937])
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L62272.v` — printed in editions [1937]:**

> KANNANGARA, CHARLES HENRY WILKOKON.—B. 1889; Ceylon civ. serv., Oct., 1928; office asst., Matara kach., Oct., 1928; extra office asst., Ratnapura kach., Jan., 1934; dep. fiscal, Colombo, Apr., 1934; ag. office asst., Kurunegala kach., Oct., 1934; addnl. office asst., Kurunegala kach., Feb., 1935; office asst., do., June., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | Ceylon civ. serv | Ceylon | [1937] |
| 1 | 1934 | extra office asst., Ratnapura kach | Ceylon *(inherited from previous clause)* | [1937] |
| 2 | 1935 | addnl. office asst., Kurunegala kach | Dominions Office | [1937] |

## Candidate stint `Kannangara, C. H. W___Ceylon___1931`

- Staff-list name: **Kannangara, C. H. W** | colony: **Ceylon** | listed 1931–1940 | editions [1931, 1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | C. H. W. Kannangara | Office Assistant | Government Agencies | — | — |
| 1934 | C. H. W. Kannangara | Office Assistant | Southern Province | — | — |
| 1936 | C. H. W. Kannangara | Office Assistant | North Western Province | — | — |
| 1937 | C. H. W. Kannangara | Office Assistant | NORTH WESTERN PROVINCE | — | — |
| 1940 | C. H. W. Kannangara | Office Assistant | Government Agencies | — | — |

### Deterministic checks: `kannangara_charles-henry-wilkokon_b1889` vs `Kannangara, C. H. W___Ceylon___1931`

- [PASS] surname_gate: bio 'KANNANGARA' vs stint 'Kannangara, C. H. W' (exact)
- [PASS] initials: bio ['C', 'H', 'W'] ~ stint ['C', 'H', 'W']
- [PASS] age_gate: stint starts 1931, birth 1889 (age 42)
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1931-1940
- [FAIL] position_sim: best 55 vs bar 60: 'extra office asst., Ratnapura kach' ~ 'Office Assistant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

