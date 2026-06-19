<!-- {"case_id": "case_hale_george-samuel_b1899", "bio_ids": ["hale_george-samuel_b1899"], "stint_ids": ["Hale, G. S___Kenya___1949"]} -->
# Dossier case_hale_george-samuel_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hale_george-samuel_b1899`

- Printed name: **HALE, George Samuel**
- Birth year: 1899 (attested in editions [1948, 1949])
- Honours: M.B
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L33078.v` — printed in editions [1948, 1949]:**

> HALE, George Samuel, M.B., B.S. (Lond.), M.R.C.S. (Eng.), L.R.C.P. (Lond.), D.T.M. (Liv.).—b. 1899; ed. Westminster, and London Univ.; on mil. serv., 1918-19, 2nd lieut.; med. offr., Ken., 1926; S.M.O., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | med. offr. | Kenya | [1948, 1949] |
| 1 | 1947 | S.M.O | Kenya *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Hale, G. S___Kenya___1949`

- Staff-list name: **Hale, G. S** | colony: **Kenya** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. S. Hale | Senior Medical Officers | Medical | — | — |
| 1950 | G. S. Hale | Senior Medical Officers | Medical | — | — |

### Deterministic checks: `hale_george-samuel_b1899` vs `Hale, G. S___Kenya___1949`

- [PASS] surname_gate: bio 'HALE' vs stint 'Hale, G. S' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G', 'S']
- [PASS] age_gate: stint starts 1949, birth 1899 (age 50)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 15 vs bar 60: 'S.M.O' ~ 'Senior Medical Officers'
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

