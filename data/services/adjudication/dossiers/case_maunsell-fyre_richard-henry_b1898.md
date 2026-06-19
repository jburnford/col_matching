<!-- {"case_id": "case_maunsell-fyre_richard-henry_b1898", "bio_ids": ["maunsell-fyre_richard-henry_b1898"], "stint_ids": ["Maunsell-Eyre, R. H___Nigeria___1929"]} -->
# Dossier case_maunsell-fyre_richard-henry_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `maunsell-fyre_richard-henry_b1898`

- Printed name: **MAUNSELL-FYRE, Richard Henry**
- Birth year: 1898 (attested in editions [1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1949-L34239.v` — printed in editions [1949]:**

> MAUNSELL-FYRE, Richard Henry.—b. 1898; ed. St. Columba's Coll., Rathfarnham Co., Dublin; on mil. serv., 1917-20, lieut.; dist. inspr., R.I.C., 1920-22; police, Nig., 1925; senr. asst. supt., 1932; supt., 1939.

**Version `col1948-L34581.v` — printed in editions [1948]:**

> MAUNSELL-EYRE, Richard Henry.—b. 1898; ed. St. Columbas Coll., Rathfarnham and Trinity Coll., Dublin; on mil. serv., 1917-20; lieut.; dist. inspr., R.I.C., 1920-22; cadet, Nig., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920–1922 | dist. inspr., R.I.C | — | [1948, 1949] |
| 1 | 1925 | police | Nigeria | [1948, 1949] |
| 2 | 1932 | senr. asst. supt | Nigeria *(inherited from previous clause)* | [1949] |
| 3 | 1939 | supt | Nigeria *(inherited from previous clause)* | [1949] |

## Candidate stint `Maunsell-Eyre, R. H___Nigeria___1929`

- Staff-list name: **Maunsell-Eyre, R. H** | colony: **Nigeria** | listed 1929–1939 | editions [1929, 1930, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | R. H. Maunsell-Eyre | Commissioners and Assistant Commissioners | Marine | — | — |
| 1930 | R. H. Maunsell-Eyre | Commissioners and Assistant Commissioners | Police | — | — |
| 1933 | R. H. Maunsell-Eyre | Commissioner/Assistant Commissioner | Police | — | — |
| 1934 | R. H. Maunsell-Eyre | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | R. H. Maunsell-Eyre | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | R. H. Maunsell-Eyre | Senior Assistant Superintendent | Police | — | — |

### Deterministic checks: `maunsell-fyre_richard-henry_b1898` vs `Maunsell-Eyre, R. H___Nigeria___1929`

- [PASS] surname_gate: bio 'MAUNSELL-FYRE' vs stint 'Maunsell-Eyre, R. H' (fuzzy:1)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1929, birth 1898 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1929-1939
- [PASS] position_sim: best 62 vs bar 60: 'senr. asst. supt' ~ 'Senior Assistant Superintendent'
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

