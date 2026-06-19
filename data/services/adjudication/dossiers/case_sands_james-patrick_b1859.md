<!-- {"case_id": "case_sands_james-patrick_b1859", "bio_ids": ["sands_james-patrick_b1859"], "stint_ids": ["Sands, J.P___Bahamas___1899"]} -->
# Dossier case_sands_james-patrick_b1859

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sands_james-patrick_b1859`

- Printed name: **SANDS, JAMES PATRICK**
- Birth year: 1859 (attested in editions [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925])
- Honours: KT. BACH (1917)
- Appears in editions: [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1918-L53929.v` — printed in editions [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]:**

> SANDS, SIR JAMES PATRICK, KT. BACH. (1917).—B. 1859; mem. H. of A., Bahamas, 1889-1916; and leader for the gov't., 1909-1916; M.E.C. since 1901; pres. of leg. coun., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889–1916 | mem. H. of A. | Bahamas | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 1 | 1901 | M.E.C. since | Bahamas *(inherited from previous clause)* | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 2 | 1909–1916 | and leader for the gov't | Bahamas *(inherited from previous clause)* | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 3 | 1916 | pres. of leg. coun | Bahamas *(inherited from previous clause)* | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |

## Candidate stint `Sands, J.P___Bahamas___1899`

- Staff-list name: **Sands, J.P** | colony: **Bahamas** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | J. P. Sands | Member | House of Assembly | — | — |
| 1900 | J.P. Sands | — | — | — | — |

### Deterministic checks: `sands_james-patrick_b1859` vs `Sands, J.P___Bahamas___1899`

- [PASS] surname_gate: bio 'SANDS' vs stint 'Sands, J.P' (exact)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J', 'P']
- [PASS] age_gate: stint starts 1899, birth 1859 (age 40)
- [PASS] colony: 4 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1899-1900
- [FAIL] position_sim: best 40 vs bar 60: 'M.E.C. since' ~ 'Member'
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

