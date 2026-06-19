<!-- {"case_id": "case_anson_charles-john_b1904", "bio_ids": ["anson_charles-john_b1904"], "stint_ids": ["Anson, C. J___Nyasaland___1939"]} -->
# Dossier case_anson_charles-john_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `anson_charles-john_b1904`

- Printed name: **ANSON, Charles John**
- Birth year: 1904 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L30820.v` — printed in editions [1948, 1949, 1950, 1951]:**

> ANSON, Charles John.—b. 1904; Suez Canal police, 1929; police, Nyasa., 1938; inspr., 1940; asst. supt., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | Suez Canal police | — | [1948, 1949, 1950, 1951] |
| 1 | 1938 | police | Nyasaland | [1948, 1949, 1950, 1951] |
| 2 | 1940 | inspr | Nyasaland *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1946 | asst. supt | Nyasaland *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Anson, C. J___Nyasaland___1939`

- Staff-list name: **Anson, C. J** | colony: **Nyasaland** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | C. J. Anson | Assistants Inspectors | Police, Prisons and Lunatic Asylum | — | — |
| 1940 | C. J. Anson | Inspector | Police, Prisons and Lunatic Asylum | — | — |

### Deterministic checks: `anson_charles-john_b1904` vs `Anson, C. J___Nyasaland___1939`

- [PASS] surname_gate: bio 'ANSON' vs stint 'Anson, C. J' (exact)
- [PASS] initials: bio ['C', 'J'] ~ stint ['C', 'J']
- [PASS] age_gate: stint starts 1939, birth 1904 (age 35)
- [PASS] colony: 3 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1939-1940
- [PASS] position_sim: best 71 vs bar 60: 'inspr' ~ 'Inspector'
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

