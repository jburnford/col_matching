<!-- {"case_id": "case_nugent_charles-evelyn_b1883", "bio_ids": ["nugent_charles-evelyn_b1883"], "stint_ids": ["Nugent, C E___Straits Settlements___1931"]} -->
# Dossier case_nugent_charles-evelyn_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Nugent, C E___Straits Settlements___1931` is also gate-compatible with biography(ies) outside this case: ['nugent_x_e1836'] (already linked elsewhere or filtered).

## Biography `nugent_charles-evelyn_b1883`

- Printed name: **NUGENT, CHARLES EVELYN**
- Birth year: 1883 (attested in editions [1932, 1933])
- Appears in editions: [1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1932-L62899.v` — printed in editions [1932, 1933]:**

> NUGENT, CAPT. CHARLES EVELYN, M.C.—B. 1883; survr., probt., F.M.S., Oct., 1912; survr., grade II, Dec., 1913; cadet, R.F.A., Mar., 1916; lieut., R.G.A., June, 1916; M.C., demob., Mar., 1919; asst. supt., rev. surveys, N. Sem bilan, Jan., 1919; asst. supt., surveys, F.M.S., May, 1927; asst. supt., rev. surveys, Selangor, Jan., 1928; supt., surveys, Johore, Aug., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | survr., probt. | Federated Malay States | [1932, 1933] |
| 1 | 1913 | survr., grade II | Federated Malay States *(inherited from previous clause)* | [1932, 1933] |
| 2 | 1916 | cadet, R.F.A | Federated Malay States *(inherited from previous clause)* | [1932, 1933] |
| 3 | 1919 | M.C., demob | Federated Malay States *(inherited from previous clause)* | [1932, 1933] |
| 4 | 1927 | asst. supt., surveys | Federated Malay States | [1932, 1933] |
| 5 | 1928 | asst. supt., rev. surveys, Selangor | Federated Malay States *(inherited from previous clause)* | [1932, 1933] |
| 6 | 1929 | supt., surveys | Johore | [1932, 1933] |

## Candidate stint `Nugent, C E___Straits Settlements___1931`

- Staff-list name: **Nugent, C E** | colony: **Straits Settlements** | listed 1931–1932 | editions [1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | C E Nugent | Superintendents | SURVEYS | — | — |
| 1932 | C. E. Nugent | Superintendent | Surveys | — | — |

### Deterministic checks: `nugent_charles-evelyn_b1883` vs `Nugent, C E___Straits Settlements___1931`

- [PASS] surname_gate: bio 'NUGENT' vs stint 'Nugent, C E' (exact)
- [PASS] initials: bio ['C', 'E'] ~ stint ['C', 'E']
- [PASS] age_gate: stint starts 1931, birth 1883 (age 48)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
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

