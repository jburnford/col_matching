<!-- {"case_id": "case_trafford_wm_b1911", "bio_ids": ["trafford_wm_b1911"], "stint_ids": ["Trafford, W___Singapore___1959"]} -->
# Dossier case_trafford_wm_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['trafford_wm_b1911'] carry a single initial only — the namesake trap applies.

## Biography `trafford_wm_b1911`

- Printed name: **TRAFFORD, Wm**
- Birth year: 1911 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Honours: M.B.E (1948)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L24626.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> TRAFFORD, Wm., M.B.E. (1948).—b. 1911; ed. Magnus Sch., Newark, and Univ. Coll., Nottingham; engrnr., posts and tels., K. Lumpur, 1939; asst. contrlr., 1941; asst. contrlr., telecoms., 1945; contrlr., telecoms., S'pore, 1951; special services, 1952; Mal. and S'pore I.E.E. o'sea rep. of coun., 1956; contrlr., telecoms., spec. servs., 1957-60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | engrnr., posts and tels., K. Lumpur | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1941 | asst. contrlr | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1945 | asst. contrlr., telecoms | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1951 | contrlr., telecoms., S'pore | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 4 | 1952 | special services | — | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 5 | 1956 | Mal. and S'pore I.E.E. o'sea rep. of coun | Malaya | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 6 | 1957–1960 | contrlr., telecoms., spec. servs | Malaya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Trafford, W___Singapore___1959`

- Staff-list name: **Trafford, W** | colony: **Singapore** | listed 1959–1960 | editions [1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | W. Trafford | Controller of Telecommunications | Singapore : Somaliland Protectorate | — | — |
| 1960 | W. Trafford | Controllers of Telecommunications | Ministry of National Development | — | — |

### Deterministic checks: `trafford_wm_b1911` vs `Trafford, W___Singapore___1959`

- [PASS] surname_gate: bio 'TRAFFORD' vs stint 'Trafford, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1959, birth 1911 (age 48)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1960
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

