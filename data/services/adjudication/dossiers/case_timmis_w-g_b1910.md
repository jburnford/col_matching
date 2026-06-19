<!-- {"case_id": "case_timmis_w-g_b1910", "bio_ids": ["timmis_w-g_b1910"], "stint_ids": ["Timmis, W. G___Uganda___1949"]} -->
# Dossier case_timmis_w-g_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `timmis_w-g_b1910`

- Printed name: **TIMMIS, W. G**
- Birth year: 1910 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1958-L27609.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> TIMMIS, W. G.—b. 1910; ed. Birkenhead Sch., Univ. of L'pool and L.S.T.M.; mil. serv., 1939–45, S.M.O.; M.O., Uga., 1946–62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946–1962 | M.O. | Uganda | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Timmis, W. G___Uganda___1949`

- Staff-list name: **Timmis, W. G** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. G. Timmis | Medical Officers | Medical | — | — |
| 1951 | W. G. Timmis | Medical Officers | MEDICAL | — | — |

### Deterministic checks: `timmis_w-g_b1910` vs `Timmis, W. G___Uganda___1949`

- [PASS] surname_gate: bio 'TIMMIS' vs stint 'Timmis, W. G' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 22 vs bar 60: 'M.O.' ~ 'Medical Officers'
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

