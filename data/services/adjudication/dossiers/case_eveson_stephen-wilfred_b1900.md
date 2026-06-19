<!-- {"case_id": "case_eveson_stephen-wilfred_b1900", "bio_ids": ["eveson_stephen-wilfred_b1900"], "stint_ids": ["Eveson, S. W___Straits Settlements___1931"]} -->
# Dossier case_eveson_stephen-wilfred_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `eveson_stephen-wilfred_b1900`

- Printed name: **EVESON, STEPHEN WILFRED**
- Birth year: 1900 (attested in editions [1937, 1940])
- Appears in editions: [1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L60655.v` — printed in editions [1937, 1940]:**

> EVESON, STEPHEN WILFRED, M.R.C.S. (Eng.), L.R.C.P. (Lond.), D.P.H. (R.C.P. & S., F.R.S.S., Certif., Schl. of Trop., Med. and Hyg., B. 1900; clin. asst., ven. dis. clin. (L.C.C.), Lond. Hosp., 1924-26; med. offr., S.S., July, 1926; health offr., Malacca, Feb., 1926 and Dec., 1927; do., Kedah, Sept., 1927; do., S'pore, Dec., 1931; health offr., B. Padang and L. Perak, Sept., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924–1926 | clin. asst., ven. dis. clin. (L.C.C.) | London | [1937, 1940] |
| 1 | 1926–1926 | med. offr. | Straits Settlements | [1937, 1940] |
| 2 | 1926–1927 | health offr. | Malacca | [1937, 1940] |
| 3 | 1927–1927 | health offr. | Kedah | [1937, 1940] |
| 4 | 1931–1931 | health offr. | Singapore | [1937, 1940] |
| 5 | 1934–1934 | health offr. | Batang Padang and Lower Perak | [1937, 1940] |

## Candidate stint `Eveson, S. W___Straits Settlements___1931`

- Staff-list name: **Eveson, S. W** | colony: **Straits Settlements** | listed 1931–1939 | editions [1931, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | S. W. Eveson | Medical and Health Officer | Medical | — | — |
| 1933 | S. W. Eveson | Medical and Health Officer | Medical | — | — |
| 1934 | S. W. Eveson | Senior Health Officer | Penang | — | — |
| 1934 | S. W. Eveson | Medical and Health Officer | Singapore | — | — |
| 1936 | S. W. Eveson | Senior Health Officer | Medical | — | — |
| 1939 | S. W. Eveson | Supercase Medical Officer, Grade B. | Medical | — | — |

### Deterministic checks: `eveson_stephen-wilfred_b1900` vs `Eveson, S. W___Straits Settlements___1931`

- [PASS] surname_gate: bio 'EVESON' vs stint 'Eveson, S. W' (exact)
- [PASS] initials: bio ['S', 'W'] ~ stint ['S', 'W']
- [PASS] age_gate: stint starts 1931, birth 1900 (age 31)
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1939
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

