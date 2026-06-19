<!-- {"case_id": "case_millar_arthur-ronald_b1916", "bio_ids": ["millar_arthur-ronald_b1916"], "stint_ids": ["Millar, A. R___Gold Coast___1949"]} -->
# Dossier case_millar_arthur-ronald_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `millar_arthur-ronald_b1916`

- Printed name: **MILLAR, Arthur Ronald**
- Birth year: 1916 (attested in editions [1956, 1957, 1958])
- Honours: C.P.M (1950)
- Appears in editions: [1950, 1951, 1956, 1957, 1958]

### Verbatim printed entry text (OCR)

**Version `col1956-L23053.v` — printed in editions [1956, 1957, 1958]:**

> MILLAR, A. R.—b. 1916; ed. Govt. High Sch., Nassau, and R.M.C. of Canada; Met. Police Coll., Hendon; police cadet, G.C., 1938; asst. supt., 1941; supt., 1949; N. Borneo, 1951; senr. supt., 1955.

**Version `col1950-L38003.v` — printed in editions [1950, 1951]:**

> MILLAR, Arthur Ronald, C.P.M. (1950).—b. 1916; ed. R.M.C., Canada, and Hendon Police Coll.; asst. supt., police, G.C., 1937; senr. asst., 1947; supt., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | asst. supt., police | Gold Coast | [1950, 1951] |
| 1 | 1938 | police cadet | Gold Coast | [1956, 1957, 1958] |
| 2 | 1941 | asst. supt | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958] |
| 3 | 1947 | senr. asst | Gold Coast *(inherited from previous clause)* | [1950, 1951] |
| 4 | 1949 | supt | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1956, 1957, 1958] |
| 5 | 1951 | supt | North Borneo | [1956, 1957, 1958] |
| 6 | 1955 | senr. supt | North Borneo *(inherited from previous clause)* | [1956, 1957, 1958] |

## Candidate stint `Millar, A. R___Gold Coast___1949`

- Staff-list name: **Millar, A. R** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. R. Millar | Senior Assistant Superintendents and Assistant Superintendents | Police | — | — |
| 1951 | A. R. Millar | Superintendent of Police | Police | — | — |

### Deterministic checks: `millar_arthur-ronald_b1916` vs `Millar, A. R___Gold Coast___1949`

- [PASS] surname_gate: bio 'MILLAR' vs stint 'Millar, A. R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [PASS] colony: 5 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 40 vs bar 60: 'senr. asst' ~ 'Senior Assistant Superintendents and Assistant Superintendents'
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

