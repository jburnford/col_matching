<!-- {"case_id": "case_ramsbotham_w-a-m_b1915", "bio_ids": ["ramsbotham_w-a-m_b1915"], "stint_ids": ["Ramsbotham, W. A. M___Hong Kong___1949"]} -->
# Dossier case_ramsbotham_w-a-m_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ramsbotham_w-a-m_b1915`

- Printed name: **RAMSBOTHAM, W. A. M**
- Birth year: 1915 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L27097.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> RAMSBOTHAM, W. A. M.—b. 1915; ed. Doveton Coll., India, and Faraday Hse., Elec. Engng. Coll., London; telecomms. dept., H.K., 1947; engnr., b'casting dept., S'pore, 1950; N. Borneo, 1961; ch. engnr., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | telecomms. dept. | Hong Kong | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1950 | engnr., b'casting dept., S'pore | Hong Kong *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1961 | engnr., b'casting dept., S'pore | North Borneo | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1962 | ch. engnr | North Borneo *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Ramsbotham, W. A. M___Hong Kong___1949`

- Staff-list name: **Ramsbotham, W. A. M** | colony: **Hong Kong** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. A. M. Ramsbotham | Wireless Engineers | Telecommunications Branch | — | — |
| 1950 | W. A. M. Ramsbotham | Wireless Engineer | Telecommunications | — | — |

### Deterministic checks: `ramsbotham_w-a-m_b1915` vs `Ramsbotham, W. A. M___Hong Kong___1949`

- [PASS] surname_gate: bio 'RAMSBOTHAM' vs stint 'Ramsbotham, W. A. M' (exact)
- [PASS] initials: bio ['W', 'A', 'M'] ~ stint ['W', 'A', 'M']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 39 vs bar 60: 'telecomms. dept.' ~ 'Wireless Engineer'
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

