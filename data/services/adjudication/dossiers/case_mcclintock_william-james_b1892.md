<!-- {"case_id": "case_mcclintock_william-james_b1892", "bio_ids": ["mcclintock_william-james_b1892"], "stint_ids": ["McClintock, W. J___Gold Coast___1932"]} -->
# Dossier case_mcclintock_william-james_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcclintock_william-james_b1892`

- Printed name: **McCLINTOCK, William James**
- Birth year: 1892 (attested in editions [1949])
- Honours: B.A, M.B
- Appears in editions: [1949]

### Verbatim printed entry text (OCR)

**Version `col1949-L33863.v` — printed in editions [1949]:**

> McCLINTOCK, William James, B.A., M.B., B.Ch., B.A.O. (Dub.).—b. 1892; ed. Dublin Univ. and L.S.H.T.M. (cert.); on naval serv., surg.-lieut. (temp. R.N.); med. offr., Nig., 1921; S.M.O., G.C., 1929; asst. D.M.S., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | med. offr. | Nigeria | [1949] |
| 1 | 1929 | S.M.O. | Gold Coast | [1949] |
| 2 | 1936 | asst. D.M.S | Gold Coast *(inherited from previous clause)* | [1949] |

## Candidate stint `McClintock, W. J___Gold Coast___1932`

- Staff-list name: **McClintock, W. J** | colony: **Gold Coast** | listed 1932–1936 | editions [1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | W. J. McClintock | Senior Medical Officer | Medical Department | — | — |
| 1934 | W. J. McClintock | Senior Medical Officers | Medical Department | — | — |
| 1936 | W. J. McClintock | Senior Medical Officers | Medical Department | — | — |

### Deterministic checks: `mcclintock_william-james_b1892` vs `McClintock, W. J___Gold Coast___1932`

- [PASS] surname_gate: bio 'McCLINTOCK' vs stint 'McClintock, W. J' (exact)
- [PASS] initials: bio ['W', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1932, birth 1892 (age 40)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1932-1936
- [FAIL] position_sim: best 26 vs bar 60: 'asst. D.M.S' ~ 'Senior Medical Officers'
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

