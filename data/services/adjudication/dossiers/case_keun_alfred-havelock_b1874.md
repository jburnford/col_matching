<!-- {"case_id": "case_keun_alfred-havelock_b1874", "bio_ids": ["keun_alfred-havelock_b1874"], "stint_ids": ["Keun, A. H___Straits Settlements___1911"]} -->
# Dossier case_keun_alfred-havelock_b1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `keun_alfred-havelock_b1874`

- Printed name: **KEUN, ALFRED HAVELOCK**
- Birth year: 1874 (attested in editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920])
- Honours: M.B
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920]

### Verbatim printed entry text (OCR)

**Version `col1905-L44274.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920]:**

> KEUN, ALFRED HAVELOCK, M.B., B.Ch. (Edin.).—B. 1874; house surg., gen. hosp., Singapore, 1st Apr., 1900; super. col. surg., S. Settlements, 17th Nov., 1900; col. surg., Prov. Wellesley South, 1st Mar., 1901; res. med. offr., dist. hosp., Penang, Oct., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | house surg., gen. hosp. | Singapore | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920] |
| 1 | 1901 | col. surg., Prov. Wellesley South | Singapore *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920] |
| 2 | 1906 | res. med. offr., dist. hosp., Penang | Singapore *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920] |

## Candidate stint `Keun, A. H___Straits Settlements___1911`

- Staff-list name: **Keun, A. H** | colony: **Straits Settlements** | listed 1911–1913 | editions [1911, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | A. H. Keun | Medical Officer | Malacca | — | — |
| 1913 | A. H. Keun | Medical Officer | Malacca | — | — |

### Deterministic checks: `keun_alfred-havelock_b1874` vs `Keun, A. H___Straits Settlements___1911`

- [PASS] surname_gate: bio 'KEUN' vs stint 'Keun, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1911, birth 1874 (age 37)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1913
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

