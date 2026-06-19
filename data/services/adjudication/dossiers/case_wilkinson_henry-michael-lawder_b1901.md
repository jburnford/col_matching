<!-- {"case_id": "case_wilkinson_henry-michael-lawder_b1901", "bio_ids": ["wilkinson_henry-michael-lawder_b1901"], "stint_ids": ["Wilkinson, H. M. L___Northern Rhodesia___1939"]} -->
# Dossier case_wilkinson_henry-michael-lawder_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 72 official(s) with this surname in the graph's staff lists; 34 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wilkinson_henry-michael-lawder_b1901`

- Printed name: **WILKINSON, Henry Michael Lawder**
- Birth year: 1901 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L36865.v` — printed in editions [1948]:**

> WILKINSON, Henry Michael Lawder.—b. 1901; ed. Private Sch., Canada, Fitzwilliam Hall, Cambridge Univ. (Sch. of Agric.); police const., N. Rhod., 1929; asst. inspr., 1931; inspr., 1935; asst. supt., 1938; supt., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | police const. | Northern Rhodesia | [1948] |
| 1 | 1931 | asst. inspr | Northern Rhodesia *(inherited from previous clause)* | [1948] |
| 2 | 1935 | inspr | Northern Rhodesia *(inherited from previous clause)* | [1948] |
| 3 | 1938 | asst. supt | Northern Rhodesia *(inherited from previous clause)* | [1948] |
| 4 | 1946 | supt | Northern Rhodesia *(inherited from previous clause)* | [1948] |

## Candidate stint `Wilkinson, H. M. L___Northern Rhodesia___1939`

- Staff-list name: **Wilkinson, H. M. L** | colony: **Northern Rhodesia** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | H. M. L. Wilkinson | Assistant Superintendent | Northern Rhodesia Police | — | — |
| 1940 | H. M. L. Wilkinson | Assistant Superintendent | Northern Rhodesia Police | — | — |

### Deterministic checks: `wilkinson_henry-michael-lawder_b1901` vs `Wilkinson, H. M. L___Northern Rhodesia___1939`

- [PASS] surname_gate: bio 'WILKINSON' vs stint 'Wilkinson, H. M. L' (exact)
- [PASS] initials: bio ['H', 'M', 'L'] ~ stint ['H', 'M', 'L']
- [PASS] age_gate: stint starts 1939, birth 1901 (age 38)
- [PASS] colony: 5 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 55 vs bar 60: 'asst. supt' ~ 'Assistant Superintendent'
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

