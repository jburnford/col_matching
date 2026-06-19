<!-- {"case_id": "case_struthers_ernest-andrew_b1901", "bio_ids": ["struthers_ernest-andrew_b1901"], "stint_ids": ["Struthers, E. A___Straits Settlements___1931"]} -->
# Dossier case_struthers_ernest-andrew_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `struthers_ernest-andrew_b1901`

- Printed name: **STRUTHERS, ERNEST ANDREW**
- Birth year: 1901 (attested in editions [1939, 1940])
- Honours: M.B
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70984.v` — printed in editions [1939, 1940]:**

> STRUTHERS, ERNEST ANDREW, M.B., Ch.B., D.P.H. (St. Andrew's), D.T.M. & H. (Eng.), Cert. L.S.T.M.—B. 1901; ed. Harris Acad., Univ. Coll., Dundee, St. Andrew's Univ., and Lond. Univ.; M.O., Malaya, Mar., 1926; ag. sr. health offr., Johore, June, 1936; sup. scale offr., gd. B., M.M.S., July, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | M.O. | Malaya | [1939, 1940] |
| 1 | 1936 | ag. sr. health offr. | Johore | [1939, 1940] |
| 2 | 1938 | sup. scale offr., gd. B., M.M.S | Johore *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Struthers, E. A___Straits Settlements___1931`

- Staff-list name: **Struthers, E. A** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | E. A. Struthers | Health Officer | Health Branch | — | — |
| 1933 | E. A. Struthers | Health Officer | Health Branch | — | — |

### Deterministic checks: `struthers_ernest-andrew_b1901` vs `Struthers, E. A___Straits Settlements___1931`

- [PASS] surname_gate: bio 'STRUTHERS' vs stint 'Struthers, E. A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1931, birth 1901 (age 30)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

