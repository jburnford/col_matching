<!-- {"case_id": "case_fletcher_denzil-cornwall_b1903", "bio_ids": ["fletcher_denzil-cornwall_b1903"], "stint_ids": ["Fletcher, D. C___Nyasaland___1951"]} -->
# Dossier case_fletcher_denzil-cornwall_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fletcher_denzil-cornwall_b1903`

- Printed name: **FLETCHER, Denzil Cornwall**
- Birth year: 1903 (attested in editions [1949])
- Appears in editions: [1949]

### Verbatim printed entry text (OCR)

**Version `col1949-L32048.v` — printed in editions [1949]:**

> FLETCHER, Denzil Cornwall, B.Sc.—b. 1903; ed. Sheffield Univ.; cadet, Nig., 1925; admin. offr., cl. I, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | cadet | Nigeria | [1949] |
| 1 | 1946 | admin. offr., cl. I | Nigeria *(inherited from previous clause)* | [1949] |

## Candidate stint `Fletcher, D. C___Nyasaland___1951`

- Staff-list name: **Fletcher, D. C** | colony: **Nyasaland** | listed 1951–1952 | editions [1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | D. C. Fletcher | Lands Adviser | Secretariat | — | — |
| 1952 | D. C. Fletcher | Lands Adviser | Civil Establishment | — | — |

### Deterministic checks: `fletcher_denzil-cornwall_b1903` vs `Fletcher, D. C___Nyasaland___1951`

- [PASS] surname_gate: bio 'FLETCHER' vs stint 'Fletcher, D. C' (exact)
- [PASS] initials: bio ['D', 'C'] ~ stint ['D', 'C']
- [PASS] age_gate: stint starts 1951, birth 1903 (age 48)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1952
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

