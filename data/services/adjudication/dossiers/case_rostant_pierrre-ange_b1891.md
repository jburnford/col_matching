<!-- {"case_id": "case_rostant_pierrre-ange_b1891", "bio_ids": ["rostant_pierrre-ange_b1891"], "stint_ids": ["Rostant, P. A___Trinidad and Tobago___1927"]} -->
# Dossier case_rostant_pierrre-ange_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rostant_pierrre-ange_b1891`

- Printed name: **ROSTANT, PIERRRE ANGE**
- Birth year: 1891 (attested in editions [1937, 1939, 1940])
- Honours: M.B
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L64377.v` — printed in editions [1937, 1939, 1940]:**

> ROSTANT, PIERRRE ANGE, M.B., Ch.B. (Edin.).—B. 1891; govt. med. offr., Trinidad, Dec., 1919; asst. resp. surgn., col. hosp., San Fernando, Mar., 1928; sen. med. offr. (surg.), col. hosp., San Fernando, 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | govt. med. offr. | Trinidad | [1937, 1939, 1940] |
| 1 | 1928 | asst. resp. surgn., col. hosp., San Fernando | Trinidad *(inherited from previous clause)* | [1937, 1939, 1940] |
| 2 | 1936 | sen. med. offr. (surg.), col. hosp., San Fernando | Trinidad *(inherited from previous clause)* | [1937, 1939, 1940] |

## Candidate stint `Rostant, P. A___Trinidad and Tobago___1927`

- Staff-list name: **Rostant, P. A** | colony: **Trinidad and Tobago** | listed 1927–1937 | editions [1927, 1928, 1929, 1931, 1933, 1934, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | P. A. Rostant | Assistant Res. Surgeon, Colonial Hospital, Port of Spain | Government Medical Officers | — | — |
| 1928 | P. A. Rostant | Assistant Res. Surgeon, Colonial Hospital | Government Medical Officers | — | — |
| 1929 | P. A. Rostant | Assistant Res. Surgeon, Colonial Hospital, Port of Spain | Government Medical Officers | — | — |
| 1931 | P. A. Rostant | Res. Surgeon, Colonial Hospital | Government Medical Officers | — | — |
| 1933 | P. A. Rostant | Res. Surgeon, Colonial Hospital, San Fernando | Medical Establishment | — | — |
| 1934 | P. A. Rostant | Res. Surgeon, Colonial Hospital | Government Medical Officers | — | — |
| 1937 | P. A. Rostant | Senior Medical Officer (Surgeon) | Colonial Hospital, San Fernando | — | — |

### Deterministic checks: `rostant_pierrre-ange_b1891` vs `Rostant, P. A___Trinidad and Tobago___1927`

- [PASS] surname_gate: bio 'ROSTANT' vs stint 'Rostant, P. A' (exact)
- [PASS] initials: bio ['P', 'A'] ~ stint ['P', 'A']
- [PASS] age_gate: stint starts 1927, birth 1891 (age 36)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1937
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

