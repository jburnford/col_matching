<!-- {"case_id": "case_rouse_robert-stuart_b1888", "bio_ids": ["rouse_robert-stuart_b1888"], "stint_ids": ["Rouse, S___Ceylon___1934"]} -->
# Dossier case_rouse_robert-stuart_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Rouse, S___Ceylon___1934` is also gate-compatible with biography(ies) outside this case: ['rouse_harold-stuart_b1888'] (already linked elsewhere or filtered).

## Biography `rouse_robert-stuart_b1888`

- Printed name: **ROUSE, ROBERT STUART**
- Birth year: 1888 (attested in editions [1927])
- Honours: A.M.I.C.E., C.E.
- Appears in editions: [1927]

### Verbatim printed entry text (OCR)

**Version `col1927-L62456.v` — printed in editions [1927]:**

> ROUSE, ROBERT STUART, C.E., A.M.I.C.E.—B. 1888; ed. Truro Coll. and Christ's Hosp.; survr., P.W.D., Hong Kong, Jan., 1912; engnr. drainage wks. office, Dec., 1913; transf. to gen. wks. office, P.W.D., Apr., 1915; ag. exec. engnr., G.W.O., Sept., 1915-16 and from Feb., 1921 to Oct., 1922; offr. in charge, G.W.O., May, 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | survr., P.W.D. | Hong Kong | [1927] |
| 1 | 1913 | engnr. drainage wks. office | — | [1927] |
| 2 | 1915 | transf. to gen. wks. office, P.W.D. | — | [1927] |
| 3 | 1915–1922 | ag. exec. engnr., G.W.O. | — | [1927] |
| 4 | 1924 | offr. in charge, G.W.O. | — | [1927] |

## Candidate stint `Rouse, S___Ceylon___1934`

- Staff-list name: **Rouse, S** | colony: **Ceylon** | listed 1934–1940 | editions [1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | S. Rouse | District Engineer | District Engineers | — | — |
| 1936 | S. Rouse | District Engineer | District Engineers | — | — |
| 1937 | S. Rouse | District Engineer | Public Works Department | — | — |
| 1940 | S. Rouse | District Engineer | Public Works Department | — | — |

### Deterministic checks: `rouse_robert-stuart_b1888` vs `Rouse, S___Ceylon___1934`

- [PASS] surname_gate: bio 'ROUSE' vs stint 'Rouse, S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1934, birth 1888 (age 46)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1940
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

