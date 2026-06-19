<!-- {"case_id": "case_de-silva_lucian-macull-dominic_b1893", "bio_ids": ["de-silva_lucian-macull-dominic_b1893"], "stint_ids": ["de Silva, L. M. D___Ceylon___1927"]} -->
# Dossier case_de-silva_lucian-macull-dominic_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-silva_lucian-macull-dominic_b1893`

- Printed name: **DE SILVA, LUCIAN MACULL DOMINIC**
- Birth year: 1893 (attested in editions [1933, 1934, 1935])
- Appears in editions: [1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `col1933-L59150.v` — printed in editions [1933, 1934, 1935]:**

> DE SILVA, LUCIAN MACULL DOMINIC, B.A. (Cantab), Barrister-at-Law, Gray’s Inn.—B. 1893; comsnr., requests, Colombo, 1925; dep. solr.-gen., Ceylon, Apr., 1929; ag. atty.-gen., in 1930 and 1931; solr.-gen., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925–1925 | comsnr., requests | Colombo | [1933, 1934, 1935] |
| 1 | 1929–1929 | dep. solr.-gen. | Ceylon | [1933, 1934, 1935] |
| 2 | 1930–1931 | ag. atty.-gen. | — | [1933, 1934, 1935] |
| 3 | 1932–1932 | solr.-gen. | — | [1933, 1934, 1935] |

## Candidate stint `de Silva, L. M. D___Ceylon___1927`

- Staff-list name: **de Silva, L. M. D** | colony: **Ceylon** | listed 1927–1934 | editions [1927, 1928, 1929, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | L. M. D. de Silva | Assistant to Attorney-General | Judicial Establishment | — | — |
| 1928 | L. M. D. de Silva | Assistant to Attorney-General | Judicial Establishment | — | — |
| 1929 | L. M. D. de Silva | Assistant to Attorney-General | Judicial Establishment | — | — |
| 1934 | L. M. D. de Silva | Solicitor-General | Law Officers’ Department | — | — |

### Deterministic checks: `de-silva_lucian-macull-dominic_b1893` vs `de Silva, L. M. D___Ceylon___1927`

- [PASS] surname_gate: bio 'DE SILVA' vs stint 'de Silva, L. M. D' (exact)
- [PASS] initials: bio ['L', 'M', 'D'] ~ stint ['L', 'M', 'D']
- [PASS] age_gate: stint starts 1927, birth 1893 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1934
- [FAIL] position_sim: best 52 vs bar 60: 'dep. solr.-gen.' ~ 'Solicitor-General'
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

