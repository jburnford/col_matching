<!-- {"case_id": "case_deering_samuel_e1851", "bio_ids": ["deering_samuel_e1851"], "stint_ids": ["Deering, Samuel___South Australia___1877", "Deering, Samuel___South Australia___1889"]} -->
# Dossier case_deering_samuel_e1851

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['deering_samuel_e1851'] carry a single initial only — the namesake trap applies.

## Biography `deering_samuel_e1851`

- Printed name: **DEERING, SAMUEL**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L27111.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894]:**

> DEERING, SAMUEL.—Clerk in the census office, London, 1851; clerk in audit office, South Australia, 1855; chief clerk, 1859; clerk of executive council, 1863; aide-de-camp to Sir D. Daly, governor-in-chief, 1867; captain volunteer military staff, 1867; aide-de-camp to the Right Hon. Sir James Fergusson, Bart., 1869; also clerk to the court of appeals, Jan., 1869; resigned the foregoing appointments on being made secretary to the attorney-general, July, 1869; secretary to the commissioner of crown lands, Nov., 1870; a magistrate of the province, February, 1874; a commissioner in London for taking affidavits in the supreme court of South Australia, August, 1874; assistant agent-general and assistant emigration agent in London, August, 1874.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1851 | Clerk in the census office, London | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 1 | 1855 | clerk in audit office | South Australia | [1883, 1886, 1888, 1889, 1890, 1894] |
| 2 | 1859 | chief clerk | South Australia *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 3 | 1863 | clerk of executive council | South Australia *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 4 | 1867 | aide-de-camp to Sir D. Daly, governor-in-chief | South Australia *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 5 | 1869 | aide-de-camp to the Right Hon. Sir James Fergusson, Bart | South Australia *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 6 | 1870 | secretary to the commissioner of crown lands | South Australia *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 7 | 1874 | a magistrate of the province | South Australia *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Deering, Samuel___South Australia___1877`

- Staff-list name: **Deering, Samuel** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | S. Deering | Assistant Agent-General and Assistant Emigration Agent | Agent-General's Department (London). | — | — |
| 1878 | S. Deering | Assistant Agent-General and Assistant Emigration Agent | Agent-General's Department (London) | — | — |
| 1879 | S. Deering | Assistant Agent-General and Assistant Emigration Agent | Agent-General's Department (London) | — | — |
| 1880 | S. Deering | Assistant Agent-General and Assistant Emigration Agent | Agent-General's Department (London) | — | — |

### Deterministic checks: `deering_samuel_e1851` vs `Deering, Samuel___South Australia___1877`

- [PASS] surname_gate: bio 'DEERING' vs stint 'Deering, Samuel' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 7 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 37 vs bar 60: 'a magistrate of the province' ~ 'Assistant Agent-General and Assistant Emigration Agent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Deering, Samuel___South Australia___1889`

- Staff-list name: **Deering, Samuel** | colony: **South Australia** | listed 1889–1894 | editions [1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | S. Deering | Assistant Agent-General and Assistant Emigration Agent | Agent-General's Department (London) | — | — |
| 1890 | S. Deering | Assistant Agent-General and Assistant Emigration Agent | Agent-General's Department (London) | — | — |
| 1894 | S. Deering | Assistant Agent-General and Assistant Emigration Agent | Agent-General's Department (London) | — | — |

### Deterministic checks: `deering_samuel_e1851` vs `Deering, Samuel___South Australia___1889`

- [PASS] surname_gate: bio 'DEERING' vs stint 'Deering, Samuel' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 7 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1894
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

