<!-- {"case_id": "case_whitington_peter_e1866", "bio_ids": ["whitington_peter_e1866"], "stint_ids": ["Whittington, P___South Australia___1888"]} -->
# Dossier case_whitington_peter_e1866

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['whitington_peter_e1866'] carry a single initial only — the namesake trap applies.
- Phase 1 found `whitington_peter_e1866` ↔ `Whittington, P___South Australia___1888` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Whittington, P___South Australia___1888` is also gate-compatible with biography(ies) outside this case: ['whittington_peter_e1873'] (already linked elsewhere or filtered).

## Biography `whitington_peter_e1866`

- Printed name: **WHITINGTON, PETER**
- Birth year: not printed
- Appears in editions: [1909, 1910, 1912]

### Verbatim printed entry text (OCR)

**Version `col1909-L50336.v` — printed in editions [1909, 1910, 1912]:**

> WHITINGTON, PETER.—Ck. to acctnt. in insolvency ct., and curator of intestate estates, Sept., 1866; 2nd clk., audit off., June, 1873; chief clk., audit off., June, 1875; sec. to audit dept., Dec., 1896; mem. of pub. ser. classification bd., S. Aust., Jan., 1901, to June, 1902; mem. of W. Aust. pub. ser. comsn., July, 1902, to Dec., 1903; ag. comsnr. of audit, S. Aust., May, 1907; comsnr. of audit, Nov., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Ck. to acctnt. in insolvency ct., and curator of intestate estates | — | [1909, 1910, 1912] |
| 1 | 1873 | 2nd clk., audit off. | — | [1909, 1910, 1912] |
| 2 | 1875 | chief clk., audit off. | — | [1909, 1910, 1912] |
| 3 | 1896 | sec. to audit dept. | — | [1909, 1910, 1912] |
| 4 | 1901–1902 | mem. of pub. ser. classification bd. | South Australia | [1909, 1910, 1912] |
| 5 | 1902–1903 | mem. of W. Aust. pub. ser. comsn. | Western Australia | [1909, 1910, 1912] |
| 6 | 1907 | ag. comsnr. of audit | South Australia | [1909, 1910, 1912] |

## Candidate stint `Whittington, P___South Australia___1888`

- Staff-list name: **Whittington, P** | colony: **South Australia** | listed 1888–1909 | editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | P. Whittington | Chief Clerk and Accountant | Audit Department | — | — |
| 1889 | P Whittington | Chief Clerk and Accountant | Audit Department | — | — |
| 1890 | P Whittington | Chief Clerk and Accountant | Audit Department | — | — |
| 1894 | P. Whittington | Chief Clerk and Accountant | Audit Department | — | — |
| 1896 | P. Whittington | Chief Clerk and Accountant | Audit Department | — | — |
| 1897 | P. Whittington | Chief Clerk and Accountant | Audit Department | — | — |
| 1898 | P. Whittington | Secretary | Audit Department | — | — |
| 1900 | P. Whittington | Secretary | Audit Department | — | — |
| 1905 | P. Whittington | Secretary | Audit Department | — | — |
| 1906 | P. Whittington | Secretary | Audit Department | — | — |
| 1907 | P. Whittington | Secretary | Audit Department | — | — |
| 1908 | P. Whittington | Commissioner of Audit (acting) | Audit Department | — | — |
| 1909 | P. Whittington | Commissioner of Audit | Audit Department | — | — |

### Deterministic checks: `whitington_peter_e1866` vs `Whittington, P___South Australia___1888`

- [PASS] surname_gate: bio 'WHITINGTON' vs stint 'Whittington, P' (fuzzy:1)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1888-1909
- [PASS] position_sim: best 78 vs bar 60: 'ag. comsnr. of audit' ~ 'Commissioner of Audit (acting)'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1909] pos~77 (bar: >=2)
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

