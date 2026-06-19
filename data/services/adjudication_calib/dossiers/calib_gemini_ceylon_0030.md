<!-- {"case_id": "calib_gemini_ceylon_0030", "bio_ids": ["griffin_c-t_e1883"], "stint_ids": ["Griffin, C. T___Ceylon___1898"]} -->
# Dossier calib_gemini_ceylon_0030

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 77 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `griffin_c-t_e1883`

- Printed name: **GRIFFIN, C. T.**
- Birth year: not printed
- Honours: I.S.O. (1911)
- Appears in editions: [1905, 1906, 1907, 1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1905-L43546.v` — printed in editions [1905, 1906, 1907, 1910, 1911, 1912, 1913, 1914, 1915]:**

> GRIFFIN, C. T., I.S.O. (1911).—M.R.C.S., Eng.; L.R.C.P., Edin.; L.S.A., Lond.; suptlg. med. offr., Dikoya, Ceylon, 1st Jan., 1883; dist. med. offr., 17th Jan., 1888; govt. med. offr., 1st Sept., 1892; col. surg., prov. of Uva, 21st Sept., 1898; ast. prin. civ. med. offr. and insp. gen. of hospitals, 17th Jan., 1901. GRiffin, Eugene Patrick.—Third clk., treas., Gibraltar (after compet. exam.), Feb., 1883; pol. clk., 1883; 3rd clk., col. sec.'s office, 1886; 2nd class clk., Jan., 1890; 1st class clk., Jan., 1893; ch. clk. and cashier, P.O., Nov., 1893; transferred to col. sec.'s office, July, 1895; ch. clk., col. sec.'s office, and regis. of births, marriages, and deaths, 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | suptlg. med. offr. | Ceylon | [1905, 1906, 1907, 1910, 1911, 1912, 1913, 1914, 1915] |
| 1 | 1888 | dist. med. offr. | — | [1905, 1906, 1907, 1910, 1911, 1912, 1913, 1914, 1915] |
| 2 | 1892 | govt. med. offr. | — | [1905, 1906, 1907, 1910, 1911, 1912, 1913, 1914, 1915] |
| 3 | 1898 | col. surg. | — | [1905, 1906, 1907, 1910, 1911, 1912, 1913, 1914, 1915] |
| 4 | 1901 | ast. prin. civ. med. offr. and insp. gen. of hospitals | — | [1905, 1906, 1907, 1910, 1911, 1912, 1913, 1914, 1915] |

## Candidate stint `Griffin, C. T___Ceylon___1898`

- Staff-list name: **Griffin, C. T** | colony: **Ceylon** | listed 1898–1911 | editions [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | C. T. Griffin | Senior Medical Officer | Medical Department | — | — |
| 1899 | C. T. Griffin | Senior Medical Officer | Medical Department | — | — |
| 1900 | C. T. Griffin | Colonial Surgeon | Medical Department | — | — |
| 1905 | C. T. Griffin | Assistant to the Principal Civil Medical Officer | Medical Department | — | — |
| 1906 | C. T. Griffin | Assistant Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1907 | C. T. Griffin | Assistant Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1908 | C. T. Griffin | Assistant Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1909 | C. T. Griffin | Assistant Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1910 | C. T. Griffin | Assistant Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1911 | C. T. Griffin | Assistant Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |

### Deterministic checks: `griffin_c-t_e1883` vs `Griffin, C. T___Ceylon___1898`

- [PASS] surname_gate: bio 'GRIFFIN' vs stint 'Griffin, C. T' (exact)
- [PASS] initials: bio ['C', 'T'] ~ stint ['C', 'T']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1911
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

