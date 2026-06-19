<!-- {"case_id": "case_macrae_farquhar-bailoi_b1903", "bio_ids": ["macrae_farquhar-bailoi_b1903"], "stint_ids": ["Macrae, F. B___Northern Rhodesia___1936"]} -->
# Dossier case_macrae_farquhar-bailoi_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `macrae_farquhar-bailoi_b1903`

- Printed name: **MACRAE, Farquhar Bailoi**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L34423.v` — printed in editions [1948, 1949, 1950, 1951]:**

> MACRAE, Farquhar Bailoi.—b. 1903; ed. Haileybury and Camb. Univ., B.A. (Cantab.), F.R.A.I.; probr., N. Rhod., 1925; dist. offr., 1927; senr., 1950; author of articles on archaeology and anthropology.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | probr. | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 1 | 1927 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1950 | senr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Macrae, F. B___Northern Rhodesia___1936`

- Staff-list name: **Macrae, F. B** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | F. B. Macrae | District Officers | District Administration | — | — |
| 1939 | F. B. Macrae | District Officer | District Administration | — | — |
| 1940 | F. B. Macrae | District Officer | District Administration | — | — |

### Deterministic checks: `macrae_farquhar-bailoi_b1903` vs `Macrae, F. B___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'MACRAE' vs stint 'Macrae, F. B' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F', 'B']
- [PASS] age_gate: stint starts 1936, birth 1903 (age 33)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
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

