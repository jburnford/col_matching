<!-- {"case_id": "case_katul_jibrall_b1895", "bio_ids": ["katul_jibrall_b1895"], "stint_ids": ["Katul, J___Palestine___1923"]} -->
# Dossier case_katul_jibrall_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['katul_jibrall_b1895'] carry a single initial only — the namesake trap applies.

## Biography `katul_jibrall_b1895`

- Printed name: **KATUL, Jibrall**
- Birth year: 1895 (attested in editions [1948])
- Honours: O.B.E (1945)
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L33760.v` — printed in editions [1948]:**

> KATUL, Jibrall, O.B.E. (1945), M.B.E. (hon.) (1934).—b. 1895; ed. American Univ., Beirut; apptd. educ. dept., Pal., 1922; senr. inspr., 1933; asst. dir., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | apptd. educ. dept. | Palestine | [1948] |
| 1 | 1933 | senr. inspr | Palestine *(inherited from previous clause)* | [1948] |
| 2 | 1937 | asst. dir | Palestine *(inherited from previous clause)* | [1948] |

## Candidate stint `Katul, J___Palestine___1923`

- Staff-list name: **Katul, J** | colony: **Palestine** | listed 1923–1940 | editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | J. Katul | Vice-Principal | Education | — | — |
| 1924 | J. Katul | Vice-Principal | Education | — | — |
| 1925 | J. Katul | Vice-Principal | Department of Education | — | — |
| 1927 | J. Katul | Headquarters Inspector | Department of Education | — | — |
| 1928 | J. Katul | Headquarters Inspector | Department of Education | — | — |
| 1929 | J. Katul | Headquarters Inspectors | Department of Education | — | — |
| 1930 | J. Katul | Headquarters Inspector | Department of Education | — | — |
| 1931 | J. Katul | Headquarters Inspector | Department of Education | — | — |
| 1932 | J. Katul | Headquarters Inspectors | Department of Education | — | — |
| 1940 | J. Katul | Senior Inspector | Department of Education | — | — |

### Deterministic checks: `katul_jibrall_b1895` vs `Katul, J___Palestine___1923`

- [PASS] surname_gate: bio 'KATUL' vs stint 'Katul, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1923, birth 1895 (age 28)
- [PASS] colony: 3 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1923-1940
- [PASS] position_sim: best 77 vs bar 60: 'senr. inspr' ~ 'Senior Inspector'
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

