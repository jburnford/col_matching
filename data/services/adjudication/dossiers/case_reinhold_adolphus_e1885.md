<!-- {"case_id": "case_reinhold_adolphus_e1885", "bio_ids": ["reinhold_adolphus_e1885"], "stint_ids": ["Reinhold, A___Gold Coast___1890"]} -->
# Dossier case_reinhold_adolphus_e1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['reinhold_adolphus_e1885'] carry a single initial only — the namesake trap applies.

## Biography `reinhold_adolphus_e1885`

- Printed name: **REINHOLD, ADOLPHUS**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1894-L33615.v` — printed in editions [1894, 1896, 1897]:**

> REINHOLD, ADOLPHUS.—Clerical asst. treas., Gold Coast, Jan. to June, 1885; ditto audit dept., July, 1887, to Dec., 1888; 3rd class clk. col. secy.'s office, 1889; 2nd class clk., Aug., 1891; also agt. govt. interpreter, 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885–1885 | Clerical asst. treas. | Gold Coast | [1894, 1896, 1897] |
| 1 | 1887–1888 | ditto audit dept. | — | [1894, 1896, 1897] |
| 2 | 1889–1889 | 3rd class clk. col. secy.'s office | — | [1894, 1896, 1897] |
| 3 | 1891–1891 | 2nd class clk. | — | [1894, 1896, 1897] |
| 4 | 1892–1892 | agt. govt. interpreter | — | [1894, 1896, 1897] |

## Candidate stint `Reinhold, A___Gold Coast___1890`

- Staff-list name: **Reinhold, A** | colony: **Gold Coast** | listed 1890–1913 | editions [1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906, 1907, 1908, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | A. Reinhold | Third Class Clerk | Colonial Secretary's Office | — | — |
| 1894 | A. Reinhold | 2nd Class Clerk | Colonial Secretary's Office | — | — |
| 1896 | A. Reinhold | Second-Class Clerk | Colonial Secretary's Office | — | — |
| 1897 | A. Reinhold | Second-Class Clerk | Colonial Secretary's Office | — | — |
| 1898 | A. Reinhold | 2nd-Class Clerks | Colonial Secretary's Office | — | — |
| 1899 | A. Reinhold | 2nd-Class Clerk | Colonial Secretary's Office | — | — |
| 1905 | A. Reinhold | 2nd Grade Clerk | Native Affairs Department | — | — |
| 1906 | A. Reinhold | 2nd Grade Clerk | Native Affairs Department | — | — |
| 1907 | A. Reinhold | 2nd Grade Clerk | Native Affairs Department | — | — |
| 1908 | A. Reinhold | 2nd Grade Clerk | Native Affairs Department | — | — |
| 1910 | A. Reinhold | 2nd Grade Clerk | Native Affairs Department | — | — |
| 1911 | A. Reinhold | 2nd Grade Clerk | Native Affairs Department | — | — |
| 1912 | A. Reinhold | 2nd Grade Clerk | Native Affairs Department | — | — |
| 1913 | A. Reinhold | 2nd Grade Clerk | Native Affairs Department | — | — |

### Deterministic checks: `reinhold_adolphus_e1885` vs `Reinhold, A___Gold Coast___1890`

- [PASS] surname_gate: bio 'REINHOLD' vs stint 'Reinhold, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1913
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

