<!-- {"case_id": "case_brabant_w-j-s_b1908", "bio_ids": ["brabant_w-j-s_b1908"], "stint_ids": ["Brabant, W. J. S___Fiji___1950", "Brabant, W. J. S___Western Pacific___1953"]} -->
# Dossier case_brabant_w-j-s_b1908

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `brabant_w-j-s_b1908`

- Printed name: **BRABANT, W. J. S**
- Birth year: 1908 (attested in editions [1955, 1956, 1957])
- Honours: O.B.E (1957)
- Appears in editions: [1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1955-L19861.v` — printed in editions [1955, 1956, 1957]:**

> BRABANT, W. J. S., O.B.E. (1957).—b. 1908; ed. Mt. Albert Gram. Sch. and Auckland Univ. Coll., N.Z.; asst. acctnt.-gen., Fiji, 1949; acctnt.-gen., and collr., customs, G. and E.I.C., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | asst. acctnt.-gen. | Fiji | [1955, 1956, 1957] |
| 1 | 1952 | acctnt.-gen., and collr., customs, G. and E.I.C | Fiji *(inherited from previous clause)* | [1955, 1956, 1957] |

## Candidate stint `Brabant, W. J. S___Fiji___1950`

- Staff-list name: **Brabant, W. J. S** | colony: **Fiji** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | W. J. S. Brabant | Accountants | ACCOUNTANT-GENERAL | — | — |
| 1951 | W. J. S. Brabant | Accountants | ACCOUNTANT-GENERAL | — | — |

### Deterministic checks: `brabant_w-j-s_b1908` vs `Brabant, W. J. S___Fiji___1950`

- [PASS] surname_gate: bio 'BRABANT' vs stint 'Brabant, W. J. S' (exact)
- [PASS] initials: bio ['W', 'J', 'S'] ~ stint ['W', 'J', 'S']
- [PASS] age_gate: stint starts 1950, birth 1908 (age 42)
- [PASS] colony: 2 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 56 vs bar 60: 'asst. acctnt.-gen.' ~ 'Accountants'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Brabant, W. J. S___Western Pacific___1953`

- Staff-list name: **Brabant, W. J. S** | colony: **Western Pacific** | listed 1953–1956 | editions [1953, 1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | W. J. S. Brabant | Accountant-General | Civil Establishment | — | — |
| 1954 | W. J. S. Brabant | Accountant-General | Civil Establishment | — | — |
| 1955 | W. J. S. Brabant | Accountant-General | Civil Establishment | — | — |
| 1956 | W. J. S. Brabant | Accountant-General | Civil Establishment | — | — |

### Deterministic checks: `brabant_w-j-s_b1908` vs `Brabant, W. J. S___Western Pacific___1953`

- [PASS] surname_gate: bio 'BRABANT' vs stint 'Brabant, W. J. S' (exact)
- [PASS] initials: bio ['W', 'J', 'S'] ~ stint ['W', 'J', 'S']
- [PASS] age_gate: stint starts 1953, birth 1908 (age 45)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1956
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

