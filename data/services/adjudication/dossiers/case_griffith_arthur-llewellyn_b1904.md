<!-- {"case_id": "case_griffith_arthur-llewellyn_b1904", "bio_ids": ["griffith_arthur-llewellyn_b1904"], "stint_ids": ["Griffith, Llewelyn___Basutoland___1920"]} -->
# Dossier case_griffith_arthur-llewellyn_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 51 official(s) with this surname in the graph's staff lists; 26 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Griffith, Llewelyn___Basutoland___1920` is also gate-compatible with biography(ies) outside this case: ['griffith_lewellyn_b1872'] (already linked elsewhere or filtered).

## Biography `griffith_arthur-llewellyn_b1904`

- Printed name: **GRIFFITH, Arthur Llewellyn**
- Birth year: 1904 (attested in editions [1948, 1950, 1951])
- Honours: C.P.M (1954), Q.P.M (1958)
- Appears in editions: [1948, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1948-L33017.v` — printed in editions [1948, 1950, 1951]:**

> GRIFFITH, Arthur Llewellyn.—b. 1904; ed. St. Andrew's Coll., Grahamstown, S.A.; police const., Ken., 1930; asst. inspr., 1938; inspr., 1942; asst. supt., 1945; silvericulturist, E.A.H.C., 1950.

**Version `col1957-L23612.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962]:**

> GRIFFITH, A. L., Q.P.M. (1958), C.P.M. (1954).—b. 1904; ed. St. Andrew's Coll., Grahamstown, S.A.; European police constable, Ken., 1930; asst. supt., 1945; supt., 1951; senr., 1954; asst. comsnr., police, 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | police const. | Kenya | [1948, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1938 | asst. inspr | Kenya *(inherited from previous clause)* | [1948, 1950, 1951] |
| 2 | 1942 | inspr | Kenya *(inherited from previous clause)* | [1948, 1950, 1951] |
| 3 | 1945 | asst. supt | Kenya *(inherited from previous clause)* | [1948, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962] |
| 4 | 1950 | silvericulturist, E.A.H.C | Kenya *(inherited from previous clause)* | [1948, 1950, 1951] |
| 5 | 1951 | supt | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |
| 6 | 1954 | senr | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |
| 7 | 1955 | asst. comsnr., police | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Griffith, Llewelyn___Basutoland___1920`

- Staff-list name: **Griffith, Llewelyn** | colony: **Basutoland** | listed 1920–1924 | editions [1920, 1921, 1922, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Llewelyn Griffith | Assistant Commissioner | Establishment | — | — |
| 1921 | Llewelyn Griffith | Assistant Commissioner | Establishment | — | — |
| 1922 | Llewelyn Griffith | Assistant Commissioner, Berea District | Establishment | — | — |
| 1924 | Llewelyn Griffith | Assistant Commissioner | District Administration | — | — |

### Deterministic checks: `griffith_arthur-llewellyn_b1904` vs `Griffith, Llewelyn___Basutoland___1920`

- [PASS] surname_gate: bio 'GRIFFITH' vs stint 'Griffith, Llewelyn' (exact)
- [PASS] initials: bio ['A', 'L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1920, birth 1904 (age 16)
- [FAIL] colony: no placed event resolves to 'Basutoland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1924
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

