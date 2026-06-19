<!-- {"case_id": "case_bourdillon_victor-edmund_b1897", "bio_ids": ["bourdillon_victor-edmund_b1897"], "stint_ids": ["Bourdillon, V. E___Northern Rhodesia___1936"]} -->
# Dossier case_bourdillon_victor-edmund_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bourdillon_victor-edmund_b1897`

- Printed name: **BOURDILLON, Victor Edmund**
- Birth year: 1897 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L31304.v` — printed in editions [1948]:**

> BOURDILLON, Victor Edmund.—b.1897; ed. Brighton Coll.; on mil. serv. 1916–18, flt.-lieut.; probationer, B.S.A. Coy., 1922; asst. native comsnr., N. Rhod., 1924; dist. offr., gr. 3, 1929; gr. 2, 1934; gr. 1, 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | probationer, B.S.A. Coy | — | [1948] |
| 1 | 1924 | asst. native comsnr. | Northern Rhodesia | [1948] |
| 2 | 1929 | dist. offr., gr. 3 | Northern Rhodesia *(inherited from previous clause)* | [1948] |
| 3 | 1934 | gr. 2 | Northern Rhodesia *(inherited from previous clause)* | [1948] |
| 4 | 1942 | gr. 1 | Northern Rhodesia *(inherited from previous clause)* | [1948] |

## Candidate stint `Bourdillon, V. E___Northern Rhodesia___1936`

- Staff-list name: **Bourdillon, V. E** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | V. E. Bourdillon | District Officers | District Administration | — | — |
| 1939 | V. E. Bourdillon | District Officer | District Administration | — | — |
| 1940 | V. E. Bourdillon | District Officer | District Administration | — | — |

### Deterministic checks: `bourdillon_victor-edmund_b1897` vs `Bourdillon, V. E___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'BOURDILLON' vs stint 'Bourdillon, V. E' (exact)
- [PASS] initials: bio ['V', 'E'] ~ stint ['V', 'E']
- [PASS] age_gate: stint starts 1936, birth 1897 (age 39)
- [PASS] colony: 4 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 20 vs bar 60: 'gr. 2' ~ 'District Officer'
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

