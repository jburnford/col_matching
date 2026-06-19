<!-- {"case_id": "case_gagan_arthur-ernest_b1897", "bio_ids": ["gagan_arthur-ernest_b1897"], "stint_ids": ["Gagan, A. E___British Guiana___1925"]} -->
# Dossier case_gagan_arthur-ernest_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gagan_arthur-ernest_b1897`

- Printed name: **GAGAN, Arthur Ernest**
- Birth year: 1897 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32729.v` — printed in editions [1948, 1949, 1950, 1951]:**

> GAGAN, Arthur Ernest.—b. 1897; ed. Wandsworth Tech. Inst., London; wireless operator; Br. Guiana, 1922; wireless engnr., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | — | British Guiana | [1948, 1949, 1950, 1951] |
| 1 | 1928 | wireless engnr | British Guiana *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Gagan, A. E___British Guiana___1925`

- Staff-list name: **Gagan, A. E** | colony: **British Guiana** | listed 1925–1939 | editions [1925, 1927, 1928, 1929, 1930, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | A. Gagan | Superintendent | Wireless Department | — | — |
| 1927 | A. Gagan | Superintendent | Wireless Department | — | — |
| 1928 | A. Gagan | Superintendent | Wireless Department | — | — |
| 1929 | A. E. Gagan | Wireless Engineer | Post Office, Engineering Branch | — | — |
| 1930 | A. E. Gagan | Wireless Engineer | Engineering Branch | — | — |
| 1939 | A. E. Gagan | Engineer | Post Office, Telecommunications Branch | — | — |

### Deterministic checks: `gagan_arthur-ernest_b1897` vs `Gagan, A. E___British Guiana___1925`

- [PASS] surname_gate: bio 'GAGAN' vs stint 'Gagan, A. E' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1925, birth 1897 (age 28)
- [PASS] colony: 2 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1925-1939
- [PASS] position_sim: best 90 vs bar 60: 'wireless engnr' ~ 'Wireless Engineer'
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

