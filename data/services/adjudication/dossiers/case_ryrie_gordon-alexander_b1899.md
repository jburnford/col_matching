<!-- {"case_id": "case_ryrie_gordon-alexander_b1899", "bio_ids": ["ryrie_gordon-alexander_b1899"], "stint_ids": ["Ryrie, G. A___Straits Settlements___1931"]} -->
# Dossier case_ryrie_gordon-alexander_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ryrie_gordon-alexander_b1899`

- Printed name: **RYRIE, GORDON ALEXANDER**
- Birth year: 1899 (attested in editions [1939])
- Honours: M.A, M.B
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L70369.v` — printed in editions [1939]:**

> RYRIE, GORDON ALEXANDER, M.A., M.B., Ch.B. (Edin.).—B. 1899; ed. Montrose Acad. and Edin. Univ.; M.O., Malaya, Mar., 1928; med. supt., Sungei Buloh leper & decrepit stltm., Dec., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | M.O. | Malaya | [1939] |
| 1 | 1930 | med. supt., Sungei Buloh leper & decrepit stltm | Malaya *(inherited from previous clause)* | [1939] |

## Candidate stint `Ryrie, G. A___Straits Settlements___1931`

- Staff-list name: **Ryrie, G. A** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | G. A. Ryrie | Medical Officer | Medical | — | — |
| 1932 | G. A. Ryrie | Medical Officer | Medical | — | — |
| 1933 | G. A. Ryrie | Medical Officer | Medical | — | — |

### Deterministic checks: `ryrie_gordon-alexander_b1899` vs `Ryrie, G. A___Straits Settlements___1931`

- [PASS] surname_gate: bio 'RYRIE' vs stint 'Ryrie, G. A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1931, birth 1899 (age 32)
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

