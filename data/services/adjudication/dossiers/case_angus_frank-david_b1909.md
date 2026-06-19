<!-- {"case_id": "case_angus_frank-david_b1909", "bio_ids": ["angus_frank-david_b1909"], "stint_ids": ["Angus, F. D___Hong Kong___1949"]} -->
# Dossier case_angus_frank-david_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `angus_frank-david_b1909`

- Printed name: **ANGUS, Frank David**
- Birth year: 1909 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1950-L33240.v` — printed in editions [1950, 1951]:**

> ANGUS, Frank David.—b. 1909; ed. Victoria Br. Sch. and Central Br. Sch., H.K.; probr. senr. cl. and acctg. staff, H.K., 1927; class III, 1930; class I, 1946; assessor, gr. II, incl. rev. dept., 1947; gr. I, 1949.

**Version `col1961-L19249.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> ANGUS, F. D.—b. 1909; ed. Victoria British Sch., and Central British Sch., H.K.; apptd. H.K., 1927; assessor, gr. II, inland rev. dept., 1947; gr. I, 1949; chief assessor, 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | probr. senr. cl. and acctg. staff | Hong Kong | [1950, 1951] |
| 1 | 1927 | apptd. H.K | — | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1930 | class III | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 3 | 1946 | class I | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 4 | 1947 | assessor, gr. II, incl. rev. dept | Hong Kong *(inherited from previous clause)* | [1950, 1951, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1949 | gr. I | Hong Kong *(inherited from previous clause)* | [1950, 1951, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1959 | chief assessor | — | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Angus, F. D___Hong Kong___1949`

- Staff-list name: **Angus, F. D** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. D. Angus | Assessors, Grade II | Inland Revenue | — | — |
| 1950 | F. D. Angus | Assessors, Grade I | INLAND REVENUE | — | — |
| 1951 | F. D. Angus | Assessors, Grade I | INLAND REVENUE | — | — |

### Deterministic checks: `angus_frank-david_b1909` vs `Angus, F. D___Hong Kong___1949`

- [PASS] surname_gate: bio 'ANGUS' vs stint 'Angus, F. D' (exact)
- [PASS] initials: bio ['F', 'D'] ~ stint ['F', 'D']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [PASS] colony: 5 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 65 vs bar 60: 'assessor, gr. II, incl. rev. dept' ~ 'Assessors, Grade II'
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

