<!-- {"case_id": "case_fox_j_b1927", "bio_ids": ["fox_j_b1927"], "stint_ids": ["Fox, J. E___Nyasaland___1950"]} -->
# Dossier case_fox_j_b1927

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 43 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['fox_j_b1927'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Fox, J. E___Nyasaland___1950` is also gate-compatible with biography(ies) outside this case: ['fox_jocelyn-errol_b1907', 'fox_john_b1868'] (already linked elsewhere or filtered).

## Biography `fox_j_b1927`

- Printed name: **FOX, J**
- Birth year: 1927 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L14764.v` — printed in editions [1966]:**

> FOX, J.—b. 1927; ed. Cathays High Sch.; mil. serv., 1947-49; Br. P.O., 1943-49; techn., gr. II, E.A.P. & T. admin., 1949; gr. I, 1950; asst. engrnr., gr. II, 1955; gr. I (old style), 1959; gr. I (new style), 1960; retd., re-apptd., 1963; senr. asst. engrnr., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943–1949 | Br. P.O | — | [1966] |
| 1 | 1949 | techn., gr. II, E.A.P. & T. admin | East Africa Protectorate | [1966] |
| 2 | 1950 | gr. I | East Africa Protectorate *(inherited from previous clause)* | [1966] |
| 3 | 1955 | asst. engrnr., gr. II | East Africa Protectorate *(inherited from previous clause)* | [1966] |
| 4 | 1959 | gr. I (old style) | East Africa Protectorate *(inherited from previous clause)* | [1966] |
| 5 | 1960 | gr. I (new style) | East Africa Protectorate *(inherited from previous clause)* | [1966] |
| 6 | 1963 | retd., re-apptd | East Africa Protectorate *(inherited from previous clause)* | [1966] |
| 7 | 1964 | senr. asst. engrnr | East Africa Protectorate *(inherited from previous clause)* | [1966] |

## Candidate stint `Fox, J. E___Nyasaland___1950`

- Staff-list name: **Fox, J. E** | colony: **Nyasaland** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | J. E. Fox | Superintendent | PRISONS AND LUNATIC ASYLUM | — | — |
| 1951 | J. E. Fox | Superintendents of Prisons | PRISONS AND LUNATIC ASYLUM | — | — |

### Deterministic checks: `fox_j_b1927` vs `Fox, J. E___Nyasaland___1950`

- [PASS] surname_gate: bio 'FOX' vs stint 'Fox, J. E' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1950, birth 1927 (age 23)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

