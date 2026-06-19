<!-- {"case_id": "case_haussmann_g-c-j-l-f_b1868", "bio_ids": ["haussmann_g-c-j-l-f_b1868"], "stint_ids": ["Haussmann, G. C. J. L. F___Cape of Good Hope___1890"]} -->
# Dossier case_haussmann_g-c-j-l-f_b1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `haussmann_g-c-j-l-f_b1868`

- Printed name: **HAUSSMANN, G. C. J. L. F**
- Birth year: 1868 (attested in editions [1924, 1925, 1927])
- Appears in editions: [1923, 1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1924-L54986.v` — printed in editions [1924, 1925, 1927]:**

> HAUSSMANN, G. C. J. L. F.—B. 1868; clk., treas., Cape, 1889; acct., pension funds, Cape, 1896; prin. clk., treas., Pretoria, 1910; ch. clk., pensions, treas., 1917; ch. pensions offr., 1919.

**Version `col1923-L55097.v` — printed in editions [1923]:**

> HAUSSMANN, G. C. J. L. F.—B. 1868; elk., treasy., Cape, 1889; astt. acctnt., 1904; astt. acctnt., treasy., Union of S. Africa, 1910; ch. clk. (pensions), treasy., 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | clk., treas. | Cape of Good Hope | [1923, 1924, 1925, 1927] |
| 1 | 1896 | acct., pension funds | Cape of Good Hope | [1924, 1925, 1927] |
| 2 | 1904 | astt. acctnt | Cape of Good Hope *(inherited from previous clause)* | [1923] |
| 3 | 1910 | prin. clk., treas., Pretoria | Cape of Good Hope *(inherited from previous clause)* | [1923, 1924, 1925, 1927] |
| 4 | 1917 | ch. clk., pensions, treas | Cape of Good Hope *(inherited from previous clause)* | [1923, 1924, 1925, 1927] |
| 5 | 1919 | ch. pensions offr | Cape of Good Hope *(inherited from previous clause)* | [1924, 1925, 1927] |

## Candidate stint `Haussmann, G. C. J. L. F___Cape of Good Hope___1890`

- Staff-list name: **Haussmann, G. C. J. L. F** | colony: **Cape of Good Hope** | listed 1890–1900 | editions [1890, 1896, 1897, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | G. C. Haussmann | Clerk | Civil Service and Pension Fund Branch | — | — |
| 1896 | G. C. Haussmann | Clerk | Accounting and Pension Fund's Branch | — | — |
| 1897 | G. C. Haussmann | — | Accounting and Pension Fund's Branch | — | — |
| 1899 | G. C. J. L. F. Haussmann | Accountant | Pension Funds Branch | — | — |
| 1900 | G. C. J. L. F. Haussmann | Accountant | Pension Funds Branch | — | — |

### Deterministic checks: `haussmann_g-c-j-l-f_b1868` vs `Haussmann, G. C. J. L. F___Cape of Good Hope___1890`

- [PASS] surname_gate: bio 'HAUSSMANN' vs stint 'Haussmann, G. C. J. L. F' (exact)
- [PASS] initials: bio ['G', 'C', 'J', 'L', 'F'] ~ stint ['G', 'C', 'J', 'L', 'F']
- [PASS] age_gate: stint starts 1890, birth 1868 (age 22)
- [PASS] colony: 6 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1890-1900
- [FAIL] position_sim: best 43 vs bar 60: 'clk., treas.' ~ 'Clerk'
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

