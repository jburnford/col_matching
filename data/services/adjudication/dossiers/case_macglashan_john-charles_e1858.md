<!-- {"case_id": "case_macglashan_john-charles_e1858", "bio_ids": ["macglashan_john-charles_e1858"], "stint_ids": ["Macglashan, John C___Jamaica___1888"]} -->
# Dossier case_macglashan_john-charles_e1858

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `macglashan_john-charles_e1858`

- Printed name: **MACGLASHAN, JOHN CHARLES**
- Birth year: not printed
- Honours: C.M.G (1897)
- Appears in editions: [1888, 1889, 1890, 1894, 1898, 1899]

### Verbatim printed entry text (OCR)

**Version `col1888-L34666.v` — printed in editions [1888, 1889]:**

> MACGLASHAN, JOHN CHARLES.—Auditor-general, Jamaica, April, 1875; clerk in executive committee office, Jamaica, in June, 1868; appointed, provisionally, secretary to executive committee and clerk to privy council, in April, 1866, till Jamaica became a crown colony, then chief clerk, in financial secretary's office; subsequently in colonial secretary's office; has acted on several occasions as assistant colonial secretary, and an colonial secretary, prior to April, 1875; and April to July, 1877; member of legislative council, 1878-82.

**Version `col1898-L34603.v` — printed in editions [1898, 1899]:**

> MACGLASHAN, JOHN CHARLES, C.M.G. (1897).—Clk. in exec. comtee. office, Jamaica, 1858; sec. to exec. comtee. and clk. to privy coun., 1866; ch. clk. in financial sec.'s office, 1886; subsequently in col. sec.'s office; acted on several occasions as asst. col. sec., and as col. sec.; auditor-gen., 1875; M.L.C., 1878-82; is lieut.-col. comdg. the Kingston militia; ret. 1896.

**Version `col1890-L35447.v` — printed in editions [1890, 1894]:**

> MACGLASHAN, JOHN CHARLES.—Clerk in executive committee office, Jamaica, 1858; secretary to executive committee and clerk to privy council, 1866; chief clerk in financial secretary's office, 1866; subsequently in colonial secretary's office; has acted on several occasions as assistant colonial secretary, and as colonial secretary; auditor-general, 1875; M.I.C., 1878-82; is major in the Kingston militia.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858 | Clk. in exec. comtee. office | Jamaica | [1890, 1894, 1898, 1899] |
| 1 | 1866 | secretary to executive committee and clerk to privy council | Jamaica | [1888, 1889, 1890, 1894, 1898, 1899] |
| 2 | 1868 | clerk in executive committee office | Jamaica | [1888, 1889] |
| 3 | 1875 | Auditor-general | Jamaica | [1888, 1889, 1890, 1894, 1898, 1899] |
| 4 | 1877–1877 | — | — | [1888, 1889] |
| 5 | 1878–1882 | member of legislative council | — | [1888, 1889] |
| 6 | 1878–1882 | M.L.C | Jamaica *(inherited from previous clause)* | [1890, 1894, 1898, 1899] |
| 7 | 1886 | ch. clk. in financial sec.'s office | Jamaica *(inherited from previous clause)* | [1898, 1899] |
| 8 | 1896 | ret | Jamaica *(inherited from previous clause)* | [1898, 1899] |
| 9 | ? | chief clerk | — | [1888, 1889] |
| 10 | ? | — | — | [1888, 1889] |
| 11 | ?–1875 | assistant colonial secretary, and an colonial secretary | — | [1888, 1889] |

## Candidate stint `Macglashan, John C___Jamaica___1888`

- Staff-list name: **Macglashan, John C** | colony: **Jamaica** | listed 1888–1896 | editions [1888, 1889, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | John C. Macglashan | Auditor-General | Audit Office | — | — |
| 1889 | John C. Macglashan | Auditor-General | Audit Office | — | — |
| 1890 | John C. Macglashan | Auditor-General | Audit Office | — | — |
| 1894 | J. C. Macglashan | Member | Board of Supervision for the Relief of the Poor | — | — |
| 1894 | John C. Macglashan | Auditor-General | Audit Office | — | — |
| 1896 | J. C. Macglashan | Member | Board of Supervision for the Relief of the Poor | — | — |
| 1896 | John C. Macglashan | Auditor-General | Audit Office | — | — |
| 1896 | J. C. Macglashan | Vice-Chairman | Schools Commission | — | — |

### Deterministic checks: `macglashan_john-charles_e1858` vs `Macglashan, John C___Jamaica___1888`

- [PASS] surname_gate: bio 'MACGLASHAN' vs stint 'Macglashan, John C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 7 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1888-1896
- [FAIL] position_sim: best 28 vs bar 60: 'ch. clk. in financial sec.'s office' ~ 'Vice-Chairman'
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

