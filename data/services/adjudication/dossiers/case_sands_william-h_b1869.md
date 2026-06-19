<!-- {"case_id": "case_sands_william-h_b1869", "bio_ids": ["sands_william-h_b1869"], "stint_ids": ["Sands, W. H___Bahamas___1918"]} -->
# Dossier case_sands_william-h_b1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sands_william-h_b1869`

- Printed name: **SANDS, WILLIAM H**
- Birth year: 1869 (attested in editions [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929])
- Appears in editions: [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929]

### Verbatim printed entry text (OCR)

**Version `col1918-L53931.v` — printed in editions [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929]:**

> SANDS, WILLIAM H.—B. 1869; pub. schl. teacher, Bahamas, 1889; Out Island comanr. (4th div.) and teacher, 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | pub. schl. teacher | Bahamas | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929] |
| 1 | 1917 | Out Island comanr. (4th div.) and teacher | Bahamas *(inherited from previous clause)* | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929] |

## Candidate stint `Sands, W. H___Bahamas___1918`

- Staff-list name: **Sands, W. H** | colony: **Bahamas** | listed 1918–1928 | editions [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | W. H. Sands | Commissioner, 4th Division | Commissioners of Out-Island Districts | — | — |
| 1919 | W. H. Sands | Commissioner, 4th Division | Commissioners of Out-Island Districts | — | — |
| 1920 | W. H. Sands | Commissioner, 4th Division | Commissioners of Out-Island Districts | — | — |
| 1921 | W. H. Sands | Commissioner, 4th Division | Commissioners of Out-Island Districts | — | — |
| 1922 | W. H. Sands | Commissioner, 4th Division | Commissioners of Out-Island Districts | — | — |
| 1923 | W. H. Sands | Commissioner, 3rd Division | Commissioners of Out-Island Districts | — | — |
| 1924 | W. H. Sands | Commissioner, 3rd Division | Commissioners of Out-Island Districts | — | — |
| 1925 | W. H. Sands | Commissioner, 3rd Division | Commissioners of Out-Island Districts | — | — |
| 1928 | W. H. Sands | Commissioners, Grade II | Out-Island Commissioners | — | — |

### Deterministic checks: `sands_william-h_b1869` vs `Sands, W. H___Bahamas___1918`

- [PASS] surname_gate: bio 'SANDS' vs stint 'Sands, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1918, birth 1869 (age 49)
- [PASS] colony: 2 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1918-1928
- [FAIL] position_sim: best 52 vs bar 60: 'Out Island comanr. (4th div.) and teacher' ~ 'Commissioner, 4th Division'
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

