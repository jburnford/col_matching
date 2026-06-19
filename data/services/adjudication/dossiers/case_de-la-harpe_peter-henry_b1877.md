<!-- {"case_id": "case_de-la-harpe_peter-henry_b1877", "bio_ids": ["de-la-harpe_peter-henry_b1877"], "stint_ids": ["de la Harpe, P. H___Ceylon___1931"]} -->
# Dossier case_de-la-harpe_peter-henry_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-la-harpe_peter-henry_b1877`

- Printed name: **DE LA HARPE, PETER HENRY**
- Birth year: 1877 (attested in editions [1936, 1937])
- Honours: I.S.O (1935)
- Appears in editions: [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1936-L60196.v` — printed in editions [1936, 1937]:**

> DE LA HARPE, PETER HENRY, I.S.O. (1935).—B. 1877; apptd. to cls. V., Ceylon civ. serv., June, 1923; extra offr., asst., Galle Kach., June, 1923; ditto to col. sec., Aug., 1928; office asst. to col. sec., Sept., 1929; do. to ch. sec., July, 1931.

**Version `col1924-L53695.v` — printed in editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935]:**

> DE LA HARPE, PETER HENRY.—B. 1877; apptd. to cls. V., Ceylon civ. serv., June, 1923; extra off. asst., Galle Kach., June, 1923; ditto to col. sec., Aug., 1928; office assist. to col. sec., Sept., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | apptd. to cls. V., Ceylon civ. serv | Ceylon | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1928 | ditto to col. sec | Ceylon *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 2 | 1929 | office asst. to col. sec | Ceylon *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 3 | 1931 | do. to ch. sec | Dominions Office | [1936, 1937] |

## Candidate stint `de la Harpe, P. H___Ceylon___1931`

- Staff-list name: **de la Harpe, P. H** | colony: **Ceylon** | listed 1931–1936 | editions [1931, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | P. H. de la Harpe | Office Assistant | Civil Establishment | — | — |
| 1934 | P. H. de la Harpe | Office Assistant | Civil Establishment | — | — |
| 1936 | P. H. de la Harpe | Office Assistant | Civil Establishment | — | — |

### Deterministic checks: `de-la-harpe_peter-henry_b1877` vs `de la Harpe, P. H___Ceylon___1931`

- [PASS] surname_gate: bio 'DE LA HARPE' vs stint 'de la Harpe, P. H' (exact)
- [PASS] initials: bio ['P', 'H'] ~ stint ['P', 'H']
- [PASS] age_gate: stint starts 1931, birth 1877 (age 54)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1936
- [PASS] position_sim: best 63 vs bar 60: 'office asst. to col. sec' ~ 'Office Assistant'
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

