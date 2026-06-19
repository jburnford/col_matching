<!-- {"case_id": "case_mccleland_reginald-hugh_b1894", "bio_ids": ["mccleland_reginald-hugh_b1894"], "stint_ids": ["McCleland, R. H___Straits Settlements___1934"]} -->
# Dossier case_mccleland_reginald-hugh_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mccleland_reginald-hugh_b1894`

- Printed name: **McCLELAND, REGINALD HUGH**
- Birth year: 1894 (attested in editions [1932])
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L62113.v` — printed in editions [1932]:**

> McCLELAND, REGINALD HUGH, L.C.E. (Dub.)—B. 1894; engrnr.-survr., S.S., May, 1908; lent to Kodah Nov., 1909; asst. engrnr., Aug., 1918; exec. engrnr., Dec., 1925; dep. col. engrnr. in addn., Mar.-May, 1927 and Oct.-Nov., 1927; ag. sr. exec. engrnr., P.W., Sept., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | engrnr.-survr. | Straits Settlements | [1932] |
| 1 | 1909 | lent to Kodah | Straits Settlements *(inherited from previous clause)* | [1932] |
| 2 | 1918 | asst. engrnr | Straits Settlements *(inherited from previous clause)* | [1932] |
| 3 | 1925 | exec. engrnr | Straits Settlements *(inherited from previous clause)* | [1932] |
| 4 | 1927 | dep. col. engrnr. in addn., Mar.- | Straits Settlements *(inherited from previous clause)* | [1932] |
| 5 | 1929 | ag. sr. exec. engrnr., P.W | Straits Settlements *(inherited from previous clause)* | [1932] |

## Candidate stint `McCleland, R. H___Straits Settlements___1934`

- Staff-list name: **McCleland, R. H** | colony: **Straits Settlements** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | R. H. McCleland | Senior Executive Engineer | Public Works | — | — |
| 1939 | R. H. McCleland | Senior Executive Engineers | Public Works | — | — |

### Deterministic checks: `mccleland_reginald-hugh_b1894` vs `McCleland, R. H___Straits Settlements___1934`

- [PASS] surname_gate: bio 'McCLELAND' vs stint 'McCleland, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1934, birth 1894 (age 40)
- [PASS] colony: 6 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 58 vs bar 60: 'ag. sr. exec. engrnr., P.W' ~ 'Senior Executive Engineer'
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

