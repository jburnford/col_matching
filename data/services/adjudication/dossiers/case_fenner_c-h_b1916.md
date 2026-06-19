<!-- {"case_id": "case_fenner_c-h_b1916", "bio_ids": ["fenner_c-h_b1916"], "stint_ids": ["Renner, Charles___Hong Kong___1936"]} -->
# Dossier case_fenner_c-h_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fenner_c-h_b1916`

- Printed name: **FENNER, C. H**
- Birth year: 1916 (attested in editions [1956, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: C.M.G (1963), C.P.M (1950), K.B.E (1965), M.B.E (1946), Q.P.M (1957)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L21099.v` — printed in editions [1956, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> FENNER, Sir C. H., K.B.E. (1965), C.M.G. (1963), M.B.E. (1946), Q.P.M. (1957), C.P.M. (1950).—b. 1916; ed. Highgate Sch., Mddx.; mil. serv., 1942-44; prob. asst. comsnr., police, F.M.S., 1936; asst. supt., 1939; supt., 1950; asst. comsnr., 1953; senr. asst. comsnr., police, Fed. of Mal., 1954; dir., pol. affrs., 1962; insptr.-gen., 1963.

**Version `col1957-L22961.v` — printed in editions [1957]:**

> FENNERT, C. H., M.B.E. (1946), C.P.M. (1950).—b. 1916; ed. Highgate Sch., Mdxx.; mil. serv., 1942-44; prob. asst. comsrr., police, F.M.S., 1936; asst. supt., 1939; supt., 1950; asst. comsrr., 1953; senr. asst. comsrr., police, Fed. of Mal., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | prob. asst. comsnr., police | Federated Malay States | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1939 | asst. supt | Federated Malay States *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1950 | supt | Federated Malay States *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1953 | asst. comsnr | Federated Malay States *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1954 | senr. asst. comsnr., police, Fed. of Mal | Federated Malay States *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1962 | dir., pol. affrs | Federated Malay States *(inherited from previous clause)* | [1956, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1963 | insptr.-gen | Federated Malay States *(inherited from previous clause)* | [1956, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Renner, Charles___Hong Kong___1936`

- Staff-list name: **Renner, Charles** | colony: **Hong Kong** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | Charles Renner | Vice-Consul | Consuls | — | — |
| 1937 | Charles Renner | Vice-Consul | Consular Service | — | — |
| 1939 | C. Renner | Vice-Consul | Other Ranking Consular Officers | — | — |
| 1940 | Charles Renner | Vice-Consul | Other Ranking Consular Officers | — | — |

### Deterministic checks: `fenner_c-h_b1916` vs `Renner, Charles___Hong Kong___1936`

- [PASS] surname_gate: bio 'FENNER' vs stint 'Renner, Charles' (fuzzy:1)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C']
- [PASS] age_gate: stint starts 1936, birth 1916 (age 20)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

