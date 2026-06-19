<!-- {"case_id": "case_palliser_charles-frederick-wray_e1874", "bio_ids": ["palliser_charles-frederick-wray_e1874"], "stint_ids": ["Palliser, C. F. W___New Zealand___1914"]} -->
# Dossier case_palliser_charles-frederick-wray_e1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `palliser_charles-frederick-wray_e1874`

- Printed name: **PALLISER, CHARLES FREDERICK WRAY**
- Birth year: not printed
- Honours: C.M.G (1916)
- Appears in editions: [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1913-L48525.v` — printed in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]:**

> PALLISER, CHARLES FREDERICK WRAY, C.M.G. (1916).—Entered civ. serv., New Zealand, 1874; sec. to high comsnr. for N.Z. in London, 1909; ag. high comsnr., May to Aug., 1912; ret., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | Entered civ. serv. | New Zealand | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 1 | 1909 | sec. to high comsnr. for N.Z. in London | New Zealand *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 2 | 1912 | ag. high comsnr | New Zealand *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 3 | 1916 | ret | New Zealand *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |

## Candidate stint `Palliser, C. F. W___New Zealand___1914`

- Staff-list name: **Palliser, C. F. W** | colony: **New Zealand** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | C. F. W. Palliser | Secretary | High Commissioner's Office. | — | — |
| 1915 | C. F. W. Palliser | Secretary | High Commissioner's Office | — | — |

### Deterministic checks: `palliser_charles-frederick-wray_e1874` vs `Palliser, C. F. W___New Zealand___1914`

- [PASS] surname_gate: bio 'PALLISER' vs stint 'Palliser, C. F. W' (exact)
- [PASS] initials: bio ['C', 'F', 'W'] ~ stint ['C', 'F', 'W']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'New Zealand'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1914-1915
- [FAIL] position_sim: best 50 vs bar 60: 'ret' ~ 'Secretary'
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

