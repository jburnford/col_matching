<!-- {"case_id": "case_festing_francis-worgan_e1873", "bio_ids": ["festing_francis-worgan_e1873", "fiesting_francis-worgan_e1850"], "stint_ids": ["Festing, Francis___Gold Coast___1921"]} -->
# Dossier case_festing_francis-worgan_e1873

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Festing, Francis___Gold Coast___1921'] have more than one claimant biography in this case.

## Biography `festing_francis-worgan_e1873`

- Printed name: **FESTING, FRANCIS WORGAN**
- Birth year: not printed
- Honours: C.B., K.C.M.G. (1874)
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27425.v` — printed in editions [1883]:**

> FESTING, COLONEL SIR FRANCIS WORGAN, R.M.A., K.C.M.G. (1874), C.B., held a dormant commission to administer the government of the Gold Coast whilst commanding the regular troops during the earlier stages of the Ashanti war, and was of the executive council; commanded at the repulse of the attack by the Ashantis on Elmina, June, 1873; took a distinguished part in the subsequent operations under Sir G. Wolseley Aide-de-Camp to the Queen, 15th July, 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1873–1873 | — | Elmina | [1883] |
| 1 | 1879–1879 | Aide-de-Camp to the Queen | — | [1883] |

## Biography `fiesting_francis-worgan_e1850`

- Printed name: **FIESTING, FRANCIS WORGAN**
- Birth year: not printed
- Honours: C.B., K.C.M.G. (1874)
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33347.v` — printed in editions [1886]:**

> FIESTING, COLONEL SIR FRANCIS WORGAN, R.M.A., K.C.M.G. (1874), C.B., entered the royal marine artillery 1850; served with distinction in the Crimea and in China, held a dormant commission to administer the government of the Gold Coast whilst commanding the regular troops during the earlier stages of the Ashanti war; commanded at the repulse of the attack by the Ashantis on Elmina, June, 1873; took a distinguished part in the subsequent operations under Sir G. Wolseley; major of royal marine artillery, Feb., 1878; Aide-de-Camp to the Queen, 15th July, 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1850 | royal marine artillery | — | [1886] |
| 1 | 1873–1873 | commanded at the repulse of the attack by the Ashantis | Elmina | [1886] |
| 2 | 1878–1878 | major of royal marine artillery | — | [1886] |
| 3 | 1879–1879 | Aide-de-Camp to the Queen | — | [1886] |

## Candidate stint `Festing, Francis___Gold Coast___1921`

- Staff-list name: **Festing, Francis** | colony: **Gold Coast** | listed 1921–1925 | editions [1921, 1922, 1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | Francis Festing | Colonel | — | — | Colonel |
| 1922 | Colonel Francis Festing | Colonel | Ashanti | — | Colonel |
| 1923 | Francis Festing | — | — | — | — |
| 1925 | Francis Festing | — | — | — | Colonel |

### Deterministic checks: `festing_francis-worgan_e1873` vs `Festing, Francis___Gold Coast___1921`

- [PASS] surname_gate: bio 'FESTING' vs stint 'Festing, Francis' (exact)
- [PASS] initials: bio ['F', 'W'] ~ stint ['F']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1925
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `fiesting_francis-worgan_e1850` vs `Festing, Francis___Gold Coast___1921`

- [PASS] surname_gate: bio 'FIESTING' vs stint 'Festing, Francis' (fuzzy:1)
- [PASS] initials: bio ['F', 'W'] ~ stint ['F']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1925
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

