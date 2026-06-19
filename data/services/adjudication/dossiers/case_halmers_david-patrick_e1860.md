<!-- {"case_id": "case_halmers_david-patrick_e1860", "bio_ids": ["halmers_david-patrick_e1860"], "stint_ids": ["Chalmers, D___British Guiana___1880"]} -->
# Dossier case_halmers_david-patrick_e1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `halmers_david-patrick_e1860` ↔ `Chalmers, D___British Guiana___1880` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Chalmers, D___British Guiana___1880` is also gate-compatible with biography(ies) outside this case: ['chalmers_david-patrick_e1860'] (already linked elsewhere or filtered).

## Biography `halmers_david-patrick_e1860`

- Printed name: **HALMERS, David Patrick**
- Birth year: not printed
- Honours: Knt. Bach. (1875)
- Terminal: retired 1894 — “retired 1894”
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L31270.v` — printed in editions [1897]:**

> HALMERS, Sir David Patrick, Knt. Bach. (1875).—Member of the Scottish Faculty of Advocates, and called to the bar, 1860; appointed magistrate of the Gambia, 1867; magistrate of the Gold Coast and judicial assessor to the native courts, 1869; queen's advocate of Sierra Leone, 1872; queen's advocate, Gold Coast, 1874; prepared codes of civil and criminal procedure, measures for the abolition of slavery, and other important measures necessary on the foundation of the Gold Coast Colony; in 1876, knighted, in recognition of his services on the West Coast of Africa; chief justice, Gold Coast Colony, 1876; chief justice, Br. Guiana, 1878; mem. of commission to inquire into charges against the attorney-general of Jamaica, 1893; retired 1894.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860 | Member of the Scottish Faculty of Advocates, and called to the bar | — | [1897] |
| 1 | 1867 | magistrate | Gambia | [1897] |
| 2 | 1869 | magistrate of the Gold Coast and judicial assessor to the native courts | Gold Coast | [1897] |
| 3 | 1872 | queen's advocate | Sierra Leone | [1897] |
| 4 | 1874 | queen's advocate | Gold Coast | [1897] |
| 5 | 1876 | knighted | West Coast of Africa | [1897] |
| 6 | 1876 | chief justice | Gold Coast | [1897] |
| 7 | 1878 | chief justice | British Guiana | [1897] |
| 8 | 1893 | mem. of commission to inquire into charges against the attorney-general | Jamaica | [1897] |

## Candidate stint `Chalmers, D___British Guiana___1880`

- Staff-list name: **Chalmers, D** | colony: **British Guiana** | listed 1880–1894 | editions [1880, 1883, 1886, 1888, 1889, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | Sir D. Chalmers | Chief Justice and Judge of Court of Vice-Admiralty | Judicial Establishment | — | — |
| 1883 | Sir D. Chalmers | Chief Justice and Judge of Court of Vice-Admiralty | Judicial Establishment | — | — |
| 1886 | Sir D. Chalmers | Chief Justice and Judge of Court of Vice-Admiralty | Judicial Establishment | — | — |
| 1888 | Sir D. Chalmers | Chief Justice and Judge of Court of Vice-Admiralty | Judicial Establishment | — | — |
| 1889 | Sir D. Chalmers | Chief Justice and Judge of Court of Vice-Admiralty | Judicial Establishment | — | — |
| 1894 | Sir D. Chalmers | Chief Justice and Judge of Court of Vice-Admiralty | Judicial Establishment | — | — |

### Deterministic checks: `halmers_david-patrick_e1860` vs `Chalmers, D___British Guiana___1880`

- [PASS] surname_gate: bio 'HALMERS' vs stint 'Chalmers, D' (fuzzy:1)
- [PASS] initials: bio ['D', 'P'] ~ stint ['D']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1880-1894
- [PASS] position_sim: best 100 vs bar 60: 'chief justice' ~ 'Chief Justice and Judge of Court of Vice-Admiralty'
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

