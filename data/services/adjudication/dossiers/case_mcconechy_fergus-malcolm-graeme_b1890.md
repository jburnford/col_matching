<!-- {"case_id": "case_mcconechy_fergus-malcolm-graeme_b1890", "bio_ids": ["mcconechy_fergus-malcolm-graeme_b1890"], "stint_ids": ["McConechy, F. M. G___Straits Settlements___1936"]} -->
# Dossier case_mcconechy_fergus-malcolm-graeme_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcconechy_fergus-malcolm-graeme_b1890`

- Printed name: **MCCONECHY, FERGUS MALCOLM GRAEME**
- Birth year: 1890 (attested in editions [1932, 1940])
- Honours: A.M.I.C.E
- Appears in editions: [1932, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L62121.v` — printed in editions [1932, 1940]:**

> MCCONECHY, FERGUS MALCOLM GRAEME, B.Sc., A.M.I.C.E.—B. 1890; ed. Sevenoaks Grammar Schol. and Manchester Univ.; astt. engrnr., P.W.D., F.M.S., Apr., 1914; exec. engrnr., 1922; senr. exec. engrnr., 1929; ag. dep. dir. pub. works, S.S., Apr. to Dec., 1932 and July-Nov., 1934; state engrnr., grade I, Nov., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | astt. engrnr., P.W.D. | Federated Malay States | [1932, 1940] |
| 1 | 1922 | exec. engrnr | Federated Malay States *(inherited from previous clause)* | [1932, 1940] |
| 2 | 1929 | senr. exec. engrnr | Federated Malay States *(inherited from previous clause)* | [1932, 1940] |
| 3 | 1932 | ag. dep. dir. pub. works | Straits Settlements | [1932, 1940] |
| 4 | 1934 | July- | Straits Settlements *(inherited from previous clause)* | [1932, 1940] |
| 5 | 1935 | state engrnr., grade I | Straits Settlements *(inherited from previous clause)* | [1932, 1940] |

## Candidate stint `McConechy, F. M. G___Straits Settlements___1936`

- Staff-list name: **McConechy, F. M. G** | colony: **Straits Settlements** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | F. M. G. McConechy | State Engineer, Johore | Civil Engineering Establishment | — | — |
| 1939 | F. M. G. McConechy | State Engineers, Grade I | Public Works | — | — |

### Deterministic checks: `mcconechy_fergus-malcolm-graeme_b1890` vs `McConechy, F. M. G___Straits Settlements___1936`

- [PASS] surname_gate: bio 'MCCONECHY' vs stint 'McConechy, F. M. G' (exact)
- [PASS] initials: bio ['F', 'M', 'G'] ~ stint ['F', 'M', 'G']
- [PASS] age_gate: stint starts 1936, birth 1890 (age 46)
- [PASS] colony: 3 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1936-1939
- [PASS] position_sim: best 88 vs bar 60: 'state engrnr., grade I' ~ 'State Engineers, Grade I'
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

