<!-- {"case_id": "case_stevens_george-richard-robert_b1900", "bio_ids": ["stevens_george-richard-robert_b1900"], "stint_ids": ["Stevens, G. R. R___Northern Rhodesia___1936"]} -->
# Dossier case_stevens_george-richard-robert_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 28 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stevens_george-richard-robert_b1900`

- Printed name: **STEVENS, George Richard Robert**
- Birth year: 1900 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L36135.v` — printed in editions [1948, 1949, 1950]:**

> STEVENS, George Richard Robert.—b. 1900; ed. The Charterhouse, Magdalen Coll., Oxford (hon. sch. of Jurisprudence), M.A. (Oxon.) ; prob.; dist. admin., N. Rhod., 1924; dist. offr., gr. III, 1929; gr. II, 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | dist. admin. | Northern Rhodesia | [1948, 1949, 1950] |
| 1 | 1929 | dist. offr., gr. III | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950] |
| 2 | 1934 | gr. II | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Stevens, G. R. R___Northern Rhodesia___1936`

- Staff-list name: **Stevens, G. R. R** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | G. R. R. Stevens | District Officers | District Administration | — | — |
| 1939 | G. R. R. Stevens | District Officer | District Administration | — | — |
| 1940 | G. R. R. Stevens | District Officer | District Administration | — | — |

### Deterministic checks: `stevens_george-richard-robert_b1900` vs `Stevens, G. R. R___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'STEVENS' vs stint 'Stevens, G. R. R' (exact)
- [PASS] initials: bio ['G', 'R', 'R'] ~ stint ['G', 'R', 'R']
- [PASS] age_gate: stint starts 1936, birth 1900 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 29 vs bar 60: 'gr. II' ~ 'District Officer'
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

