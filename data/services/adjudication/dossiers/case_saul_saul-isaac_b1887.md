<!-- {"case_id": "case_saul_saul-isaac_b1887", "bio_ids": ["saul_saul-isaac_b1887"], "stint_ids": ["Saul, S. I___Straits Settlements___1922"]} -->
# Dossier case_saul_saul-isaac_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `saul_saul-isaac_b1887`

- Printed name: **SAUL, SAUL ISAAC**
- Birth year: 1887 (attested in editions [1935, 1936])
- Appears in editions: [1935, 1936]

### Verbatim printed entry text (OCR)

**Version `dol1935-L61989.v` — printed in editions [1935, 1936]:**

> SAUL, SAUL ISAAC.—B. 1887; ed. privately; shorthand writer, off. of dir.-gen. of educn., Simla, Mar., 1906; ag. confd'l. shorthand writer to the Viceroy, July, 1912; coun. reporter, Imp. leg. coun., Simla, Feb., 1913; on staff of Viceroy, Aug., 1914; coun. reporter Burma and per. astt. to lieut.-gov. of Bengal, June, 1916; European coun. reporter, S.S. & F.M.S., May, 1921; do., S.S., May, 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | shorthand writer, off. of dir.-gen. of educn., Simla | — | [1935, 1936] |
| 1 | 1912 | ag. confd'l. shorthand writer to the Viceroy | — | [1935, 1936] |
| 2 | 1913 | coun. reporter, Imp. leg. coun., Simla | — | [1935, 1936] |
| 3 | 1914 | on staff of Viceroy | — | [1935, 1936] |
| 4 | 1916 | coun. reporter Burma and per. astt. to lieut.-gov. of Bengal | — | [1935, 1936] |
| 5 | 1921 | European coun. reporter, S.S. & F.M.S | Straits Settlements | [1935, 1936] |
| 6 | 1922 | European coun. reporter, S.S. & F.M.S | Straits Settlements | [1935, 1936] |

## Candidate stint `Saul, S. I___Straits Settlements___1922`

- Staff-list name: **Saul, S. I** | colony: **Straits Settlements** | listed 1922–1936 | editions [1922, 1923, 1925, 1931, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | S. I. Saul | Official Shorthand Reporter | Colonial Secretary's Department | — | — |
| 1923 | S. I. Saul | Official Shorthand Reporter | Colonial Secretary's Office | — | — |
| 1925 | S. I. Saul | Official Shorthand Reporter | Colonial Secretary's Office | — | — |
| 1931 | S. I. Saul | Official Shorthand Reporter | Colonial Secretary's Office | — | — |
| 1932 | S. I. Saul | Official Shorthand Reporter | Colonial Secretary's Office | — | — |
| 1934 | S. I. Saul | Official Shorthand Reporter | Colonial Secretary's Office | — | — |
| 1936 | S. I. Saul | Official Shorthand Reporter | Colonial Secretary's Office | — | — |

### Deterministic checks: `saul_saul-isaac_b1887` vs `Saul, S. I___Straits Settlements___1922`

- [PASS] surname_gate: bio 'SAUL' vs stint 'Saul, S. I' (exact)
- [PASS] initials: bio ['S', 'I'] ~ stint ['S', 'I']
- [PASS] age_gate: stint starts 1922, birth 1887 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1922-1936
- [FAIL] position_sim: best 50 vs bar 60: 'European coun. reporter, S.S. & F.M.S' ~ 'Official Shorthand Reporter'
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

