<!-- {"case_id": "case_khalifa_a-h_b1912", "bio_ids": ["khalifa_a-h_b1912"], "stint_ids": ["Khalifa, A. H___Aden___1964"]} -->
# Dossier case_khalifa_a-h_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `khalifa_a-h_b1912`

- Printed name: **KHALIFA, A. H**
- Birth year: 1912 (attested in editions [1966])
- Honours: M.B.E (1960)
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L15905.v` — printed in editions [1966]:**

> KHALIFA, A. H., M.B.E. (1960).—b. 1912; mosquito o'seer, Aden, 1930; market o'seer, 1935; hd., clk. and asst. acctnt., 1941; office supt., Sheikh Othman Township, 1947; exec. offr., 1956; asst. sec., 1960; senr. admin. offr., 1962; admin. offr., cl. III, 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | mosquito o'seer | Aden | [1966] |
| 1 | 1935 | market o'seer | Aden *(inherited from previous clause)* | [1966] |
| 2 | 1941 | hd., clk. and asst. acctnt | Aden *(inherited from previous clause)* | [1966] |
| 3 | 1947 | office supt., Sheikh Othman Township | Aden *(inherited from previous clause)* | [1966] |
| 4 | 1956 | exec. offr | Aden *(inherited from previous clause)* | [1966] |
| 5 | 1960 | asst. sec | Aden *(inherited from previous clause)* | [1966] |
| 6 | 1962 | senr. admin. offr | Aden *(inherited from previous clause)* | [1966] |
| 7 | 1963 | admin. offr., cl. III | Aden *(inherited from previous clause)* | [1966] |

## Candidate stint `Khalifa, A. H___Aden___1964`

- Staff-list name: **Khalifa, A. H** | colony: **Aden** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | A. H. Khalifa | Administrative Officers (Superscale) | CIVIL ESTABLISHMENT | — | — |
| 1965 | A. H. Khalifa | Administrative Officers (Superscale) | Civil Establishment | — | — |
| 1966 | A. H. Khalifa | Secretary for Lands and Housing | Civil Establishment | — | — |

### Deterministic checks: `khalifa_a-h_b1912` vs `Khalifa, A. H___Aden___1964`

- [PASS] surname_gate: bio 'KHALIFA' vs stint 'Khalifa, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1964, birth 1912 (age 52)
- [PASS] colony: 8 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1964-1966
- [FAIL] position_sim: best 57 vs bar 60: 'senr. admin. offr' ~ 'Administrative Officers (Superscale)'
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

