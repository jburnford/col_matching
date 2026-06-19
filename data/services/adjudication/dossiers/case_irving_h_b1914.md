<!-- {"case_id": "case_irving_h_b1914", "bio_ids": ["irving_h_b1914"], "stint_ids": ["Irving, T. H___Nigeria___1929"]} -->
# Dossier case_irving_h_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['irving_h_b1914'] carry a single initial only — the namesake trap applies.

## Biography `irving_h_b1914`

- Printed name: **IRVING, H**
- Birth year: 1914 (attested in editions [1959, 1960])
- Appears in editions: [1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1959-L24519.v` — printed in editions [1959, 1960]:**

> IRVING, H.—b. 1914; Central Collegiate Inst., London, Ont., and Ontario Agric. Coll., Univ. of Toronto; mil. serv., 1939-47; agric. chemist, Nig., 1948; N. Nig., 1954; senr. specialist offr., 1954; prin. research offr., 1958-59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | agric. chemist | Nigeria | [1959, 1960] |
| 1 | 1954 | agric. chemist | Northern Nigeria | [1959, 1960] |
| 2 | 1958–1959 | prin. research offr | Northern Nigeria *(inherited from previous clause)* | [1959, 1960] |

## Candidate stint `Irving, T. H___Nigeria___1929`

- Staff-list name: **Irving, T. H** | colony: **Nigeria** | listed 1929–1936 | editions [1929, 1930, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | T. H. Irving | Commissioners and Assistant Commissioners | Marine | M.C. | Captain |
| 1930 | Capt. T. H. Irving | Commissioners and Assistant Commissioners | Police | — | Captain |
| 1933 | T. H. Irving | Commissioner/Assistant Commissioner | Police | — | Captain |
| 1934 | T. H. Irving | Commissioner/Assistant Commissioner | Police | — | Captain |
| 1936 | T. H. Irving | Commissioners and Assistant Commissioners | Police | — | Captain |

### Deterministic checks: `irving_h_b1914` vs `Irving, T. H___Nigeria___1929`

- [PASS] surname_gate: bio 'IRVING' vs stint 'Irving, T. H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['T', 'H']
- [PASS] age_gate: stint starts 1929, birth 1914 (age 15)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1936
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

