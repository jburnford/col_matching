<!-- {"case_id": "case_beal_j-c_e1862", "bio_ids": ["beal_j-c_e1862"], "stint_ids": ["Beal, J. C___Queensland___1878"]} -->
# Dossier case_beal_j-c_e1862

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beal_j-c_e1862`

- Printed name: **BEAL, J. C**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1888-L32019.v` — printed in editions [1888, 1889, 1894, 1896, 1897]:**

> BEAL, J. C.—Educated St. James' Grammar School, Sydney; superintendent government printing office, Queensland, 1862; acting government printer, Dec., 1865; confirmed, 1867.

**Version `col1898-L32139.v` — printed in editions [1898]:**

> BEAL, J. C.—Ed. St. James' Grammar Sch., Sydney; supt.; govt. printing office, Queensland, 1862; govt. printer, 1867.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | superintendent government printing office | Queensland | [1888, 1889, 1894, 1896, 1897, 1898] |
| 1 | 1865 | acting government printer | Queensland *(inherited from previous clause)* | [1888, 1889, 1894, 1896, 1897] |
| 2 | 1867 | confirmed | Queensland *(inherited from previous clause)* | [1888, 1889, 1894, 1896, 1897, 1898] |

## Candidate stint `Beal, J. C___Queensland___1878`

- Staff-list name: **Beal, J. C** | colony: **Queensland** | listed 1878–1890 | editions [1878, 1879, 1880, 1883, 1886, 1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | J. C. Beal | Government Printer | Colonial Secretary's Department | — | — |
| 1879 | J. C. Beal | Government Printer | Colonial Secretary's Department | — | — |
| 1880 | J. C. Beal | Government Printer | Colonial Secretary's Department | — | — |
| 1883 | J. C. Beal | Government Printer | Colonial Secretary's Department | — | — |
| 1886 | J. C. Beal | Government Printer | Colonial Secretary's Department | — | — |
| 1888 | J. C. Beal | Government Printer | Colonial Secretary's Department | — | — |
| 1890 | J. C. Beal | Government Printer | Colonial Secretary's Department | — | — |

### Deterministic checks: `beal_j-c_e1862` vs `Beal, J. C___Queensland___1878`

- [PASS] surname_gate: bio 'BEAL' vs stint 'Beal, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1890
- [FAIL] position_sim: best 30 vs bar 60: 'confirmed' ~ 'Government Printer'
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

