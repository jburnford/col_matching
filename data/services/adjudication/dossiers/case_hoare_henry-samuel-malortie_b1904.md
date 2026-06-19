<!-- {"case_id": "case_hoare_henry-samuel-malortie_b1904", "bio_ids": ["hoare_henry-samuel-malortie_b1904"], "stint_ids": ["Hoare, H. S. M___Ceylon___1931"]} -->
# Dossier case_hoare_henry-samuel-malortie_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hoare_henry-samuel-malortie_b1904`

- Printed name: **HOARE, HENRY SAMUEL MALORTIE**
- Birth year: 1904 (attested in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940])
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1931-L65341.v` — printed in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]:**

> HOARE, HENRY SAMUEL MALORTIE, B.A. (Oxon.)—B. 1904; cadet, Ceylon civ. serv., Jan., 1928; attd., Kurunegala kach., Feb., 1928; attd., Anuradhapura kach., April, 1928; office asst., Jaffna kach., Feb., 1929; pvt. sec. to gov., Feb., 1931; landing survr., cust., Nov., 1932; ag. dep. collr., cust., July-Sept., 1933; temp. attd., C.O., Aug., 1936-Apr., 1937; asst. govt. agt., Kandy, June, 1937; sec. to finance sec., Apr., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | cadet, Ceylon civ. serv | Ceylon | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 1 | 1929 | office asst., Jaffna kach | Ceylon *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 2 | 1931 | pvt. sec. to gov | Ceylon *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 3 | 1932 | landing survr., cust | Ceylon *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 4 | 1933 | ag. dep. collr., cust., July- | Ceylon *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 5 | 1936–1937 | temp. attd. | Colonial Office | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 6 | 1937 | asst. govt. agt., Kandy | Colonial Office *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 7 | 1939 | sec. to finance sec | Colonial Office *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |

## Candidate stint `Hoare, H. S. M___Ceylon___1931`

- Staff-list name: **Hoare, H. S. M** | colony: **Ceylon** | listed 1931–1940 | editions [1931, 1934, 1936, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. S. M. Hoare | Office Assistant | Government Agencies | — | — |
| 1931 | H. S. M. Hoare | Assistant Collector and Landing Surveyor | Northern Province | — | — |
| 1934 | H. S. M. Hoare | Landing Surveyor | Customs Department | — | — |
| 1936 | H. S. M. Hoare | Landing Surveyor | Customs Department | — | — |
| 1940 | H. S. M. Hoare | Deputy Collector | Customs Department | — | — |

### Deterministic checks: `hoare_henry-samuel-malortie_b1904` vs `Hoare, H. S. M___Ceylon___1931`

- [PASS] surname_gate: bio 'HOARE' vs stint 'Hoare, H. S. M' (exact)
- [PASS] initials: bio ['H', 'S', 'M'] ~ stint ['H', 'S', 'M']
- [PASS] age_gate: stint starts 1931, birth 1904 (age 27)
- [PASS] colony: 5 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1931-1940
- [PASS] position_sim: best 76 vs bar 60: 'landing survr., cust' ~ 'Landing Surveyor'
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

