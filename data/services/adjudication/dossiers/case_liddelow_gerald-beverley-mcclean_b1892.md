<!-- {"case_id": "case_liddelow_gerald-beverley-mcclean_b1892", "bio_ids": ["liddelow_gerald-beverley-mcclean_b1892"], "stint_ids": ["Liddelow, G. B___Trinidad and Tobago___1925"]} -->
# Dossier case_liddelow_gerald-beverley-mcclean_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `liddelow_gerald-beverley-mcclean_b1892`

- Printed name: **LIDDELOW, Gerald Beverley McClean**
- Birth year: 1892 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L40091.v` — printed in editions [1951]:**

> LIDDELOW, Gerald Beverley McClean.—b. 1892; ed. Queen's Royal Coll., Trin. and Lancing Coll., Sussex; on mil. serv., 1939–43, maj.; apptd. police dept., Trin., 1921; supt., police, 1934; asst. comsnr., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | apptd. police dept. | Trinidad | [1951] |
| 1 | 1934 | supt., police | Trinidad *(inherited from previous clause)* | [1951] |
| 2 | 1948 | asst. comsnr | Trinidad *(inherited from previous clause)* | [1951] |

## Candidate stint `Liddelow, G. B___Trinidad and Tobago___1925`

- Staff-list name: **Liddelow, G. B** | colony: **Trinidad and Tobago** | listed 1925–1949 | editions [1925, 1927, 1928, 1929, 1931, 1933, 1934, 1937, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | G. Liddelow | Sub-Inspector | Constabulary and Gaols | — | — |
| 1927 | G. Liddelow | Sub-Inspector | Constabulary and Gaols | — | — |
| 1928 | G. Liddelow | Sub-Inspectors | Constabulary and Gaols | — | — |
| 1929 | G. Liddelow | Sub-Inspectors | Constabulary and Gaols | — | — |
| 1931 | G. Liddelow | Sub-Inspector | Constabulary and Gaols | — | — |
| 1933 | G. Liddelow | Sub-Inspector | Constabulary and Gaols | — | — |
| 1934 | G. Liddelow | Sub-Inspector | Constabulary and Gaols | — | — |
| 1937 | Capt. G. B. Liddelow | Inspectors | Constabulary | — | Captain |
| 1940 | G. B. Liddelow | Superintendent | Police | — | Major |
| 1949 | G. B. Liddelow | Superintendents | Police | — | — |

### Deterministic checks: `liddelow_gerald-beverley-mcclean_b1892` vs `Liddelow, G. B___Trinidad and Tobago___1925`

- [PASS] surname_gate: bio 'LIDDELOW' vs stint 'Liddelow, G. B' (exact)
- [PASS] initials: bio ['G', 'B', 'M'] ~ stint ['G', 'B']
- [PASS] age_gate: stint starts 1925, birth 1892 (age 33)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1949
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

