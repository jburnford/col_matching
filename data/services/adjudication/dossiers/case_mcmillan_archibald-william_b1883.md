<!-- {"case_id": "case_mcmillan_archibald-william_b1883", "bio_ids": ["mcmillan_archibald-william_b1883"], "stint_ids": ["McMillan, A. W___Fiji___1932", "McMillan, Alex___Canada___1920"]} -->
# Dossier case_mcmillan_archibald-william_b1883

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcmillan_archibald-william_b1883`

- Printed name: **McMILLAN, Archibald William**
- Birth year: 1883 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L34406.v` — printed in editions [1948, 1949, 1950]:**

> McMILLAN, Archibald William.—b. 1883; ed. Livingstone Coll. and Harley Coll., Lond.; studied Hindi and Urdu in India; on mil. serv., 1917–19, twice men. in desps.; inspr. of schls., Fiji, 1929; comsnt. on prob. work, 1944; chmn., bd. of examrs. in Hindustani, 1930–47; author of Hindustani Handbook, 1931 and Guide to Hindustani, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | inspr. of schls. | Fiji | [1948, 1949, 1950] |
| 1 | 1930–1947 | chmn., bd. of examrs. in Hindustani | Fiji *(inherited from previous clause)* | [1948, 1949, 1950] |
| 2 | 1931 | author of Hindustani Handbook | Fiji *(inherited from previous clause)* | [1948, 1949, 1950] |
| 3 | 1944 | comsnt. on prob. work | Fiji *(inherited from previous clause)* | [1948, 1949, 1950] |
| 4 | 1947 | Guide to Hindustani | Fiji *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `McMillan, A. W___Fiji___1932`

- Staff-list name: **McMillan, A. W** | colony: **Fiji** | listed 1932–1940 | editions [1932, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | A. W. McMillan | Inspector of Indian Schools | Education Department | — | — |
| 1933 | A. W. McMillan | Inspector of Indian Schools | Education Department | — | — |
| 1934 | A. W. McMillan | Inspector of Indian Schools | Education Department | — | — |
| 1936 | A. W. McMillan | Inspector of Indian Schools | Education Department | — | — |
| 1937 | A. W. McMillan | Inspector of Indian Schools | Education Department | — | — |
| 1939 | A. W. McMillan | Inspector of Schools | Education Department | — | — |
| 1940 | A. W. McMillan | Inspector of Schools | Education Department | — | — |

### Deterministic checks: `mcmillan_archibald-william_b1883` vs `McMillan, A. W___Fiji___1932`

- [PASS] surname_gate: bio 'McMILLAN' vs stint 'McMillan, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1932, birth 1883 (age 49)
- [PASS] colony: 5 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1932-1940
- [FAIL] position_sim: best 45 vs bar 60: 'author of Hindustani Handbook' ~ 'Inspector of Schools'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `McMillan, Alex___Canada___1920`

- Staff-list name: **McMillan, Alex** | colony: **Canada** | listed 1920–1922 | editions [1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Alex. McMillan | Aides-de-Camp | Civil Establishment | — | Major |
| 1922 | Alex. McMillan | Aides-de-Camp | Civil Establishment | — | Major |

### Deterministic checks: `mcmillan_archibald-william_b1883` vs `McMillan, Alex___Canada___1920`

- [PASS] surname_gate: bio 'McMILLAN' vs stint 'McMillan, Alex' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A']
- [PASS] age_gate: stint starts 1920, birth 1883 (age 37)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1922
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

