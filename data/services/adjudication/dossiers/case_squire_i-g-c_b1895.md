<!-- {"case_id": "case_squire_i-g-c_b1895", "bio_ids": ["squire_i-g-c_b1895"], "stint_ids": ["Squire, I. G. C___Zanzibar___1934"]} -->
# Dossier case_squire_i-g-c_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `squire_i-g-c_b1895`

- Printed name: **SQUIRE, I. G. C.**
- Birth year: 1895 (attested in editions [1957, 1958, 1959])
- Appears in editions: [1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1957-L27449.v` — printed in editions [1957, 1958, 1959]:**

> SQUIRE, I. G. C.—b. 1895; ed. Epsom Coll.; mil. serv., 1917–19; manager, plantations, S.L., 1928; Zanz., 1932; secon., debt sett., 1938–42, econ. control bd., 1942–43, clove control, 1950–51, fruit scheme, 1951; field offr., citrus fruit industry, 1952–58.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1919 | mil. serv. | — | [1957, 1958, 1959] |
| 1 | 1928 | manager, plantations | Sierra Leone | [1957, 1958, 1959] |
| 2 | 1932 | — | Zanzibar | [1957, 1958, 1959] |
| 3 | 1938–1942 | secon., debt sett. | — | [1957, 1958, 1959] |
| 4 | 1942–1943 | econ. control bd. | — | [1957, 1958, 1959] |
| 5 | 1950–1951 | clove control | — | [1957, 1958, 1959] |
| 6 | 1951 | fruit scheme | — | [1957, 1958, 1959] |
| 7 | 1952–1958 | field offr., citrus fruit industry | — | [1957, 1958, 1959] |

## Candidate stint `Squire, I. G. C___Zanzibar___1934`

- Staff-list name: **Squire, I. G. C** | colony: **Zanzibar** | listed 1934–1940 | editions [1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | I. G. C. Squire | Manager of Government Plantations | Agricultural Department | — | — |
| 1936 | I. G. C. Squire | Manager of Government Plantations | Agricultural Department | — | — |
| 1937 | I. G. C. Squire | Manager of Plantations | Agricultural Department | — | — |
| 1940 | I. G. C. Squire | Manager of Plantations | Agricultural Department | — | — |

### Deterministic checks: `squire_i-g-c_b1895` vs `Squire, I. G. C___Zanzibar___1934`

- [PASS] surname_gate: bio 'SQUIRE' vs stint 'Squire, I. G. C' (exact)
- [PASS] initials: bio ['I', 'G', 'C'] ~ stint ['I', 'G', 'C']
- [PASS] age_gate: stint starts 1934, birth 1895 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

