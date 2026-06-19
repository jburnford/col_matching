<!-- {"case_id": "case_gee_hugh-leslie-denham_b1899", "bio_ids": ["gee_hugh-leslie-denham_b1899"], "stint_ids": ["Gee, H. L. D___Cyprus___1934"]} -->
# Dossier case_gee_hugh-leslie-denham_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gee_hugh-leslie-denham_b1899`

- Printed name: **GEE, Hugh Leslie Denham**
- Birth year: 1899 (attested in editions [1948, 1949])
- Honours: M.B.E (1948)
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L32782.v` — printed in editions [1948, 1949]:**

> GEE, Hugh Leslie Denham, M.B.E. (1948).—b. 1899; ed. privately; apptd. col. serv., 1929; resp. supt., prisons, Cyp.; temp. asst. supt., police and prisons, Pal., 1941; asst. supt., prisons, 1946; senr. asst. supt., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | apptd. col. serv | — | [1948, 1949] |
| 1 | 1941 | temp. asst. supt., police and prisons | Palestine | [1948, 1949] |
| 2 | 1946 | asst. supt., prisons | Palestine *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1947 | senr. asst. supt | Palestine *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Gee, H. L. D___Cyprus___1934`

- Staff-list name: **Gee, H. L. D** | colony: **Cyprus** | listed 1934–1939 | editions [1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | H. L. D. Gee | Resident Superintendent, Central Prison | Prison Department | — | — |
| 1936 | H. L. D. Gee | Resident Superintendent, Central Prison | Prison Department | — | — |
| 1939 | H. L. D. Gee | Resident Superintendent, Central Prison | Prison Department | — | — |

### Deterministic checks: `gee_hugh-leslie-denham_b1899` vs `Gee, H. L. D___Cyprus___1934`

- [PASS] surname_gate: bio 'GEE' vs stint 'Gee, H. L. D' (exact)
- [PASS] initials: bio ['H', 'L', 'D'] ~ stint ['H', 'L', 'D']
- [PASS] age_gate: stint starts 1934, birth 1899 (age 35)
- [FAIL] colony: no placed event resolves to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1939
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

