<!-- {"case_id": "case_stallard_charles-frampton_b1871", "bio_ids": ["stallard_charles-frampton_b1871"], "stint_ids": ["Stallard, C. F___South Africa___1912"]} -->
# Dossier case_stallard_charles-frampton_b1871

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stallard_charles-frampton_b1871`

- Printed name: **STALLARD, Charles Frampton**
- Birth year: 1871 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L68628.v` — printed in editions [1940]:**

> STALLARD, Charles Frampton.—B. 1871; ed. St. Edward's Schil. and Merton Coll., Oxford; Grays Inn (Holt schil.); called to bar, 1895; S. African War, 1900-02; advoc., Union of S. Africa; K.C., 1910; prov. coun., Transvaal, 1910-13; Great War, S.W. Africa, 1914-16, Flanders and Italy, 1916-18 (D.S.O., M.C., ment. in desps. three times); lieut.-col.: M.P. for Roodepoort, 1929-38; Pietermaritzburg, 1939; min. of mines, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895–1895 | called to bar | — | [1940] |
| 1 | 1900–1902 | S. African War | — | [1940] |
| 2 | 1910–1910 | K.C. | — | [1940] |
| 3 | 1910–1913 | prov. coun. | Transvaal | [1940] |
| 4 | 1914–1916 | Great War | South West Africa | [1940] |
| 5 | 1916–1918 | — | — | [1940] |
| 6 | 1929–1938 | M.P. for Roodepoort | — | [1940] |
| 7 | 1939–1939 | — | — | [1940] |
| 8 | 1939–1939 | min. of mines | — | [1940] |

## Candidate stint `Stallard, C. F___South Africa___1912`

- Staff-list name: **Stallard, C. F** | colony: **South Africa** | listed 1912–1914 | editions [1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | C. F. Stallard | Elected Member | Provincial Council of the Transvaal | — | — |
| 1914 | C. F. Stallard | Elected Member | Provincial Council of the Transvaal | — | — |

### Deterministic checks: `stallard_charles-frampton_b1871` vs `Stallard, C. F___South Africa___1912`

- [PASS] surname_gate: bio 'STALLARD' vs stint 'Stallard, C. F' (exact)
- [PASS] initials: bio ['C', 'F'] ~ stint ['C', 'F']
- [PASS] age_gate: stint starts 1912, birth 1871 (age 41)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
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

