<!-- {"case_id": "case_bonnici-enriquez_r_b1900", "bio_ids": ["bonnici-enriquez_r_b1900"], "stint_ids": ["Bonnici Enriquez, R.G___Malta___1931"]} -->
# Dossier case_bonnici-enriquez_r_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bonnici-enriquez_r_b1900'] carry a single initial only — the namesake trap applies.

## Biography `bonnici-enriquez_r_b1900`

- Printed name: **BONNICI ENRIQUEZ, R**
- Birth year: 1900 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L19897.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> BONNICI ENRIQUEZ, R.—b. 1900; ed. Lyceum, Malta; 2nd cl. customs asst., 1919; civ. serv. (admin.), Malta, 1922; asst. manager, milk marketing undertaking, 1943; asst. manager, savings bank, 1958; asst. manager, milk marketing undertaking, 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | 2nd cl. customs asst | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1922 | civ. serv. (admin.) | Malta | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1943 | asst. manager, milk marketing undertaking | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1958 | asst. manager, savings bank | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1959 | asst. manager, milk marketing undertaking | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Bonnici Enriquez, R.G___Malta___1931`

- Staff-list name: **Bonnici Enriquez, R.G** | colony: **Malta** | listed 1931–1934 | editions [1931, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | R.G. Bonnici Enriquez | Clerks, 2nd Class | Treasury | — | — |
| 1934 | R. G. Bonnici Enriquez | Clerks, 2nd Class | Treasury | — | — |

### Deterministic checks: `bonnici-enriquez_r_b1900` vs `Bonnici Enriquez, R.G___Malta___1931`

- [PASS] surname_gate: bio 'BONNICI ENRIQUEZ' vs stint 'Bonnici Enriquez, R.G' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R', 'G']
- [PASS] age_gate: stint starts 1931, birth 1900 (age 31)
- [PASS] colony: 4 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1934
- [FAIL] position_sim: best 40 vs bar 60: 'civ. serv. (admin.)' ~ 'Clerks, 2nd Class'
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

