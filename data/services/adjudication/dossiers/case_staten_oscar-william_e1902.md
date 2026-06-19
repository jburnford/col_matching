<!-- {"case_id": "case_staten_oscar-william_e1902", "bio_ids": ["staten_oscar-william_e1902"], "stint_ids": ["Staten, O. W___Transvaal___1906"]} -->
# Dossier case_staten_oscar-william_e1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `staten_oscar-william_e1902`

- Printed name: **STATEN, OSCAR WILLIAM**
- Birth year: not printed
- Appears in editions: [1924, 1925, 1927, 1928, 1929, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1924-L58094.v` — printed in editions [1924, 1925, 1927, 1928, 1929, 1930, 1931]:**

> STATEN, OSCAR WILLIAM—Asst. res. mag., Heidelberg, Transvaal, 1902; ag. res. mag. and res. mag., Barberton, 1902-11; ag. res. mag., Heidelberg, 1911-16; inspgr. mag., 1916-21; ch. pub. serv. inspr., 1921; sec., pub. wks., Jan., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | Asst. res. mag., Heidelberg | Transvaal | [1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 1 | 1911–1916 | ag. res. mag., Heidelberg | Transvaal *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 2 | 1916–1921 | inspgr. mag | Transvaal *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 3 | 1921 | ch. pub. serv. inspr | Transvaal *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 4 | 1925 | sec., pub. wks | Transvaal *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931] |

## Candidate stint `Staten, O. W___Transvaal___1906`

- Staff-list name: **Staten, O. W** | colony: **Transvaal** | listed 1906–1907 | editions [1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | O. W. Staten (acting) | Magistrate | Magistrates | — | — |
| 1907 | O. W. Staten | Magistrate | Magistrates | — | — |

### Deterministic checks: `staten_oscar-william_e1902` vs `Staten, O. W___Transvaal___1906`

- [PASS] surname_gate: bio 'STATEN' vs stint 'Staten, O. W' (exact)
- [PASS] initials: bio ['O', 'W'] ~ stint ['O', 'W']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Transvaal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1906-1907
- [FAIL] position_sim: best 36 vs bar 60: 'Asst. res. mag., Heidelberg' ~ 'Magistrate'
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

