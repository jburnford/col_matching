<!-- {"case_id": "case_naudi_alfredo_e1878", "bio_ids": ["naudi_alfredo_e1878"], "stint_ids": ["Naudi, A___Leeward Islands___1897", "Naudi, A___Malta___1896"]} -->
# Dossier case_naudi_alfredo_e1878

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['naudi_alfredo_e1878'] carry a single initial only — the namesake trap applies.

## Biography `naudi_alfredo_e1878`

- Printed name: **NAUDI, ALFREDO**
- Birth year: not printed
- Honours: C.M.G (1901), LL.D (1877)
- Appears in editions: [1896, 1897, 1898, 1899, 1900, 1905]

### Verbatim printed entry text (OCR)

**Version `col1896-L40511.v` — printed in editions [1896, 1897, 1898, 1899, 1900, 1905]:**

> NAUDI, ALFREDO, C.M.G. (1901), LL.D. (1877).—Received at the bar, Malta, 1878; elected mem. coun. of govt., 1889; prof. of law, Malta Univ., 1892; crown advoc. and govt. legal adviser, with seat in exec. coun. and council of govt., 1895.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Received at the bar | Malta | [1896, 1897, 1898, 1899, 1900, 1905] |
| 1 | 1889 | elected mem. coun. of govt | Malta *(inherited from previous clause)* | [1896, 1897, 1898, 1899, 1900, 1905] |
| 2 | 1892 | prof. of law, Malta Univ | Malta | [1896, 1897, 1898, 1899, 1900, 1905] |
| 3 | 1895 | crown advoc. and govt. legal adviser, with seat in exec. coun. and council of govt | Malta *(inherited from previous clause)* | [1896, 1897, 1898, 1899, 1900, 1905] |

## Candidate stint `Naudi, A___Leeward Islands___1897`

- Staff-list name: **Naudi, A** | colony: **Leeward Islands** | listed 1897–1900 | editions [1897, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | A. Naudi | Crown Advocate | Council of Government | — | — |
| 1897 | A. Naudi | Crown Advocate | Crown Lawyers | — | — |
| 1899 | A. Naudi | Crown Advocate | Executive Council | — | — |
| 1899 | A. Naudi | Crown Advocate | Crown Lawyers | — | — |
| 1899 | A. Naudi | Crown Advocate | Council of Government | — | — |
| 1900 | A. Naudi | Crown Advocate | Crown Lawyers | — | — |
| 1900 | A. Naudi | Crown Advocate | Council of Government | — | — |
| 1900 | A. Naudi | Crown Advocate | Executive Council | — | — |

### Deterministic checks: `naudi_alfredo_e1878` vs `Naudi, A___Leeward Islands___1897`

- [PASS] surname_gate: bio 'NAUDI' vs stint 'Naudi, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Naudi, A___Malta___1896`

- Staff-list name: **Naudi, A** | colony: **Malta** | listed 1896–1905 | editions [1896, 1898, 1899, 1905]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | A. Naudi | Crown Advocate | Crown Lawyers | — | — |
| 1896 | A. Naudi | Judge of the Civil Court, First Hall | Judicial Establishment | — | — |
| 1898 | A. Naudi | Crown Advocate | Crown Lawyers | — | — |
| 1899 | A. Naudi | Crown Advocate | Crown Lawyers | — | — |
| 1905 | A. Naudi | Crown Advocate | Crown Lawyers | — | — |

### Deterministic checks: `naudi_alfredo_e1878` vs `Naudi, A___Malta___1896`

- [PASS] surname_gate: bio 'NAUDI' vs stint 'Naudi, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1896-1905
- [FAIL] position_sim: best 53 vs bar 60: 'crown advoc. and govt. legal adviser, with seat in exec. coun. and council of govt' ~ 'Crown Advocate'
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

