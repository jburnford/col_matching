<!-- {"case_id": "case_westmorland_arthur-stewart_b1892", "bio_ids": ["westmorland_arthur-stewart_b1892"], "stint_ids": ["Westmorland, A. S___Jamaica___1937"]} -->
# Dossier case_westmorland_arthur-stewart_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `westmorland_arthur-stewart_b1892`

- Printed name: **WESTMORLAND, Arthur Stewart**
- Birth year: 1892 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L36777.v` — printed in editions [1948, 1949]:**

> WESTMORLAND, Arthur Stewart, O.B.E. (civ.), M.R.C.S. (Eng.), L.R.C.P. (Lond.), D.T.M. & H. (Eng.).—b. 1892; ed. Bedford Sch.; on mil. serv. 1918-20, capt.; med. offr., Jca., 1921; S.M.O., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | med. offr. | Jamaica | [1948, 1949] |
| 1 | 1927 | S.M.O | Jamaica *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Westmorland, A. S___Jamaica___1937`

- Staff-list name: **Westmorland, A. S** | colony: **Jamaica** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | A. S. Westmorland | Senior Medical Officer | Public Hospital, Kingston | — | — |
| 1940 | A. S. Westmorland | Senior Medical Officer | Public Hospital, Kingston | — | — |

### Deterministic checks: `westmorland_arthur-stewart_b1892` vs `Westmorland, A. S___Jamaica___1937`

- [PASS] surname_gate: bio 'WESTMORLAND' vs stint 'Westmorland, A. S' (exact)
- [PASS] initials: bio ['A', 'S'] ~ stint ['A', 'S']
- [PASS] age_gate: stint starts 1937, birth 1892 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 16 vs bar 60: 'S.M.O' ~ 'Senior Medical Officer'
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

