<!-- {"case_id": "case_barnes_james-ivor_b1903", "bio_ids": ["barnes_james-ivor_b1903"], "stint_ids": ["Barnes, J. I___Hong Kong___1936"]} -->
# Dossier case_barnes_james-ivor_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 46 official(s) with this surname in the graph's staff lists; 25 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `barnes_james-ivor_b1903`

- Printed name: **BARNES, James Ivor**
- Birth year: 1903 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L33436.v` — printed in editions [1950, 1951]:**

> BARNES, James Ivor, M.R.San.I.—b. 1903; ed. elem. sch. and army, 1st cl. cert., R.S.I. certs.; sany. inspr., H.K., 1928; senr. cl. and acctg. staff, 1934; exec. offr., cl. I (regraded), 1947; senr. exec. offr., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | sany. inspr. | Hong Kong | [1950, 1951] |
| 1 | 1934 | senr. cl. and acctg. staff | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 2 | 1947 | exec. offr., cl. I (regraded) | Hong Kong *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Barnes, J. I___Hong Kong___1936`

- Staff-list name: **Barnes, J. I** | colony: **Hong Kong** | listed 1936–1937 | editions [1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | J. I. Barnes | Asst. Secretary | Medical Department | — | — |
| 1937 | J. I. Barnes | Asst. Secretary | Medical Department | — | — |

### Deterministic checks: `barnes_james-ivor_b1903` vs `Barnes, J. I___Hong Kong___1936`

- [PASS] surname_gate: bio 'BARNES' vs stint 'Barnes, J. I' (exact)
- [PASS] initials: bio ['J', 'I'] ~ stint ['J', 'I']
- [PASS] age_gate: stint starts 1936, birth 1903 (age 33)
- [PASS] colony: 3 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1937
- [FAIL] position_sim: best 43 vs bar 60: 'senr. cl. and acctg. staff' ~ 'Asst. Secretary'
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

