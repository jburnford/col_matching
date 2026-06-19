<!-- {"case_id": "case_bloomburgh_joseph-hugh_b1867", "bio_ids": ["bloomburgh_joseph-hugh_b1867"], "stint_ids": ["Bloomburgh, J. H___British Somaliland___1917", "Bloomburgh, J. H___Sierra Leone___1927"]} -->
# Dossier case_bloomburgh_joseph-hugh_b1867

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bloomburgh_joseph-hugh_b1867`

- Printed name: **BLOOMBURGH, JOSEPH HUGH**
- Birth year: 1867 (attested in editions [1927, 1928])
- Honours: O.B.E.
- Appears in editions: [1927, 1928]

### Verbatim printed entry text (OCR)

**Version `col1927-L57264.v` — printed in editions [1927, 1928]:**

> BLOOMBURGH, CAPT. JOSEPH HUGH, O.B.E.—B. 1867; late King's Own Scottish Borderers, 1883-1906; 6th K.A.R., Somaliland, 1905-10; ch., Khartoum prov. civ. pol., 1910-16; coy. commdr. and qmr., Somaliland Camel Corps, 1915-19; asst. commdt., pol. and dir., prisons, Somaliland, 1919; Sudan med. and clasp, 1888, Gemaizah, Br. War med., Indian med. with clasp, Relief of Chitral, 1895, Punjab Frontier, 1897-98, and Tirah 1897-98, A.G.S. med., clasp, Somaliland, 1908, Mily. Serv. med. and Khodivilis Star.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883–1906 | late King's Own Scottish Borderers | — | [1927, 1928] |
| 1 | 1905–1910 | 6th K.A.R. | Somaliland | [1927, 1928] |
| 2 | 1910–1916 | ch., Khartoum prov. civ. pol. | Khartoum | [1927, 1928] |
| 3 | 1915–1919 | coy. commdr. and qmr., Somaliland Camel Corps | Somaliland | [1927, 1928] |
| 4 | 1919 | asst. commdt., pol. and dir., prisons | Somaliland | [1927, 1928] |

## Candidate stint `Bloomburgh, J. H___British Somaliland___1917`

- Staff-list name: **Bloomburgh, J. H** | colony: **British Somaliland** | listed 1917–1925 | editions [1917, 1918, 1919, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | J. H. Bloomburgh | Company Officer | Military Department | — | Lieut. |
| 1918 | J. H. Bloomburgh | Company Commanders | Military Department | — | Capt. |
| 1919 | J. H. Bloomburgh | Company Commanders | Military Department | — | Captain |
| 1922 | J. H. Bloomburgh | Assistant Commandant | Police | — | Capt. |
| 1923 | J. H. Bloomburgh | Assistant Commandant | Police | — | Capt. |
| 1924 | J. H. Bloomburgh | Assistant Commandant | Police | — | Captain |
| 1925 | J. H. Bloomburgh | Assistant Commandant | Police | — | Capt. |

### Deterministic checks: `bloomburgh_joseph-hugh_b1867` vs `Bloomburgh, J. H___British Somaliland___1917`

- [PASS] surname_gate: bio 'BLOOMBURGH' vs stint 'Bloomburgh, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1917, birth 1867 (age 50)
- [PASS] colony: 3 placed event(s) resolve to 'British Somaliland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1917-1925
- [FAIL] position_sim: best 44 vs bar 60: 'coy. commdr. and qmr., Somaliland Camel Corps' ~ 'Company Commanders'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Bloomburgh, J. H___Sierra Leone___1927`

- Staff-list name: **Bloomburgh, J. H** | colony: **Sierra Leone** | listed 1927–1928 | editions [1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | J. H. Bloomburgh | Assistant Commandant | Police | O.B.E. | Capt. |
| 1928 | J. H. Bloomburgh | Commandant | Police | — | Captain |

### Deterministic checks: `bloomburgh_joseph-hugh_b1867` vs `Bloomburgh, J. H___Sierra Leone___1927`

- [PASS] surname_gate: bio 'BLOOMBURGH' vs stint 'Bloomburgh, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1927, birth 1867 (age 60)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1928
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: O.B.E.
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

