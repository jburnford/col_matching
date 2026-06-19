<!-- {"case_id": "case_bateman_g-s_e1912", "bio_ids": ["bateman_g-s_e1912"], "stint_ids": ["Bateman, G. S___Uganda___1918"]} -->
# Dossier case_bateman_g-s_e1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bateman_g-s_e1912`

- Printed name: **BATEMAN, G. S.**
- Birth year: not printed
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1927-L57031.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]:**

> BATEMAN, G. S., L.D.S., R.S.G., Eng.—Serv. with Forces in E. Africa, 1915 and 1916; dental surg., Uganda, May, 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | dental surg. | Uganda | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1915–1916 | Serv. with Forces | East Africa | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Bateman, G. S___Uganda___1918`

- Staff-list name: **Bateman, G. S** | colony: **Uganda** | listed 1918–1923 | editions [1918, 1919, 1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | G. S. Bateman | Dental Surgeon | Medical | — | — |
| 1919 | G. S. Bateman | Dental Surgeon | Medical | — | — |
| 1921 | G. S. Bateman | Dental Surgeon | Medical | — | — |
| 1922 | G. S. Bateman | Dental Surgeon | Medical | — | — |
| 1923 | G. S. Bateman | Dental Surgeon | Medical | — | — |

### Deterministic checks: `bateman_g-s_e1912` vs `Bateman, G. S___Uganda___1918`

- [PASS] surname_gate: bio 'BATEMAN' vs stint 'Bateman, G. S' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G', 'S']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1923
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

