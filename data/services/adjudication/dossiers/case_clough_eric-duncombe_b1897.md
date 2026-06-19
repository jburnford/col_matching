<!-- {"case_id": "case_clough_eric-duncombe_b1897", "bio_ids": ["clough_eric-duncombe_b1897"], "stint_ids": ["Clough, E. D___Northern Rhodesia___1936"]} -->
# Dossier case_clough_eric-duncombe_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `clough_eric-duncombe_b1897`

- Printed name: **CLOUGH, Eric Duncombe**
- Birth year: 1897 (attested in editions [1949])
- Appears in editions: [1949]

### Verbatim printed entry text (OCR)

**Version `col1949-L31163.v` — printed in editions [1949]:**

> CLOUGH, Eric Duncombe.—b. 1897; ed. Brighton Gram. Sch.; on mil. serv. 1914-19, lieut.; prob., B.S.A. Coy., 1921; asst. native comsnr., N. Rhod., 1923; dist. offr., gr. III, 1929; gr. II, 1934; gr. I, 1941; prov. comsnr., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | prob., B.S.A. Coy | — | [1949] |
| 1 | 1923 | asst. native comsnr. | Northern Rhodesia | [1949] |
| 2 | 1929 | dist. offr., gr. III | Northern Rhodesia *(inherited from previous clause)* | [1949] |
| 3 | 1934 | gr. II | Northern Rhodesia *(inherited from previous clause)* | [1949] |
| 4 | 1941 | gr. I | Northern Rhodesia *(inherited from previous clause)* | [1949] |
| 5 | 1944 | prov. comsnr | Northern Rhodesia *(inherited from previous clause)* | [1949] |

## Candidate stint `Clough, E. D___Northern Rhodesia___1936`

- Staff-list name: **Clough, E. D** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | E. D. Clough | District Officers | District Administration | — | — |
| 1939 | E. D. Clough | District Officer | District Administration | — | — |
| 1940 | E. D. Clough | District Officer | District Administration | — | — |

### Deterministic checks: `clough_eric-duncombe_b1897` vs `Clough, E. D___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'CLOUGH' vs stint 'Clough, E. D' (exact)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E', 'D']
- [PASS] age_gate: stint starts 1936, birth 1897 (age 39)
- [PASS] colony: 5 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 30 vs bar 60: 'gr. I' ~ 'District Officer'
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

