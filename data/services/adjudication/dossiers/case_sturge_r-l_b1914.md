<!-- {"case_id": "case_sturge_r-l_b1914", "bio_ids": ["sturge_r-l_b1914"], "stint_ids": ["Sturge, R. L___Aden___1965"]} -->
# Dossier case_sturge_r-l_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sturge_r-l_b1914`

- Printed name: **STURGE, R. L**
- Birth year: 1914 (attested in editions [1957])
- Appears in editions: [1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L27606.v` — printed in editions [1957]:**

> STURGE, R. L., T.D.—b. 1914; ed. Trowbridge Boys' High Sch. and King Edward Sch., Bath; mil. serv., 1939-45, maj.; devel. offr., Nig., 1946; asst. regisr., co-op. socs., 1950; senr. asst., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | devel. offr. | Nigeria | [1957] |
| 1 | 1950 | asst. regisr., co-op. socs | Nigeria *(inherited from previous clause)* | [1957] |
| 2 | 1954 | senr. asst | Nigeria *(inherited from previous clause)* | [1957] |

## Candidate stint `Sturge, R. L___Aden___1965`

- Staff-list name: **Sturge, R. L** | colony: **Aden** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | R. L. Sturge | Commissioner for Co-operative Development & Marketing and Registrar of Co-operative Societies | Civil Establishment | — | — |
| 1966 | R. L. Sturge | Commissioner for Co-operative Development and Marketing | Civil Establishment | — | — |

### Deterministic checks: `sturge_r-l_b1914` vs `Sturge, R. L___Aden___1965`

- [PASS] surname_gate: bio 'STURGE' vs stint 'Sturge, R. L' (exact)
- [PASS] initials: bio ['R', 'L'] ~ stint ['R', 'L']
- [PASS] age_gate: stint starts 1965, birth 1914 (age 51)
- [FAIL] colony: no placed event resolves to 'Aden'
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

