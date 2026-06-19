<!-- {"case_id": "case_skelton_alfred-norman_b1896", "bio_ids": ["skelton_alfred-norman_b1896"], "stint_ids": ["Skelton, A. N___Nyasaland___1949"]} -->
# Dossier case_skelton_alfred-norman_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `skelton_alfred-norman_b1896`

- Printed name: **SKELTON, Alfred Norman**
- Birth year: 1896 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L42524.v` — printed in editions [1951]:**

> SKELTON, Alfred Norman.—b. 1896; ed. High Sch., Scarborough; on mil. serv., 1915–19; appt. Br. postal serv., 1914; T.T., 1921; E.A.P.S., 1933; asst. P.M.G., Nyasa., 1947; T.T. European civ. serv. bd., 1946–47; attd. African post and telecom. union conf., Cape Town, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | appt. Br. postal serv | — | [1951] |
| 1 | 1921 | T.T | — | [1951] |
| 2 | 1933 | E.A.P.S | — | [1951] |
| 3 | 1946–1947 | T.T. European civ. serv. bd | Nyasaland *(inherited from previous clause)* | [1951] |
| 4 | 1947 | asst. P.M.G. | Nyasaland | [1951] |
| 5 | 1948 | attd. African post and telecom. union conf., Cape Town | Cape of Good Hope | [1951] |

## Candidate stint `Skelton, A. N___Nyasaland___1949`

- Staff-list name: **Skelton, A. N** | colony: **Nyasaland** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. N. Skelton | Assistant Postmaster-General | Posts and Telegraphs | — | — |
| 1950 | A. N. Skelton | Assistant Postmaster-General | POSTS AND TELEGRAPHS | — | — |
| 1951 | A. N. Skelton | Assistant Postmaster-General | POSTS AND TELEGRAPHHS | — | — |

### Deterministic checks: `skelton_alfred-norman_b1896` vs `Skelton, A. N___Nyasaland___1949`

- [PASS] surname_gate: bio 'SKELTON' vs stint 'Skelton, A. N' (exact)
- [PASS] initials: bio ['A', 'N'] ~ stint ['A', 'N']
- [PASS] age_gate: stint starts 1949, birth 1896 (age 53)
- [PASS] colony: 2 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 46 vs bar 60: 'asst. P.M.G.' ~ 'Assistant Postmaster-General'
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

