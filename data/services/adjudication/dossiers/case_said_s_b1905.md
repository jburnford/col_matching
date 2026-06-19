<!-- {"case_id": "case_said_s_b1905", "bio_ids": ["said_s_b1905"], "stint_ids": ["Said, Saba___Palestine___1923"]} -->
# Dossier case_said_s_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['said_s_b1905'] carry a single initial only — the namesake trap applies.

## Biography `said_s_b1905`

- Printed name: **SAID, S**
- Birth year: 1905 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1959-L27547.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964]:**

> SAID, S.—b. 1905; ed. Lyceum, Malta; apptd., Malta, 1929; offr., landing and warehousing bch., 1935; senr. asst. rationing offr., 1948; rationing and essential supplies offr., 1955; chief exec. offr., 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | apptd. | Malta | [1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1935 | offr., landing and warehousing bch | Malta *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1948 | senr. asst. rationing offr | Malta *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1955 | rationing and essential supplies offr | Malta *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1956 | chief exec. offr | Malta *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Said, Saba___Palestine___1923`

- Staff-list name: **Said, Saba** | colony: **Palestine** | listed 1923–1932 | editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | Saba Said | Public Prosecutors | Legal | — | — |
| 1924 | Saba Said | Public Prosecutors | Legal | — | — |
| 1925 | Saba Said | Public Prosecutors | Attorney General's Department | — | — |
| 1927 | Saba Said | Assistant Judicial Inspector | Supreme Court | — | — |
| 1928 | Saba Said | Magistrate | Magistrates | — | — |
| 1929 | Saba Said | Magistrate | Magistrates | — | — |
| 1930 | Saba Said | Magistrate | Magistrates | — | — |
| 1931 | Saba Said | Magistrates | Magistrates | — | — |
| 1932 | Saba Said | Magistrate | District Courts | — | — |

### Deterministic checks: `said_s_b1905` vs `Said, Saba___Palestine___1923`

- [PASS] surname_gate: bio 'SAID' vs stint 'Said, Saba' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1923, birth 1905 (age 18)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1932
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

