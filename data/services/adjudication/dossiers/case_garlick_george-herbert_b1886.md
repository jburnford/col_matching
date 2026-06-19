<!-- {"case_id": "case_garlick_george-herbert_b1886", "bio_ids": ["garlick_george-herbert_b1886"], "stint_ids": ["Garlick, G. H___Straits Settlements___1925"]} -->
# Dossier case_garlick_george-herbert_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `garlick_george-herbert_b1886`

- Printed name: **GARLICK, George Herbert**
- Birth year: 1886 (attested in editions [1932, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L60394.v` — printed in editions [1932, 1934, 1935, 1936, 1937, 1939, 1940]:**

> GARLICK, George Herbert, M.R.C.S. (Eng.), L.R.C.P. (Lond.), D.M.R.E. (Camb.).—B. 1886; med. offr., Johore, 1917; Malayan med. serv., 1923; ag. prin., med. offr., Johore, 1924, 1927 and 1931; physician and radiologist, Johore, 1927; prin. med. offr., 1934; Johore rep. at Far Eastern Cong., trop. med., Nanking, Sept., 1934.

**Version `col1933-L60045.v` — printed in editions [1933]:**

> GARLICK, George Herbert, M.R.C.S. (Eng.), L.R.C.P. (London), D.M.R.E. (Cambridge).—B. 1886; medical officer, Johore, 1917; Malayan medical service, 1923; assistant principal medical officer, Johore, 1924; physician and radiologist, Johore, 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1917 | med. offr. | Johore | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1923–1923 | Malayan med. serv. | Malaya | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1924–1931 | ag. prin., med. offr. | Johore | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1927–1927 | physician and radiologist | Johore | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1934–1934 | prin. med. offr. | — | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1934–1934 | Johore rep. at Far Eastern Cong., trop. med. | Johore | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Garlick, G. H___Straits Settlements___1925`

- Staff-list name: **Garlick, G. H** | colony: **Straits Settlements** | listed 1925–1932 | editions [1925, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | G. H. Garlick | Medical Officer (seconded to Unfederated Malay States) | LABUAN | — | — |
| 1932 | G. H. Garlick | Medical Officers | Medical | — | — |

### Deterministic checks: `garlick_george-herbert_b1886` vs `Garlick, G. H___Straits Settlements___1925`

- [PASS] surname_gate: bio 'GARLICK' vs stint 'Garlick, G. H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1925, birth 1886 (age 39)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1932
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

