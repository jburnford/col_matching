<!-- {"case_id": "case_fawcett_arthur-edward_b1890", "bio_ids": ["fawcett_arthur-edward_b1890"], "stint_ids": ["Fawcett, A___British Guiana___1921"]} -->
# Dossier case_fawcett_arthur-edward_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Fawcett, A___British Guiana___1921` is also gate-compatible with biography(ies) outside this case: ['fawcett_j-f-st-a_e1910', 'fawcett_j-f-st-a_e1910-2', 'fawcett_x_e1885', 'fawoett_j-f-sr-a_e1910'] (already linked elsewhere or filtered).

## Biography `fawcett_arthur-edward_b1890`

- Printed name: **FAWCETT, ARTHUR EDWARD**
- Birth year: 1890 (attested in editions [1936, 1937, 1939, 1940])
- Honours: A.M.I.C.E, B.A
- Appears in editions: [1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L60612.v` — printed in editions [1936, 1937, 1939, 1940]:**

> FAWCETT, CAPT. ARTHUR EDWARD, B.A., B.A.I. (Dublin), A.M.I.C.E., Chtd. Civ. Engrnr.—B. 1890; war serv., 1916-19, R.E., France, Persia, Afghanistan, ment. in des.; astt. engrnr., F.M.S. Rlys., Apr., 1920; dist. engrnr., Apr., 1925; do., grade I, Apr., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | astt. engrnr., F.M.S. Rlys | Federated Malay States | [1936, 1937, 1939, 1940] |
| 1 | 1925 | dist. engrnr | Federated Malay States *(inherited from previous clause)* | [1936, 1937, 1939, 1940] |
| 2 | 1929 | do., grade I | Federated Malay States *(inherited from previous clause)* | [1936, 1937, 1939, 1940] |

## Candidate stint `Fawcett, A___British Guiana___1921`

- Staff-list name: **Fawcett, A** | colony: **British Guiana** | listed 1921–1930 | editions [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | A. Fawcett | Bandmaster, Militia | Militia | — | Lieutenant |
| 1922 | A. Fawcett | Bandmaster, Militia | Militia | — | Lieutenant |
| 1923 | A. Fawcett | Bandmaster | Militia | — | — |
| 1924 | Lieut. A. Fawcett | Bandmaster | Militia | — | — |
| 1925 | A. Fawcett | Bandmaster | Militia | — | Captain |
| 1927 | A. Fawcett | Bandmaster, Militia | Militia | — | Captain |
| 1928 | Capt. A. Fawcett | Bandmaster | Militia | — | Captain |
| 1929 | A. Fawcett | Bandmaster, Militia | Militia | — | Captain |
| 1930 | Capt. A. Fawcett | Bandmaster, Militia | Militia | — | Captain |

### Deterministic checks: `fawcett_arthur-edward_b1890` vs `Fawcett, A___British Guiana___1921`

- [PASS] surname_gate: bio 'FAWCETT' vs stint 'Fawcett, A' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A']
- [PASS] age_gate: stint starts 1921, birth 1890 (age 31)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1930
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

