<!-- {"case_id": "case_strachan_peter-donald_b1872", "bio_ids": ["strachan_peter-donald_b1872"], "stint_ids": ["Strachan, Peter Donald___Basutoland___1924"]} -->
# Dossier case_strachan_peter-donald_b1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `strachan_peter-donald_b1872`

- Printed name: **STRACHAN, PETER DONALD**
- Birth year: 1872 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937])
- Honours: C.B.E (1934)
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1927-L63069.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]:**

> STRACHAN, PETER DONALD, C.B.E. (1934), M.D.—B. 1872; med. offr., Bechuana Land Prot., 1921-23; supt., Bauteiland leper asylum, 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921–1923 | med. offr. | Bechuana Land | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1923 | supt., Bauteiland leper asylum | Bechuana Land *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Strachan, Peter Donald___Basutoland___1924`

- Staff-list name: **Strachan, Peter Donald** | colony: **Basutoland** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | Peter Donald Strachan | Superintendent | Lepor Settlement | — | — |
| 1925 | Peter Donald Strachan | Superintendent | Leper Settlement | — | — |

### Deterministic checks: `strachan_peter-donald_b1872` vs `Strachan, Peter Donald___Basutoland___1924`

- [PASS] surname_gate: bio 'STRACHAN' vs stint 'Strachan, Peter Donald' (exact)
- [PASS] initials: bio ['P', 'D'] ~ stint ['P', 'D']
- [PASS] age_gate: stint starts 1924, birth 1872 (age 52)
- [FAIL] colony: no placed event resolves to 'Basutoland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1925
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

