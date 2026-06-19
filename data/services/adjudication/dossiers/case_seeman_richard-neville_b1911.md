<!-- {"case_id": "case_seeman_richard-neville_b1911", "bio_ids": ["seeman_richard-neville_b1911"], "stint_ids": ["Seaman, R___Bermuda___1950"]} -->
# Dossier case_seeman_richard-neville_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `seeman_richard-neville_b1911`

- Printed name: **SEEMAN, Richard Neville**
- Birth year: 1911 (attested in editions [1956, 1957])
- Honours: O.B.E (1956)
- Appears in editions: [1948, 1949, 1950, 1951, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L24044.v` — printed in editions [1956, 1957]:**

> SEEMAN, R. N., O.B.E. (1956).—b. 1911; ed. Uppingham Sch. and Oxford Univ.; asst. audr., C.A.D., 1935; Tang., 1935; senr. asst. audr., Nig., 1946; prin. asst. audr., 1946; dep. dir., audit, E. regn., 1951; dir., 1954-57.

**Version `col1948-L35786.v` — printed in editions [1948, 1949, 1950, 1951]:**

> SEEMAN, Richard Neville.—b. 1911; ed. Uppingham and Corpus Christi Coll., Oxford, M.A. (Oxon.); war serv., 1942-44; asst. audr., T.T., 1935; senr. asst. audr., Nig., 1946; prin. asst. (later prin. audr.), 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | asst. audr., C.A.D | Tanganyika | [1948, 1949, 1950, 1951, 1956, 1957] |
| 1 | 1946 | senr. asst. audr. | Nigeria | [1948, 1949, 1950, 1951, 1956, 1957] |
| 2 | 1951 | dep. dir., audit, E. regn | Nigeria *(inherited from previous clause)* | [1956, 1957] |
| 3 | 1954–1957 | dir | Nigeria *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `Seaman, R___Bermuda___1950`

- Staff-list name: **Seaman, R** | colony: **Bermuda** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. Seaman | Aide-de-Camp | Governor and Personal Staff | — | Captain |
| 1951 | R. Seaman | Aide-de-Camp | Governor and Personal Staff | — | Captain |

### Deterministic checks: `seeman_richard-neville_b1911` vs `Seaman, R___Bermuda___1950`

- [PASS] surname_gate: bio 'SEEMAN' vs stint 'Seaman, R' (fuzzy:1)
- [PASS] initials: bio ['R', 'N'] ~ stint ['R']
- [PASS] age_gate: stint starts 1950, birth 1911 (age 39)
- [FAIL] colony: no placed event resolves to 'Bermuda'
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

