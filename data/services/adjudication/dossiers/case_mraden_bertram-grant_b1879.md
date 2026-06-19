<!-- {"case_id": "case_mraden_bertram-grant_b1879", "bio_ids": ["mraden_bertram-grant_b1879"], "stint_ids": ["Meaden, B. G___Ceylon___1907"]} -->
# Dossier case_mraden_bertram-grant_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `mraden_bertram-grant_b1879` ↔ `Meaden, B. G___Ceylon___1907` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Meaden, B. G___Ceylon___1907` is also gate-compatible with biography(ies) outside this case: ['meaden_berteam-grant_b1879'] (already linked elsewhere or filtered).

## Biography `mraden_bertram-grant_b1879`

- Printed name: **MRADEN, BERTRAM GRANT**
- Birth year: 1879 (attested in editions [1933])
- Honours: M.I.C.R
- Appears in editions: [1933]

### Verbatim printed entry text (OCR)

**Version `col1933-L62028.v` — printed in editions [1933]:**

> MRADEN, BERTRAM GRANT, M.I.C.R.—B. 1879; irrig. engnr., Ceylon, Sept., 1905; dep. dir., irrig., Nov., 1928; ag. dir., irrig., Oct., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1905 | irrig. engnr. | Ceylon | [1933] |
| 1 | 1928 | dep. dir., irrig | Ceylon *(inherited from previous clause)* | [1933] |
| 2 | 1931 | ag. dir., irrig | Ceylon *(inherited from previous clause)* | [1933] |

## Candidate stint `Meaden, B. G___Ceylon___1907`

- Staff-list name: **Meaden, B. G** | colony: **Ceylon** | listed 1907–1934 | editions [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922, 1923, 1925, 1928, 1929, 1931, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | B. G. Meaden | Temporarily Engaged | Irrigation Department | — | — |
| 1908 | B. G. Meaden | Irrigation Engineer (Temporary) | Irrigation Department | — | — |
| 1909 | B. G. Meaden | Irrigation Engineer | Irrigation Department | — | — |
| 1910 | B. G. Meaden | Irrigation Engineer | Irrigation Department | — | — |
| 1911 | B. G. Meaden | Irrigation Engineer, Permanent Staff | Irrigation Department | — | — |
| 1912 | B. G. Meaden | Irrigation Engineer, Permanent Staff | Irrigation Department | — | — |
| 1913 | B. G. Meaden | Irrigation Engineer | Irrigation Department | — | — |
| 1914 | B. G. Meaden | Irrigation Engineer (Permanent) | Irrigation Department | — | — |
| 1915 | B. G. Meaden | Divisional Irrigation Engineer | Irrigation Department | — | — |
| 1917 | B. G. Meaden | Divisional Irrigation Engineer | Irrigation Department | — | — |
| 1918 | B. G. Meaden | Divisional Irrigation Engineer | Irrigation Department | — | — |
| 1920 | B. G. Meaden | Divisional Irrigation Engineer | Irrigation Department | — | — |
| 1921 | B. G. Meaden | Divisional Irrigation Engineer | Irrigation Department | — | — |
| 1922 | B. G. Meaden | Divisional Irrigation Engineer | Irrigation Department | — | — |
| 1923 | B. G. Meaden | Divisional Irrigation Engineer | Irrigation Department | — | — |
| 1925 | B. G. Meaden | Divisional Irrigation Engineer | Irrigation Department | — | — |
| 1928 | B. G. Meaden | Divisional Irrigation Engineer | Irrigation Department | — | — |
| 1929 | B. G. Meaden | Divisional Irrigation Engineer | Irrigation Department | — | — |
| 1931 | B. G. Meaden | Deputy Director of Irrigation | Irrigation Department | — | — |
| 1934 | B. G. Meaden | Director of Irrigation | Irrigation Department | — | — |

### Deterministic checks: `mraden_bertram-grant_b1879` vs `Meaden, B. G___Ceylon___1907`

- [PASS] surname_gate: bio 'MRADEN' vs stint 'Meaden, B. G' (fuzzy:1)
- [PASS] initials: bio ['B', 'G'] ~ stint ['B', 'G']
- [PASS] age_gate: stint starts 1907, birth 1879 (age 28)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1907-1934
- [PASS] position_sim: best 73 vs bar 60: 'irrig. engnr.' ~ 'Irrigation Engineer'
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

