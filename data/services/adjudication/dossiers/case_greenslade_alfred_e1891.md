<!-- {"case_id": "case_greenslade_alfred_e1891", "bio_ids": ["greenslade_alfred_e1891"], "stint_ids": ["Greenslade, A___Natal___1905", "Greenslade, A___South Africa___1912"]} -->
# Dossier case_greenslade_alfred_e1891

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['greenslade_alfred_e1891'] carry a single initial only — the namesake trap applies.

## Biography `greenslade_alfred_e1891`

- Printed name: **GREENSLADE, ALFRED**
- Birth year: not printed
- Appears in editions: [1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1911-L45149.v` — printed in editions [1911, 1912, 1913]:**

> GREENSLADE, ALFRED.—Book-keeper, Natal govt. rly., Harrismith extension, 1st Feb., 1891; dist. acctnt., Newcastle, 1st Nov., 1891, to 15th July, 1892; chief book-keeper, stores dept., Charlestown-Johannesburg rly., May, 1894, to Apr., 1896; 3rd cls. clk., port captain's dept., 13th May, 1896; transf'd. to audit offr., 25th Oct., 1897; 2nd cls. clk., 1st Feb., 1898; 1st cls. clk., 1st July, 1900; asst. inspr., aud. dept., 1st July, 1901; inspr., 1st July, 1903.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | Book-keeper, Natal govt. rly., Harrismith extension | Natal | [1911, 1912, 1913] |
| 1 | 1891–1892 | dist. acctnt. | — | [1911, 1912, 1913] |
| 2 | 1894–1896 | chief book-keeper, stores dept., Charlestown-Johannesburg rly. | — | [1911, 1912, 1913] |
| 3 | 1896 | 3rd cls. clk., port captain's dept. | — | [1911, 1912, 1913] |
| 4 | 1897 | audit offr. | — | [1911, 1912, 1913] |
| 5 | 1898 | 2nd cls. clk. | — | [1911, 1912, 1913] |
| 6 | 1900 | 1st cls. clk. | — | [1911, 1912, 1913] |
| 7 | 1901 | asst. inspr., aud. dept. | — | [1911, 1912, 1913] |
| 8 | 1903 | inspr. | — | [1911, 1912, 1913] |

## Candidate stint `Greenslade, A___Natal___1905`

- Staff-list name: **Greenslade, A** | colony: **Natal** | listed 1905–1910 | editions [1905, 1906, 1907, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | A. Greenslade | Inspector | Audit Office | — | — |
| 1906 | A. Greenslade | Inspector | Audit Office | — | — |
| 1907 | A. Greenslade | Inspector | Audit Office | — | — |
| 1910 | A. Greenslade | Inspector | Audit Office | — | — |

### Deterministic checks: `greenslade_alfred_e1891` vs `Greenslade, A___Natal___1905`

- [PASS] surname_gate: bio 'GREENSLADE' vs stint 'Greenslade, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1910
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Greenslade, A___South Africa___1912`

- Staff-list name: **Greenslade, A** | colony: **South Africa** | listed 1912–1914 | editions [1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | A. Greenslade | Principal Clerk | Control and Audit Office | — | — |
| 1914 | A. Greenslade | Principal Clerk | Controller and Auditor-General's Department | — | — |

### Deterministic checks: `greenslade_alfred_e1891` vs `Greenslade, A___South Africa___1912`

- [PASS] surname_gate: bio 'GREENSLADE' vs stint 'Greenslade, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
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

