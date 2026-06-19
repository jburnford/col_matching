<!-- {"case_id": "case_oliver_stuart_e1885", "bio_ids": ["oliver_stuart_e1885"], "stint_ids": ["Oliver, F. P. S___Kenya___1922"]} -->
# Dossier case_oliver_stuart_e1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 32 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['oliver_stuart_e1885'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Oliver, F. P. S___Kenya___1922` is also gate-compatible with biography(ies) outside this case: ['oliver_frank_b1853'] (already linked elsewhere or filtered).

## Biography `oliver_stuart_e1885`

- Printed name: **OLIVER, STUART**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L33282.v` — printed in editions [1894]:**

> OLIVER, STUART, L.R.C.P. (Lond.), L.S.A. (Lond.)—Ed. Dulwich Coll., King's Coll. (Lond.), and King's Coll. Hosp.; asst. house surgeon, Shrewsbury, 1885; govt. medl. offr., Fiji, May, 1889; supt. of colonial hosp. and med. offr., Suva, Oct., 1889; is also visiting surgeon, Suva prison.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885 | asst. house surgeon, Shrewsbury | — | [1894] |
| 1 | 1889 | govt. medl. offr. | Fiji | [1894] |

## Candidate stint `Oliver, F. P. S___Kenya___1922`

- Staff-list name: **Oliver, F. P. S** | colony: **Kenya** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | F. P. S. Oliver | Form School Teachers | Education | — | — |
| 1923 | F. P. S. Oliver | Farm School Teacher | Usain Gishu | — | — |
| 1924 | F. P. S. Oliver | Farm School Teacher | Education | — | — |
| 1925 | F. P. S. Oliver | Farm School Teachers | Education | — | — |

### Deterministic checks: `oliver_stuart_e1885` vs `Oliver, F. P. S___Kenya___1922`

- [PASS] surname_gate: bio 'OLIVER' vs stint 'Oliver, F. P. S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['F', 'P', 'S']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
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

