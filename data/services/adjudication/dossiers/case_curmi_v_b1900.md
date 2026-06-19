<!-- {"case_id": "case_curmi_v_b1900", "bio_ids": ["curmi_v_b1900"], "stint_ids": ["Curmi, V. M___Malta___1929", "Curmi, V. M___Malta___1936"]} -->
# Dossier case_curmi_v_b1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['curmi_v_b1900'] carry a single initial only — the namesake trap applies.

## Biography `curmi_v_b1900`

- Printed name: **CURMI, V**
- Birth year: 1900 (attested in editions [1956])
- Appears in editions: [1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L20667.v` — printed in editions [1956]:**

> CURMI, V.—b. 1900; ed. Lyceum, Malta; civ. serv. (admin.), Malta, 1921; contrlr., bldg. materials, 1947; prin. offr., 1948; dep. food and commerce contr. offr., 1949; chief clk., educ. dept., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | civ. serv. (admin.) | Malta | [1956] |
| 1 | 1947 | contrlr., bldg. materials | Malta *(inherited from previous clause)* | [1956] |
| 2 | 1948 | prin. offr | Malta *(inherited from previous clause)* | [1956] |
| 3 | 1949 | dep. food and commerce contr. offr | Malta *(inherited from previous clause)* | [1956] |
| 4 | 1952 | chief clk., educ. dept | Malta *(inherited from previous clause)* | [1956] |

## Candidate stint `Curmi, V. M___Malta___1929`

- Staff-list name: **Curmi, V. M** | colony: **Malta** | listed 1929–1931 | editions [1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | V. Curmi | Clerk, 3rd Class | Emigration Department | — | — |
| 1931 | V. Curmi | Clerk, 2nd Class | Emigration Department | — | — |

### Deterministic checks: `curmi_v_b1900` vs `Curmi, V. M___Malta___1929`

- [PASS] surname_gate: bio 'CURMI' vs stint 'Curmi, V. M' (exact)
- [PASS] initials: bio ['V'] ~ stint ['V', 'M']
- [PASS] age_gate: stint starts 1929, birth 1900 (age 29)
- [PASS] colony: 5 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1931
- [FAIL] position_sim: best 41 vs bar 60: 'civ. serv. (admin.)' ~ 'Clerk, 2nd Class'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Curmi, V. M___Malta___1936`

- Staff-list name: **Curmi, V. M** | colony: **Malta** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | V. M. Curmi | Physician and Surgeon-in-Charge of Venereal Diseases Section | Hospitals, etc. | — | — |
| 1936 | V. Curmi | Clerk, 2nd Class | Labour Department | — | — |
| 1936 | V. M. Curmi | Lecturer on Venereology and Dermatology | Professors | — | — |
| 1937 | V. Curmi | Clerks, 2nd Class | Labour Department | — | — |
| 1937 | V. M. Curmi | Lecturer on Venerology and Dermatology | Professors | — | — |
| 1937 | V. M. Curmi | Physician and Surgeon-in-Charge of Venereal Diseases Section | Hospitals, etc. | — | — |
| 1939 | V. M. Curmi | Physician and Surgeon in charge of Venereal Diseases Department | Central Hospital | — | — |
| 1939 | V. Curmi | Clerks, 2nd Class | Labour Department | — | — |
| 1939 | V. M. Curmi | Lecturer on Venereology and Dermatology | Professors | — | — |
| 1940 | V. M. Curmi | Physician and Surgeon in charge of Venereal Diseases Department | Central Hospital | — | — |
| 1940 | V. Curmi | Clerk, 1st Class | Labour and Emigration Department | — | — |

### Deterministic checks: `curmi_v_b1900` vs `Curmi, V. M___Malta___1936`

- [PASS] surname_gate: bio 'CURMI' vs stint 'Curmi, V. M' (exact)
- [PASS] initials: bio ['V'] ~ stint ['V', 'M']
- [PASS] age_gate: stint starts 1936, birth 1900 (age 36)
- [PASS] colony: 5 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 41 vs bar 60: 'civ. serv. (admin.)' ~ 'Clerk, 2nd Class'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

