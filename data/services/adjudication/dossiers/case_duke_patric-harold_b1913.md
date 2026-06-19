<!-- {"case_id": "case_duke_patric-harold_b1913", "bio_ids": ["duke_patric-harold_b1913"], "stint_ids": ["Duke, P. H___Barbados___1949"]} -->
# Dossier case_duke_patric-harold_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 19 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `duke_patric-harold_b1913`

- Printed name: **DUKE, Patric Harold**
- Birth year: 1913 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L37739.v` — printed in editions [1951]:**

> DUKE, Patric Harold.—b. 1913; ed. Bedford Sch.; appt. police, Pal., 1934; Barb., 1943; asst. supt., police, G.C., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | appt. police | Palestine | [1951] |
| 1 | 1943 | appt. police | Barbados | [1951] |
| 2 | 1950 | asst. supt., police | Gold Coast | [1951] |

## Candidate stint `Duke, P. H___Barbados___1949`

- Staff-list name: **Duke, P. H** | colony: **Barbados** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. H. Duke | Superintendent | Police and Prisons | — | Captain |
| 1950 | P. H. Duke | Superintendents | Police and Prisons | — | Captain |

### Deterministic checks: `duke_patric-harold_b1913` vs `Duke, P. H___Barbados___1949`

- [PASS] surname_gate: bio 'DUKE' vs stint 'Duke, P. H' (exact)
- [PASS] initials: bio ['P', 'H'] ~ stint ['P', 'H']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 24 vs bar 60: 'appt. police' ~ 'Superintendent'
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

