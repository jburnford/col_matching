<!-- {"case_id": "case_rowley_l_b1912", "bio_ids": ["rowley_l_b1912"], "stint_ids": ["Rowley, L___Grenada___1963"]} -->
# Dossier case_rowley_l_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['rowley_l_b1912'] carry a single initial only — the namesake trap applies.

## Biography `rowley_l_b1912`

- Printed name: **ROWLEY, L**
- Birth year: 1912 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L26879.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> ROWLEY, Miss L.—b. 1912; ed. St. Joseph's Convent, Grenada; apptd. treasy. dept., Grenada, 1930; admin. asst., govt. office, 1954; prin. asst. sec., min. of comms. and works, 1956; perm. sec., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | apptd. treasy. dept. | Grenada | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1954 | admin. asst., govt. office | Grenada *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1956 | prin. asst. sec., min. of comms. and works | Grenada *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1963 | perm. sec | Grenada *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Rowley, L___Grenada___1963`

- Staff-list name: **Rowley, L** | colony: **Grenada** | listed 1963–1965 | editions [1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | Miss L. Rowley | Ministry of Social Services | Civil Establishment | — | — |
| 1964 | Miss L. Rowley | Ministry of Social Services | Civil Establishment | — | — |
| 1965 | Miss L. Rowley | Ministry of Social Services | Civil Establishment | — | — |

### Deterministic checks: `rowley_l_b1912` vs `Rowley, L___Grenada___1963`

- [PASS] surname_gate: bio 'ROWLEY' vs stint 'Rowley, L' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1963, birth 1912 (age 51)
- [PASS] colony: 4 placed event(s) resolve to 'Grenada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1963-1965
- [FAIL] position_sim: best 41 vs bar 60: 'prin. asst. sec., min. of comms. and works' ~ 'Ministry of Social Services'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

