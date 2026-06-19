<!-- {"case_id": "case_overton_stanley-daniel_b1894", "bio_ids": ["overton_stanley-daniel_b1894"], "stint_ids": ["Overton, S. D___Kenya___1927"]} -->
# Dossier case_overton_stanley-daniel_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `overton_stanley-daniel_b1894`

- Printed name: **OVERTON, Stanley Daniel**
- Birth year: 1894 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35068.v` — printed in editions [1948, 1949, 1950, 1951]:**

> OVERTON, Stanley Daniel.—b. 1894; ed. Lincoln Continuation Sec., Sch., Southern Command Military Sch., England; on mil. serv., 1914-18; police const., Ken., 1921; asst. inspr., police, 1926; inspr., 1930; ch. inspr., 1941; asst. supt., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | police const. | Kenya | [1948, 1949, 1950, 1951] |
| 1 | 1926 | asst. inspr., police | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1930 | inspr | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1941 | ch. inspr | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1943 | asst. supt | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Overton, S. D___Kenya___1927`

- Staff-list name: **Overton, S. D** | colony: **Kenya** | listed 1927–1930 | editions [1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | S. D. Overton | Inspector | Police Department | — | — |
| 1928 | S. D. Overton | Assistant Inspector | Police Department | — | — |
| 1929 | S. D. Overton | Assistant Inspector | Police Department | — | — |
| 1930 | S. D. Overton | Assistant Inspector | Police Department | — | — |

### Deterministic checks: `overton_stanley-daniel_b1894` vs `Overton, S. D___Kenya___1927`

- [PASS] surname_gate: bio 'OVERTON' vs stint 'Overton, S. D' (exact)
- [PASS] initials: bio ['S', 'D'] ~ stint ['S', 'D']
- [PASS] age_gate: stint starts 1927, birth 1894 (age 33)
- [PASS] colony: 5 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1927-1930
- [PASS] position_sim: best 71 vs bar 60: 'inspr' ~ 'Inspector'
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

