<!-- {"case_id": "case_noble_james-morton_b1890", "bio_ids": ["noble_james-morton_b1890"], "stint_ids": ["Noble, Joseph___Straits Settlements___1922"]} -->
# Dossier case_noble_james-morton_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Noble, Joseph___Straits Settlements___1922` is also gate-compatible with biography(ies) outside this case: ['noble_john_e1865'] (already linked elsewhere or filtered).

## Biography `noble_james-morton_b1890`

- Printed name: **NOBLE, JAMES MORTON**
- Birth year: 1890 (attested in editions [1936, 1937, 1939, 1940])
- Appears in editions: [1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L63380.v` — printed in editions [1936, 1937, 1939, 1940]:**

> NOBLE, CAPT. JAMES MORTON, A.M.I.C.E., Chtd. Civ. Engnr.—B., 1890; asst. engrnr., F.M.S., Nov., 1919; do., Kedah, Jan., 1920-Feb., 1924; exec. engrnr., F.M.S., Nov., 1928; ag. senr. exec. engrnr., various occasions, 1929-31 and 1934; senr. exec. engrnr., July, 1935; ag. state engrnr., Pahang, Jan., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | asst. engrnr. | Federated Malay States | [1936, 1937, 1939, 1940] |
| 1 | 1920–1924 | asst. engrnr. | Kedah | [1936, 1937, 1939, 1940] |
| 2 | 1928 | exec. engrnr. | Federated Malay States | [1936, 1937, 1939, 1940] |
| 3 | 1929–1934 | ag. senr. exec. engrnr. | — | [1936, 1937, 1939, 1940] |
| 4 | 1935 | senr. exec. engrnr. | — | [1936, 1937, 1939, 1940] |
| 5 | 1938 | ag. state engrnr. | Pahang | [1936, 1937, 1939, 1940] |

## Candidate stint `Noble, Joseph___Straits Settlements___1922`

- Staff-list name: **Noble, Joseph** | colony: **Straits Settlements** | listed 1922–1931 | editions [1922, 1923, 1925, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | Joseph Noble | Acting Consul | SINGAPORE | — | — |
| 1923 | Joseph Noble | Acting-Consul | SINGAPORE | — | — |
| 1925 | Joseph Noble | Acting-Consul | Consular Service | — | — |
| 1931 | J M Noble | Executive Engineers | PUBLIC WORKS | — | — |

### Deterministic checks: `noble_james-morton_b1890` vs `Noble, Joseph___Straits Settlements___1922`

- [PASS] surname_gate: bio 'NOBLE' vs stint 'Noble, Joseph' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J']
- [PASS] age_gate: stint starts 1922, birth 1890 (age 32)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1931
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

