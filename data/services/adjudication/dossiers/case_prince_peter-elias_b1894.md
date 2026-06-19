<!-- {"case_id": "case_prince_peter-elias_b1894", "bio_ids": ["prince_peter-elias_b1894"], "stint_ids": ["Prince, P. E___Cyprus___1929"]} -->
# Dossier case_prince_peter-elias_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `prince_peter-elias_b1894`

- Printed name: **PRINCE, Peter Elias**
- Birth year: 1894 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L35344.v` — printed in editions [1948]:**

> PRINCE, Peter Elias.—b. 1894; ed. Terra Santa Sch., Greek Sch., English Sch., Nicosia; gen. clerical staff, Cyp., 1910; examiner of accnts., 1927; audr., 1944; mem. of comte. to examine affairs of the mun. coun., Morphou, 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | gen. clerical staff | Cyprus | [1948] |
| 1 | 1927 | examiner of accnts | Cyprus *(inherited from previous clause)* | [1948] |
| 2 | 1929 | mem. of comte. to examine affairs of the mun. coun., Morphou | Cyprus *(inherited from previous clause)* | [1948] |
| 3 | 1944 | audr | Cyprus *(inherited from previous clause)* | [1948] |

## Candidate stint `Prince, P. E___Cyprus___1929`

- Staff-list name: **Prince, P. E** | colony: **Cyprus** | listed 1929–1939 | editions [1929, 1930, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | P. E. Prince | Examiners of Accounts | Audit Department | — | — |
| 1930 | P. E. Prince | Examiner of Accounts | Audit Department | — | — |
| 1934 | P. E. Prince | Examiner of Accounts | Audit Department | — | — |
| 1936 | P. E. Prince | Examiner of Accounts | Audit Department | — | — |
| 1939 | P. E. Prince | Examiner of Accounts | Audit Department | — | — |

### Deterministic checks: `prince_peter-elias_b1894` vs `Prince, P. E___Cyprus___1929`

- [PASS] surname_gate: bio 'PRINCE' vs stint 'Prince, P. E' (exact)
- [PASS] initials: bio ['P', 'E'] ~ stint ['P', 'E']
- [PASS] age_gate: stint starts 1929, birth 1894 (age 35)
- [PASS] colony: 4 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1929-1939
- [PASS] position_sim: best 95 vs bar 60: 'examiner of accnts' ~ 'Examiner of Accounts'
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

