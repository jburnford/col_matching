<!-- {"case_id": "case_wilde_gilbert_b1885", "bio_ids": ["wilde_gilbert_b1885"], "stint_ids": ["Wilde, G___Tanganyika___1922", "Wilde, O. G___Gold Coast___1927"]} -->
# Dossier case_wilde_gilbert_b1885

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['wilde_gilbert_b1885'] carry a single initial only — the namesake trap applies.

## Biography `wilde_gilbert_b1885`

- Printed name: **WILDE, GILBERT**
- Birth year: 1885 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L69572.v` — printed in editions [1940]:**

> WILDE, GILBERT.—B. 1885; ed. King Edward VI Gram. Schl., Birmingham, Mun. Tech. Schl., Birmingham, Merchant Venturers' Tech. Coll., Bristol; Br. P.O., engng. dept., Apr., 1913; Imp. serv., 1915-19; resumed duties in tech. sect., May, 1919; engnr. asst., P. & T. east half, Tanganjika Territory, Mar., 1921; tel. engnr., do., Apr., 1926; asst. tel. engnr., P. & T., F.M.S., June, 1926; engnr., P. & T., Oct., 1926; engnr., Negri Sembilan, Nov., 1927; ag. snr. engnr., Perak and Dindings, July, 1934; snr. engnr., P. & T., S.S. and F.M.S., Nov., 1937; divnl. engnr., P. & T., Perak, Mar., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | Br. P.O., engng. dept | — | [1940] |
| 1 | 1915–1919 | Imp. serv | — | [1940] |
| 2 | 1919 | resumed duties in tech. sect | — | [1940] |
| 3 | 1921 | engnr. asst., P. & T. east half, Tanganjika Territory | — | [1940] |
| 4 | 1926 | tel. engnr. | Dominions Office | [1940] |
| 5 | 1927 | engnr., Negri Sembilan | Federated Malay States *(inherited from previous clause)* | [1940] |
| 6 | 1934 | ag. snr. engnr., Perak and Dindings | Federated Malay States *(inherited from previous clause)* | [1940] |
| 7 | 1937 | snr. engnr., P. & T., S.S. and F.M.S | Straits Settlements | [1940] |
| 8 | 1938 | divnl. engnr., P. & T., Perak | Straits Settlements *(inherited from previous clause)* | [1940] |

## Candidate stint `Wilde, G___Tanganyika___1922`

- Staff-list name: **Wilde, G** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | G. Wilde | Engineering Assistants | Post and Telegraphs Department | — | — |
| 1923 | G. Wilde | Engineering Assistants | Post and Telegraphs Department | — | — |
| 1924 | G. Wilde | Engineering Assistants | Post and Telegraphs Department | — | — |
| 1925 | G. Wilde | Engineering Assistants | Post and Telegraphs Department | — | — |

### Deterministic checks: `wilde_gilbert_b1885` vs `Wilde, G___Tanganyika___1922`

- [PASS] surname_gate: bio 'WILDE' vs stint 'Wilde, G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1922, birth 1885 (age 37)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Wilde, O. G___Gold Coast___1927`

- Staff-list name: **Wilde, O. G** | colony: **Gold Coast** | listed 1927–1936 | editions [1927, 1928, 1929, 1930, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | O. G. Wilde | Medical Officers | Medical Department | — | — |
| 1928 | O. G. Wilde | Medical Officers | Medical Department | — | — |
| 1929 | O. G. Wilde | Medical Officers | Medical Department | — | — |
| 1930 | O. G. Wilde | Medical Officers | Medical Department | — | — |
| 1932 | O. G. Wilde | Medical Officer | Medical Department | — | — |
| 1934 | O. G. Wilde | Medical Officers | Medical Department | — | — |
| 1936 | O. G. Wilde | Medical Officers | Medical Department | — | — |

### Deterministic checks: `wilde_gilbert_b1885` vs `Wilde, O. G___Gold Coast___1927`

- [PASS] surname_gate: bio 'WILDE' vs stint 'Wilde, O. G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['O', 'G']
- [PASS] age_gate: stint starts 1927, birth 1885 (age 42)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1936
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

