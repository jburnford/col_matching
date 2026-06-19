<!-- {"case_id": "case_thorpe_w-f-h_b1921", "bio_ids": ["thorpe_w-f-h_b1921"], "stint_ids": ["Thorpe, W. F. H___Uganda___1949"]} -->
# Dossier case_thorpe_w-f-h_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Thorpe, W. F. H___Uganda___1949` is also gate-compatible with biography(ies) outside this case: ['thorpe_henry_b1874'] (already linked elsewhere or filtered).

## Biography `thorpe_w-f-h_b1921`

- Printed name: **THORPE, W. F. H**
- Birth year: 1921 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L27831.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> THORPE, W. F. H.—b. 1921; ed. Mill Hill Sch. and Jesus Coll., Camb.; mil. serv., 1941–42, lieut.; cadet, Uga., 1942; asst. D.O., 1944; secon. co-op. devel. dept., 1951; co-op. offr., 1955–62. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1942 | cadet | Uganda | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1944 | asst. D.O | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1951 | secon. co-op. devel. dept | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1955–1962 | co-op. offr | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Thorpe, W. F. H___Uganda___1949`

- Staff-list name: **Thorpe, W. F. H** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. F. H. Thorpe | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | W. F. H. Thorpe | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `thorpe_w-f-h_b1921` vs `Thorpe, W. F. H___Uganda___1949`

- [PASS] surname_gate: bio 'THORPE' vs stint 'Thorpe, W. F. H' (exact)
- [PASS] initials: bio ['W', 'F', 'H'] ~ stint ['W', 'F', 'H']
- [PASS] age_gate: stint starts 1949, birth 1921 (age 28)
- [PASS] colony: 4 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 37 vs bar 60: 'asst. D.O' ~ 'District Officers and Assistant District Officers'
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

