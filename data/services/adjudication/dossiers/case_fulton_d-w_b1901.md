<!-- {"case_id": "case_fulton_d-w_b1901", "bio_ids": ["fulton_d-w_b1901"], "stint_ids": ["Fulton, D. William___Sierra Leone___1949"]} -->
# Dossier case_fulton_d-w_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fulton_d-w_b1901`

- Printed name: **FULTON, D. W**
- Birth year: 1901 (attested in editions [1956])
- Appears in editions: [1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L21254.v` — printed in editions [1956]:**

> FULTON, D. W.—b. 1901; E. A. rly., 1931; asst. acctnt., S. Leone, rly., 1942; chief acctnt., 1949; dep. chief acctnt., G.C. rly., 1953 (G.C. local service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | E. A. rly | — | [1956] |
| 1 | 1942 | asst. acctnt., S. Leone, rly | — | [1956] |
| 2 | 1949 | chief acctnt | — | [1956] |
| 3 | 1953 | dep. chief acctnt., G.C. rly | Gold Coast | [1956] |

## Candidate stint `Fulton, D. William___Sierra Leone___1949`

- Staff-list name: **Fulton, D. William** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. William Fulton | Assistant Accountants | Railway | — | — |
| 1950 | D. W. Fulton | Chief Accountant | Accounts | — | — |
| 1951 | D. W. Fulton | Chief Accountant | Accounts | — | — |

### Deterministic checks: `fulton_d-w_b1901` vs `Fulton, D. William___Sierra Leone___1949`

- [PASS] surname_gate: bio 'FULTON' vs stint 'Fulton, D. William' (exact)
- [PASS] initials: bio ['D', 'W'] ~ stint ['D', 'W']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
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

