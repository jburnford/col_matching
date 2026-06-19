<!-- {"case_id": "case_madde_john-brinto-culler_b1892", "bio_ids": ["madde_john-brinto-culler_b1892"], "stint_ids": ["Madden, John___Australia___1912"]} -->
# Dossier case_madde_john-brinto-culler_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Madden, John___Australia___1912` is also gate-compatible with biography(ies) outside this case: ['madden_john_b1844'] (already linked elsewhere or filtered).

## Biography `madde_john-brinto-culler_b1892`

- Printed name: **MADDE, JOHN BRINTO CULLER**
- Birth year: 1892 (attested in editions [1931])
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L66477.v` — printed in editions [1931]:**

> MADDE, JOHN BRINTO CULLER, M.B. (Edin.), Ch.B.—B.1892; med. offr., Zanzibar, 4th Feb., 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | med. offr. | Zanzibar | [1931] |

## Candidate stint `Madden, John___Australia___1912`

- Staff-list name: **Madden, John** | colony: **Australia** | listed 1912–1927 | editions [1912, 1913, 1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | J. J. Madden | Bench Clerk and Information Clerk | Magistracy | — | — |
| 1912 | Sir John Madden | Lieutenant-Governor | Government | G.C.M.G. | — |
| 1913 | Sir John Madden | Administrator | — | Kt., LL.D. | — |
| 1913 | Sir J. Madden | Lieutenant-Governor | — | K.C.M.G. | — |
| 1913 | J. J. Madden | Bench Clerk and Information Clerk | Magistracy | — | — |
| 1913 | Sir John Madden | Lieut.-Governor | Government | G.C.M.G. | — |
| 1913 | Sir John Madden | Chief Justice | Law Department | G.C.M.G. | — |
| 1918 | John Madden | Lieut.-Governor | Government | G.C.M.G. | — |
| 1918 | Sir John Madden | Chief Justice | Law Department | G.C.M.G. | — |
| 1927 | Sir J. Madden | Lieut.-Governor | Government | K.C.M.G. | — |
| 1927 | Sir John Madden | Administrator | Government | Kt. | — |

### Deterministic checks: `madde_john-brinto-culler_b1892` vs `Madden, John___Australia___1912`

- [PASS] surname_gate: bio 'MADDE' vs stint 'Madden, John' (fuzzy:1)
- [PASS] initials: bio ['J', 'B', 'C'] ~ stint ['J']
- [PASS] age_gate: stint starts 1912, birth 1892 (age 20)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1927
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

