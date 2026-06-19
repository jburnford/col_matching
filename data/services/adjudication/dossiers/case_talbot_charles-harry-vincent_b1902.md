<!-- {"case_id": "case_talbot_charles-harry-vincent_b1902", "bio_ids": ["talbot_charles-harry-vincent_b1902"], "stint_ids": ["Talbot, C. H. V___Bermuda___1927", "Talbot, C. H. V___Windward Islands___1948"]} -->
# Dossier case_talbot_charles-harry-vincent_b1902

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `talbot_charles-harry-vincent_b1902`

- Printed name: **TALBOT, CHARLES HARRY VINCENT**
- Birth year: 1902 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71065.v` — printed in editions [1939, 1940]:**

> TALBOT, CHARLES HARRY VINCENT.—B. 1902; ed. Dulwich Coll. & St. John's Coll., Oxford; ent. ch. sec.'s office, Bermuda, July, 1925; asst. col. sec., Feb., 1937; ag. col. sec., Mar.-Oct., 1937, July-Oct., 1938, Aug.-Oct., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | ent. ch. sec.'s office | Bermuda | [1939, 1940] |
| 1 | 1937 | asst. col. sec. | — | [1939, 1940] |

## Candidate stint `Talbot, C. H. V___Bermuda___1927`

- Staff-list name: **Talbot, C. H. V** | colony: **Bermuda** | listed 1927–1939 | editions [1927, 1928, 1929, 1930, 1932, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | C. H. V. Talbot | Junior Clerk | Colonial Secretary's Department | — | — |
| 1928 | C. H. V. Talbot | Junior Clerk | Colonial Secretary's Department | — | — |
| 1929 | C. H. V. Talbot | Junior Clerk | Senior Clerk and Clerk to Legislative Council | — | — |
| 1930 | C. H. V. Talbot | Senior Clerk and Clerk to Legislative Council | Colonial Secretary's Department | — | — |
| 1932 | C. H. V. Talbot | Senior Clerk and Clerk to Legislative Council | Colonial Secretary's Department | — | — |
| 1933 | C. H. V. Talbot | Senior Clerk and Clerk to Legislative Council | Colonial Secretary's Department | — | — |
| 1934 | C. H. V. Talbot | Senior Clerk and Clerk to Legislative Council | Colonial Secretary's Department | — | — |
| 1936 | C. H. V. Talbot | Senior Clerk and Clerk to Legislative Council | Colonial Secretary's Department | — | — |
| 1939 | C. H. V. Talbot | Assistant Colonial Secretary and Clerk to Executive Council | Colonial Secretary's Department | — | — |

### Deterministic checks: `talbot_charles-harry-vincent_b1902` vs `Talbot, C. H. V___Bermuda___1927`

- [PASS] surname_gate: bio 'TALBOT' vs stint 'Talbot, C. H. V' (exact)
- [PASS] initials: bio ['C', 'H', 'V'] ~ stint ['C', 'H', 'V']
- [PASS] age_gate: stint starts 1927, birth 1902 (age 25)
- [PASS] colony: 1 placed event(s) resolve to 'Bermuda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1939
- [FAIL] position_sim: best 32 vs bar 60: 'ent. ch. sec.'s office' ~ 'Senior Clerk and Clerk to Legislative Council'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Talbot, C. H. V___Windward Islands___1948`

- Staff-list name: **Talbot, C. H. V** | colony: **Windward Islands** | listed 1948–1950 | editions [1948, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1948 | C. H. V. Talbot | — | Administrators | — | — |
| 1950 | C. H. V. Talbot | — | Administrators | — | — |

### Deterministic checks: `talbot_charles-harry-vincent_b1902` vs `Talbot, C. H. V___Windward Islands___1948`

- [PASS] surname_gate: bio 'TALBOT' vs stint 'Talbot, C. H. V' (exact)
- [PASS] initials: bio ['C', 'H', 'V'] ~ stint ['C', 'H', 'V']
- [PASS] age_gate: stint starts 1948, birth 1902 (age 46)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1948-1950
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

