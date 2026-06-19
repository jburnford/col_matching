<!-- {"case_id": "case_gater_bossley-alan-rex_b1896", "bio_ids": ["gater_bossley-alan-rex_b1896"], "stint_ids": ["Gater, B. A. R___Straits Settlements___1931"]} -->
# Dossier case_gater_bossley-alan-rex_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gater_bossley-alan-rex_b1896`

- Printed name: **GATER, BOSSLEY ALAN REX**
- Birth year: 1896 (attested in editions [1932, 1933, 1935, 1936, 1937, 1939, 1940])
- Honours: D.I.C, F.E.S, F.R.M.S, F.Z.S, M.A
- Appears in editions: [1932, 1933, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L60419.v` — printed in editions [1932, 1933, 1935, 1936, 1937, 1939, 1940]:**

> GATER, BOSSLEY ALAN REX, M.A., Dip. Agric. (Cantab.), D.I.C., F.R.M.S., F.E.S., F.Z.S.—B. 1896; war serv., 1914-19; asst. entomologist, dept. of agric., F.M.S., Nov., 1922; malaria resch. offr., Nov., 1926; entomologist, Inst. Med. Resch., 1927; prof., biology, King Edward VII Coll. of Medicine, S'pore, Aug., 1930; del. to 8th cong. of Far Eastern Assoc. of Trop. Med., Dec., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | asst. entomologist, dept. of agric. | Federated Malay States | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1926 | malaria resch. offr | Federated Malay States *(inherited from previous clause)* | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1927 | entomologist, Inst. Med. Resch | Federated Malay States *(inherited from previous clause)* | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1930 | prof., biology, King Edward VII Coll. of Medicine, S'pore | Federated Malay States *(inherited from previous clause)* | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Gater, B. A. R___Straits Settlements___1931`

- Staff-list name: **Gater, B. A. R** | colony: **Straits Settlements** | listed 1931–1934 | editions [1931, 1932, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | B. A. R. Gater | Professor of Biology | King Edward VII College of Medicine | — | — |
| 1932 | B. A. R. Gater | Professor of Biology | Raffles College | — | — |
| 1933 | B. A. R. Gater | Professor of Biology | King Edward VII College of Medicine | — | — |
| 1933 | B. A. R. Gater | Professor of Biology | Raffles College | — | — |
| 1934 | B. A. R. Gater | Professor of Biology | King Edward VII College of Medicine, Singapore | — | — |

### Deterministic checks: `gater_bossley-alan-rex_b1896` vs `Gater, B. A. R___Straits Settlements___1931`

- [PASS] surname_gate: bio 'GATER' vs stint 'Gater, B. A. R' (exact)
- [PASS] initials: bio ['B', 'A', 'R'] ~ stint ['B', 'A', 'R']
- [PASS] age_gate: stint starts 1931, birth 1896 (age 35)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1934
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

