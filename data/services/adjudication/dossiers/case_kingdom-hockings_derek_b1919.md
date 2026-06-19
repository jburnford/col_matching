<!-- {"case_id": "case_kingdom-hockings_derek_b1919", "bio_ids": ["kingdom-hockings_derek_b1919"], "stint_ids": ["Kingdom-Hockings, D___Tanganyika___1940"]} -->
# Dossier case_kingdom-hockings_derek_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['kingdom-hockings_derek_b1919'] carry a single initial only — the namesake trap applies.

## Biography `kingdom-hockings_derek_b1919`

- Printed name: **KINGDOM-HOCKINGS, Derek**
- Birth year: 1919 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L22319.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> KINGDOM-HOCKINGS, D.—b. 1919; ed. Hoe Gram. Sch., King Edward VI Sch. and St. Catharine's Coll., Camb.; supt., educ., Tang., 1937; educ. offr., 1940; senr., 1958. (Tanzania Govt. service.)

**Version `col1950-L37018.v` — printed in editions [1950, 1951]:**

> KINGDOM-HOCKINGS, Derek.—b. 1919; ed. Hoe Gram. Sch., King Edward VI Sch., and St. Catharine's Coll., Camb., M.A. (Cantab.); supt., educ., T.T., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | supt., educ. | Tanganyika | [1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1958 | senr | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Kingdom-Hockings, D___Tanganyika___1940`

- Staff-list name: **Kingdom-Hockings, D** | colony: **Tanganyika** | listed 1940–1949 | editions [1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | D. Kingdom-Hockings | Superintendent of Education | Education | — | — |
| 1949 | D. Kingdom-Hockings | Education Officer | Education | — | — |

### Deterministic checks: `kingdom-hockings_derek_b1919` vs `Kingdom-Hockings, D___Tanganyika___1940`

- [PASS] surname_gate: bio 'KINGDOM-HOCKINGS' vs stint 'Kingdom-Hockings, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1940, birth 1919 (age 21)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1940-1949
- [FAIL] position_sim: best 50 vs bar 60: 'supt., educ.' ~ 'Superintendent of Education'
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

