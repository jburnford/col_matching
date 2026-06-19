<!-- {"case_id": "case_facey_samuel-dyke_b1904", "bio_ids": ["facey_samuel-dyke_b1904"], "stint_ids": ["Facey, S. D___Northern Rhodesia___1936"]} -->
# Dossier case_facey_samuel-dyke_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `facey_samuel-dyke_b1904`

- Printed name: **FACEY, Samuel Dyke**
- Birth year: 1904 (attested in editions [1948, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32501.v` — printed in editions [1948, 1950, 1951]:**

> FACEY, Samuel Dyke.—b. 1904; ed. Blundell's Sch. and Balliol Coll., Oxford, B.A. (Oxon); cadet, N. Rhod., 1928; dist. offr., 1930.

**Version `col1949-L31934.v` — printed in editions [1949]:**

> FACEY'S, Samuel Dyke.—b. 1904; ed. Blundell's Sch. and Balliol Coll., Oxford, B.A. (Oxon); cadet, N. Rhod., 1928; dist. offr., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | cadet | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 1 | 1930 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Facey, S. D___Northern Rhodesia___1936`

- Staff-list name: **Facey, S. D** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | S. D. Facey | District Officers | District Administration | — | — |
| 1939 | S. D. Facey | District Officer | District Administration | — | — |
| 1940 | S. D. Facey | District Officer | District Administration | — | — |

### Deterministic checks: `facey_samuel-dyke_b1904` vs `Facey, S. D___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'FACEY' vs stint 'Facey, S. D' (exact)
- [PASS] initials: bio ['S', 'D'] ~ stint ['S', 'D']
- [PASS] age_gate: stint starts 1936, birth 1904 (age 32)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [PASS] position_sim: best 72 vs bar 60: 'dist. offr' ~ 'District Officer'
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

