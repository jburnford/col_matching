<!-- {"case_id": "case_shipman_victor-heugh_b1912", "bio_ids": ["shipman_victor-heugh_b1912"], "stint_ids": ["Shipman, V. H___Northern Rhodesia___1949"]} -->
# Dossier case_shipman_victor-heugh_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `shipman_victor-heugh_b1912`

- Printed name: **SHIPMAN, Victor Heugh**
- Birth year: 1912 (attested in editions [1951])
- Honours: B.A
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L42465.v` — printed in editions [1951]:**

> SHIPMAN, Victor Heugh, B.A., B.Sc.—b. 1912; ed. St. Joseph Coll., Cape Town (medallist), Univ. of Cape Town (sec. teach. dip. educ.) and Rhodes Univ. Coll., S.A.; on mil. serv., 1940-43; mstr., European educ. dept., N. Rhod., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | mstr., European educ. dept. | Northern Rhodesia | [1951] |

## Candidate stint `Shipman, V. H___Northern Rhodesia___1949`

- Staff-list name: **Shipman, V. H** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | V. H. Shipman | Master | Education | — | — |
| 1951 | V. H. Shipman | Master | Education | — | — |

### Deterministic checks: `shipman_victor-heugh_b1912` vs `Shipman, V. H___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'SHIPMAN' vs stint 'Shipman, V. H' (exact)
- [PASS] initials: bio ['V', 'H'] ~ stint ['V', 'H']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

