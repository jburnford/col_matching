<!-- {"case_id": "case_borcardona_j-g_b1905", "bio_ids": ["borcardona_j-g_b1905"], "stint_ids": ["Borg Cardona, J. G___Malta___1954"]} -->
# Dossier case_borcardona_j-g_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `borcardona_j-g_b1905`

- Printed name: **BORCARDONA, J. G**
- Birth year: 1905 (attested in editions [1955])
- Appears in editions: [1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1955-L19822.v` — printed in editions [1955]:**

> BORCARDONA, J. G.—b. 1905; ed. St. Aloysius Coll., Malta; civ. serv. (admin.), Malta, 1923; soc. serv. offr., 1947; dir., social welfare, 1948.

**Version `col1956-L19906.v` — printed in editions [1956]:**

> BORG CARDONA, J. G.—b. 1905; ed. St. Aloysius Coll., Malta; civ. serv. (admin.), Malta, 1923; soc. serv. offr., 1947; dir., social welfare, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | civ. serv. (admin.) | Malta | [1955, 1956] |
| 1 | 1947 | soc. serv. offr | Malta *(inherited from previous clause)* | [1955, 1956] |
| 2 | 1948 | dir., social welfare | Malta *(inherited from previous clause)* | [1955, 1956] |

## Candidate stint `Borg Cardona, J. G___Malta___1954`

- Staff-list name: **Borg Cardona, J. G** | colony: **Malta** | listed 1954–1955 | editions [1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | J. G. Borg Cardona | Director of Social Welfare | The Maltese Government | — | — |
| 1955 | J. G. Borg Cardona | Director of Social Welfare | THE MALTESE GOVERNMENT | — | — |

### Deterministic checks: `borcardona_j-g_b1905` vs `Borg Cardona, J. G___Malta___1954`

- [PASS] surname_gate: bio 'BORCARDONA' vs stint 'Borg Cardona, J. G' (fuzzy:2)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1954, birth 1905 (age 49)
- [PASS] colony: 3 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1954-1955
- [PASS] position_sim: best 88 vs bar 60: 'dir., social welfare' ~ 'Director of Social Welfare'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1955] pos~88 (bar: >=2)
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

