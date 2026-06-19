<!-- {"case_id": "case_hurst_raymond-george_b1877", "bio_ids": ["hurst_raymond-george_b1877"], "stint_ids": ["Hurst, Geo___Falkland Islands___1906"]} -->
# Dossier case_hurst_raymond-george_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hurst, Geo___Falkland Islands___1906` is also gate-compatible with biography(ies) outside this case: ['hurst_george_e1885'] (already linked elsewhere or filtered).

## Biography `hurst_raymond-george_b1877`

- Printed name: **HURST, RAYMOND GEORGE**
- Birth year: 1877 (attested in editions [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1939])
- Appears in editions: [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1939]

### Verbatim printed entry text (OCR)

**Version `col1929-L61277.v` — printed in editions [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1939]:**

> HURST, RAYMOND GEORGE.—B. 1877; Indian State rlya., 1900; E. African rlya., 1917; asst. traffic supt., Tanganyika rlya., July, 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | Indian State rlya | — | [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1939] |
| 1 | 1917 | E. African rlya | — | [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1939] |
| 2 | 1925 | asst. traffic supt., Tanganyika rlya | Tanganyika | [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1939] |

## Candidate stint `Hurst, Geo___Falkland Islands___1906`

- Staff-list name: **Hurst, Geo** | colony: **Falkland Islands** | listed 1906–1910 | editions [1906, 1907, 1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | Geo. Hurst | Postmaster, Manager of Savings Bank, Registrar-General and Official Administrator | Civil Establishment | — | — |
| 1907 | Geo. Hurst | Postmaster, Manager of Savings Bank, Registrar-General and Official Administrator | Civil Establishment | — | — |
| 1909 | Geo. Hurst | Postmaster, Manager of Savings Bank, Registrar-General and Official Administrator | Civil Establishment | — | — |
| 1910 | Geo. Hurst | Postmaster, Manager of Savings Bank, Registrar-General and Official Administrator | Civil Establishment | — | — |

### Deterministic checks: `hurst_raymond-george_b1877` vs `Hurst, Geo___Falkland Islands___1906`

- [PASS] surname_gate: bio 'HURST' vs stint 'Hurst, Geo' (exact)
- [PASS] initials: bio ['R', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1906, birth 1877 (age 29)
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1910
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

