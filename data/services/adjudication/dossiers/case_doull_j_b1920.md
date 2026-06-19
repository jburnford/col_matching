<!-- {"case_id": "case_doull_j_b1920", "bio_ids": ["doull_j_b1920"], "stint_ids": ["Doull, J___Sierra Leone___1949"]} -->
# Dossier case_doull_j_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['doull_j_b1920'] carry a single initial only — the namesake trap applies.

## Biography `doull_j_b1920`

- Printed name: **DOULL, J**
- Birth year: 1920 (attested in editions [1960, 1961])
- Appears in editions: [1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1960-L22435.v` — printed in editions [1960, 1961]:**

> DOULL, J.—b. 1920; ed. Dollar Academy and Skerry's Coll.; asst. inspr., police, Ken., 1941; asst. supt., S. Leone, 1948; senr. supt., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | asst. inspr., police | Kenya | [1960, 1961] |
| 1 | 1948 | asst. supt., S. Leone | Kenya *(inherited from previous clause)* | [1960, 1961] |
| 2 | 1959 | senr. supt | Kenya *(inherited from previous clause)* | [1960, 1961] |

## Candidate stint `Doull, J___Sierra Leone___1949`

- Staff-list name: **Doull, J** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. Doull | Assistant Superintendents of Police | POLICE | — | — |
| 1950 | J. Doull | Assistant Superintendents of Police | POLICE | — | — |
| 1951 | J. Doull | Assistant Superintendents of Police | Police | — | — |

### Deterministic checks: `doull_j_b1920` vs `Doull, J___Sierra Leone___1949`

- [PASS] surname_gate: bio 'DOULL' vs stint 'Doull, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1949, birth 1920 (age 29)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

