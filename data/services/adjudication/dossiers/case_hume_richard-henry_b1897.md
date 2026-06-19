<!-- {"case_id": "case_hume_richard-henry_b1897", "bio_ids": ["hume_richard-henry_b1897"], "stint_ids": ["Hume, R. H___Gold Coast___1932", "Hume, R. H___Tanganyika___1921"]} -->
# Dossier case_hume_richard-henry_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hume_richard-henry_b1897`

- Printed name: **HUME, RICHARD HENRY**
- Birth year: 1897 (attested in editions [1935, 1936, 1937, 1939])
- Appears in editions: [1935, 1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `dol1935-L59636.v` — printed in editions [1935, 1936, 1937, 1939]:**

> HUME, RICHARD HENRY.—B. 1897; Imp. post office, 1912-1919 (war serv. R.E. Signals, G.E.A., 1915-19); postmtr., Tanganyika Territory, 1919; senr. postmtr., do., 1923; dist. survr., posts and tels., Gold Coast, 1930; senr. survr., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912–1919 | Imp. post office | German East Africa | [1935, 1936, 1937, 1939] |
| 1 | 1919–1919 | postmtr. | Tanganyika Territory | [1935, 1936, 1937, 1939] |
| 2 | 1923–1923 | senr. postmtr. | Tanganyika Territory | [1935, 1936, 1937, 1939] |
| 3 | 1930–1930 | dist. survr., posts and tels. | Gold Coast | [1935, 1936, 1937, 1939] |
| 4 | 1937–1937 | senr. survr. | — | [1935, 1936, 1937, 1939] |

## Candidate stint `Hume, R. H___Gold Coast___1932`

- Staff-list name: **Hume, R. H** | colony: **Gold Coast** | listed 1932–1936 | editions [1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | R. H. Hume | District Surveyor | Posts and Telegraphs Department | — | — |
| 1934 | R. H. Hume | District Surveyor | Posts and Telegraphs Department | — | — |
| 1936 | R. H. Hume | Surveyor | Posts and Telegraph Department | — | — |

### Deterministic checks: `hume_richard-henry_b1897` vs `Hume, R. H___Gold Coast___1932`

- [PASS] surname_gate: bio 'HUME' vs stint 'Hume, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1932, birth 1897 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1936
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hume, R. H___Tanganyika___1921`

- Staff-list name: **Hume, R. H** | colony: **Tanganyika** | listed 1921–1925 | editions [1921, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | R. H. Hume | Postmasters | Post and Telegraphs Department | — | — |
| 1922 | R. H. Hume | Postmasters | Post and Telegraphs Department | — | — |
| 1923 | R. H. Hume | Postmasters | Post and Telegraphs Department | — | — |
| 1924 | R. H. Hume | Postmasters | Post and Telegraphs Department | — | — |
| 1925 | R. H. Hume | Postmasters | Post and Telegraphs Department | — | — |

### Deterministic checks: `hume_richard-henry_b1897` vs `Hume, R. H___Tanganyika___1921`

- [PASS] surname_gate: bio 'HUME' vs stint 'Hume, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1921, birth 1897 (age 24)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1925
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

