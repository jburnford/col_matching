<!-- {"case_id": "case_coleiro_c_b1908", "bio_ids": ["coleiro_c_b1908"], "stint_ids": ["Coleiro, C___Malta___1956"]} -->
# Dossier case_coleiro_c_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['coleiro_c_b1908'] carry a single initial only — the namesake trap applies.

## Biography `coleiro_c_b1908`

- Printed name: **COLEIRO, C**
- Birth year: 1908 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1964])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L20475.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1964]:**

> COLEIRO, C.—b. 1908; ed. Lyceum and Royal Univ. of Malta; asst. port M.O., Malta, 1939; port M.O., 1948; S.M.O., 1948; C.G.M.O., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | asst. port M.O. | Malta | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1964] |
| 1 | 1948 | port M.O | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1964] |
| 2 | 1961 | C.G.M.O | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1964] |

## Candidate stint `Coleiro, C___Malta___1956`

- Staff-list name: **Coleiro, C** | colony: **Malta** | listed 1956–1964 | editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | C. Coleiro | Senior Medical Officer | The Maltese Government | — | — |
| 1957 | C. Coleiro | Senior Medical Officer | The Maltese Government | — | — |
| 1958 | C. Coleiro | Senior Medical Officer | The Maltese Government | — | — |
| 1959 | C. Coleiro | Senior Medical Officer | The Maltese Government | — | — |
| 1960 | C. Coleiro | Senior Medical Officer | Judiciary | — | — |
| 1961 | C. Coleiro | Senior Medical Officer | Civil Establishment | — | — |
| 1962 | C. Coleiro | Chief Government Medical Officer | Civil Establishment | — | — |
| 1963 | C. Coleiro | Chief Government Medical Officer | Civil Establishment | — | — |
| 1964 | C. Coleiro | Chief Government Medical Officer | Law Officers | — | — |

### Deterministic checks: `coleiro_c_b1908` vs `Coleiro, C___Malta___1956`

- [PASS] surname_gate: bio 'COLEIRO' vs stint 'Coleiro, C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1956, birth 1908 (age 48)
- [PASS] colony: 3 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1956-1964
- [FAIL] position_sim: best 34 vs bar 60: 'port M.O' ~ 'Senior Medical Officer'
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

