<!-- {"case_id": "calib_gemini_jamaica_0153", "bio_ids": ["newton_edward_e1859"], "stint_ids": ["Newton, Edward___Jamaica___1878"]} -->
# Dossier calib_gemini_jamaica_0153

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 70 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['newton_edward_e1859'] carry a single initial only — the namesake trap applies.

## Biography `newton_edward_e1859`

- Printed name: **NEWTON, EDWARD**
- Birth year: not printed
- Honours: C.M.G (1875), K.C.M.G (1887)
- Terminal: retired 1883 — “retired, 1883.”
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1883-L28853.v` — printed in editions [1883, 1886]:**

> NEWTON, EDWARD, C.M.G. (1875).—Assistant colonial secretary of Mauritius, May, 1859; acting auditor-general, September, 1863; auditor-general, April, 1866; colonial secretary, 1868; has on several occasions administered the government of Mauritius; lieutenant-governor and colonial secretary, Jamaica, Nov., 1877; retired, 1883.

**Version `col1888-L35133.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897]:**

> NEWTON, SIR EDWARD, K.C.M.G. (1887), C.M.G. (1875).—Assistant colonial secretary of Mauritius, May, 1859; acting auditor-general, Sept., 1863; auditor-general, April, 1866; colonial secretary, 1868; lieutenant-governor and colonial secretary, Jamaica, Nov., 1877; on several occasions administered the governments of Mauritius and Jamaica; retired, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1859 | Assistant colonial secretary of Mauritius | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 1 | 1863 | acting auditor-general | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 2 | 1866 | auditor-general | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 3 | 1868 | colonial secretary | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 4 | 1877 | lieutenant-governor and colonial secretary | Jamaica | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |

## Candidate stint `Newton, Edward___Jamaica___1878`

- Staff-list name: **Newton, Edward** | colony: **Jamaica** | listed 1878–1886 | editions [1878, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | Edward Newton | Colonial Secretary | Colonial Secretary's Office | C.M.G. | — |
| 1880 | Edward Newton | Lieutenant-Governor | Civil Establishment | C.M.G. | — |
| 1880 | Edward Newton | Colonial Secretary | Colonial Secretary's Office | C.M.G. | — |
| 1883 | Edward Newton | Lieutenant-Governor | Civil Establishment | C.M.G. | — |
| 1883 | Edward Newton | Colonial Secretary | Colonial Secretary's Office | C.M.G. | — |
| 1886 | E. Newton | Lieut.-Governor | — | C.M.G. | — |

### Deterministic checks: `newton_edward_e1859` vs `Newton, Edward___Jamaica___1878`

- [PASS] surname_gate: bio 'NEWTON' vs stint 'Newton, Edward' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1886
- [PASS] position_sim: best 100 vs bar 60: 'lieutenant-governor and colonial secretary' ~ 'Lieutenant-Governor'
- [PASS] honour: shared: C.M.G
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1883] pos~100 (bar: >=2)
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

