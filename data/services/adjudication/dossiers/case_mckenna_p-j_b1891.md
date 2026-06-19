<!-- {"case_id": "case_mckenna_p-j_b1891", "bio_ids": ["mckenna_p-j_b1891"], "stint_ids": ["McKenna, Jno___Australia___1912"]} -->
# Dossier case_mckenna_p-j_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mckenna_p-j_b1891`

- Printed name: **MCKENNA, P. J**
- Birth year: 1891 (attested in editions [1931, 1932, 1934])
- Appears in editions: [1931, 1932, 1934]

### Verbatim printed entry text (OCR)

**Version `col1931-L66385.v` — printed in editions [1931, 1932, 1934]:**

> MCKENNA, P. J.—B. 1891; ed. Christian Bros. Schl., Belfast; warehouse supervisor, Nigeria, 1915; asst. traffic supt., Nigerian rly., 1918; ditto, 2nd grade, 1920; asst. divnl. supt. (traffic), 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | warehouse supervisor | Nigeria | [1931, 1932, 1934] |
| 1 | 1918 | asst. traffic supt., Nigerian rly | Nigeria *(inherited from previous clause)* | [1931, 1932, 1934] |
| 2 | 1920 | ditto, 2nd grade | Nigeria *(inherited from previous clause)* | [1931, 1932, 1934] |
| 3 | 1928 | asst. divnl. supt. (traffic) | Nigeria *(inherited from previous clause)* | [1931, 1932, 1934] |

## Candidate stint `McKenna, Jno___Australia___1912`

- Staff-list name: **McKenna, Jno** | colony: **Australia** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Jno. McKenna | Inspector | Police Department | — | — |
| 1913 | Jno. McKenna | Inspector | Police Department | — | — |

### Deterministic checks: `mckenna_p-j_b1891` vs `McKenna, Jno___Australia___1912`

- [PASS] surname_gate: bio 'MCKENNA' vs stint 'McKenna, Jno' (exact)
- [PASS] initials: bio ['P', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1912, birth 1891 (age 21)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1913
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

