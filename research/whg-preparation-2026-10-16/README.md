# Place-only WHG preparation snapshot — 16 October 2026

> **Superseded** by the [v2 gazetteer snapshot](../whg-gazetteer-2026-10-16/README.md).
> This v1 run drew direct evidence only from the rules parser's colony-level
> `place` field, so it reached 151 of 2,126 candidates. Kept for the record.

This snapshot records automated preparation and text-based triage, not a
validated gazetteer or an image-reviewed release. Nothing has been uploaded to
WHG. Candidate identities are inherited from existing grounding and need
independent verification before publication.

## Results

- 2,126 candidate identities across both graph corpora.
- 821,871 retrieved source-name occurrences across 1,499 candidates.
- 93,931 source-specific explicit place/year passages across 149 candidates.
- 131 LP-TSV preview rows; zero independently approved publication rows.
- Nineteen variants with stray delimiters or unsafe export punctuation retained
  in evidence but held out of the preview; clean variants and places retained.
- 911 candidates with one to five event references, representing 2,540 events.
- All 911 tail candidates retained. Source examples retrieved for 651.
- 1,755 internal image-review packets; 1,600 aligned to an entire excerpt in
  original OCR blocks, 153 additional packets aligned by name, two without
  successful name/block alignment. No source images are available locally.
- 300 tail candidates have at least one event-year endpoint absent from the
  retrieved name-bearing clauses; 61 have possible authority-date conflicts;
  eight have settlement-versus-administrative-area signals. These groups overlap
  and are not counts of confirmed errors.

Event frequency, source-name frequency, distinct text signatures, and independent
historical support are different quantities. Repeated biographies across
editions can amplify a single statement. Lexical retrieval can also return
school names, surnames, or other non-geographic uses.

## Text-based triage examples

These observations identify review questions; they do not adjudicate locations.

| Candidate | Local source evidence and question |
| --- | --- |
| Ohakune (`Q2016369`) | Retrieved clause supports the name with 1922. Graph years 1924, 1925, 1928, and 1931 lack a retrieved name-bearing clause. The source moves on to later railway roles; do not carry the town forward without evidence. |
| Keningau (`Q1299852`) | Source spells the name “Keningan” with 1899. Graph years 1903, 1905, and 1906 lack corresponding retrieved name-bearing clauses. Check the image spelling and later locations separately. |
| Kingdom of Nejd and Hejaz (`Q1756546`) | The source mentions an envoy to its king in 1925 and 1927. The cached candidate entity starts in 1926, so 1925 needs a period-specific identity check. Do not remove the historical mention. |
| Mbale City (`Q1015727`) | Candidate variant says “Mbale district.” Settlement and district must be distinguished; no source example was retrieved under that exact variant. |
| Repton (`Q1018787`) | One graph event but hundreds of lexical occurrences. Retrieved contexts include education and Repton School; those occurrences are not automatically evidence for the town or a dated posting. |
| Phuket, former circle (`Q108180040`) | Source clauses explicitly contain “Puket, West Siam” and 1907. Verify the historical administrative unit rather than assuming a modern city identity. |

## Files and reproduction

- `gazetteer-summary.json`: first-stage coverage and limitations.
- `tail-summary.json`: frequency, diagnostic signals, and image-handoff coverage.
- `tail-review.tsv`: excerpt-free candidate queue; all decisions remain pending.
- `whg-preview.tsv`: illustrative upload-shaped table, not a publication release.
- `reproduction-hashes.json`: source/code and generated-output hashes for this run.

```sh
python build_whg_gazetteer.py
python build_whg_tail_review.py
python -m unittest discover -s tests -p 'test_whg*.py' -v
```

Nineteen tests pass. Generated evidence ledgers and internal review excerpts
stay in ignored `out/whg/` and `out/whg-tail/`; they are not committed here.
See [the workflow](../../docs/WHG_GAZETTEER.md) and
[OCR/parsing provenance](../../docs/OCR_AND_PARSING.md).

## Environment boundary and next stage

The missing artifacts are original page images/PDFs, raw India Office
HTML/markdown, and per-batch OCR execution logs. Several implementation files
call the layout-aware OCR Infinity-2; the former public methods description
called it Chandra 2. Exact batch/checkpoint attribution remains unresolved.

Once scans are available, use the image-source mapping and review-response
schema in `config/`, preserving literal transcription separately from geographic
interpretation. Independent authority reconciliation, calibrated automatic
acceptance, richer Linked Places export, and WHG validation remain future
stages. Rare records must not be discarded merely to improve apparent precision.
