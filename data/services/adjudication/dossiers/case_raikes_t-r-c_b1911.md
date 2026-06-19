<!-- {"case_id": "case_raikes_t-r-c_b1911", "bio_ids": ["raikes_t-r-c_b1911"], "stint_ids": ["Raikes, T. R. C___Sierra Leone___1953"]} -->
# Dossier case_raikes_t-r-c_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `raikes_t-r-c_b1911`

- Printed name: **RAIKES, T. R. C**
- Birth year: 1911 (attested in editions [1953, 1954, 1955, 1956, 1957, 1959, 1960, 1961, 1962])
- Honours: O.B.E (1960)
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1953-L18811.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1959, 1960, 1961, 1962]:**

> RAIKES, T. R. C., O.B.E. (1960).—b. 1911; ed. Central and Secondary Schs., Port Talbot, S. Wales; Br. P.O., 1928; survr., Nig., 1944; div. survr., 1949; asst. P.M.G., S.L., 1952; P.M.G., 1952-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | Br. P.O | — | [1953, 1954, 1955, 1956, 1957, 1959, 1960, 1961, 1962] |
| 1 | 1944 | survr. | Nigeria | [1953, 1954, 1955, 1956, 1957, 1959, 1960, 1961, 1962] |
| 2 | 1949 | div. survr | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1959, 1960, 1961, 1962] |
| 3 | 1952 | asst. P.M.G. | Sierra Leone | [1953, 1954, 1955, 1956, 1957, 1959, 1960, 1961, 1962] |

## Candidate stint `Raikes, T. R. C___Sierra Leone___1953`

- Staff-list name: **Raikes, T. R. C** | colony: **Sierra Leone** | listed 1953–1960 | editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | T. R. C. Raikes | Postmaster-General | Civil Establishment | — | — |
| 1954 | T. R. C. Raikes | Postmaster-General | Civil Establishment | — | — |
| 1955 | T. R. C. Raikes | Postmaster-General | Civil Establishment | — | — |
| 1956 | T. R. C. Raikes | Postmaster-General | Civil Establishment | — | — |
| 1957 | T. R. C. Raikes | Postmaster-General | Civil Establishment | — | — |
| 1958 | T. R. C. Raikes | Postmaster-General | Civil Establishment | — | — |
| 1959 | T. R. C. Raikes | Postmaster-General | Civil Establishment | — | — |
| 1960 | T. R. C. Raikes | Postmaster-General | Civil Establishment | — | — |

### Deterministic checks: `raikes_t-r-c_b1911` vs `Raikes, T. R. C___Sierra Leone___1953`

- [PASS] surname_gate: bio 'RAIKES' vs stint 'Raikes, T. R. C' (exact)
- [PASS] initials: bio ['T', 'R', 'C'] ~ stint ['T', 'R', 'C']
- [PASS] age_gate: stint starts 1953, birth 1911 (age 42)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1953-1960
- [FAIL] position_sim: best 32 vs bar 60: 'asst. P.M.G.' ~ 'Postmaster-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

