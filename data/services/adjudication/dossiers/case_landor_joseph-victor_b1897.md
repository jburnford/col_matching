<!-- {"case_id": "case_landor_joseph-victor_b1897", "bio_ids": ["landor_joseph-victor_b1897"], "stint_ids": ["Landor, J. V___Straits Settlements___1936"]} -->
# Dossier case_landor_joseph-victor_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `landor_joseph-victor_b1897`

- Printed name: **LANDOR, JOSEPH VICTOR**
- Birth year: 1897 (attested in editions [1939, 1940])
- Honours: B.S, D.P.H
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L68337.v` — printed in editions [1939, 1940]:**

> LANDOR, JOSEPH VICTOR, M.D. (London), B.S., M.R.C.S. (Eng.), D.P.H., D.T.M. & H. (Eng.), M.R.C.P. (London); Certificate of London S.T.M., with distinc.—B. 1897; med. offr., S.S., Aug., 1927; med. offr. i/c. gen. hosp., Jo. Bahru, ag. phys. and radiologist, Johore, in addn., Apr., 1933; ag. prof. of med., Coll. of Med., Spore, June, 1934; phys., gen. hosp., Spore, Apr., 1935; phys. and regsr., gen. hosp., Spore, Jan., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | med. offr. | Straits Settlements | [1939, 1940] |
| 1 | 1933 | med. offr. i/c. gen. hosp., Jo. Bahru, ag. phys. and radiologist, Johore, in addn | Straits Settlements *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1934 | ag. prof. of med., Coll. of Med., Spore | Straits Settlements *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1935 | phys., gen. hosp., Spore | Straits Settlements *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1936 | phys. and regsr., gen. hosp., Spore | Straits Settlements *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Landor, J. V___Straits Settlements___1936`

- Staff-list name: **Landor, J. V** | colony: **Straits Settlements** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | J. V. Landor | Medical and Health Officer | Medical | — | — |
| 1939 | J. V. Landor | Supercase Specialist Officer, Grade B. | Medical | — | — |

### Deterministic checks: `landor_joseph-victor_b1897` vs `Landor, J. V___Straits Settlements___1936`

- [PASS] surname_gate: bio 'LANDOR' vs stint 'Landor, J. V' (exact)
- [PASS] initials: bio ['J', 'V'] ~ stint ['J', 'V']
- [PASS] age_gate: stint starts 1936, birth 1897 (age 39)
- [PASS] colony: 5 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1936-1939
- [FAIL] position_sim: best 47 vs bar 60: 'ag. prof. of med., Coll. of Med., Spore' ~ 'Medical and Health Officer'
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

