<!-- {"case_id": "case_weeks_f-b_b1919", "bio_ids": ["weeks_f-b_b1919"], "stint_ids": ["Weeks, F. B___Western Pacific___1964"]} -->
# Dossier case_weeks_f-b_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `weeks_f-b_b1919`

- Printed name: **WEEKS, F. B**
- Birth year: 1919 (attested in editions [1963])
- Terminal: retired 1963 — “retd., re-apptd. admin. offr., G. & E. Is. Col., 1963.”
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L26183.v` — printed in editions [1963]:**

> WEEKS, F. B.—b. 1919; ed. Cheltenham and New Coll., Oxford; mil. serv., 1939–46, capt.; cadet, Tang., 1946; dist. offr., 1948; prin. astt. sec., 1961. (Tang. Govt. service.)

**Version `col1964-L22948.v` — printed in editions [1964, 1965, 1966]:**

> WEEKS, F. B.—b. 1919; ed. Cheltenham and New Coll., Oxford; mil. serv., 1939-46, capt.; cadet, Tang., 1946; dist. offr., 1948; prin. asst. sec., 1961; retd., re-apptd. admin. offr., G. & E. Is. Col., 1963.

**Version `col1957-L28279.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962]:**

> WEEKS, F. B.—b. 1919; ed. Cheltenham and New Coll., Oxford; mil. serv., 1939-46, capt.; cadet, Tang., 1946; dist. offr., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | cadet | Tanganyika | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948 | dist. offr | Tanganyika *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1961 | prin. astt. sec | Tanganyika *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Weeks, F. B___Western Pacific___1964`

- Staff-list name: **Weeks, F. B** | colony: **Western Pacific** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | F. B. Weeks | Administrative Officer | Civil Establishment | — | — |
| 1965 | F. B. Weeks | Administrative Officer | Civil Establishment | — | — |
| 1966 | F. B. Weeks | Administrative Officer (Class B) | Civil Establishment | — | — |

### Deterministic checks: `weeks_f-b_b1919` vs `Weeks, F. B___Western Pacific___1964`

- [PASS] surname_gate: bio 'WEEKS' vs stint 'Weeks, F. B' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F', 'B']
- [PASS] age_gate: stint starts 1964, birth 1919 (age 45)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1966
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

