<!-- {"case_id": "case_whitman_vivian-emlyn_b1899", "bio_ids": ["whitman_vivian-emlyn_b1899"], "stint_ids": ["Whitman, V. E___Gold Coast___1929"]} -->
# Dossier case_whitman_vivian-emlyn_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `whitman_vivian-emlyn_b1899`

- Printed name: **WHITMAN, Vivian Emlyn**
- Birth year: 1899 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36820.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WHITMAN, Vivian Emlyn, B.Sc. (Wales), M.R.C.S. (eng.), L.R.C.P. (Lond.), D.P.H. (Lond.), D.T.M. & H. (Lond.).—b. 1899; ed. Sec. Sch. and Univ. of Wales; on mil. serv., 1916-19; M.O.H., G.C., 1928; S.M.O., S.L., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | M.O.H. | Gold Coast | [1948, 1949, 1950, 1951] |
| 1 | 1944 | S.M.O. | Sierra Leone | [1948, 1949, 1950, 1951] |

## Candidate stint `Whitman, V. E___Gold Coast___1929`

- Staff-list name: **Whitman, V. E** | colony: **Gold Coast** | listed 1929–1936 | editions [1929, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | V. E. Whitman | Medical Officer of Health | Sanitation Branch | — | — |
| 1932 | V. E. Whitman | Medical Officer of Health | Sanitation Branch | — | — |
| 1934 | V. E. Whitman | Medical Officers of Health | Health Branch | — | — |
| 1936 | V. E. Whitman | Medical Officers of Health | Health Branch | — | — |

### Deterministic checks: `whitman_vivian-emlyn_b1899` vs `Whitman, V. E___Gold Coast___1929`

- [PASS] surname_gate: bio 'WHITMAN' vs stint 'Whitman, V. E' (exact)
- [PASS] initials: bio ['V', 'E'] ~ stint ['V', 'E']
- [PASS] age_gate: stint starts 1929, birth 1899 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1936
- [FAIL] position_sim: best 14 vs bar 60: 'M.O.H.' ~ 'Medical Officer of Health'
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

