<!-- {"case_id": "case_stockenstrom_audrey_e1895", "bio_ids": ["stockenstrom_audrey_e1895"], "stint_ids": ["Stockenstrom, A___Cape of Good Hope___1878", "Stockenstrom, A___Cape of Good Hope___1906"]} -->
# Dossier case_stockenstrom_audrey_e1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['stockenstrom_audrey_e1895'] carry a single initial only — the namesake trap applies.

## Biography `stockenstrom_audrey_e1895`

- Printed name: **STOCKENSTROM, AUDREY**
- Birth year: not printed
- Honours: B.A
- Appears in editions: [1922]

### Verbatim printed entry text (OCR)

**Version `col1922-L56359.v` — printed in editions [1922]:**

> STOCKENSTROM, SIR AUDREY, B.A., B.A. (Cantab.)—Barrister-at-law, Middle Temple; sec. law dept., S. African Repub., 1895; chmn. criminal divn., atty.-gen.'s dept., S.A. Repub., 1898; chmn. of comteces., leg. assem., Transvaal, 1907-10; chmn., pub. serv. comsn., 1912; asst. chmn. of comteces., Union H. of A., 1916; rly. and harbour comsnr., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | sec. law dept., S. African Repub | — | [1922] |
| 1 | 1898 | chmn. criminal divn., atty.-gen.'s dept., S.A. Repub | — | [1922] |
| 2 | 1907–1910 | chmn. of comteces., leg. assem. | Transvaal | [1922] |
| 3 | 1912 | chmn., pub. serv. comsn | Transvaal *(inherited from previous clause)* | [1922] |
| 4 | 1916 | asst. chmn. of comteces., Union H. of A | Transvaal *(inherited from previous clause)* | [1922] |
| 5 | 1920 | rly. and harbour comsnr | Transvaal *(inherited from previous clause)* | [1922] |

## Candidate stint `Stockenstrom, A___Cape of Good Hope___1878`

- Staff-list name: **Stockenstrom, A** | colony: **Cape of Good Hope** | listed 1878–1880 | editions [1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | Hon. A. Stockenstrom | Attorney-General | Attorney-General's Office | — | — |
| 1880 | A. Stockenstrom | 2nd Puisne Judge | Supreme Court | — | — |

### Deterministic checks: `stockenstrom_audrey_e1895` vs `Stockenstrom, A___Cape of Good Hope___1878`

- [PASS] surname_gate: bio 'STOCKENSTROM' vs stint 'Stockenstrom, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Stockenstrom, A___Cape of Good Hope___1906`

- Staff-list name: **Stockenstrom, A** | colony: **Cape of Good Hope** | listed 1906–1909 | editions [1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | A. Stockenstrom | Clerk to Judge Maasdorp | Supreme Court | — | — |
| 1907 | A. Stockenstrom | Clerk to Judge Maasdorp | Supreme Court | — | — |
| 1908 | A. Stockenstrom | Clerk to Judge Maasdorp | SUPREME COURT | — | — |
| 1909 | A. Stockenstrom | Clerk to Judge Maasdorp | Supreme Court | — | — |

### Deterministic checks: `stockenstrom_audrey_e1895` vs `Stockenstrom, A___Cape of Good Hope___1906`

- [PASS] surname_gate: bio 'STOCKENSTROM' vs stint 'Stockenstrom, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1909
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

