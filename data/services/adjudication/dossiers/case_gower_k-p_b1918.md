<!-- {"case_id": "case_gower_k-p_b1918", "bio_ids": ["gower_k-p_b1918"], "stint_ids": ["Gower, K. P___Zanzibar___1949"]} -->
# Dossier case_gower_k-p_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gower_k-p_b1918`

- Printed name: **GOWER, K. P**
- Birth year: 1918 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1957-L23492.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> GOWER, K. P.—b. 1918; ed. Shrewsbury Sch. and Merton Coll., Oxford; mil. serv., 1940-45, capt.; cadet, Zanz., 1945; D.O., 1947; Uga., 1949; dist. comsnr., Bunyoro, 1953; asst. sec., min. of comms. and wks., 1957-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | cadet | Zanzibar | [1957, 1958, 1959, 1960, 1961] |
| 1 | 1947 | cadet | Dominions Office | [1957, 1958, 1959, 1960, 1961] |
| 2 | 1949 | cadet | Uganda | [1957, 1958, 1959, 1960, 1961] |
| 3 | 1953 | dist. comsnr., Bunyoro | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 4 | 1957–1961 | asst. sec., min. of comms. and wks | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Gower, K. P___Zanzibar___1949`

- Staff-list name: **Gower, K. P** | colony: **Zanzibar** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | K. P. Gower | Administrative Officer | District Administration | — | — |
| 1950 | K. P. Gower | Administrative Officer | District Administration | — | — |
| 1951 | K. P. Gower | Administrative Officers | District Administration | — | — |

### Deterministic checks: `gower_k-p_b1918` vs `Gower, K. P___Zanzibar___1949`

- [PASS] surname_gate: bio 'GOWER' vs stint 'Gower, K. P' (exact)
- [PASS] initials: bio ['K', 'P'] ~ stint ['K', 'P']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
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

