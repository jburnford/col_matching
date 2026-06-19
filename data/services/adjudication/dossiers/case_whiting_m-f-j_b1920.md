<!-- {"case_id": "case_whiting_m-f-j_b1920", "bio_ids": ["whiting_m-f-j_b1920"], "stint_ids": ["Whiting, M. F. J___Nyasaland___1950"]} -->
# Dossier case_whiting_m-f-j_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `whiting_m-f-j_b1920`

- Printed name: **WHITING, M. F. J**
- Birth year: 1920 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L28102.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> WHITING, M. F. J.—b. 1920; ed. Boys' Sch., Anse Royale, Seychelles, and St. Louis Coll.; clk., Nyasa., 1947; asst. collr., customs, 1949; supt., customs, Sarawak, 1955–64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | clk. | Nyasaland | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1949 | asst. collr., customs | Nyasaland *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1955–1964 | supt., customs | Sarawak | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Whiting, M. F. J___Nyasaland___1950`

- Staff-list name: **Whiting, M. F. J** | colony: **Nyasaland** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | M. F. J. Whiting | Collector of Customs | CUSTOMS | — | — |
| 1951 | M. F. J. Whiting | Collector of Customs / Assistant Collector | CUSTOMS | — | — |

### Deterministic checks: `whiting_m-f-j_b1920` vs `Whiting, M. F. J___Nyasaland___1950`

- [PASS] surname_gate: bio 'WHITING' vs stint 'Whiting, M. F. J' (exact)
- [PASS] initials: bio ['M', 'F', 'J'] ~ stint ['M', 'F', 'J']
- [PASS] age_gate: stint starts 1950, birth 1920 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1950-1951
- [PASS] position_sim: best 75 vs bar 60: 'asst. collr., customs' ~ 'Collector of Customs / Assistant Collector'
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

