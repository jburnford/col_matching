<!-- {"case_id": "case_randabel_jean-paul_b1903", "bio_ids": ["randabel_jean-paul_b1903"], "stint_ids": ["Randabel, P___Mauritius___1927"]} -->
# Dossier case_randabel_jean-paul_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `randabel_jean-paul_b1903`

- Printed name: **RANDABEL, Jean Paul**
- Birth year: 1903 (attested in editions [1958, 1959, 1960])
- Appears in editions: [1948, 1949, 1950, 1951, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1958-L26225.v` — printed in editions [1958, 1959, 1960]:**

> RANDABEL, J. P.—b. 1903; ed. Royal Coll., Maur.; prov. asst. master, Maur., 1923; asst. master, 1925; inspr., educ., 1941; tutor, training coll., 1945; educ. offr., 1948-59.

**Version `col1948-L35412.v` — printed in editions [1948, 1949, 1950, 1951]:**

> RANDABEL, Jean Paul.—b. 1903; ed. Royal Coll., Mauritius; asst. mstr, Royal Coll., Maur., 1923; inspr. of schs., 1942; tutor, train. coll., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | prov. asst. master | Mauritius | [1948, 1949, 1950, 1951, 1958, 1959, 1960] |
| 1 | 1925 | asst. master | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960] |
| 2 | 1941 | inspr., educ | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960] |
| 3 | 1942 | inspr. of schs | Mauritius *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1945 | tutor, training coll | Mauritius *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1958, 1959, 1960] |

## Candidate stint `Randabel, P___Mauritius___1927`

- Staff-list name: **Randabel, P** | colony: **Mauritius** | listed 1927–1929 | editions [1927, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | P. Randabel | Assistant Masters | Education | — | — |
| 1929 | P. Randabel | Assistant Masters | Education | — | — |

### Deterministic checks: `randabel_jean-paul_b1903` vs `Randabel, P___Mauritius___1927`

- [PASS] surname_gate: bio 'RANDABEL' vs stint 'Randabel, P' (exact)
- [PASS] initials: bio ['J', 'P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1927, birth 1903 (age 24)
- [PASS] colony: 5 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1929
- [PASS] position_sim: best 79 vs bar 60: 'asst. master' ~ 'Assistant Masters'
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

