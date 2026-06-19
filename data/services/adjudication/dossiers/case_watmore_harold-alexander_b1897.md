<!-- {"case_id": "case_watmore_harold-alexander_b1897", "bio_ids": ["watmore_harold-alexander_b1897"], "stint_ids": ["Watmore, H. A___Northern Rhodesia___1940"]} -->
# Dossier case_watmore_harold-alexander_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `watmore_harold-alexander_b1897`

- Printed name: **WATMORE, Harold Alexander**
- Birth year: 1897 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L36691.v` — printed in editions [1948, 1949]:**

> WATMORE, Harold Alexander.—b. 1897; ed. privately; on mil. serv. 1914-18, lieut.; prob., N. Rhod., 1921; asst. native comsnr., 1924; native comsnr., 1928; prov. comsnr., 1944; senr. prov. comsnr., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | prob. | Northern Rhodesia | [1948, 1949] |
| 1 | 1924 | asst. native comsnr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949] |
| 2 | 1928 | native comsnr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1944 | prov. comsnr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949] |
| 4 | 1947 | senr. prov. comsnr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Watmore, H. A___Northern Rhodesia___1940`

- Staff-list name: **Watmore, H. A** | colony: **Northern Rhodesia** | listed 1940–1948 | editions [1940, 1948]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | H. A. Watmore | District Officer | District Administration | — | — |
| 1948 | H. A. Watmore | Nominated Official Member | LEGISLATIVE COUNCIL | — | — |

### Deterministic checks: `watmore_harold-alexander_b1897` vs `Watmore, H. A___Northern Rhodesia___1940`

- [PASS] surname_gate: bio 'WATMORE' vs stint 'Watmore, H. A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1940, birth 1897 (age 43)
- [PASS] colony: 5 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1940-1948
- [FAIL] position_sim: best 38 vs bar 60: 'senr. prov. comsnr' ~ 'District Officer'
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

