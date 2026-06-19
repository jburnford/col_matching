<!-- {"case_id": "case_leung_fung-ki_b1905", "bio_ids": ["leung_fung-ki_b1905"], "stint_ids": ["Leung, F. K___Hong Kong___1950"]} -->
# Dossier case_leung_fung-ki_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `leung_fung-ki_b1905`

- Printed name: **LEUNG, Fung Ki**
- Birth year: 1905 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Honours: M.B.E
- Appears in editions: [1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1957-L24975.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> LEUNG, Fung Ki, M.B.E.—b. 1905; ed. Queen's Coll., H.K. Univ.; asst. master, H.K., 1927; master (educ. offr.), 1946; senr. educ. offr., 1954; mem. of court, H. K. Univ.; dir., widows' and orphans' pensions fund.

**Version `col1962-L23554.v` — printed in editions [1962]:**

> LEUNG, Fung Ki, M.B.E.—b. 1905; ed. Queen's Coll., H.K. Univ.; asst. master, H.K., 1927; master (educ. offr.), 1946; senr. educ. offr., 1954-61.

**Version `col1950-L37244.v` — printed in editions [1950, 1951]:**

> LEUNG, Fung Ki.—b. 1905; ed. Queen’s Coll. and H.K. Univ., B.A. (educ.) (H.K.); univ. trained mstr., educ. dept., H.K., 1927; mstr., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | asst. master | Hong Kong | [1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1946 | master (educ. offr.) | Hong Kong *(inherited from previous clause)* | [1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1954 | senr. educ. offr | Hong Kong *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Leung, F. K___Hong Kong___1950`

- Staff-list name: **Leung, F. K** | colony: **Hong Kong** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | F. K. Leung | Masters | Education | — | — |
| 1951 | F. K. Leung | Masters | Education | — | — |

### Deterministic checks: `leung_fung-ki_b1905` vs `Leung, F. K___Hong Kong___1950`

- [PASS] surname_gate: bio 'LEUNG' vs stint 'Leung, F. K' (exact)
- [PASS] initials: bio ['F', 'K'] ~ stint ['F', 'K']
- [PASS] age_gate: stint starts 1950, birth 1905 (age 45)
- [PASS] colony: 3 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 52 vs bar 60: 'master (educ. offr.)' ~ 'Masters'
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

