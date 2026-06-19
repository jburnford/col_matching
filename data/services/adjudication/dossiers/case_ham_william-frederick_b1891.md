<!-- {"case_id": "case_ham_william-frederick_b1891", "bio_ids": ["ham_william-frederick_b1891"], "stint_ids": ["Ham, W___Australia___1913"]} -->
# Dossier case_ham_william-frederick_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ham_william-frederick_b1891`

- Printed name: **HAM, WILLIAM FREDERICK**
- Birth year: 1891 (attested in editions [1931])
- Honours: F.R.I
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L66758.v` — printed in editions [1931]:**

> HAM, WILLIAM FREDERICK, B.SC., F.R.I.—B. 1891; LIET. NIGERIAN REGT.; SURVEY DEPT., NIGERIA, 1914-27; DEP. EN., GOLD COAST, JUNE, 1927; AG. SURVR. VARIOUS OCCASION, 1927-30.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1927 | SURVEY DEPT. | NIGERIA | [1931] |
| 1 | 1927 | DEP. EN., GOLD COAST, JUNE | NIGERIA *(inherited from previous clause)* | [1931] |

## Candidate stint `Ham, W___Australia___1913`

- Staff-list name: **Ham, W** | colony: **Australia** | listed 1913–1927 | editions [1913, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | W. Ham | Assistant Inspector | Education Department | — | — |
| 1927 | W. Ham | Senior Lecturer | Teachers' Training College | — | — |

### Deterministic checks: `ham_william-frederick_b1891` vs `Ham, W___Australia___1913`

- [PASS] surname_gate: bio 'HAM' vs stint 'Ham, W' (exact)
- [PASS] initials: bio ['W', 'F'] ~ stint ['W']
- [PASS] age_gate: stint starts 1913, birth 1891 (age 22)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1927
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

