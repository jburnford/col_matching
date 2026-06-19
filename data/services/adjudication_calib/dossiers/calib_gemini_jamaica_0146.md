<!-- {"case_id": "calib_gemini_jamaica_0146", "bio_ids": ["mackglashan_john-charles_e1858"], "stint_ids": ["Mackglashan, John C___Jamaica___1877"]} -->
# Dossier calib_gemini_jamaica_0146

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mackglashan_john-charles_e1858`

- Printed name: **MACKGLASHAN, JOHN CHARLES**
- Birth year: not printed
- Terminal: resigned 1882 — “resigned seat in Council 1882.”
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L28503.v` — printed in editions [1883, 1886]:**

> MACKGLASHAN, JOHN CHARLES.—Auditor-general, Jamaica, April, 1875; appointed clerk in executive committee office, Jamaica, in June, 1858; appointed, provisionally, secretary to executive committee and clerk to privy council, in April, 1866, till Jamaica became a crown colony, then chief clerk in financial secretary's office; subsequently in colonial secretary's office; has acted on several occasions as assistant colonial secretary, and as colonial secretary, prior to April, 1875; and from April to July, 1877; member of legislative council, April, 1878; resigned seat in Council 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858 | clerk in executive committee office | Jamaica | [1883, 1886] |
| 1 | 1866 | secretary to executive committee and clerk to privy council | Jamaica | [1883, 1886] |
| 2 | 1875 | Auditor-general | Jamaica | [1883, 1886] |
| 3 | 1877–1877 | — | — | [1883, 1886] |
| 4 | 1878 | member of legislative council | — | [1883, 1886] |
| 5 | ? | chief clerk in financial secretary's office | — | [1883, 1886] |
| 6 | ?–1875 | assistant colonial secretary, and as colonial secretary | — | [1883, 1886] |

## Candidate stint `Mackglashan, John C___Jamaica___1877`

- Staff-list name: **Mackglashan, John C** | colony: **Jamaica** | listed 1877–1886 | editions [1877, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | John C. Mackglashan | Auditor-General | Audit Office | — | — |
| 1877 | John C. Mackglashan | Clerk to the Privy Council | Privy Council | — | — |
| 1879 | John C. Mackglashan | Auditor-General | Audit Office | — | — |
| 1879 | J. C. Mackglashan | Auditor General | Official Members | — | — |
| 1880 | J. C. Mackglashan | Auditor General | Legislative Council | — | — |
| 1880 | John C. Mackglashan | Auditor-General | Audit Office | — | — |
| 1883 | John C. Mackglashan | Auditor-General | Audit Office | — | — |
| 1886 | John C. Mackglashan | Auditor-General | Audit Office | — | — |

### Deterministic checks: `mackglashan_john-charles_e1858` vs `Mackglashan, John C___Jamaica___1877`

- [PASS] surname_gate: bio 'MACKGLASHAN' vs stint 'Mackglashan, John C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1886
- [PASS] position_sim: best 100 vs bar 60: 'Auditor-general' ~ 'Auditor-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1883] pos~100 (bar: >=2)
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

