<!-- {"case_id": "case_hofwood_francis-john-stephens_b1860", "bio_ids": ["hofwood_francis-john-stephens_b1860"], "stint_ids": ["Horwood, F. J___Trinidad and Tobago___1922"]} -->
# Dossier case_hofwood_francis-john-stephens_b1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hofwood_francis-john-stephens_b1860`

- Printed name: **HOFWOOD, FRANCIS JOHN STEPHENS**
- Birth year: 1860 (attested in editions [1907])
- Honours: C.B. (1895), C.M.G. (1893), K.C.B. (1901), K.C.M.G. (1906)
- Appears in editions: [1907]

### Verbatim printed entry text (OCR)

**Version `col1907-L44953.v` — printed in editions [1907]:**

> HOFWOOD, SIR FRANCIS JOHN STEPHENS.—B. 1860; K.C.B., 1901; K.C.M.G., 1906; C.B., 1895; C.M.G., 1893; barrister-at-law, Lincoln's Inn; solr., 1882; astl. law clk. to Bd. of T., 1885; astl. solr., ditto, 1888; priv. sec. to pres. of Bd. of T., 1892; sec. of rly. dept., 1893; perm. sec. to Bd. of T., 1901; perm. under-sec. of S. for the colonies, Jan., 1907; founded hospital and medical service for Canadian and Newfoundland fishermen; was hon. sec. to chmn. of H. of C. comttee on Jameson raid; Brit. deleg. to internat. rly. congress in London, 1895; ditto, Paris, 1900; was also mem. of London traffic comsnr., and Transvaal constitution coman., 1906; is registr. of Order of St. Michael and St. George.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | solr. | — | [1907] |
| 1 | 1885 | astl. law clk. to Bd. of T. | — | [1907] |
| 2 | 1888 | astl. solr. | — | [1907] |
| 3 | 1892 | priv. sec. to pres. of Bd. of T. | — | [1907] |
| 4 | 1893 | sec. of rly. dept. | — | [1907] |
| 5 | 1895 | Brit. deleg. to internat. rly. congress | — | [1907] |
| 6 | 1900 | ditto | — | [1907] |
| 7 | 1901 | perm. sec. to Bd. of T. | — | [1907] |
| 8 | 1906 | mem. of London traffic comsnr., and Transvaal constitution coman. | Transvaal | [1907] |
| 9 | 1907 | perm. under-sec. of S. for the colonies | — | [1907] |

## Candidate stint `Horwood, F. J___Trinidad and Tobago___1922`

- Staff-list name: **Horwood, F. J** | colony: **Trinidad and Tobago** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | F. J. Horwood | Assistant Engineer of Works | Public Works Department | — | — |
| 1923 | F. J. Horwood | Assistant Engineer of Works | Public Works Department | — | — |

### Deterministic checks: `hofwood_francis-john-stephens_b1860` vs `Horwood, F. J___Trinidad and Tobago___1922`

- [PASS] surname_gate: bio 'HOFWOOD' vs stint 'Horwood, F. J' (fuzzy:1)
- [PASS] initials: bio ['F', 'J', 'S'] ~ stint ['F', 'J']
- [PASS] age_gate: stint starts 1922, birth 1860 (age 62)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
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

