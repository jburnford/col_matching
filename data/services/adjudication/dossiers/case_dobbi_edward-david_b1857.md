<!-- {"case_id": "case_dobbi_edward-david_b1857", "bio_ids": ["dobbi_edward-david_b1857"], "stint_ids": ["Dobbie, E. D___Tasmania___1889"]} -->
# Dossier case_dobbi_edward-david_b1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dobbi_edward-david_b1857`

- Printed name: **DOBBI, EDWARD DAVID**
- Birth year: 1857 (attested in editions [1910])
- Appears in editions: [1910]

### Verbatim printed entry text (OCR)

**Version `col1910-L45395.v` — printed in editions [1910]:**

> DOBBI, EDWARD DAVID.—B. 1857; barrister, etc., sup. ct., Tasmania, admitted July, 1882; joined civ. ser., Tasmania, Mar., 1883; was part. draftman and afterwards solr.-gen., from Mar. to May, 1887; cr. solr. from 30th May, 1887, to 1896; sec. law dept., to 1898; then recrs. Launceston, to 1st Apr., 1901; solr.-gen. and crown solr., and grand juror, 1st Apr., 1901.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | barrister | Tasmania | [1910] |
| 1 | 1883 | civ. ser. | Tasmania | [1910] |
| 2 | 1887–1887 | part. draftman and afterwards solr.-gen. | — | [1910] |
| 3 | 1887–1896 | cr. solr. | — | [1910] |
| 4 | 1901 | solr.-gen. and crown solr., and grand juror | — | [1910] |
| 5 | ?–1898 | sec. law dept. | — | [1910] |
| 6 | ?–1901 | recrs. | Launceston | [1910] |

## Candidate stint `Dobbie, E. D___Tasmania___1889`

- Staff-list name: **Dobbie, E. D** | colony: **Tasmania** | listed 1889–1909 | editions [1889, 1894, 1897, 1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | E. D. Dobbie | Crown Solicitor | Law Officers | — | — |
| 1894 | E. D. Dobbie | Crown Solicitor | Law Officers | — | — |
| 1897 | E. D. Dobbie | Secretary to Law Department | Law Officers | — | — |
| 1899 | E. D. Dobbie | Secretary to Law Department | Law Officers | — | — |
| 1900 | E. D. Dobbie | Recorder and Commissioner | General Sessions, Court of Requests, and Court of Bankruptcy, Launceston | — | — |
| 1905 | E. D. Dobbie | Solicitor-General and Crown Solicitor | Law Officers | — | — |
| 1906 | E. D. Dobbie | Solicitor-General and Crown Solicitor | Law Officers | — | — |
| 1907 | E. D. Dobbie | Solicitor-General and Crown Solicitor | Law Officers | — | — |
| 1908 | E. Dobbie | Clerk | Office of Taxes | — | — |
| 1908 | E. D. Dobbie | Solicitor-General and Crown Solicitor | Law Officers | — | — |
| 1909 | E. Dobbie | Clerk | Office of Taxes | — | — |

### Deterministic checks: `dobbi_edward-david_b1857` vs `Dobbie, E. D___Tasmania___1889`

- [PASS] surname_gate: bio 'DOBBI' vs stint 'Dobbie, E. D' (fuzzy:1)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E', 'D']
- [PASS] age_gate: stint starts 1889, birth 1857 (age 32)
- [PASS] colony: 2 placed event(s) resolve to 'Tasmania'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1909
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

