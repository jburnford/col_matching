<!-- {"case_id": "case_neal_w-j-l_b1903", "bio_ids": ["neal_w-j-l_b1903"], "stint_ids": ["Neal, W. J. L___Aden___1949", "Neal, W. J. L___North Borneo___1952"]} -->
# Dossier case_neal_w-j-l_b1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `neal_w-j-l_b1903`

- Printed name: **NEAL, W. J. L**
- Birth year: 1903 (attested in editions [1953])
- Honours: O.B.E
- Appears in editions: [1953]

### Verbatim printed entry text (OCR)

**Version `col1953-L18555.v` — printed in editions [1953]:**

> NEAL, W. J. L., O.B.E.—b. 1903; ed. Queen's Univ., Belfast; Ind. Med. Serv., 1926; ret., 1949; med. supt., Aden, 1948; D.M.S., N. Borneo, 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | Ind. Med. Serv | — | [1953] |
| 1 | 1948 | med. supt. | Aden | [1953] |
| 2 | 1949 | ret | — | [1953] |
| 3 | 1951 | D.M.S. | North Borneo | [1953] |

## Candidate stint `Neal, W. J. L___Aden___1949`

- Staff-list name: **Neal, W. J. L** | colony: **Aden** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. J. L. Neal | Medical Officer | Medical | — | — |
| 1950 | W. J. L. Neal | Medical Superintendent | Medical | — | Lieut.-Col. |

### Deterministic checks: `neal_w-j-l_b1903` vs `Neal, W. J. L___Aden___1949`

- [PASS] surname_gate: bio 'NEAL' vs stint 'Neal, W. J. L' (exact)
- [PASS] initials: bio ['W', 'J', 'L'] ~ stint ['W', 'J', 'L']
- [PASS] age_gate: stint starts 1949, birth 1903 (age 46)
- [PASS] colony: 1 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 53 vs bar 60: 'med. supt.' ~ 'Medical Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Neal, W. J. L___North Borneo___1952`

- Staff-list name: **Neal, W. J. L** | colony: **North Borneo** | listed 1952–1953 | editions [1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | W. J. L. Neal | Director of Medical Services | Civil Establishment | — | — |
| 1953 | W. J. L. Neal | Director of Medical Services | Civil Establishment | — | — |

### Deterministic checks: `neal_w-j-l_b1903` vs `Neal, W. J. L___North Borneo___1952`

- [PASS] surname_gate: bio 'NEAL' vs stint 'Neal, W. J. L' (exact)
- [PASS] initials: bio ['W', 'J', 'L'] ~ stint ['W', 'J', 'L']
- [PASS] age_gate: stint starts 1952, birth 1903 (age 49)
- [PASS] colony: 1 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1952-1953
- [FAIL] position_sim: best 19 vs bar 60: 'D.M.S.' ~ 'Director of Medical Services'
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

