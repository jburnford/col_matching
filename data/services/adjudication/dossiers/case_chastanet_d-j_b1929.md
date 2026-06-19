<!-- {"case_id": "case_chastanet_d-j_b1929", "bio_ids": ["chastanet_d-j_b1929"], "stint_ids": ["Chastanet, D. J___St Lucia___1963"]} -->
# Dossier case_chastanet_d-j_b1929

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chastanet_d-j_b1929`

- Printed name: **CHASTANET, D. J**
- Birth year: 1929 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L21621.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> CHASTANET, D. J.—b. 1929; ed. St. Mary's Coll., St. L., and Battersea Poly., London; asst. col. engrn., St. L., 1954; col. engrn. (now D.P.W.), 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1954 | asst. col. engrn. | St. Lucia | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1957 | col. engrn. (now D.P.W.) | St. Lucia *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Chastanet, D. J___St Lucia___1963`

- Staff-list name: **Chastanet, D. J** | colony: **St Lucia** | listed 1963–1965 | editions [1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | D. J. Chastanet | Director of Public Works | Civil Establishment | — | — |
| 1964 | D. J. Chastanet | Director of Public Works | Civil Establishment | — | — |
| 1965 | D. J. Chastanet | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `chastanet_d-j_b1929` vs `Chastanet, D. J___St Lucia___1963`

- [PASS] surname_gate: bio 'CHASTANET' vs stint 'Chastanet, D. J' (exact)
- [PASS] initials: bio ['D', 'J'] ~ stint ['D', 'J']
- [PASS] age_gate: stint starts 1963, birth 1929 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'St Lucia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1963-1965
- [FAIL] position_sim: best 29 vs bar 60: 'col. engrn. (now D.P.W.)' ~ 'Director of Public Works'
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

