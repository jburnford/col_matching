<!-- {"case_id": "case_elmes_basil-george-tonge_b1903", "bio_ids": ["elmes_basil-george-tonge_b1903"], "stint_ids": ["Elmes, B. G. T___Nigeria___1933"]} -->
# Dossier case_elmes_basil-george-tonge_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `elmes_basil-george-tonge_b1903`

- Printed name: **ELMES, Basil George Tonge**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32443.v` — printed in editions [1948, 1949, 1950, 1951]:**

> ELMES, Basil George Tonge, M.D. (Edin.), Ch.B. (Edin.), F.R.C.P. (Edin.)—b. 1903; ed. Rossall Sch., Lancs., and Univ. of Edinburgh, Rotunda Hosp., Dublin, and Univ. of London, L.S.H.T.M. cert. (distinc.); on mil. serv. 1940-42, maj.; med. offr., Nig., 1927; pathologist, 1930; asst. dir. of lab. serv., 1943; author of various contribtns. to medical journals.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | med. offr. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1930 | pathologist | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1943 | asst. dir. of lab. serv | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Elmes, B. G. T___Nigeria___1933`

- Staff-list name: **Elmes, B. G. T** | colony: **Nigeria** | listed 1933–1939 | editions [1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | B. G. T. Elmes | Pathologist | Medical Laboratory Service | — | — |
| 1933 | B. G. T. Elmes | Pathologists | Medical | — | — |
| 1934 | B. G. T. Elmes | Pathologist | Medical Laboratory Service | — | — |
| 1936 | B. G. T. Elmes | Pathologists | Medical Laboratory Service | — | — |
| 1939 | B. G. T. Elmes | Pathologist | Medical Laboratory Service | — | — |

### Deterministic checks: `elmes_basil-george-tonge_b1903` vs `Elmes, B. G. T___Nigeria___1933`

- [PASS] surname_gate: bio 'ELMES' vs stint 'Elmes, B. G. T' (exact)
- [PASS] initials: bio ['B', 'G', 'T'] ~ stint ['B', 'G', 'T']
- [PASS] age_gate: stint starts 1933, birth 1903 (age 30)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1933-1939
- [PASS] position_sim: best 100 vs bar 60: 'pathologist' ~ 'Pathologist'
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

