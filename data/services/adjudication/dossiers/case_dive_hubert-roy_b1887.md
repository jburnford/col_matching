<!-- {"case_id": "case_dive_hubert-roy_b1887", "bio_ids": ["dive_hubert-roy_b1887"], "stint_ids": ["Dive, H. R___Straits Settlements___1931"]} -->
# Dossier case_dive_hubert-roy_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dive_hubert-roy_b1887`

- Printed name: **DIVE, HUBERT ROY**
- Birth year: 1887 (attested in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: M.C
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L59228.v` — printed in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> DIVE, MAJOR HUBERT ROY, M.C., M.R.C.S. (Eng.), L.R.C.P. (Lond.), D.T.M. & H. (Lond.), D.O.M.S. (Lond.), graduate Lond. Schl. of Trop. Med., certif. Royal Lond. Opthalmic Hosp. (Moorfields).—B. 1887; great war, Gallipoli; Egypt, Palestine and France, 1915-19; 1st med. offr./i.c war pensioners., St. Barth. Hosp., Lond., 1919-20; student and house surgn., L.S.T.M., and Albert Dock Hosp., Feb.-Aug., 1920; med. offr., F.M.S., Dec., 1920; sr. med. offr., Pahang Nov., 1927; assisting in office of prin. med. offr., F.M.S., Aug., 1930; ch. med. offr., Penang, June, 1932; superscale offr., grade A, Sept., 1934; sg. D.M.S.M., S.S., Feb., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | Egypt, Palestine and France | Palestine | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1919–1920 | 1st med. offr./i.c war pensioners., St. Barth. Hosp., Lond | Palestine *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1920 | student and house surgn., L.S.T.M., and Albert Dock Hosp., Feb.- | Palestine *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1920 | med. offr. | Federated Malay States | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1927 | sr. med. offr., Pahang | Federated Malay States *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1930 | assisting in office of prin. med. offr. | Federated Malay States | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1932 | ch. med. offr., Penang | Federated Malay States *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 7 | 1934 | superscale offr., grade A | Federated Malay States *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 8 | 1936 | sg. D.M.S.M. | Straits Settlements | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Dive, H. R___Straits Settlements___1931`

- Staff-list name: **Dive, H. R** | colony: **Straits Settlements** | listed 1931–1939 | editions [1931, 1932, 1933, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. R. Dive | Senior Medical Officer, Pahang | Medical | — | — |
| 1932 | H. R. Dive | Senior Medical Officer, Pahang | Medical | — | — |
| 1933 | H. R. Dive | Chief Medical Officer | Medical | — | — |
| 1936 | H. R. Dive | Chief Medical Officer | Medical | — | — |
| 1939 | H. R. Dive | Supercase Medical Officer, Grade A. | Medical | — | — |

### Deterministic checks: `dive_hubert-roy_b1887` vs `Dive, H. R___Straits Settlements___1931`

- [PASS] surname_gate: bio 'DIVE' vs stint 'Dive, H. R' (exact)
- [PASS] initials: bio ['H', 'R'] ~ stint ['H', 'R']
- [PASS] age_gate: stint starts 1931, birth 1887 (age 44)
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1939
- [FAIL] position_sim: best 20 vs bar 60: 'sg. D.M.S.M.' ~ 'Supercase Medical Officer, Grade A.'
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

