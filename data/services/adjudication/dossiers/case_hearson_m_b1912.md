<!-- {"case_id": "case_hearson_m_b1912", "bio_ids": ["hearson_m_b1912"], "stint_ids": ["Hearson, M___Hong Kong___1949"]} -->
# Dossier case_hearson_m_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hearson_m_b1912'] carry a single initial only — the namesake trap applies.

## Biography `hearson_m_b1912`

- Printed name: **HEARSON, M**
- Birth year: 1912 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1956-L21791.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> HEARSON, Miss M.—b. 1912; ed. Bishop Blackall Sch. and Univ. Coll. of the S.W., Exeter; aux. nursing serv., 1941–42; mistress, educ. dept., H.K., 1940; senr. educ. offr. (woman), 1955; senr. prin., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | mistress, educ. dept. | Hong Kong | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1941–1942 | aux. nursing serv | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1955 | senr. educ. offr. (woman) | Hong Kong *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1961 | senr. prin | Hong Kong *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Hearson, M___Hong Kong___1949`

- Staff-list name: **Hearson, M** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | M. Hearson | Mistresses | Education Department | — | — |
| 1950 | M. Hearson | Mistresses | Education | — | — |
| 1951 | M. Hearson | Mistresses | Education | — | — |

### Deterministic checks: `hearson_m_b1912` vs `Hearson, M___Hong Kong___1949`

- [PASS] surname_gate: bio 'HEARSON' vs stint 'Hearson, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 3 placed event(s) resolve to 'Hong Kong'
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

