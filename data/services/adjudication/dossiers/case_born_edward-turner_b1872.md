<!-- {"case_id": "case_born_edward-turner_b1872", "bio_ids": ["born_edward-turner_b1872"], "stint_ids": ["Born, E. T___Falkland Islands___1906"]} -->
# Dossier case_born_edward-turner_b1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `born_edward-turner_b1872`

- Printed name: **BORN, EDWARD TURNER**
- Birth year: 1872 (attested in editions [1908, 1909])
- Appears in editions: [1905, 1906, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1908-L43295.v` — printed in editions [1908, 1909]:**

> BORN, EDWARD TURNER.—B. 1872; M.B., Dunelm; honours, 1st, 2nd and 3rd M.B.; prelim. sci. and regist. exams.; ast. col. surgeon, St. Lucia, 1901; ditto, Falklands, 1903; col. surgeon, pres. of bd. of health, pub. vaccinator, and J.P., Falklands, 1904; mem. exec. and legis. couns., 1904.

**Version `col1905-L42121.v` — printed in editions [1905, 1906]:**

> BORN, EDWARD TURNER, M.B.—Asst. col. surgeon, St. Lucia, 1901; ditto, Falkland Is., 1903; col. surg., Falklands, 1904.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | ast. col. surgeon | St. Lucia | [1905, 1906, 1908, 1909] |
| 1 | 1903 | ditto, Falklands | St. Lucia *(inherited from previous clause)* | [1905, 1906, 1908, 1909] |
| 2 | 1904 | col. surgeon, pres. of bd. of health, pub. vaccinator, and J.P., Falklands | St. Lucia *(inherited from previous clause)* | [1905, 1906, 1908, 1909] |

## Candidate stint `Born, E. T___Falkland Islands___1906`

- Staff-list name: **Born, E. T** | colony: **Falkland Islands** | listed 1906–1909 | editions [1906, 1907, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | E. T. Born | Colonial Surgeon, Public Vaccinator, and President Board of Health | Civil Establishment | — | — |
| 1907 | E. T. Born | Colonial Surgeon, Public Vaccinator, and President Board of Health | Civil Establishment | — | — |
| 1909 | E. T. Born | Colonial Surgeon, Public Vaccinator, and President Board of Health | Civil Establishment | — | — |

### Deterministic checks: `born_edward-turner_b1872` vs `Born, E. T___Falkland Islands___1906`

- [PASS] surname_gate: bio 'BORN' vs stint 'Born, E. T' (exact)
- [PASS] initials: bio ['E', 'T'] ~ stint ['E', 'T']
- [PASS] age_gate: stint starts 1906, birth 1872 (age 34)
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1909
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

