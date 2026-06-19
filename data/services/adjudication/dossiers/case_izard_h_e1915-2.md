<!-- {"case_id": "case_izard_h_e1915-2", "bio_ids": ["izard_h_e1915-2"], "stint_ids": ["Izard, H. C___Straits Settlements___1905", "Izard, H___Kenya___1939"]} -->
# Dossier case_izard_h_e1915-2

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['izard_h_e1915-2'] carry a single initial only — the namesake trap applies.

## Biography `izard_h_e1915-2`

- Printed name: **IZARD, H**
- Birth year: not printed
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L67865.v` — printed in editions [1939, 1940]:**

> IZARD, H.—Asst. dist. comanr., E. Africa Prot., Feb., 1915; war serv., 1915-19, E. Africa, Egypt, Mespot., Persia; dist. offr., 1921; junr. asst. sec. and clk. of couns., 1923; called to bar (Inner Temple), 1929; senr. dist. comsnr., Kenya, July, 1936; offr.-in-ch., Turkana, Feb., 1937; comanr., mines, Dec., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | Asst. dist. comanr., E. Africa Prot | — | [1939, 1940] |
| 1 | 1921 | dist. offr | — | [1939, 1940] |
| 2 | 1923 | junr. asst. sec. and clk. of couns | — | [1939, 1940] |
| 3 | 1929 | called to bar (Inner Temple) | — | [1939, 1940] |
| 4 | 1936 | senr. dist. comsnr. | Kenya | [1939, 1940] |
| 5 | 1937 | offr.-in-ch., Turkana | Kenya *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Izard, H. C___Straits Settlements___1905`

- Staff-list name: **Izard, H. C** | colony: **Straits Settlements** | listed 1905–1914 | editions [1905, 1907, 1908, 1910, 1911, 1912, 1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. C. Izard | Colonial Chaplain | Malacca | — | — |
| 1907 | H. C. Izard | Colonial Chaplain, Rev. | Ecclesiastical | — | — |
| 1908 | Rev. H. C. Izard | Colonial Chaplain | Ecclesiastical | — | — |
| 1910 | H. C. Izard | Colonial Chaplain | Ecclesiastical | — | — |
| 1911 | H. C. Izard | Colonial Chaplain, Venerable Archdeacon | Ecclesiastical | — | — |
| 1912 | H. C. Izard | Colonial Chaplain | Ecclesiastical | — | — |
| 1913 | H. C. Izard | Colonial Chaplain, Venerable Archdeacon | Ecclesiastical | — | — |
| 1914 | H. C. Izard | Colonial Chaplain | Ecclesiastical | — | — |

### Deterministic checks: `izard_h_e1915-2` vs `Izard, H. C___Straits Settlements___1905`

- [PASS] surname_gate: bio 'IZARD' vs stint 'Izard, H. C' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H', 'C']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1914
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Izard, H___Kenya___1939`

- Staff-list name: **Izard, H** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | H. Izard | Commissioner of Mines (seconded from administration) | Mining and Geological | — | — |
| 1940 | H. Izard | Commissioner of Mines | Mining and Geological | — | — |
| 1940 | H. Izard | Senior District Commissioners | Provincial Administration | — | — |

### Deterministic checks: `izard_h_e1915-2` vs `Izard, H___Kenya___1939`

- [PASS] surname_gate: bio 'IZARD' vs stint 'Izard, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1939; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 31 vs bar 60: 'offr.-in-ch., Turkana' ~ 'Senior District Commissioners'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

