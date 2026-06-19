<!-- {"case_id": "case_aylward_walter-precival_b1899", "bio_ids": ["aylward_walter-precival_b1899"], "stint_ids": ["Aylward, W. P___Unfederated Malay States___1933"]} -->
# Dossier case_aylward_walter-precival_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `aylward_walter-precival_b1899`

- Printed name: **AYLWARD, WALTER PRECIVAL**
- Birth year: 1899 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L64520.v` — printed in editions [1939, 1940]:**

> AYLWARD, WALTER PRECIVAL.—B. 1899; ed. Cranleigh Sch.; survey probr., Selangor, July, 1921; surv.-on-agr., Aug., 1926; asst. supt., N.S., Mar., 1930; do., Kelantan, Jan., 1931; ag. supt., Kelantan, June, 1935; ag. ch. surv., Pahang, June, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | survey probr., Selangor | — | [1939, 1940] |
| 1 | 1926 | surv.-on-agr | — | [1939, 1940] |
| 2 | 1930 | asst. supt. | Nova Scotia | [1939, 1940] |
| 3 | 1931 | asst. supt. | Kelantan | [1939, 1940] |
| 4 | 1935 | ag. supt. | Kelantan | [1939, 1940] |
| 5 | 1938 | ag. ch. surv., Pahang | Kelantan *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Aylward, W. P___Unfederated Malay States___1933`

- Staff-list name: **Aylward, W. P** | colony: **Unfederated Malay States** | listed 1933–1936 | editions [1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | W. P. Aylward | Assistant Superintendent of Surveys | Civil Establishment | — | — |
| 1936 | W. P. Aylward | Superintendent of Surveys | Civil Establishment | — | — |

### Deterministic checks: `aylward_walter-precival_b1899` vs `Aylward, W. P___Unfederated Malay States___1933`

- [PASS] surname_gate: bio 'AYLWARD' vs stint 'Aylward, W. P' (exact)
- [PASS] initials: bio ['W', 'P'] ~ stint ['W', 'P']
- [PASS] age_gate: stint starts 1933, birth 1899 (age 34)
- [PASS] colony: 3 placed event(s) resolve to 'Unfederated Malay States'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1936
- [FAIL] position_sim: best 41 vs bar 60: 'asst. supt.' ~ 'Assistant Superintendent of Surveys'
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

