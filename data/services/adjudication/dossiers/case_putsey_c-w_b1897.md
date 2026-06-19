<!-- {"case_id": "case_putsey_c-w_b1897", "bio_ids": ["putsey_c-w_b1897"], "stint_ids": ["Pusey, C___Palestine___1929"]} -->
# Dossier case_putsey_c-w_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `putsey_c-w_b1897`

- Printed name: **PUTSEY, C. W**
- Birth year: 1897 (attested in editions [1949, 1950, 1951, 1953])
- Appears in editions: [1949, 1950, 1951, 1953]

### Verbatim printed entry text (OCR)

**Version `col1949-L35078.v` — printed in editions [1949, 1950, 1951, 1953]:**

> PUTSEY, C. W.—b. 1897; ed. St. Clement's Ch. Sch., York.; mil. serv., 1915-19; traff. inspr., Nig., 1927; asst. traff. offr., 1936; senr. asst., 1944; dist. traff. supt., 1946; asst. traff. man., 1949; ch. supt., Nig. rly., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | traff. inspr. | Nigeria | [1949, 1950, 1951, 1953] |
| 1 | 1936 | asst. traff. offr | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953] |
| 2 | 1944 | senr. asst | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953] |
| 3 | 1946 | dist. traff. supt | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953] |
| 4 | 1949 | asst. traff. man | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953] |
| 5 | 1951 | ch. supt., Nig. rly | Nigeria | [1949, 1950, 1951, 1953] |

## Candidate stint `Pusey, C___Palestine___1929`

- Staff-list name: **Pusey, C** | colony: **Palestine** | listed 1929–1940 | editions [1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | C. Pusey | Senior Assistant Land Settlement Officer | Land Settlement | — | — |
| 1930 | C. Pusey | Senior Assistant Land Settlement Officer | Land Settlement | — | — |
| 1931 | C. Pusey | Senior Assistant Land Settlement Officer | Land Settlement | — | — |
| 1932 | C. Pusey | Senior Assistant Land Settlement Officers | Land Settlement | — | — |
| 1940 | C. Pusey | Settlement Officers | Department of Lands and Surveys | — | — |

### Deterministic checks: `putsey_c-w_b1897` vs `Pusey, C___Palestine___1929`

- [PASS] surname_gate: bio 'PUTSEY' vs stint 'Pusey, C' (fuzzy:1)
- [PASS] initials: bio ['C', 'W'] ~ stint ['C']
- [PASS] age_gate: stint starts 1929, birth 1897 (age 32)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1940
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

