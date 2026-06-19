<!-- {"case_id": "case_cavill_dorothy-mary_b1904", "bio_ids": ["cavill_dorothy-mary_b1904"], "stint_ids": ["Cavill, D. M___Hong Kong___1949"]} -->
# Dossier case_cavill_dorothy-mary_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cavill_dorothy-mary_b1904`

- Printed name: **CAVILL, Dorothy Mary**
- Birth year: 1904 (attested in editions [1948, 1949, 1950, 1951])
- Honours: A.L.C.M
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31688.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CAVILL, Dorothy Mary, A.L.C.M., LL.C.M.—b. 1904; ed. Ashburton Gram. Sch., Devon, Whitclands Coll., London, and Manchester Univ., higher Frobel dip.; N.F.U.; bd. of educ. cert. general subjects; mistress, H.K., 1933; N. Rhod., 1942; reverted to H.K., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | mistress | Hong Kong | [1948, 1949, 1950, 1951] |
| 1 | 1942 | mistress | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 2 | 1946 | reverted to H.K | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Cavill, D. M___Hong Kong___1949`

- Staff-list name: **Cavill, D. M** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. M. Cavill | Mistresses | Education Department | — | — |
| 1950 | D. M. Cavill | Mistresses | Education | — | — |
| 1951 | D. M. Cavill | Mistresses | Education | — | — |

### Deterministic checks: `cavill_dorothy-mary_b1904` vs `Cavill, D. M___Hong Kong___1949`

- [PASS] surname_gate: bio 'CAVILL' vs stint 'Cavill, D. M' (exact)
- [PASS] initials: bio ['D', 'M'] ~ stint ['D', 'M']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
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

