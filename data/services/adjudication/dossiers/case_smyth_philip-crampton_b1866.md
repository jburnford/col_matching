<!-- {"case_id": "case_smyth_philip-crampton_b1866", "bio_ids": ["smyth_philip-crampton_b1866"], "stint_ids": ["Smyth, Patrick___Trinidad and Tobago___1906", "Smyth, Patrick___Trinidad___1908"]} -->
# Dossier case_smyth_philip-crampton_b1866

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `smyth_philip-crampton_b1866`

- Printed name: **SMYTH, PHILIP CRAMPTON**
- Birth year: 1866 (attested in editions [1914, 1936])
- Honours: KT. BACH (1905)
- Appears in editions: [1914, 1936]

### Verbatim printed entry text (OCR)

**Version `col1914-L50020.v` — printed in editions [1914, 1936]:**

> SMYTH, SIR PHILIP CRAMPTON, KT. BACH. (1905).—B. 1866; ed. at Trin. Coll., Dub., B.A., LL.B.; called to the bar, King's Inn, Dub., 1888; LL.D., 1891; called to the bar, Gray's Inn, 1902; Queen's advoc., S. Leone, 1895; atty.-gen., 1896; ch. just., S. Leone, 1901; ch. just., Gold Coast, 1911; ret., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1888 | called to the bar, King's Inn, Dub | — | [1914, 1936] |
| 1 | 1891 | LL.D | — | [1914, 1936] |
| 2 | 1895 | Queen's advoc., S. Leone | — | [1914, 1936] |
| 3 | 1896 | atty.-gen | — | [1914, 1936] |
| 4 | 1901 | ch. just., S. Leone | — | [1914, 1936] |
| 5 | 1902 | called to the bar, Gray's Inn | — | [1914, 1936] |
| 6 | 1911 | ch. just. | Gold Coast | [1914, 1936] |
| 7 | 1929 | ret | Gold Coast *(inherited from previous clause)* | [1914, 1936] |

## Candidate stint `Smyth, Patrick___Trinidad and Tobago___1906`

- Staff-list name: **Smyth, Patrick** | colony: **Trinidad and Tobago** | listed 1906–1917 | editions [1906, 1907, 1910, 1912, 1913, 1914, 1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | Patrick Smyth | Reverend | Roman Catholic Church | — | — |
| 1907 | Patrick Smyth | Chaplain, Colonial Hospital | Roman Catholic Church | — | — |
| 1910 | P. Smyth | Assistant Priests | Roman Catholic Church | — | — |
| 1912 | P. Smyth | Assistant Priest | Roman Catholic Church | — | — |
| 1913 | P. Smyth | Assistant Priest | Roman Catholic Church | — | — |
| 1914 | P. Smyth | Assistant Priest | Roman Catholic Church | — | — |
| 1915 | P. Smyth | Assistant Priests | Roman Catholic Church | — | — |
| 1917 | P. Smyth | Assistant Priest | Roman Catholic Church | — | — |

### Deterministic checks: `smyth_philip-crampton_b1866` vs `Smyth, Patrick___Trinidad and Tobago___1906`

- [PASS] surname_gate: bio 'SMYTH' vs stint 'Smyth, Patrick' (exact)
- [PASS] initials: bio ['P', 'C'] ~ stint ['P']
- [PASS] age_gate: stint starts 1906, birth 1866 (age 40)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1917
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Smyth, Patrick___Trinidad___1908`

- Staff-list name: **Smyth, Patrick** | colony: **Trinidad** | listed 1908–1911 | editions [1908, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | Patrick Smyth | Chaplain | Roman Catholic Church | — | — |
| 1911 | P. Smyth | Assistant Priests | Roman Catholic Church | — | — |

### Deterministic checks: `smyth_philip-crampton_b1866` vs `Smyth, Patrick___Trinidad___1908`

- [PASS] surname_gate: bio 'SMYTH' vs stint 'Smyth, Patrick' (exact)
- [PASS] initials: bio ['P', 'C'] ~ stint ['P']
- [PASS] age_gate: stint starts 1908, birth 1866 (age 42)
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1911
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

