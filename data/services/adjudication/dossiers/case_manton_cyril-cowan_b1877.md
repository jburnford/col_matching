<!-- {"case_id": "case_manton_cyril-cowan_b1877", "bio_ids": ["manton_cyril-cowan_b1877"], "stint_ids": ["Manton, C. C___Jamaica___1922"]} -->
# Dossier case_manton_cyril-cowan_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `manton_cyril-cowan_b1877`

- Printed name: **MANTON, Cyril Cowan**
- Birth year: 1877 (attested in editions [1935, 1936, 1937])
- Appears in editions: [1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `dol1935-L60681.v` — printed in editions [1935, 1936, 1937]:**

> MANTON, Cyril Cowan.—B. 1877; 2nd cls. clk., collectorate, Black River, Jamaica, 1897; 1st cls. treasy. clk., 1903; junr. astt. collr. taxes, 1912; astt. collr., Kingston, 1920; dep. stamp commnr., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897 | 2nd cls. clk., collectorate, Black River | Jamaica | [1935, 1936, 1937] |
| 1 | 1903 | 1st cls. treasy. clk | Jamaica *(inherited from previous clause)* | [1935, 1936, 1937] |
| 2 | 1912 | junr. astt. collr. taxes | Jamaica *(inherited from previous clause)* | [1935, 1936, 1937] |
| 3 | 1920 | astt. collr., Kingston | Jamaica *(inherited from previous clause)* | [1935, 1936, 1937] |

## Candidate stint `Manton, C. C___Jamaica___1922`

- Staff-list name: **Manton, C. C** | colony: **Jamaica** | listed 1922–1937 | editions [1922, 1923, 1925, 1927, 1928, 1930, 1931, 1933, 1934, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | C. C. Manton | Deputy Stamp Commissioner | Stamp Office | — | — |
| 1923 | C. C. Manton | Deputy Stamp Commissioner | Stamp Office | — | — |
| 1925 | C. C. Manton | Deputy Stamp Commissioner | Stamp Office | — | — |
| 1927 | C. C. Manton | Deputy Stamp Commissioner | Stamp Office | — | — |
| 1928 | C. C. Manton | Deputy Stamp Commissioner | Stamp Office | — | — |
| 1930 | C. C. Manton | Deputy Stamp Commissioner | Stamp Office | — | — |
| 1931 | C. C. Manton | Deputy Stamp Commissioner | Stamp Office | — | — |
| 1933 | C. C. Manton | Deputy Stamp Commissioner | Stamp Office | — | — |
| 1934 | C. C. Manton | Deputy Stamp Commissioner | Stamp Office | — | — |
| 1937 | C. C. Manton | Deputy Stamp Commissioner | Stamp Office | — | — |

### Deterministic checks: `manton_cyril-cowan_b1877` vs `Manton, C. C___Jamaica___1922`

- [PASS] surname_gate: bio 'MANTON' vs stint 'Manton, C. C' (exact)
- [PASS] initials: bio ['C', 'C'] ~ stint ['C', 'C']
- [PASS] age_gate: stint starts 1922, birth 1877 (age 45)
- [PASS] colony: 4 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1937
- [FAIL] position_sim: best 27 vs bar 60: 'astt. collr., Kingston' ~ 'Deputy Stamp Commissioner'
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

