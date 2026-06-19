<!-- {"case_id": "case_schranz_j_b1907", "bio_ids": ["schranz_j_b1907"], "stint_ids": ["Schranz, J___Malta___1937", "Schranz, J___Malta___1962"]} -->
# Dossier case_schranz_j_b1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['schranz_j_b1907'] carry a single initial only — the namesake trap applies.

## Biography `schranz_j_b1907`

- Printed name: **SCHRANZ, J**
- Birth year: 1907 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1958-L26715.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> SCHRANZ, J.—b. 1907; ed. Lyceum, Malta; teacher, Malta, 1925; civ. serv. (admin.), 1929; acctnt., 1947; prin. offr., 1948; import licensing and price reg. offr., 1955; chief exec. offr., 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | teacher | Malta | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1929 | civ. serv. (admin.) | Malta *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1947 | acctnt | Malta *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1948 | prin. offr | Malta *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1955 | import licensing and price reg. offr | Malta *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1956 | chief exec. offr | Malta *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Schranz, J___Malta___1937`

- Staff-list name: **Schranz, J** | colony: **Malta** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | J. Schranz | Clerks, 2nd Class | Labour Department | — | — |
| 1939 | J. Schranz | Clerks, 2nd Class | Labour Department | — | — |
| 1940 | J. Schranz | Clerk, 2nd Class | Labour and Emigration Department | — | — |

### Deterministic checks: `schranz_j_b1907` vs `Schranz, J___Malta___1937`

- [PASS] surname_gate: bio 'SCHRANZ' vs stint 'Schranz, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1937, birth 1907 (age 30)
- [PASS] colony: 6 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 41 vs bar 60: 'civ. serv. (admin.)' ~ 'Clerk, 2nd Class'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Schranz, J___Malta___1962`

- Staff-list name: **Schranz, J** | colony: **Malta** | listed 1962–1964 | editions [1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | J. Schranz | Assistant Director | Civil Establishment | — | — |
| 1963 | J. Schranz | Assistant Director | Civil Establishment | — | — |
| 1964 | J. Schranz | Assistant Director | Civil Establishment | — | — |

### Deterministic checks: `schranz_j_b1907` vs `Schranz, J___Malta___1962`

- [PASS] surname_gate: bio 'SCHRANZ' vs stint 'Schranz, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1962, birth 1907 (age 55)
- [PASS] colony: 6 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1962-1964
- [FAIL] position_sim: best 36 vs bar 60: 'chief exec. offr' ~ 'Assistant Director'
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

