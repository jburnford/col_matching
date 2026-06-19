<!-- {"case_id": "case_haebens_w-j_e1864", "bio_ids": ["haebens_w-j_e1864"], "stint_ids": ["Habens, William J___New Zealand___1880"]} -->
# Dossier case_haebens_w-j_e1864

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `haebens_w-j_e1864` ↔ `Habens, William J___New Zealand___1880` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Habens, William J___New Zealand___1880` is also gate-compatible with biography(ies) outside this case: ['habens_w-j_e1864'] (already linked elsewhere or filtered).

## Biography `haebens_w-j_e1864`

- Printed name: **HAEBENS, W. J.**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L31907.v` — printed in editions [1894]:**

> HAEBENS, REV. W. J., B.A. (Lond., 1862).—Minister, Congregational church, New Zealand 1864-78; secretary, board of education, Christchurch, Jan., 1877, to May, 1878; inspector-general of schools, 1878; member (and secretary) of Royal Commission to inquire into the operations of New Zealand University and its relation to the secondary schools, 1879-80; fellow New Zealand Univ., 1889; sec. and inspr.-gen. edn. dept., Wellington, 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864–1878 | Minister, Congregational church | New Zealand | [1894] |
| 1 | 1877–1878 | secretary, board of education | Christchurch | [1894] |
| 2 | 1878–1878 | inspector-general of schools | — | [1894] |
| 3 | 1879–1880 | member (and secretary) of Royal Commission to inquire into the operations of New Zealand University and its relation to the secondary schools | New Zealand | [1894] |
| 4 | 1888–1888 | sec. and inspr.-gen. edn. dept. | Wellington | [1894] |
| 5 | 1889–1889 | fellow | New Zealand | [1894] |

## Candidate stint `Habens, William J___New Zealand___1880`

- Staff-list name: **Habens, William J** | colony: **New Zealand** | listed 1880–1899 | editions [1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | W. J. Habens | Inspector-General | Education Office | — | — |
| 1883 | Rev. W. J. Habens | Inspector-General | Education Office | — | — |
| 1886 | Rev. W. J. Habens | Inspector-General | Education Office | — | — |
| 1888 | Rev. W. J. Habens | Secretary and Inspector-General | Education Office | — | — |
| 1889 | Rev. W. J. Habens | Secretary and Inspector-General | Education Office | — | — |
| 1890 | Rev. W. J. Habens | Secretary and Inspector-General | Education Office | — | — |
| 1894 | Rev. W. J. Habens | Secretary and Inspector-General | Education Office | — | — |
| 1896 | W. J. Habens | Secretary and Inspector-General | Education Office | — | — |
| 1897 | W. J. Habens | resident Secretary for Education and Inspector-General Schools | Education Office | — | — |
| 1898 | Rev. W. J. Habens | Secretary for Education and Inspector-General of Schools | Education Office | — | — |
| 1899 | Rev. W. J. Habens | Secretary for Education and Inspector-General of Schools | Education Office | — | — |

### Deterministic checks: `haebens_w-j_e1864` vs `Habens, William J___New Zealand___1880`

- [PASS] surname_gate: bio 'HAEBENS' vs stint 'Habens, William J' (fuzzy:1)
- [PASS] initials: bio ['W', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'New Zealand'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1880-1899
- [PASS] position_sim: best 61 vs bar 60: 'member (and secretary) of Royal Commission to inquire into the operations of New Zealand University and its relation to the secondary schools' ~ 'Secretary for Education and Inspector-General of Schools'
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

