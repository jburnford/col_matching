<!-- {"case_id": "case_bicheno_beatrice-may_b1905", "bio_ids": ["bicheno_beatrice-may_b1905"], "stint_ids": ["Bicheno, B. M___Hong Kong___1949"]} -->
# Dossier case_bicheno_beatrice-may_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bicheno_beatrice-may_b1905`

- Printed name: **BICHENO, Beatrice May**
- Birth year: 1905 (attested in editions [1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L33683.v` — printed in editions [1950, 1951]:**

> BICHENO, Beatrice May.—b. 1905; ed. Convent of Sion, Hamilton, Berm., St. Mary’s Sch., Bungay, Suffolk, and Maria Grey Training Coll., Lond. (nat. Froebel union and B. of E. cert.); interned, 1941; asst. mstr., H.K., 1931; headmistress, The Peak Sch., and senr. mstr., 1946.

**Version `col1948-L31181.v` — printed in editions [1948, 1949]:**

> BICHENO, Beatrice May.—b. 1905; ed. S. Agnes Convent, Bermuda, St. Mary’s Sch., Bungay, Suffolk, and Maria Grey Coll., London (nat. Froebel union and b. of e. certs.); asst. mist., H.K., 1931; senr. mist., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | asst. mstr. | Hong Kong | [1948, 1949, 1950, 1951] |
| 1 | 1941 | interned | — | [1950, 1951] |
| 2 | 1946 | headmistress, The Peak Sch., and senr. mstr | Hong Kong *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Bicheno, B. M___Hong Kong___1949`

- Staff-list name: **Bicheno, B. M** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | B. M. Bicheno | Senior Mistresses | Education Department | — | — |
| 1950 | B. M. Bicheno | Senior Mistresses | Education | — | — |
| 1951 | B. M. Bicheno | Senior Mistresses | Education | — | — |

### Deterministic checks: `bicheno_beatrice-may_b1905` vs `Bicheno, B. M___Hong Kong___1949`

- [PASS] surname_gate: bio 'BICHENO' vs stint 'Bicheno, B. M' (exact)
- [PASS] initials: bio ['B', 'M'] ~ stint ['B', 'M']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 54 vs bar 60: 'headmistress, The Peak Sch., and senr. mstr' ~ 'Senior Mistresses'
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

