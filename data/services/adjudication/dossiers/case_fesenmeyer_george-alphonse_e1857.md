<!-- {"case_id": "case_fesenmeyer_george-alphonse_e1857", "bio_ids": ["fesenmeyer_george-alphonse_e1857"], "stint_ids": ["Fesenmeyer, G. A___South Australia___1877"]} -->
# Dossier case_fesenmeyer_george-alphonse_e1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fesenmeyer_george-alphonse_e1857`

- Printed name: **FESENMEYER, GEORGE ALPHONSE**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27427.v` — printed in editions [1883]:**

> FESENMEYER, GEORGE ALPHONSE.—Appointed clerk in audit office, South Australia, 1857; chief clerk, 1868; assistant auditor-general, 1870.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857 | Appointed clerk in audit office | South Australia | [1883] |
| 1 | 1868 | chief clerk | South Australia *(inherited from previous clause)* | [1883] |
| 2 | 1870 | assistant auditor-general | South Australia *(inherited from previous clause)* | [1883] |

## Candidate stint `Fesenmeyer, G. A___South Australia___1877`

- Staff-list name: **Fesenmeyer, G. A** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. A. Fesenmeyer | Assistant Auditor-General | Audit Department | — | — |
| 1878 | G. A. Fesenmeyer | Assistant Auditor-General | Audit Department | — | — |
| 1879 | G. A. Fesenmeyer | Assistant Auditor-General | Audit Department | — | — |
| 1880 | G. A. Fesenmeyer | Assistant Auditor-General | Audit Department | — | — |

### Deterministic checks: `fesenmeyer_george-alphonse_e1857` vs `Fesenmeyer, G. A___South Australia___1877`

- [PASS] surname_gate: bio 'FESENMEYER' vs stint 'Fesenmeyer, G. A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 100 vs bar 60: 'assistant auditor-general' ~ 'Assistant Auditor-General'
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

