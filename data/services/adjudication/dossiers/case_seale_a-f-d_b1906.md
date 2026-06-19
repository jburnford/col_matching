<!-- {"case_id": "case_seale_a-f-d_b1906", "bio_ids": ["seale_a-f-d_b1906"], "stint_ids": ["Seale, A. F. D___Gold Coast___1949"]} -->
# Dossier case_seale_a-f-d_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `seale_a-f-d_b1906`

- Printed name: **SEALE, A. F. D**
- Birth year: 1906 (attested in editions [1956, 1957, 1958, 1959])
- Honours: O.B.E (1958)
- Appears in editions: [1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1956-L24028.v` — printed in editions [1956, 1957, 1958, 1959]:**

> SEALE, A. F. D., O.B.E. (1958).—b. 1906; ed. Allhallows, Honiton; archt., P.W.D., G.C., 1944; chief archt., 1946; asst. D.P.W., 1956-58 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | archt., P.W.D. | Gold Coast | [1956, 1957, 1958, 1959] |
| 1 | 1946 | chief archt | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 2 | 1956–1958 | asst. D.P.W | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |

## Candidate stint `Seale, A. F. D___Gold Coast___1949`

- Staff-list name: **Seale, A. F. D** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. F. D. Seale | Chief Architect | Public Works | — | — |
| 1951 | A. F. D. Seale | Chief Architect | Architectural and Drawing Office Staff | — | — |

### Deterministic checks: `seale_a-f-d_b1906` vs `Seale, A. F. D___Gold Coast___1949`

- [PASS] surname_gate: bio 'SEALE' vs stint 'Seale, A. F. D' (exact)
- [PASS] initials: bio ['A', 'F', 'D'] ~ stint ['A', 'F', 'D']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 85 vs bar 60: 'chief archt' ~ 'Chief Architect'
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

