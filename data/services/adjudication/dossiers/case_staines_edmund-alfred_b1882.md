<!-- {"case_id": "case_staines_edmund-alfred_b1882", "bio_ids": ["staines_edmund-alfred_b1882"], "stint_ids": ["Staines, Edgar___Malta___1919"]} -->
# Dossier case_staines_edmund-alfred_b1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `staines_edmund-alfred_b1882`

- Printed name: **STAINES, Edmund Alfred**
- Birth year: 1882 (attested in editions [1932, 1933, 1934, 1935, 1936, 1937])
- Appears in editions: [1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1932-L64145.v` — printed in editions [1932, 1933, 1934, 1935, 1936, 1937]:**

> STAINES, Capt. Edmund Alfred.—B. 1882; P. and T. dept., G. Britain, 1899; Br. sea post offr., U.K.-U.S.A., 1907; asst. supt., P. and T., F.M.S., Sept., 1911; mil. service, 1915-18; ag. acct., P. and T., F.M.S., 1921-1925; contrlr., P. and T., Perak and Dindings, June, 1927; ditto, Selangor and Pahang, June, 1928; do., Penang and P.W., May, 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | P. and T. dept., G. Britain | — | [1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1907 | Br. sea post offr., U.K.-U.S.A | — | [1932, 1933, 1934, 1935, 1936, 1937] |
| 2 | 1911 | asst. supt., P. and T. | Federated Malay States | [1932, 1933, 1934, 1935, 1936, 1937] |
| 3 | 1921–1925 | ag. acct., P. and T. | Federated Malay States | [1932, 1933, 1934, 1935, 1936, 1937] |
| 4 | 1927 | contrlr., P. and T., Perak and Dindings | Federated Malay States *(inherited from previous clause)* | [1932, 1933, 1934, 1935, 1936, 1937] |
| 5 | 1928 | ditto, Selangor and Pahang | Federated Malay States *(inherited from previous clause)* | [1932, 1933, 1934, 1935, 1936, 1937] |
| 6 | 1932 | do., Penang and P.W | Federated Malay States *(inherited from previous clause)* | [1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Staines, Edgar___Malta___1919`

- Staff-list name: **Staines, Edgar** | colony: **Malta** | listed 1919–1940 | editions [1919, 1920, 1921, 1922, 1923, 1924, 1925, 1929, 1930, 1931, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | E. Staines | Deputy Registrars | Judicial Establishment | — | — |
| 1920 | E. Staines | Deputy Registrar | Judicial Establishment | — | — |
| 1921 | Edgar Staines | Registrar and Secretary of the University | Public Instruction | — | — |
| 1922 | Edgar Staines | Registrar and Secretary of the University | Public Instruction | — | — |
| 1923 | E. Staines | Deputy Registrar | Judicial Establishment | — | — |
| 1924 | E. Staines | Deputy Registrar | Judicial Establishment | — | — |
| 1925 | E. Staines | Deputy Registrar | Judicial Establishment | — | — |
| 1929 | E. Staines | Deputy Registrar | Judicial Establishment | — | — |
| 1930 | E. Staines | Assistant Registrar | Judicial Establishment | — | — |
| 1931 | E. Staines | Assistant Registrar | Judicial Establishment | — | — |
| 1934 | E. Staines | Assistant Registrar | Judicial Establishment | — | — |
| 1936 | E. Staines | Registrar, Superior Courts | Judicial Establishment | — | — |
| 1937 | E. Staines | Registrar, Superior Courts | Judicial Establishment | — | — |
| 1939 | E. Staines | Registrar, Superior Courts | Judicial Establishment | — | — |
| 1940 | E. Staines | Registrar, Superior Courts | Judicial Establishment | — | — |

### Deterministic checks: `staines_edmund-alfred_b1882` vs `Staines, Edgar___Malta___1919`

- [PASS] surname_gate: bio 'STAINES' vs stint 'Staines, Edgar' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E']
- [PASS] age_gate: stint starts 1919, birth 1882 (age 37)
- [FAIL] colony: no placed event resolves to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1940
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

