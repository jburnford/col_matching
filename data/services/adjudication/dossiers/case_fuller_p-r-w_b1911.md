<!-- {"case_id": "case_fuller_p-r-w_b1911", "bio_ids": ["fuller_p-r-w_b1911"], "stint_ids": ["Fuller, P. R. W___Northern Rhodesia___1949"]} -->
# Dossier case_fuller_p-r-w_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 40 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fuller_p-r-w_b1911`

- Printed name: **FULLER, P. R. W**
- Birth year: 1911 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Honours: M.B.E
- Appears in editions: [1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1957-L23181.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> FULLER, P. R. W., M.B.E.—b. 1911; ed. Plumtree High Sch., S. Rhod.; clk., N. Rhod., 1931; asst. estab. offr., 1945; estab. offr., 1951; ret.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | clk. | Northern Rhodesia | [1957, 1958, 1959, 1960, 1961] |
| 1 | 1945 | asst. estab. offr | Northern Rhodesia *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 2 | 1951 | estab. offr | Northern Rhodesia *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Fuller, P. R. W___Northern Rhodesia___1949`

- Staff-list name: **Fuller, P. R. W** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. R. W. Fuller | Assistant Establishment Officers | Secretariat | — | — |
| 1951 | P. R. W. Fuller | Assistant Establishment Officers | Secretariat | — | — |

### Deterministic checks: `fuller_p-r-w_b1911` vs `Fuller, P. R. W___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'FULLER' vs stint 'Fuller, P. R. W' (exact)
- [PASS] initials: bio ['P', 'R', 'W'] ~ stint ['P', 'R', 'W']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 64 vs bar 60: 'asst. estab. offr' ~ 'Assistant Establishment Officers'
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

