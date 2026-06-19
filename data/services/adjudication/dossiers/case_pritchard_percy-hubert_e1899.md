<!-- {"case_id": "case_pritchard_percy-hubert_e1899", "bio_ids": ["pritchard_percy-hubert_e1899"], "stint_ids": ["Pritchard, P. H___Orange River Colony___1905"]} -->
# Dossier case_pritchard_percy-hubert_e1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pritchard_percy-hubert_e1899`

- Printed name: **PRITCHARD, PERCY HUBERT**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1905-L45380.v` — printed in editions [1905, 1906, 1907, 1908, 1909]:**

> PRITCHARD, PERCY HUBERT.—M.A., Edin., 1894; attach. premier's off., Cape, Nov., 1899, to June, 1900; on h. comsnr.'s staff, Cape Town, June, 1900, to Feb., 1901; elk., sec.'s office, O.R.C. admn., Feb., 1901; elk., col. sec.'s office, June, 1902; editor, O.R.C. govt. gazette, July, 1902; acted as ch. elk., Apr. to Aug., 1903; and from Dec., 1903, to Sept., 1904; elk. for mun. and native affairs, col. sec.'s off., July, 1904; mem. of comsnr. to frame model code of mun. regulations, O.R.C., Apr., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899–1900 | attach. premier's off. | Cape Colony | [1905, 1906, 1907, 1908, 1909] |
| 1 | 1900–1901 | on h. comsnr.'s staff | Cape Colony | [1905, 1906, 1907, 1908, 1909] |
| 2 | 1901 | elk., sec.'s office | Orange River Colony | [1905, 1906, 1907, 1908, 1909] |
| 3 | 1902 | clk., col. sec.'s office | — | [1905, 1906, 1907, 1908, 1909] |
| 4 | 1902 | editor | Orange River Colony | [1905, 1906, 1907, 1908, 1909] |
| 5 | 1903–1903 | acted as ch. elk. | — | [1905, 1906, 1907, 1908, 1909] |
| 6 | 1904 | clk. for mun. and native affairs | — | [1905, 1906, 1907, 1908, 1909] |
| 7 | 1907 | mem. of comsnr. to frame model code of mun. regulations | Orange River Colony | [1905, 1906, 1907, 1908, 1909] |

## Candidate stint `Pritchard, P. H___Orange River Colony___1905`

- Staff-list name: **Pritchard, P. H** | colony: **Orange River Colony** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | P. H. Pritchard | Clerk for Municipal and Native Affairs | Colonial Secretary's Office | — | — |
| 1906 | P. H. Pritchard | Clerk for Municipal Affairs | Colonial Secretary's Department | — | — |
| 1907 | P. H. Pritchard | Clerk for Municipal Affairs | Colonial Secretary's Department | — | — |
| 1908 | P. H. Pritchard | Clerk for Municipal Affairs | Colonial Secretary's Department | — | — |
| 1909 | P. H. Pritchard | Clerk for Municipal Affairs | Ministerial Department of the Colonial Secretary | — | — |

### Deterministic checks: `pritchard_percy-hubert_e1899` vs `Pritchard, P. H___Orange River Colony___1905`

- [PASS] surname_gate: bio 'PRITCHARD' vs stint 'Pritchard, P. H' (exact)
- [PASS] initials: bio ['P', 'H'] ~ stint ['P', 'H']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Orange River Colony'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1909
- [FAIL] position_sim: best 34 vs bar 60: 'mem. of comsnr. to frame model code of mun. regulations' ~ 'Clerk for Municipal and Native Affairs'
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

