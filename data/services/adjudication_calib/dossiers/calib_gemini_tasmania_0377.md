<!-- {"case_id": "calib_gemini_tasmania_0377", "bio_ids": ["fletcher_geo-wm_e1851"], "stint_ids": ["Fletcher, G. W___Tasmania___1877"]} -->
# Dossier calib_gemini_tasmania_0377

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 95 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fletcher_geo-wm_e1851`

- Printed name: **FLETCHER, Geo. Wm**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1888-L33440.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]:**

> FLETCHER, Geo. Wm.—Temporarily employed in Imperial commissionariat, Hobart, 1851; clerk colonial treasury, Hobart, July, 1852; receiver and paymaster, Jan., 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1851 | Temporarily employed in Imperial commissionariat | Hobart | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 1 | 1852 | clerk colonial treasury | Hobart | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 2 | 1886 | receiver and paymaster | — | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |

## Candidate stint `Fletcher, G. W___Tasmania___1877`

- Staff-list name: **Fletcher, G. W** | colony: **Tasmania** | listed 1877–1894 | editions [1877, 1878, 1879, 1880, 1888, 1889, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. W. Fletcher | Clerk | Treasury | — | — |
| 1878 | G. W. Fletcher | Clerks | Treasury | — | — |
| 1879 | G. W. Fletcher | Clerks | Treasury | — | — |
| 1880 | G. W. Fletcher | Clerk | Treasury | — | — |
| 1888 | G. W. Fletcher | Receiver and Paymaster | Treasury | — | — |
| 1889 | G. W. Fletcher | Receiver and Paymaster | Treasury | — | — |
| 1894 | G. W. Fletcher | Receiver and Paymaster | Treasury | — | — |

### Deterministic checks: `fletcher_geo-wm_e1851` vs `Fletcher, G. W___Tasmania___1877`

- [PASS] surname_gate: bio 'FLETCHER' vs stint 'Fletcher, G. W' (exact)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G', 'W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Tasmania'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1894
- [PASS] position_sim: best 100 vs bar 60: 'clerk colonial treasury' ~ 'Clerk'
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

