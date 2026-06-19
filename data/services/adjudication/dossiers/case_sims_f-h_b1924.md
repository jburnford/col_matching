<!-- {"case_id": "case_sims_f-h_b1924", "bio_ids": ["sims_f-h_b1924"], "stint_ids": ["Sims, F. H___Western Pacific___1956"]} -->
# Dossier case_sims_f-h_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sims_f-h_b1924`

- Printed name: **SIMS, F. H**
- Birth year: 1924 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: M.B.E
- Terminal: retired 1964 — “retd., re-apptd. audr.-gen., E.A.C.S.O., 1964.”
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L27896.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> SIMS, F. H., M.B.E.—b. 1924; ed. Queen Elizabeth's Gram. Sch., Wimborne, and British Coll. of Accountancy; mil. serv., 1943–47, capt.; cadet, coll. audit serv., G.C., 1947; auditor, O.A.D., 1950; senr. auditor, Nig., 1953; B.S.I.P., 1955; prin. auditor, 1957; Uga., 1960; dep. audr.-gen., redesign. dep. contrlr. and audr.-gen., 1962–64; retd., re-apptd. audr.-gen., E.A.C.S.O., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | cadet, coll. audit serv. | Gold Coast | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1950 | auditor, O.A.D | Gold Coast *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1953 | senr. auditor | Nigeria | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1955 | B.S.I.P | Nigeria *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1957 | prin. auditor | Nigeria *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1960 | prin. auditor | Uganda | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1962–1964 | dep. audr.-gen., redesign. dep. contrlr. and audr.-gen | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Sims, F. H___Western Pacific___1956`

- Staff-list name: **Sims, F. H** | colony: **Western Pacific** | listed 1956–1959 | editions [1956, 1957, 1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | F. H. Sims | Protectorate Auditor | Civil Establishment | — | — |
| 1957 | F. H. Sims | Senior Auditor | Civil Establishment | — | — |
| 1958 | F. H. Sims | Principal Auditor | Civil Establishment | — | — |
| 1959 | F. H. Sims | Principal Auditor | Civil Establishment | — | — |

### Deterministic checks: `sims_f-h_b1924` vs `Sims, F. H___Western Pacific___1956`

- [PASS] surname_gate: bio 'SIMS' vs stint 'Sims, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1956, birth 1924 (age 32)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1959
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

