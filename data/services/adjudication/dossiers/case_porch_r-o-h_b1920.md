<!-- {"case_id": "case_porch_r-o-h_b1920", "bio_ids": ["porch_r-o-h_b1920"], "stint_ids": ["Porch, R. O. H___Uganda___1949"]} -->
# Dossier case_porch_r-o-h_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `porch_r-o-h_b1920`

- Printed name: **PORCH, R. O. H**
- Birth year: 1920 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L23573.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> PORCH, R. O. H.—b. 1920; ed. Malvern and Trinity Coll., Oxford; cadet, Uga., 1941; dist. offr., 1943; Tang., 1951-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | cadet | Uganda | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1943 | dist. offr | Uganda *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1951–1961 | dist. offr | Tanganyika | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Porch, R. O. H___Uganda___1949`

- Staff-list name: **Porch, R. O. H** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. O. H. Porch | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | R. O. H. Porch | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `porch_r-o-h_b1920` vs `Porch, R. O. H___Uganda___1949`

- [PASS] surname_gate: bio 'PORCH' vs stint 'Porch, R. O. H' (exact)
- [PASS] initials: bio ['R', 'O', 'H'] ~ stint ['R', 'O', 'H']
- [PASS] age_gate: stint starts 1949, birth 1920 (age 29)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 45 vs bar 60: 'dist. offr' ~ 'District Officers and Assistant District Officers'
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

