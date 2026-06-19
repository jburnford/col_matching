<!-- {"case_id": "case_gosling_audley-blair-evelyn_e1891", "bio_ids": ["gosling_audley-blair-evelyn_e1891"], "stint_ids": ["Gosling, Alice E___Bermuda___1949"]} -->
# Dossier case_gosling_audley-blair-evelyn_e1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Gosling, Alice E___Bermuda___1949` is also gate-compatible with biography(ies) outside this case: ['gosling_alice-e_b1897'] (already linked elsewhere or filtered).

## Biography `gosling_audley-blair-evelyn_e1891`

- Printed name: **GOSLING, AUDLEY BLAIR EVELYN**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1896-L39124.v` — printed in editions [1896, 1897, 1899, 1900]:**

> GOSLING, AUDLEY BLAIR EVELYN.—Employed at Her Majesty's Legation in Central America, 1891-1895; acted as interpreter to Rear-Admiral Stephenson, C.B., Commander-in-Chief, Pacific Station, during occupation of Corinto, Nicaragua, Mar. and Apr., 1895; sub-inspr., B. Guiana police, Nov., 1895.

**Version `col1898-L33608.v` — printed in editions [1898]:**

> GOSLING, Audley Blair Evelyn.—Employed at H.M. Legation in Cent. America, 1891-1895; acted as interp. to Rear-Admiral Stephenson, C.B., comdr.-in-ch., Pacific station, during the occupation of Corinto, Nicaragua, Mar. and Apr., 1895; sub-inspr., Br. Guiana pol., Nov., 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891–1895 | Employed at Her Majesty's Legation in Central America | — | [1896, 1897, 1898, 1899, 1900] |
| 1 | 1895 | acted as interpreter to Rear-Admiral Stephenson, C.B., Commander-in-Chief, Pacific Station, during occupation of Corinto, Nicaragua, Mar. and | — | [1896, 1897, 1898, 1899, 1900] |
| 2 | 1895 | sub-inspr., B. Guiana police | — | [1896, 1897, 1899, 1900] |
| 3 | 1896 | sub-inspr., Br. Guiana pol | British Guiana | [1898] |

## Candidate stint `Gosling, Alice E___Bermuda___1949`

- Staff-list name: **Gosling, Alice E** | colony: **Bermuda** | listed 1949–1963 | editions [1949, 1950, 1951, 1952, 1953, 1954, 1955, 1957, 1959, 1960, 1961, 1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. E. Gosling | Librarian and Secretary to Trustees | Library | — | — |
| 1950 | A. E. Gosling | Librarian and Secretary to Trustees | LIBRARY | — | — |
| 1951 | A. E. Gosling | Librarian and Secretary to Trustees | LIBRARY | — | — |
| 1952 | A. E. Gosling | Librarian and Secretary to Trustees | Civil Establishment | — | — |
| 1953 | Alice E. Gosling | Librarian and Secretary to Trustees | Civil Establishment | — | — |
| 1954 | Alice E. Gosling | Librarian and Secretary to Trustees | Civil Establishment | — | — |
| 1955 | Alice E. Gosling | Librarian and Secretary to Trustees | Civil Establishment | — | — |
| 1957 | Alice E. Gosling | Librarian and Secretary to Trustees | Civil Establishment | — | — |
| 1959 | Alice E. Gosling | Librarian and Secretary to Trustees | Civil Establishment | — | — |
| 1960 | Alice E Gosling | Librarian and Secretary to Trustees | Civil Establishment | — | — |
| 1961 | Miss Alice E. Gosling | Librarian and Secretary to Trustees | Civil Establishment | — | — |
| 1962 | Alice E. Gosling | Librarian and Secretary to Trustees | Civil Establishment | — | — |
| 1963 | Miss Alice E. Gosling | Librarian and Secretary to Trustees | Civil Establishment | — | — |

### Deterministic checks: `gosling_audley-blair-evelyn_e1891` vs `Gosling, Alice E___Bermuda___1949`

- [PASS] surname_gate: bio 'GOSLING' vs stint 'Gosling, Alice E' (exact)
- [PASS] initials: bio ['A', 'B', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1963
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

