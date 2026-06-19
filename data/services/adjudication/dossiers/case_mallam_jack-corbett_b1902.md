<!-- {"case_id": "case_mallam_jack-corbett_b1902", "bio_ids": ["mallam_jack-corbett_b1902"], "stint_ids": ["Mallam, J. C___Nigeria___1934"]} -->
# Dossier case_mallam_jack-corbett_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mallam_jack-corbett_b1902`

- Printed name: **MALLAM, Jack Corbett**
- Birth year: 1902 (attested in editions [1956, 1957, 1958, 1959])
- Appears in editions: [1949, 1950, 1951, 1953, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1956-L22885.v` — printed in editions [1956, 1957, 1958, 1959]:**

> MALLAM, J. C.—b. 1902; ed. Lancing Coll. and Queen's Coll., Oxford; mil. serv., 1940–43, lieut.; asst. consvtr., forests, S.L., 1926; specialist, timber seasoning and preservation, Nig., 1927; asst. ch. consvtr., 1934; consvtr., 1946; asst. ch. consvtr., 1947; ch. consvtr., W. regn., 1951; consvtr., Tang., 1955–58.

**Version `col1953-L18362.v` — printed in editions [1953]:**

> MALLAM, J. C.—b. 1902; ed. Lancing and Queen's Coll., Oxford; mil. serv., 1940-43, capt.; forestry dept., S.L., 1926; specialist in seasoning and preservtn. of timber, Nig., 1927; convstr., 1946; asst. ch. convstr., 1947; ch. convstr., W. region, 1951.

**Version `col1949-L34130.v` — printed in editions [1949, 1950, 1951]:**

> MALLAM, Jack Corbett.—b. 1902; ed. Lancing and Queen's Coll., Oxford (dip. in rural econ., Oxford and dip. in for., Oxford); on mil. serv. 1940–43, capt.; forestry dept., S.L., 1926; seasoning and preservtn. of timber speclst., Nig., 1927; consvtr., forests, 1946; asst. ch. consvtr., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. consvtr., forests | Sierra Leone | [1949, 1950, 1951, 1953, 1956, 1957, 1958, 1959] |
| 1 | 1927 | specialist, timber seasoning and preservation | Nigeria | [1949, 1950, 1951, 1953, 1956, 1957, 1958, 1959] |
| 2 | 1934 | asst. ch. consvtr | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 3 | 1946 | consvtr | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1956, 1957, 1958, 1959] |
| 4 | 1947 | asst. ch. consvtr | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1956, 1957, 1958, 1959] |
| 5 | 1951 | ch. consvtr., W. regn | Nigeria *(inherited from previous clause)* | [1953, 1956, 1957, 1958, 1959] |
| 6 | 1955–1958 | consvtr. | Tanganyika | [1956, 1957, 1958, 1959] |

## Candidate stint `Mallam, J. C___Nigeria___1934`

- Staff-list name: **Mallam, J. C** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | J. C. Mallam | Wood Seasoning Officer | Forestry | — | — |
| 1939 | J. C. Mallam | Senior Assistant Conservators and Assistant Conservators of Forests | Forestry | — | — |

### Deterministic checks: `mallam_jack-corbett_b1902` vs `Mallam, J. C___Nigeria___1934`

- [PASS] surname_gate: bio 'MALLAM' vs stint 'Mallam, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1934, birth 1902 (age 32)
- [PASS] colony: 5 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 58 vs bar 60: 'specialist, timber seasoning and preservation' ~ 'Wood Seasoning Officer'
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

