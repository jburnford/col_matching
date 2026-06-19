<!-- {"case_id": "case_easton_frank_e1880", "bio_ids": ["easton_frank_e1880"], "stint_ids": ["Easton, F___South Africa___1914"]} -->
# Dossier case_easton_frank_e1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['easton_frank_e1880'] carry a single initial only — the namesake trap applies.

## Biography `easton_frank_e1880`

- Printed name: **EASTON, FRANK**
- Birth year: not printed
- Appears in editions: [1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1920-L53229.v` — printed in editions [1920, 1921]:**

> EASTON, FRANK.—Clk., post office, Exeter, Oct., 1880; transf'd. to Natal civ. ser., Feb., 1889; supt. post office, Durban, 1898; P.M.G.'s office, Pietermaritzburg, 1902; prin. clk., 1905; prin. clk., dept. of posts and telegraphs, Union of S. Africa, 1910; chief clk., 1912; ag. asst. under-sec., 20th Sept., 1914, to 9th May, 1918, and from 21st June to 17th Dec., 1919; asst. under-sec., 18th Dec., 1919; ag. under sec., 13th Aug., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Clk., post office | — | [1920, 1921] |
| 1 | 1889 | — | Natal | [1920, 1921] |
| 2 | 1898 | supt. post office | — | [1920, 1921] |
| 3 | 1902 | — | — | [1920, 1921] |
| 4 | 1905 | prin. clk. | — | [1920, 1921] |
| 5 | 1910 | prin. clk. | Union of South Africa | [1920, 1921] |
| 6 | 1912 | chief clk. | — | [1920, 1921] |
| 7 | 1914–1919 | ag. asst. under-sec. | — | [1920, 1921] |
| 8 | 1919 | asst. under-sec. | — | [1920, 1921] |
| 9 | 1920 | ag. under sec. | — | [1920, 1921] |

## Candidate stint `Easton, F___South Africa___1914`

- Staff-list name: **Easton, F** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | F. Easton | Chief Clerk | Department of Posts and Telegraphs | — | — |
| 1918 | F. Easton | Chief Clerk | Posts and Telegraphs | — | — |

### Deterministic checks: `easton_frank_e1880` vs `Easton, F___South Africa___1914`

- [PASS] surname_gate: bio 'EASTON' vs stint 'Easton, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

