<!-- {"case_id": "case_wagner_william-quinn_b1849", "bio_ids": ["wagner_william-quinn_b1849"], "stint_ids": ["Wagner, Wilhelm___Hong Kong___1928", "Wagner, William Q___South Africa___1912"]} -->
# Dossier case_wagner_william-quinn_b1849

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wagner_william-quinn_b1849`

- Printed name: **WAGNER, WILLIAM QUINN**
- Birth year: 1849 (attested in editions [1909, 1910, 1911, 1912, 1913, 1914, 1915])
- Appears in editions: [1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1909-L50196.v` — printed in editions [1909, 1910, 1911, 1912, 1913, 1914, 1915]:**

> WAGNER, WILLIAM QUINN.—B. 1849; ed. at S. African Coll., Cape Town; sec. to the Krijgaarad under pres. Burgess, in the first Secocoeni war, 1876; filled various ag. appts. in Landdrost's off., Rustenburg, subsequently becoming postmaster and town clk. of that place; served in various capacities under O.F.S. govt., 1881 to 1900; mine inspr., Jagersfonteine, 1891 to 1900; supt., refugee camp, Heilbron, O.R.C., May, 1901, to Mar., 1902; joined mines dept., Transvaal, May, 1902.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876–1876 | sec. to the Krijgaarad under pres. Burgess | — | [1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 1 | 1881–1900 | served in various capacities | Orange Free State | [1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 2 | 1891–1900 | mine inspr. | — | [1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 3 | 1901–1902 | supt., refugee camp | Orange River Colony | [1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 4 | 1902 | joined mines dept. | Transvaal | [1909, 1910, 1911, 1912, 1913, 1914, 1915] |

## Candidate stint `Wagner, Wilhelm___Hong Kong___1928`

- Staff-list name: **Wagner, Wilhelm** | colony: **Hong Kong** | listed 1928–1930 | editions [1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | Wilhelm Wagner | Consul | Consuls | — | — |
| 1929 | Wilhelm Wagner | Consul | Consuls | — | — |
| 1930 | Wilhelm Wagner | Consul | Consuls | — | — |

### Deterministic checks: `wagner_william-quinn_b1849` vs `Wagner, Wilhelm___Hong Kong___1928`

- [PASS] surname_gate: bio 'WAGNER' vs stint 'Wagner, Wilhelm' (exact)
- [PASS] initials: bio ['W', 'Q'] ~ stint ['W']
- [PASS] age_gate: stint starts 1928, birth 1849 (age 79)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1930
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Wagner, William Q___South Africa___1912`

- Staff-list name: **Wagner, William Q** | colony: **South Africa** | listed 1912–1914 | editions [1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | William Q. Wagner | Mining Commissioners | Department of Mines | — | — |
| 1914 | William Q. Wagner | Mining Commissioners | Analyses | — | — |

### Deterministic checks: `wagner_william-quinn_b1849` vs `Wagner, William Q___South Africa___1912`

- [PASS] surname_gate: bio 'WAGNER' vs stint 'Wagner, William Q' (exact)
- [PASS] initials: bio ['W', 'Q'] ~ stint ['W', 'Q']
- [PASS] age_gate: stint starts 1912, birth 1849 (age 63)
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

