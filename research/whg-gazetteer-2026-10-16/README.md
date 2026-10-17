# WHG gazetteer snapshot — 16 October 2026 (v2)

Every place named in the career biographies of the Colonial Office Lists and
India Office Lists, prepared for the [World Historical Gazetteer](https://whgazetteer.org).
Nothing has been uploaded to WHG or run through its validator. Method:
[docs/WHG_GAZETTEER.md](../../docs/WHG_GAZETTEER.md). Supersedes the
[v1 preparation snapshot](../whg-preparation-2026-10-16/README.md), which reached
151 places.

## Dataset summary

**Title:** Places of the British imperial service: a gazetteer of locations named
in Colonial Office and India Office List biographies, 1862–1966.

**Description:** Every place named in the printed "records of services"
(career biographies) of the Colonial Office Lists and India Office Lists:
colonies, provinces, districts, towns, stations and sites where officials
served. Each record gives the printed name forms, the List editions that
printed them, and the span of dated career references to the place. People and
careers are not included.

**Creator:** Jim Clifford, University of Saskatchewan. **Licence:** CC0 1.0
([LICENSE-DATA](../../LICENSE-DATA)). **Cite as:** Jim Clifford, *Imperial
Careers: a grounded person-career knowledge graph of the Colonial Office List
and India Office List*, Dataset, Zenodo, <https://doi.org/10.5281/zenodo.21079938>
(gazetteer derived from the 16 October 2026 snapshot).

**Sources:** Colonial Office Lists (Google Books scans; OCR attribution pending confirmation — see
[OCR provenance](../../docs/OCR_AND_PARSING.md)) and India Office Lists.
Per-edition scan URIs are not yet attached (`title_uri` empty).

## Results

| | |
| --- | --- |
| Place mentions in the two career graphs | 246,541 (152,132 CO + 94,409 IOL) |
| Mentions exported as places | 234,541 |
| — name and year printed in the same clause | 117,742 |
| — name printed, year elsewhere | 113,367 |
| — not found verbatim (parser-normalised; cites the biography edition) | 3,432 |
| Mentions excluded, with reasons (`excluded-mentions.tsv`) | 17,507 (offices, departments and works 12,928; generic words 2,455; descriptive phrases 1,138; unexpanded abbreviations 362; campaigns 338; regiments 120; non-place Wikidata entities 107; routes 38; malformed strings 21) |
| **Places exported** | **7,037** |
| — Wikidata-matched | 2,106 (2,083 with AAT type, 2,012 with a point) |
| — local (no period-correct Wikidata item) | 1 (Assam before 1905) |
| — name-only, awaiting reconciliation | 4,930 (517 with a parent printed in the source) |
| Name-only records held for review (`held-names.tsv`: single mention, abbreviations only) | 919 |
| Places with years outside their Wikidata entity's dates (flagged) | 242 |
| Rare places (1–5 mentions) in the tail review | 6,555; source examples for 6,203 |

A mention can yield more than one place (composites such as *Natal and Hong
Kong*), so exported + excluded exceeds the mention count.

**Measured quality (16 Oct, after an independent review):** a seeded sample of
80 name-only rows still contained about 13 that are not places (organisations
such as *Calcutta Corporation*, fragments such as *Air*); further terms were
added after that sample, but expect roughly one in ten name-only rows to need
removal at reconciliation. Wikidata-matched titles contain no bare
abbreviations (52 use the Wikidata label because only an abbreviation was
printed).

## Examples

| Record | What it shows |
| --- | --- |
| `ip-Q1301901` Natal (1843–1911), `ip-Q917867` Natal (1910–1940) | Period rule: the same printed name split between the Colony of Natal and Natal Province by event year |
| `ip-Q550374`, `ip-Q1187978`, `ip-Q190959` Transvaal | South African Republic / Transvaal Colony / Transvaal Province |
| `ip-local-assam-pre-1905` | No Wikidata item for Assam before partition; curated local record |
| `ip-Q1139314` Kathiawar | Variants include *Káthiáwár* and *Kathia-war* (no longer mistaken for a war) |
| `ip-name-pusa` | Name-only: no clean Wikidata match found (wd-mcp), parent British Raj from career context |
| `ip-name-st-thomas-q2526023`, `…-q63973349`, `…-q1904` | Name-only homonyms kept apart: St. Thomas in Jamaica, Barbados, Ontario |

## Files

- `whg-places.tsv` — LP-TSV 0.5 upload table.
- `whg-places.lpf.json` — Linked Places Format 1.3 FeatureCollection (per-name
  citations to up to five editions, timespans, AAT types, closeMatch links).
- `review.tsv` — per-place review queue and issue codes.
- `excluded-mentions.tsv` — every place string not exported, with its reason.
- `held-names.tsv` — name-only records held back (single mention, abbreviations only).
- `name-match-proposals.tsv` — 117 proposed Wikidata matches for name-only places
  (exact label, unique within 250 km of the career context); unreviewed, not applied.
- `report.json` — full counts.
- `tail-review.tsv`, `tail-summary.json` — excerpt-free rare-place queue.
- `reproduction-hashes.json` — input/output SHA-256.

The per-mention `evidence.jsonl` (≈117 MB) and internal image-review packets,
which can quote biography excerpts, stay in ignored `out/`.

## Reproduce

```sh
python3 whg_fetch_wikidata.py
python3 build_whg_gazetteer.py
python3 build_whg_tail_review.py
python3 -m unittest discover -s tests -p 'test_whg*.py'
```

India Office evidence needs the locally held `data/iol/bios/` (gitignored);
without it only Colonial Office editions are searched.

## Before upload

1. Review the 242 out-of-period flags. Most are geographic places whose
   Wikidata dates describe a modern state or district (closeMatch acceptable);
   genuine identity errors go upstream. Fixed so far: pre-Confederation Canada
   (146 events; [evidence](../canada-geography-2026-10-16.json)), New York
   (colonial province → city) and D.W.W.I. (an office, not the Danish West
   Indies) ([evidence](../geography-2026-10-16-fable-review.json)). Modern
   states used for colonial-era mentions are folded per mention into the colony
   where Wikidata has one (`entity_folds`: Western Australia, NSW, Fiji,
   Seychelles, Barbados, Trinidad and Tobago, Zambia, Aden, British Columbia);
   Dominica, Swaziland and Turks and Caicos have no colonial item.
2. Reconcile name-only places: review `name-match-proposals.tsv` (set
   `reviewed: true` in `config/whg_name_groundings.json`), wd-mcp for frequent
   ones, or WHG's reconciliation after upload.
3. Expand held abbreviations (`N.S.`, `T.W.I.`) and review `held-names.tsv`.
4. Decide the public `@id` base (currently `https://jimclifford.ca/col_matching/whg/places/`).
5. Add citation, licence (CC0), contact and scan URIs; settle OCR attribution.
6. Upload privately to WHG and run its validator.
