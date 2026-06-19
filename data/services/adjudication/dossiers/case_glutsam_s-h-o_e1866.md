<!-- {"case_id": "case_glutsam_s-h-o_e1866", "bio_ids": ["glutsam_s-h-o_e1866"], "stint_ids": ["Clutsam, H. O___Bahamas___1906", "Clutsam, S.H.O___Bahamas___1899"]} -->
# Dossier case_glutsam_s-h-o_e1866

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Clutsam, H. O___Bahamas___1906` is also gate-compatible with biography(ies) outside this case: ['clutsam_s-h-o_e1866'] (already linked elsewhere or filtered).
- NOTE: stint `Clutsam, S.H.O___Bahamas___1899` is also gate-compatible with biography(ies) outside this case: ['clutsam_s-h-o_e1866'] (already linked elsewhere or filtered).

## Biography `glutsam_s-h-o_e1866`

- Printed name: **GLUTSAM, S. H. O**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L32706.v` — printed in editions [1898]:**

> GLUTSAM, S. H. O.—Called to bar, Bahamas, July, 1868; ag. sec. to bd. of educn., 1882; ag. stip. and circuit mag., in 1887; asst. clk. and sergt-at-arms, house of assem., 1866; ch. clk., 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | asst. clk. and sergt-at-arms, house of assem | Bahamas *(inherited from previous clause)* | [1898] |
| 1 | 1868 | Called to bar | Bahamas | [1898] |
| 2 | 1882 | ag. sec. to bd. of educn | Bahamas *(inherited from previous clause)* | [1898] |
| 3 | 1887 | ag. stip. and circuit mag., in | Bahamas *(inherited from previous clause)* | [1898] |
| 4 | 1890 | ch. clk | Bahamas *(inherited from previous clause)* | [1898] |

## Candidate stint `Clutsam, H. O___Bahamas___1906`

- Staff-list name: **Clutsam, H. O** | colony: **Bahamas** | listed 1906–1912 | editions [1906, 1907, 1908, 1909, 1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | H. O. Clutsam | Clerk at Asylum | Medical Department | — | — |
| 1907 | H. O. Clutsam | Clerk at Asylum | Medical Department | — | — |
| 1908 | H. O. Clutsam | Tide Waiter | Treasury and Customs Department | — | — |
| 1909 | H. O. Clutsam | Tide Waiter | Treasury and Customs Department | — | — |
| 1911 | H. O. Clutsam | 3rd Clerk | Post Office | — | — |
| 1912 | H. O. Clutsam | 2nd Clerk | Post Office | — | — |

### Deterministic checks: `glutsam_s-h-o_e1866` vs `Clutsam, H. O___Bahamas___1906`

- [PASS] surname_gate: bio 'GLUTSAM' vs stint 'Clutsam, H. O' (fuzzy:1)
- [PASS] initials: bio ['S', 'H', 'O'] ~ stint ['H', 'O']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1912
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Clutsam, S.H.O___Bahamas___1899`

- Staff-list name: **Clutsam, S.H.O** | colony: **Bahamas** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | S. H. O. Clutsam | Chief Clerk | House of Assembly | — | — |
| 1900 | S.H.O. Clutsam | Chief Clerk | — | — | — |

### Deterministic checks: `glutsam_s-h-o_e1866` vs `Clutsam, S.H.O___Bahamas___1899`

- [PASS] surname_gate: bio 'GLUTSAM' vs stint 'Clutsam, S.H.O' (fuzzy:1)
- [PASS] initials: bio ['S', 'H', 'O'] ~ stint ['S', 'H', 'O']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1899-1900
- [PASS] position_sim: best 71 vs bar 60: 'ch. clk' ~ 'Chief Clerk'
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

