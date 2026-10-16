# WHG gazetteer snapshot — 16 October 2026 (v2)

Every place named in the career biographies of the Colonial Office Lists and
India Office Lists, prepared for the [World Historical Gazetteer](https://whgazetteer.org).
Nothing has been uploaded to WHG or run through its validator. Method:
[docs/WHG_GAZETTEER.md](../../docs/WHG_GAZETTEER.md). Supersedes the
[v1 preparation snapshot](../whg-preparation-2026-10-16/README.md), which reached
151 places.

## Results

| | |
| --- | --- |
| Place mentions in the two career graphs | 246,541 (152,132 CO + 94,409 IOL) |
| Mentions exported as places | 237,265 |
| — name and year printed in the same clause | 118,795 |
| — name printed, year elsewhere | 114,818 |
| — not found as printed (structured only) | 3,652 |
| Mentions excluded, with reasons (`excluded-mentions.tsv`) | 14,840 (offices 10,757; generic words 1,906; descriptive phrases 1,364; unexpanded abbreviations 412; campaigns 335; non-place Wikidata entities 66) |
| **Places exported** | **8,609** |
| — Wikidata-matched | 2,120 (2,097 with AAT type, 2,024 with a point) |
| — local (no period-correct Wikidata item) | 1 (Assam before 1905) |
| — name-only, awaiting reconciliation | 6,488 |
| Places with years outside their Wikidata entity's dates (kept out of the span, flagged) | 250 |
| Rare places (1–5 mentions) in the tail review | 7,192; source examples for 6,735 |

A mention can yield more than one place (composites such as *Natal and Hong
Kong*), so exported + excluded exceeds the mention count.

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

1. Review the 250 out-of-period flags. Many point to graph grounding to a
   modern or umbrella entity (Canada `Q16` before 1867, Ceylon after 1948);
   fix upstream and rebuild.
2. Reconcile name-only places, by wd-mcp grounding of the most frequent ones or
   WHG's reconciliation after upload.
3. Expand held abbreviations (`N.S.`, `T.W.I.`, `C.A.`) using career context.
4. Decide the public `@id` base (currently `https://jimclifford.ca/col_matching/whg/places/`).
5. Upload privately to WHG and run its validator.
