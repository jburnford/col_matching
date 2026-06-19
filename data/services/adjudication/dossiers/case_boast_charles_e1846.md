<!-- {"case_id": "case_boast_charles_e1846", "bio_ids": ["boast_charles_e1846"], "stint_ids": ["Boast, C. B___Natal___1896"]} -->
# Dossier case_boast_charles_e1846

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['boast_charles_e1846'] carry a single initial only — the namesake trap applies.

## Biography `boast_charles_e1846`

- Printed name: **BOAST, Charles**
- Birth year: not printed
- Appears in editions: [1888, 1890, 1894, 1896, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1890-L32710.v` — printed in editions [1890, 1894, 1896, 1898, 1899, 1900]:**

> BOAST, Charles.—Cik. to R.M., Newcastle, Natal, Mar., 1866; sub-accntnt., June, 1875; admnstr. of native law, Ulundi, May, 1878; ditto, Pagadi's loen., Sept., 1882; R.M., Ipolela div., Mar., 1889; R.M., Impendhle, 1894.

**Version `col1888-L32188.v` — printed in editions [1888]:**

> BOAST, CHARLES.—Clerk to R.M., Newcastle, Natal, Mar., 1846; sub-accountant, June, 1875; administrator of native law, Pagadi's location, Mar., 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1846 | Clerk to R.M., Newcastle | Natal | [1888] |
| 1 | 1866 | Cik. to R.M., Newcastle | Natal | [1890, 1894, 1896, 1898, 1899, 1900] |
| 2 | 1875 | sub-accntnt | Natal *(inherited from previous clause)* | [1888, 1890, 1894, 1896, 1898, 1899, 1900] |
| 3 | 1878 | admnstr. of native law, Ulundi | Natal *(inherited from previous clause)* | [1888, 1890, 1894, 1896, 1898, 1899, 1900] |
| 4 | 1882 | ditto, Pagadi's loen | Natal *(inherited from previous clause)* | [1890, 1894, 1896, 1898, 1899, 1900] |
| 5 | 1889 | R.M., Ipolela div | Natal *(inherited from previous clause)* | [1890, 1894, 1896, 1898, 1899, 1900] |
| 6 | 1894 | R.M., Impendhle | Natal *(inherited from previous clause)* | [1890, 1894, 1896, 1898, 1899, 1900] |

## Candidate stint `Boast, C. B___Natal___1896`

- Staff-list name: **Boast, C. B** | colony: **Natal** | listed 1896–1900 | editions [1896, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | C. B. Boast | Magistrate | Magistrates | — | — |
| 1899 | C. B. Boast | Magistrate | Magistrates | — | — |
| 1900 | C. B. Boast | Magistrate | Magistrates | — | — |

### Deterministic checks: `boast_charles_e1846` vs `Boast, C. B___Natal___1896`

- [PASS] surname_gate: bio 'BOAST' vs stint 'Boast, C. B' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C', 'B']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 7 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1896-1900
- [FAIL] position_sim: best 18 vs bar 60: 'R.M., Impendhle' ~ 'Magistrate'
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

