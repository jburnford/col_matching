<!-- {"case_id": "case_reid_d-g_b1925", "bio_ids": ["reid_d-g_b1925"], "stint_ids": ["Reid, D. G___Sierra Leone___1950"]} -->
# Dossier case_reid_d-g_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 106 official(s) with this surname in the graph's staff lists; 37 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `reid_d-g_b1925`

- Printed name: **REID, D. G**
- Birth year: 1925 (attested in editions [1959, 1960, 1961, 1962])
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L27199.v` — printed in editions [1959, 1960, 1961, 1962]:**

> REID, D. G.—b. 1925; ed. Sedbergh Sch. and Trinity Hall, Camb.; mil. serv., 1944-46, R.M.; cadet, S. Leone, 1949; asst. dist. comsnnr., 1952; dist. comsnnr., 1956; clk., ex-co., 1957; secon., C.O., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | cadet, S. Leone | — | [1959, 1960, 1961, 1962] |
| 1 | 1952 | asst. dist. comsnnr | — | [1959, 1960, 1961, 1962] |
| 2 | 1956 | dist. comsnnr | — | [1959, 1960, 1961, 1962] |
| 3 | 1957 | clk., ex-co | — | [1959, 1960, 1961, 1962] |
| 4 | 1958 | secon. | Colonial Office | [1959, 1960, 1961, 1962] |

## Candidate stint `Reid, D. G___Sierra Leone___1950`

- Staff-list name: **Reid, D. G** | colony: **Sierra Leone** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | D. G. Reid | Assistant District Commissioners and Cadets | Provincial Administration | — | — |
| 1951 | D. G. Reid | Assistant District Commissioner and Cadet | Provincial Administration | — | — |

### Deterministic checks: `reid_d-g_b1925` vs `Reid, D. G___Sierra Leone___1950`

- [PASS] surname_gate: bio 'REID' vs stint 'Reid, D. G' (exact)
- [PASS] initials: bio ['D', 'G'] ~ stint ['D', 'G']
- [PASS] age_gate: stint starts 1950, birth 1925 (age 25)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

