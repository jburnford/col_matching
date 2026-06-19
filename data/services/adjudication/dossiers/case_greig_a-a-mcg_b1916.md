<!-- {"case_id": "case_greig_a-a-mcg_b1916", "bio_ids": ["greig_a-a-mcg_b1916"], "stint_ids": ["Greig, A. A. M___Bahamas___1965"]} -->
# Dossier case_greig_a-a-mcg_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `greig_a-a-mcg_b1916`

- Printed name: **GREIG, A. A. McG**
- Birth year: 1916 (attested in editions [1959, 1961, 1963, 1964, 1965, 1966])
- Terminal: retired 1964 — “retd., re-apptd. dir. educ., Bah., 1964.”
- Appears in editions: [1959, 1961, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L23602.v` — printed in editions [1959, 1961, 1963, 1964, 1965, 1966]:**

> GREIG, A. A. McG.—b. 1916; ed. Tonbridge Sch., and Trinity Coll., Oxford; mil. serv., 1939-45; master, English Sch., Cyp., 1946-48; educ. offr., Ken., 1948; senr. educ. offr., Zanz., 1957; asst. dir. educ., 1957-64; retd., re-apptd. dir. educ., Bah., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946–1948 | master, English Sch. | Cyprus | [1959, 1961, 1963, 1964, 1965, 1966] |
| 1 | 1957 | senr. educ. offr. | Zanzibar | [1959, 1961, 1963, 1964, 1965, 1966] |

## Candidate stint `Greig, A. A. M___Bahamas___1965`

- Staff-list name: **Greig, A. A. M** | colony: **Bahamas** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | A. A. M. Greig | Director of Education | Civil Establishment | — | — |
| 1966 | A. A. M. Greig | Director of Education | Civil Establishment | — | — |

### Deterministic checks: `greig_a-a-mcg_b1916` vs `Greig, A. A. M___Bahamas___1965`

- [PASS] surname_gate: bio 'GREIG' vs stint 'Greig, A. A. M' (exact)
- [PASS] initials: bio ['A', 'A', 'M'] ~ stint ['A', 'A', 'M']
- [PASS] age_gate: stint starts 1965, birth 1916 (age 49)
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
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

