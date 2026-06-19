<!-- {"case_id": "case_bedington_cyril-a-m-i-c-e_b1889", "bio_ids": ["bedington_cyril-a-m-i-c-e_b1889"], "stint_ids": ["Babington, M___Cyprus___1929"]} -->
# Dossier case_bedington_cyril-a-m-i-c-e_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bedington_cyril-a-m-i-c-e_b1889`

- Printed name: **BEDINGTON, CYRIL A.M.I.C.E**
- Birth year: 1889 (attested in editions [1936])
- Honours: E.S.I, F.S.I
- Appears in editions: [1936]

### Verbatim printed entry text (OCR)

**Version `col1936-L58746.v` — printed in editions [1936]:**

> BEDINGTON, CYRIL A.M.I.C.E., F.S.I., M.I.M. & Cy.E., E.S.I., M.R.San.I., Chtd. Civ. Engrn. and Chtd. Survr.—B. 1889; ed. Univ. of Bristol; asst. engrn., P.W.D., F.M.S., July, 1913; exec. engrn., Ipoh, 1922; ag. senr. exec. engrn., Kuantan, 1927; addt. ch. hydrc. engrn.'s office, K. Lumpur, Nov., 1929; ag. senr. exec. engrn., waterworks, K. Lumpur, Oct., 1930; ar. exec. engrn., F.M.S. & S.S., Klang, 1932; sr. exec. engrn., wks. and bldgs., K. Lumpur, Apr., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | asst. engrn., P.W.D. | Federated Malay States | [1936] |
| 1 | 1922 | exec. engrn., Ipoh | Federated Malay States *(inherited from previous clause)* | [1936] |
| 2 | 1927 | ag. senr. exec. engrn., Kuantan | Federated Malay States *(inherited from previous clause)* | [1936] |
| 3 | 1929 | addt. ch. hydrc. engrn.'s office, K. Lumpur | Federated Malay States *(inherited from previous clause)* | [1936] |
| 4 | 1930 | ag. senr. exec. engrn., waterworks, K. Lumpur | Federated Malay States *(inherited from previous clause)* | [1936] |
| 5 | 1932 | ar. exec. engrn., F.M.S. & S.S., Klang | Federated Malay States *(inherited from previous clause)* | [1936] |
| 6 | 1934 | sr. exec. engrn., wks. and bldgs., K. Lumpur | Federated Malay States *(inherited from previous clause)* | [1936] |

## Candidate stint `Babington, M___Cyprus___1929`

- Staff-list name: **Babington, M** | colony: **Cyprus** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | M. Babington | Engineer | Public Works Department | — | — |
| 1930 | M. Babington | Engineer | Public Works Department | — | — |

### Deterministic checks: `bedington_cyril-a-m-i-c-e_b1889` vs `Babington, M___Cyprus___1929`

- [PASS] surname_gate: bio 'BEDINGTON' vs stint 'Babington, M' (fuzzy:2)
- [PASS] initials: bio ['C', 'A', 'M', 'I', 'C', 'E'] ~ stint ['M']
- [PASS] age_gate: stint starts 1929, birth 1889 (age 40)
- [FAIL] colony: no placed event resolves to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1930
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

