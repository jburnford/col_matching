<!-- {"case_id": "case_kirwan_brian-edmond-redshaw_b1913", "bio_ids": ["kirwan_brian-edmond-redshaw_b1913"], "stint_ids": ["Kirwan, B. E. R___Uganda___1936"]} -->
# Dossier case_kirwan_brian-edmond-redshaw_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kirwan_brian-edmond-redshaw_b1913`

- Printed name: **KIRWAN, Brian Edmond Redshaw**
- Birth year: 1913 (attested in editions [1957, 1958, 1959, 1960])
- Honours: F.G.S
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1957-L24747.v` — printed in editions [1957, 1958, 1959, 1960]:**

> KIRWAN, B. E. R.—b. 1913; ed. privately and Univ. of London; mil. serv., 1939-43; lieut.; improver, educ. dept., Uga., 1931; lab. asst., geol. survey, 1933; asst. infn. offr., 1945; community devel. offr., 1947; govt. translator, Hancock report, 1954; co-author Elementary Luganda, 1951, and A Runyankore Grammar.

**Version `col1948-L33854.v` — printed in editions [1948, 1949, 1950, 1951]:**

> KIRWAN, Brian Edmond Redshaw, F.G.S.—b. 1913; ed. privately; on mil. serv., 1939-43, lieut.; apptd. educ. dept., Uga., 1931; geol. survey dept., 1933; asst. pub. relations offr., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | improver, educ. dept. | Uganda | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960] |
| 1 | 1933 | lab. asst., geol. survey | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960] |
| 2 | 1939–1943 | mil. serv. | — | [1957, 1958, 1959, 1960] |
| 3 | 1945 | asst. infn. offr. | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960] |
| 4 | 1947 | community devel. offr. | — | [1957, 1958, 1959, 1960] |
| 5 | 1951 | co-author Elementary Luganda, and A Runyankore Grammar | — | [1957, 1958, 1959, 1960] |
| 6 | 1954 | govt. translator, Hancock report | — | [1957, 1958, 1959, 1960] |

## Candidate stint `Kirwan, B. E. R___Uganda___1936`

- Staff-list name: **Kirwan, B. E. R** | colony: **Uganda** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | B. E. R. Kirwan | Laboratory Apprentice | Geological Survey | — | — |
| 1937 | B. E. R. Kirwan | Laboratory Apprentice | Geological Survey | — | — |
| 1939 | B. E. R. Kirwan | Junior Laboratory Assistant | Geological Survey | — | — |
| 1940 | B. E. R. Kirwan | Laboratory Assistant | Geological Survey | — | — |

### Deterministic checks: `kirwan_brian-edmond-redshaw_b1913` vs `Kirwan, B. E. R___Uganda___1936`

- [PASS] surname_gate: bio 'KIRWAN' vs stint 'Kirwan, B. E. R' (exact)
- [PASS] initials: bio ['B', 'E', 'R'] ~ stint ['B', 'E', 'R']
- [PASS] age_gate: stint starts 1936, birth 1913 (age 23)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 51 vs bar 60: 'lab. asst., geol. survey' ~ 'Junior Laboratory Assistant'
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

