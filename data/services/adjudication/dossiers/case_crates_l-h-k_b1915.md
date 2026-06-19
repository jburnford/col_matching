<!-- {"case_id": "case_crates_l-h-k_b1915", "bio_ids": ["crates_l-h-k_b1915"], "stint_ids": ["Crates, L. H. K___Uganda___1949"]} -->
# Dossier case_crates_l-h-k_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `crates_l-h-k_b1915`

- Printed name: **CRATES, L. H. K**
- Birth year: 1915 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1957-L22252.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962]:**

> CRATES, L. H. K.—b. 1915; mil. serv., 1939-44, W.O. II; asst. supt., prisons, Uga., 1944; senr. asst. supt., 1950; supt., 1955; senr. supt., prisons, 1958-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | asst. supt., prisons | Uganda | [1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1950 | senr. asst. supt | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1955 | supt | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1958–1961 | senr. supt., prisons | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Crates, L. H. K___Uganda___1949`

- Staff-list name: **Crates, L. H. K** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. H. K. Crates | Assistant Superintendents | Prisons | — | — |
| 1951 | L. H. K. Crates | Assistant Superintendents | Prisons | — | — |

### Deterministic checks: `crates_l-h-k_b1915` vs `Crates, L. H. K___Uganda___1949`

- [PASS] surname_gate: bio 'CRATES' vs stint 'Crates, L. H. K' (exact)
- [PASS] initials: bio ['L', 'H', 'K'] ~ stint ['L', 'H', 'K']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [PASS] colony: 4 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 52 vs bar 60: 'asst. supt., prisons' ~ 'Assistant Superintendents'
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

