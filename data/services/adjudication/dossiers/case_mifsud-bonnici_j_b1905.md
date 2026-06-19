<!-- {"case_id": "case_mifsud-bonnici_j_b1905", "bio_ids": ["mifsud-bonnici_j_b1905"], "stint_ids": ["Mifsud Bonnici, J___Malta___1937"]} -->
# Dossier case_mifsud-bonnici_j_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mifsud-bonnici_j_b1905'] carry a single initial only — the namesake trap applies.

## Biography `mifsud-bonnici_j_b1905`

- Printed name: **MIFSUD BONNICI, J**
- Birth year: 1905 (attested in editions [1956, 1957, 1958, 1959, 1960, 1962, 1963, 1964])
- Honours: M.B.E (1951)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L23049.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1962, 1963, 1964]:**

> MIFSUD BONNICI, J., M.B.E. (1951)—b. 1905; ed. St. Aloysius Coll. and Royal Univ. of Malta; civ. serv. (admin.), Malta, 1927; acc’tant, 1944; asst. treas., 1947; senr. asst. treas., 1951; comsnr., inland rev., 1958.

**Version `col1961-L25297.v` — printed in editions [1961]:**

> MIFISUD BONNICI, J., M.B.E. (1951)—b. 1905; ed. St. Aloysius Coll. and Royal Univ. of Malta; civ. serv. (admin.), Malta, 1927; acctnt., 1944; asst. treas., 1947; senr. asst. treas., 1951; comsnr., inland rev., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | civ. serv. (admin.) | Malta | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1944 | acc’tant | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1947 | asst. treas | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1951 | senr. asst. treas | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1958 | comsnr., inland rev | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Mifsud Bonnici, J___Malta___1937`

- Staff-list name: **Mifsud Bonnici, J** | colony: **Malta** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | J. Mifsud Bonnici | Clerks, 2nd Class | Savings Bank | — | — |
| 1939 | J. Mifsud Bonnici | Clerks, 2nd Class | Savings Bank | — | — |
| 1940 | J. Mifsud Bonnici | Clerk, 2nd Class | Treasury | — | — |

### Deterministic checks: `mifsud-bonnici_j_b1905` vs `Mifsud Bonnici, J___Malta___1937`

- [PASS] surname_gate: bio 'MIFSUD BONNICI' vs stint 'Mifsud Bonnici, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1937, birth 1905 (age 32)
- [PASS] colony: 5 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 41 vs bar 60: 'civ. serv. (admin.)' ~ 'Clerk, 2nd Class'
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

