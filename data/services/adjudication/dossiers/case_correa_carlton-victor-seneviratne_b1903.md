<!-- {"case_id": "case_correa_carlton-victor-seneviratne_b1903", "bio_ids": ["correa_carlton-victor-seneviratne_b1903"], "stint_ids": ["Corea, C. V. D. S___Ceylon___1934"]} -->
# Dossier case_correa_carlton-victor-seneviratne_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Corea, C. V. D. S___Ceylon___1934` is also gate-compatible with biography(ies) outside this case: ['corea_carlton-victor-demetrius-senewiratne_b1903'] (already linked elsewhere or filtered).

## Biography `correa_carlton-victor-seneviratne_b1903`

- Printed name: **CORREA, Carlton Victor Seneviratne**
- Birth year: 1903 (attested in editions [1932])
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L59321.v` — printed in editions [1932]:**

> CORREA, Carlton Victor Seneviratne.—B. 1903; cadet, Ceylon civ. serv., Feb., 1927; attd., Matara kach., Mar., 1927; ag. office ast., Kegalle kach., Nov., 1928; pol. mag., Pt. Pedro, Mar., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | cadet, Ceylon civ. serv | Ceylon | [1932] |
| 1 | 1928 | ag. office ast., Kegalle kach | Ceylon *(inherited from previous clause)* | [1932] |
| 2 | 1930 | pol. mag., Pt. Pedro | Ceylon *(inherited from previous clause)* | [1932] |

## Candidate stint `Corea, C. V. D. S___Ceylon___1934`

- Staff-list name: **Corea, C. V. D. S** | colony: **Ceylon** | listed 1934–1940 | editions [1934, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | C. V. D. S. Corea | Assistant Government Agent (Land) | PROVINCE OF UVA | — | — |
| 1937 | C. V. D. S. Corea | Assistant Settlement Officer | Land Settlement Department | — | — |
| 1940 | C. V. D. S. Corea | Assistant Settlement Officer | Land Settlement Department | — | — |

### Deterministic checks: `correa_carlton-victor-seneviratne_b1903` vs `Corea, C. V. D. S___Ceylon___1934`

- [PASS] surname_gate: bio 'CORREA' vs stint 'Corea, C. V. D. S' (fuzzy:1)
- [PASS] initials: bio ['C', 'V', 'S'] ~ stint ['C', 'V', 'D', 'S']
- [PASS] age_gate: stint starts 1934, birth 1903 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1940
- [FAIL] position_sim: best 32 vs bar 60: 'pol. mag., Pt. Pedro' ~ 'Assistant Settlement Officer'
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

