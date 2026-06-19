<!-- {"case_id": "case_man_alexander_e1860", "bio_ids": ["man_alexander_e1860"], "stint_ids": ["Man, Alexander___Trinidad___1894"]} -->
# Dossier case_man_alexander_e1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['man_alexander_e1860'] carry a single initial only — the namesake trap applies.

## Biography `man_alexander_e1860`

- Printed name: **MAN, ALEXANDER**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1898]

### Verbatim printed entry text (OCR)

**Version `col1894-L32881.v` — printed in editions [1894, 1896, 1898]:**

> MAN, COLONEL ALEXANDER.—Served with the field force under the late Brigadier Murray, R.A.; employed on the 80-mile radius round Shanghai during the summer of 1868 (medal); also with the Anglo-Chinese contingent in Colonel Gordon's Taeping campaigns of 1860-64, being present during the operations before Soochow, and the siege and storming of Chang-chow (Chinese medal and Precious Star 2nd class); in 1868-69 was stationed in Formosa, and assisted the U.S. Consul and Mr. W. A. Pickering, C.M.G., in concluding a friendly settlement with the savage tribes; took part in the negotiations at Fort Zelandia and withdrawal of British force (thanked in despatches); selected in 1873 to raise a corps of military police for the Treaty district of Newchwang, Southern Manchuria, at that time infested by mounted banditti, and subsequently commanded the force embodied (thanks of the British and Italian ministers, and of the Imperial High Commissioner, with the brevet of colonel in the Chinese army, and the cross of the Italian Crown, 4th class); served with the Nile expedition of 1884-45, as boat officer and staff officer, and afterwards as commandant at Dal (medal with clasps and Khedive's star); A.D.C. to General Valentine Baker, Pasha, in 1885, and actg. dep. inspr.-general of gendarmerie in 1886-7-8 (thanks of Egyptian Government, and Order of the Osmanliah, 4th class); comdt. of local forces, Trinidad and Tobago, 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860–1864 | with the Anglo-Chinese contingent in Colonel Gordon's Taeping campaigns | — | [1894, 1896, 1898] |
| 1 | 1868–1868 | employed on the 80-mile radius round Shanghai | — | [1894, 1896, 1898] |
| 2 | 1868–1869 | stationed | Formosa | [1894, 1896, 1898] |
| 3 | 1873 | selected to raise a corps of military police for the Treaty district of Newchwang, Southern Manchuria, and subsequently commanded the force embodied | — | [1894, 1896, 1898] |
| 4 | 1884–1885 | boat officer and staff officer, and afterwards as commandant | — | [1894, 1896, 1898] |
| 5 | 1885–1888 | A.D.C. and actg. dep. inspr.-general of gendarmerie | — | [1894, 1896, 1898] |
| 6 | 1891–1891 | comdt. of local forces | Trinidad and Tobago | [1894, 1896, 1898] |

## Candidate stint `Man, Alexander___Trinidad___1894`

- Staff-list name: **Man, Alexander** | colony: **Trinidad** | listed 1894–1896 | editions [1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | Alexander Man | Commandant | Military Department | — | Colonel |
| 1896 | Alexander Man | Commandant | Military Department | — | Colonel |

### Deterministic checks: `man_alexander_e1860` vs `Man, Alexander___Trinidad___1894`

- [PASS] surname_gate: bio 'MAN' vs stint 'Man, Alexander' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1896
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

