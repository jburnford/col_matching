<!-- {"case_id": "case_hofmeyr_g-m_b1887", "bio_ids": ["hofmeyr_g-m_b1887"], "stint_ids": ["Hofmeyr, G. M___South Africa___1912"]} -->
# Dossier case_hofmeyr_g-m_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hofmeyr_g-m_b1887`

- Printed name: **HOFMEYR, G. M**
- Birth year: 1887 (attested in editions [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927])
- Honours: B.A
- Appears in editions: [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1917-L50424.v` — printed in editions [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]:**

> HOFMEYR, G. M., B.A., Cape.—B. 1887; ed., Victoria Coll., Stellenbosch; teacher for number of years; attorney, notary-public and conveyancer, Transvaal; regisr. and treas., Victoria Coll., 1908-1910; under-sec. for educn., Union of S. Africa, 1910; sec. for educn., Jan., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908–1910 | regisr. and treas., Victoria Coll | Victoria | [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |
| 1 | 1910 | under-sec. for educn., Union of S. Africa | Victoria *(inherited from previous clause)* | [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |
| 2 | 1920 | sec. for educn | Victoria *(inherited from previous clause)* | [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |

## Candidate stint `Hofmeyr, G. M___South Africa___1912`

- Staff-list name: **Hofmeyr, G. M** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | G. M. Hofmeyr | Under Secretary for Education | Department of Education | — | — |
| 1914 | G. M. Hofmeyr | Under Secretary for Education | Department of Education | — | — |
| 1918 | G. M. Hofmeyr | Under Secretary for Education | Department of Education | — | — |

### Deterministic checks: `hofmeyr_g-m_b1887` vs `Hofmeyr, G. M___South Africa___1912`

- [PASS] surname_gate: bio 'HOFMEYR' vs stint 'Hofmeyr, G. M' (exact)
- [PASS] initials: bio ['G', 'M'] ~ stint ['G', 'M']
- [PASS] age_gate: stint starts 1912, birth 1887 (age 25)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

