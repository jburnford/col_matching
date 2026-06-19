<!-- {"case_id": "case_lalor_peter_e1855", "bio_ids": ["lalor_peter_e1855", "lalor_peter_e1883"], "stint_ids": ["Lalor, P___Victoria___1878"]} -->
# Dossier case_lalor_peter_e1855

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['lalor_peter_e1855', 'lalor_peter_e1883'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Lalor, P___Victoria___1878'] have more than one claimant biography in this case.

## Biography `lalor_peter_e1855`

- Printed name: **LALOR, PETER**
- Birth year: not printed
- Terminal: retired 1887 — “retired, 1887”
- Appears in editions: [1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L34111.v` — printed in editions [1889, 1890]:**

> LALOR, PETER.—Member, old leg. coun., Victoria, Nov., 1855; member, leg. assembly, Oct., 1856; chairman of committees, Dec., 1859; commiss. trade and customs, and P.M.G., 7th Aug. to 20th Oct., 1865; commiss., trade and customs, May, 1877, to Mar., 1880, and P.M.G., May to July, 1877; elected speaker, leg. assembly, July, 1880; retired, 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855 | Member, old leg. coun. | Victoria | [1889, 1890] |
| 1 | 1856 | member, leg. assembly | — | [1889, 1890] |
| 2 | 1859 | chairman of committees | — | [1889, 1890] |
| 3 | 1865–1865 | commiss. trade and customs, and P.M.G. | — | [1889, 1890] |
| 4 | 1877–1880 | commiss., trade and customs, and P.M.G. | — | [1889, 1890] |
| 5 | 1880 | elected speaker, leg. assembly | — | [1889, 1890] |

## Biography `lalor_peter_e1883`

- Printed name: **LALOR, Peter**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34376.v` — printed in editions [1886]:**

> LALOR, Hon. Peter.—Speaker of the legislative assembly, Victoria, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Speaker of the legislative assembly | Victoria | [1886] |

## Candidate stint `Lalor, P___Victoria___1878`

- Staff-list name: **Lalor, P** | colony: **Victoria** | listed 1878–1880 | editions [1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | P. Lalor | Commissioner | Commissioner of Trade and Customs Division | — | — |
| 1879 | P. Lalor | Commissioner | Commissioner of Trade and Customs Division | — | — |
| 1880 | P. Lalor | Commissioner | Commissioner of Trade and Customs Division | — | — |

### Deterministic checks: `lalor_peter_e1855` vs `Lalor, P___Victoria___1878`

- [PASS] surname_gate: bio 'LALOR' vs stint 'Lalor, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `lalor_peter_e1883` vs `Lalor, P___Victoria___1878`

- [PASS] surname_gate: bio 'LALOR' vs stint 'Lalor, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

