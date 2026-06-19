<!-- {"case_id": "case_le-ray_hugh-granville_b1895", "bio_ids": ["le-ray_hugh-granville_b1895"], "stint_ids": ["Le Ray, H. G___Palestine___1927"]} -->
# Dossier case_le-ray_hugh-granville_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `le-ray_hugh-granville_b1895`

- Printed name: **LE RAY, Hugh Granville**
- Birth year: 1895 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L34004.v` — printed in editions [1948]:**

> LE RAY, Hugh Granville.—b. 1895; ed. Dulwich Coll and Trinity Coll., Cambridge, M.A. (Cantab.); on mil serv. 1915-19, lieut.; inspr. of surveys, Pal., 1921; dist. survey offr., Iraq., 1928; supt. of surveys, 1933; asst. dir. of surveys, 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | inspr. of surveys | Palestine | [1948] |
| 1 | 1928 | dist. survey offr. | Iraq | [1948] |
| 2 | 1933 | supt. of surveys | Iraq *(inherited from previous clause)* | [1948] |
| 3 | 1940 | asst. dir. of surveys | Iraq *(inherited from previous clause)* | [1948] |

## Candidate stint `Le Ray, H. G___Palestine___1927`

- Staff-list name: **Le Ray, H. G** | colony: **Palestine** | listed 1927–1928 | editions [1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | H. G. Le Ray | Inspectors | Department of Surveys | — | — |
| 1928 | H. G. Le Ray | Inspector | Department of Surveys | — | — |

### Deterministic checks: `le-ray_hugh-granville_b1895` vs `Le Ray, H. G___Palestine___1927`

- [PASS] surname_gate: bio 'LE RAY' vs stint 'Le Ray, H. G' (exact)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1927, birth 1895 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1928
- [FAIL] position_sim: best 54 vs bar 60: 'inspr. of surveys' ~ 'Inspectors'
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

