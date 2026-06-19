<!-- {"case_id": "case_cosgrove_alfred-owen_b1901", "bio_ids": ["cosgrove_alfred-owen_b1901"], "stint_ids": ["Cosgrove, A. O___Kenya___1937"]} -->
# Dossier case_cosgrove_alfred-owen_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cosgrove_alfred-owen_b1901`

- Printed name: **COSGROVE, Alfred Owen**
- Birth year: 1901 (attested in editions [1948, 1950, 1951])
- Honours: M.I.E.E
- Appears in editions: [1948, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31924.v` — printed in editions [1948, 1950, 1951]:**

> COSGROVE, Alfred Owen, B.Sc. (eng.), M.I.E.E.—b. 1901; ed. St. Andrew's Coll., Grahamstown, S.A., and Cape Town Univ., medallist and prizeman; electcn., posts and tels. dept., Union S.A., 1922; Ken., 1926; elec. inspr., 1934; elec. engnr., 1938; mem. of various technical comtees. in Kenya.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | electcn., posts and tels. dept., Union S.A | — | [1948, 1950, 1951] |
| 1 | 1926 | electcn., posts and tels. dept., Union S.A | Kenya | [1948, 1950, 1951] |
| 2 | 1934 | elec. inspr | Kenya *(inherited from previous clause)* | [1948, 1950, 1951] |
| 3 | 1938 | elec. engnr | Kenya *(inherited from previous clause)* | [1948, 1950, 1951] |

## Candidate stint `Cosgrove, A. O___Kenya___1937`

- Staff-list name: **Cosgrove, A. O** | colony: **Kenya** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | A. O. Cosgrove | Electrical Inspector | Posts and Telegraphs Department | — | — |
| 1939 | A. O. Cosgrove | Electrical Engineer | Posts and Telegraphs Department | — | — |
| 1940 | A. O. Cosgrove | Electrical Engineer | Posts and Telegraphs Department | — | — |

### Deterministic checks: `cosgrove_alfred-owen_b1901` vs `Cosgrove, A. O___Kenya___1937`

- [PASS] surname_gate: bio 'COSGROVE' vs stint 'Cosgrove, A. O' (exact)
- [PASS] initials: bio ['A', 'O'] ~ stint ['A', 'O']
- [PASS] age_gate: stint starts 1937, birth 1901 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1937-1940
- [PASS] position_sim: best 69 vs bar 60: 'elec. engnr' ~ 'Electrical Engineer'
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

