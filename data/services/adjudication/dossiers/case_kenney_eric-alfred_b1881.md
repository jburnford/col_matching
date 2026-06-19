<!-- {"case_id": "case_kenney_eric-alfred_b1881", "bio_ids": ["kenney_eric-alfred_b1881"], "stint_ids": ["Kenney, E A___Straits Settlements___1931"]} -->
# Dossier case_kenney_eric-alfred_b1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kenney_eric-alfred_b1881`

- Printed name: **KENNEY, ERIC ALFRED**
- Birth year: 1881 (attested in editions [1932])
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L61683.v` — printed in editions [1932]:**

> KENNEY, ERIC ALFRED.—B. 1881; survr., rev. survey br., F.M.S., Apr., 1911; survr., grade I. Nov., 1917; asst. supt., Jan., 1919; Malacca revisionary survey, S.S., Mar., 1923; sr. asst. supt., Singapore, July, 1926; supt., survey dept., F.M.S. and S.S., Nov., 1928; supr., rev. surveys, N. Sembilan, Feb., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | survr., rev. survey br. | Federated Malay States | [1932] |
| 1 | 1917 | survr., grade I | Federated Malay States *(inherited from previous clause)* | [1932] |
| 2 | 1919 | asst. supt | Federated Malay States *(inherited from previous clause)* | [1932] |
| 3 | 1923 | Malacca revisionary survey | Straits Settlements | [1932] |
| 4 | 1926 | sr. asst. supt. | Singapore | [1932] |
| 5 | 1928 | supt., survey dept., F.M.S. and S.S | Federated Malay States | [1932] |
| 6 | 1930 | supr., rev. surveys, N. Sembilan | Federated Malay States *(inherited from previous clause)* | [1932] |

## Candidate stint `Kenney, E A___Straits Settlements___1931`

- Staff-list name: **Kenney, E A** | colony: **Straits Settlements** | listed 1931–1932 | editions [1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | E A Kenney | Superintendents | SURVEYS | — | — |
| 1932 | E. A. Kenney | Superintendent | Surveys | — | — |

### Deterministic checks: `kenney_eric-alfred_b1881` vs `Kenney, E A___Straits Settlements___1931`

- [PASS] surname_gate: bio 'KENNEY' vs stint 'Kenney, E A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1931, birth 1881 (age 50)
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1932
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

