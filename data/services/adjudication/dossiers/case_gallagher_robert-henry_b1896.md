<!-- {"case_id": "case_gallagher_robert-henry_b1896", "bio_ids": ["gallagher_robert-henry_b1896"], "stint_ids": ["Gallagher, R. H___Tanganyika___1922"]} -->
# Dossier case_gallagher_robert-henry_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gallagher_robert-henry_b1896`

- Printed name: **GALLAGHER, Robert Henry**
- Birth year: 1896 (attested in editions [1949])
- Appears in editions: [1949]

### Verbatim printed entry text (OCR)

**Version `col1949-L32186.v` — printed in editions [1949]:**

> GALLAGHER, Robert Henry.—b. 1896; ed. Bersham Sch.; on mil. serv., 1915-19; capt.; Brit. postal serv., 1912; T.T., 1919; asst. surv., posts and tels., Nig., 1929; senr., 1931; divsnl., 1945; retd., 1947; re-appt., temp. basis, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | Brit. postal serv | — | [1949] |
| 1 | 1919 | T.T | — | [1949] |
| 2 | 1929 | asst. surv., posts and tels. | Nigeria | [1949] |
| 3 | 1931 | senr | Nigeria *(inherited from previous clause)* | [1949] |
| 4 | 1945 | divsnl | Nigeria *(inherited from previous clause)* | [1949] |
| 5 | 1947 | retd | Nigeria *(inherited from previous clause)* | [1949] |
| 6 | 1948 | re-appt., temp. basis | Nigeria *(inherited from previous clause)* | [1949] |

## Candidate stint `Gallagher, R. H___Tanganyika___1922`

- Staff-list name: **Gallagher, R. H** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | R. H. Gallagher | Postmasters | Post and Telegraphs Department | — | — |
| 1923 | R. H. Gallagher | Postmasters | Post and Telegraphs Department | — | — |
| 1924 | R. H. Gallagher | Postmasters | Post and Telegraphs Department | — | — |
| 1925 | R. H. Gallagher | Postmasters | Post and Telegraphs Department | — | — |

### Deterministic checks: `gallagher_robert-henry_b1896` vs `Gallagher, R. H___Tanganyika___1922`

- [PASS] surname_gate: bio 'GALLAGHER' vs stint 'Gallagher, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1922, birth 1896 (age 26)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
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

