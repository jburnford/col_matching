<!-- {"case_id": "case_jeffs_percy_b1881", "bio_ids": ["jeffs_percy_b1881"], "stint_ids": ["Jeffs, P___Gambia___1923", "Jeffs, P___Togoland___1920"]} -->
# Dossier case_jeffs_percy_b1881

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['jeffs_percy_b1881'] carry a single initial only — the namesake trap applies.

## Biography `jeffs_percy_b1881`

- Printed name: **JEFFS, Percy**
- Birth year: 1881 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L33637.v` — printed in editions [1948, 1949, 1950]:**

> JEFFS, Percy, M.C.—b. 1881; on mil. serv., 1916-19, staff capt.; A.D.C. and P.S., G.C., 1919; Gamb., 1922; admin. offr., 1935; A.D.C., Fiji, 1936; Jca., 1938; Br. Guiana, 1945; Imp. censorship, Jca., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | A.D.C. and P.S. | Gold Coast | [1948, 1949, 1950] |
| 1 | 1922 | Gamb | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950] |
| 2 | 1935 | admin. offr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950] |
| 3 | 1936 | A.D.C. | Fiji | [1948, 1949, 1950] |
| 4 | 1938 | A.D.C. | Jamaica | [1948, 1949, 1950] |
| 5 | 1944 | Imp. censorship | Jamaica | [1948, 1949, 1950] |
| 6 | 1945 | A.D.C. | British Guiana | [1948, 1949, 1950] |

## Candidate stint `Jeffs, P___Gambia___1923`

- Staff-list name: **Jeffs, P** | colony: **Gambia** | listed 1923–1936 | editions [1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | P. Jeffs | Aide-de-Camp and Private Secretary | Civil Establishment | — | Captain |
| 1924 | Captain P. Jeffs | Aide-de-Camp and Private Secretary | Civil Establishment | — | Captain |
| 1927 | P. Jeffs | Assistant | Provincial Administration | — | Captain |
| 1928 | P. Jeffs | Assistant | Provincial Administration | — | Captain |
| 1929 | P. Jeffs | Assistant | Provincial Administration | — | Captain |
| 1930 | Captain P. Jeffs | Assistant | Provincial Administration | — | Captain |
| 1931 | P. Jeffs | Assistant | Provincial Administration | — | Captain |
| 1932 | Captain P. Jeffs | Travelling Commissioner | Provincial Administration | — | Captain |
| 1933 | P. Jeffs | Commissioner | Provincial Administration | — | Captain |
| 1934 | P. Jeffs | Commissioner | Provincial Administration | — | Captain |
| 1936 | P. Jeffs | Commissioners and Assistant Commissioners | Provincial Administration | — | Captain |

### Deterministic checks: `jeffs_percy_b1881` vs `Jeffs, P___Gambia___1923`

- [PASS] surname_gate: bio 'JEFFS' vs stint 'Jeffs, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1923, birth 1881 (age 42)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1936
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Jeffs, P___Togoland___1920`

- Staff-list name: **Jeffs, P** | colony: **Togoland** | listed 1920–1921 | editions [1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | P. Jeffs | Private Secretary | Civil Establishment | — | Captain |
| 1921 | P. Jeffs | Aide-de-Camp | Governor's Office | — | Captain |

### Deterministic checks: `jeffs_percy_b1881` vs `Jeffs, P___Togoland___1920`

- [PASS] surname_gate: bio 'JEFFS' vs stint 'Jeffs, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1920, birth 1881 (age 39)
- [FAIL] colony: no placed event resolves to 'Togoland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1921
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

