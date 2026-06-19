<!-- {"case_id": "case_bouloix_l-g_b1909", "bio_ids": ["bouloix_l-g_b1909"], "stint_ids": ["Bouloix, G___Mauritius___1928"]} -->
# Dossier case_bouloix_l-g_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bouloix_l-g_b1909`

- Printed name: **BOULOIX, L. G**
- Birth year: 1909 (attested in editions [1961])
- Appears in editions: [1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1961-L19969.v` — printed in editions [1961]:**

> BOULOIX, L. G.—b. 1909; ed. Royal Coll., Maur.; clk., Maur., 1931; 2nd gr., 1933; 1st gr., 1945; asst. sec., devel. and welfare, 1948; asst. public assist. comsnr., 1951; estab. offr., 1952; prin. asst. sec., 1958.

**Version `col1962-L19031.v` — printed in editions [1962, 1963]:**

> BOULOUX, L. G.—b. 1909; ed. Royal Coll., Maur.; clk., Maur., 1931; 2nd gr., 1933; 1st gr., 1945; asst. sec., devel. and welfare, 1948; asst. public assist. comsnr., 1951; estab. offr., 1952; prin. asst. sec., 1958-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | clk. | Mauritius | [1961, 1962, 1963] |
| 1 | 1933 | 2nd gr | Mauritius *(inherited from previous clause)* | [1961, 1962, 1963] |
| 2 | 1945 | 1st gr | Mauritius *(inherited from previous clause)* | [1961, 1962, 1963] |
| 3 | 1948 | asst. sec., devel. and welfare | Mauritius *(inherited from previous clause)* | [1961, 1962, 1963] |
| 4 | 1951 | asst. public assist. comsnr | Mauritius *(inherited from previous clause)* | [1961, 1962, 1963] |
| 5 | 1952 | estab. offr | Mauritius *(inherited from previous clause)* | [1961, 1962, 1963] |
| 6 | 1958 | prin. asst. sec | Mauritius *(inherited from previous clause)* | [1961, 1962, 1963] |

## Candidate stint `Bouloix, G___Mauritius___1928`

- Staff-list name: **Bouloix, G** | colony: **Mauritius** | listed 1928–1929 | editions [1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | G. Bouloix | 3rd Class Clerk | District and Stipendiary Magistracies | — | — |
| 1929 | G. Bouloix | 3rd Class Clerk | District and Stipendiary Magistracies | — | — |

### Deterministic checks: `bouloix_l-g_b1909` vs `Bouloix, G___Mauritius___1928`

- [PASS] surname_gate: bio 'BOULOIX' vs stint 'Bouloix, G' (exact)
- [PASS] initials: bio ['L', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1928, birth 1909 (age 19)
- [PASS] colony: 7 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1929
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

