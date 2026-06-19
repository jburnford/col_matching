<!-- {"case_id": "case_smeeton_l-a_b1918", "bio_ids": ["smeeton_l-a_b1918"], "stint_ids": ["Smeeton, L. A___Nyasaland___1950"]} -->
# Dossier case_smeeton_l-a_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `smeeton_l-a_b1918`

- Printed name: **SMEETON, L. A**
- Birth year: 1918 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1959-L27996.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> SMEETON, L. A.—b. 1918; ed. Fairlight Prep. Sch. and Southsea Progressive Sch.; clk., Nyasa., 1948; asst. collr., customs, 1949; collr., 1953; supt., customs, Sarawak, 1954; senr. supt., 1962-64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | clk. | Nyasaland | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1949 | asst. collr., customs | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1953 | collr | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1954 | supt., customs | Sarawak | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1962–1964 | senr. supt | Sarawak *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Smeeton, L. A___Nyasaland___1950`

- Staff-list name: **Smeeton, L. A** | colony: **Nyasaland** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | L. A. Smeeton | Collector of Customs | CUSTOMS | — | — |
| 1951 | L. A. Smeeton | Collector of Customs / Assistant Collector | CUSTOMS | — | — |

### Deterministic checks: `smeeton_l-a_b1918` vs `Smeeton, L. A___Nyasaland___1950`

- [PASS] surname_gate: bio 'SMEETON' vs stint 'Smeeton, L. A' (exact)
- [PASS] initials: bio ['L', 'A'] ~ stint ['L', 'A']
- [PASS] age_gate: stint starts 1950, birth 1918 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Nyasaland'
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

