<!-- {"case_id": "case_liang_sai-wa_b1905", "bio_ids": ["liang_sai-wa_b1905"], "stint_ids": ["Liang, S. W___Hong Kong___1950"]} -->
# Dossier case_liang_sai-wa_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['liang_sai-wa_b1905'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Liang, S. W___Hong Kong___1950` is also gate-compatible with biography(ies) outside this case: ['liang_sal-wa_b1905'] (already linked elsewhere or filtered).

## Biography `liang_sai-wa_b1905`

- Printed name: **LIANG, Sai-wa**
- Birth year: 1905 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L37295.v` — printed in editions [1950, 1951]:**

> LIANG, Sai-wa.—b. 1905; ed. St. Stephen's Coll., H.K., and Oxford Univ., B.A. (Oxon); inspr., vernacular schs., educ. dept., H.K., 1929; tel. censor, 1939-40; hdmstr., vernacular senr. middle sch., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | inspr., vernacular schs., educ. dept. | Hong Kong | [1950, 1951] |
| 1 | 1939–1940 | tel. censor | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 2 | 1946 | hdmstr., vernacular senr. middle sch | Hong Kong *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Liang, S. W___Hong Kong___1950`

- Staff-list name: **Liang, S. W** | colony: **Hong Kong** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | S. W. Liang | Inspectors, Vernacular Schools | Education | — | — |
| 1951 | S. W. Liang | Masters | Education | — | — |

### Deterministic checks: `liang_sai-wa_b1905` vs `Liang, S. W___Hong Kong___1950`

- [PASS] surname_gate: bio 'LIANG' vs stint 'Liang, S. W' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S', 'W']
- [PASS] age_gate: stint starts 1950, birth 1905 (age 45)
- [PASS] colony: 3 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [PASS] position_sim: best 61 vs bar 60: 'hdmstr., vernacular senr. middle sch' ~ 'Inspectors, Vernacular Schools'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1950] pos~61 (bar: >=2)
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

