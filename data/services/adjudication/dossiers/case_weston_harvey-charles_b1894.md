<!-- {"case_id": "case_weston_harvey-charles_b1894", "bio_ids": ["weston_harvey-charles_b1894"], "stint_ids": ["Weston, H. C___Gold Coast___1930"]} -->
# Dossier case_weston_harvey-charles_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `weston_harvey-charles_b1894`

- Printed name: **WESTON, HARVEY CHARLES**
- Birth year: 1894 (attested in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: A.M.I.C.E
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1931-L69267.v` — printed in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> WESTON, HARVEY CHARLES, B.Sc. (Eng.), A.M.I.C.E.—B. 1894; ed. Chatham House Schl., Ramagata, Goldsmiths Training Coll., Univ. of Lond., Glasgow Univ., and Royal Tech. Coll., Glasgow; war serv., 1914-19; ch. ass't engrmr., Zanzibar, 1921; res. engrmr., Dar-es-Salam, 1925; prin., Acro Tech. Schl., May, 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | ch. ass't engrmr. | Zanzibar | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1925 | res. engrmr., Dar-es-Salam | Zanzibar *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1929 | prin., Acro Tech. Schl | Zanzibar *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Weston, H. C___Gold Coast___1930`

- Staff-list name: **Weston, H. C** | colony: **Gold Coast** | listed 1930–1936 | editions [1930, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | H. C. Weston | Principal | Accra Technical School | — | — |
| 1932 | H. C. Weston | Principal | Education Department | — | — |
| 1934 | H. C. Weston | Principal | Education Department | — | — |
| 1936 | H. C. Weston | Principal | Accra Technical School | — | — |

### Deterministic checks: `weston_harvey-charles_b1894` vs `Weston, H. C___Gold Coast___1930`

- [PASS] surname_gate: bio 'WESTON' vs stint 'Weston, H. C' (exact)
- [PASS] initials: bio ['H', 'C'] ~ stint ['H', 'C']
- [PASS] age_gate: stint starts 1930, birth 1894 (age 36)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1936
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

