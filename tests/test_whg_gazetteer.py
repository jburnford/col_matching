import csv
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from build_whg_gazetteer import NameMatcher, exportable_name, relationship, run, source_check


class SourceChecks(unittest.TestCase):
    def test_export_names_hold_ocr_delimiters_without_rejecting_apostrophes(self):
        for name in ['" Ceylon', '(Ceylon', 'Ashanti)', 'Name;Other', 'Name@en']:
            self.assertFalse(exportable_name(name))
        for name in ["St. John's", "'Iraq", "Washington, D.C."]:
            self.assertTrue(exportable_name(name))

    def test_matcher_finds_nested_names_and_skips_ambiguous_aliases(self):
        matcher = NameMatcher({"new york": {"Q60"}, "york": {"Q42462"},
                               "washington": {"Q61", "Q1223"}})
        raw = "New York; Washington; york"
        found = list(matcher.find(raw))
        self.assertEqual({x[0] for x in found}, {"Q60", "Q42462"})
        for _, printed, start, end in found:
            self.assertEqual(raw[start:end], printed)

    def event(self, **changes):
        return dict(place="Washington", year_start=1900,
                    text_span="Washington, 1900", **changes)

    def test_source_date_is_not_event_date(self):
        event = self.event()
        self.assertEqual(source_check(event, "Washington, 1900", 1901), "direct_source_candidate")
        self.assertEqual(source_check(event, "Washington, 1900", 1899), "missing_or_future_year")

    def test_no_inherited_or_unprinted_place(self):
        self.assertEqual(source_check(self.event(place_inherited=True), "Washington, 1900", 1901), "inherited_place")
        event = self.event()
        event["text_span"] = "appointed, 1900"
        self.assertEqual(source_check(event, "appointed, 1900", 1901), "place_not_in_span")

    def test_no_abbreviated_year_guess_or_substring_match(self):
        event = self.event()
        event["text_span"] = "Washington, '00"
        self.assertEqual(source_check(event, event["text_span"], 1901), "year_not_explicit_in_span")
        event["text_span"] = "Washingtonville, 1900"
        self.assertEqual(source_check(event, event["text_span"], 1901), "place_not_in_span")

    def test_status_is_entity_and_date_specific(self):
        rules = [{"qid": "Q61", "start": 1801, "end": 1966,
                  "status": "outside_british_empire", "source": "test:source"}]
        self.assertEqual(relationship("Q61", 1900, rules)["status"], "outside_british_empire")
        self.assertEqual(relationship("Q61", 1799, rules)["status"], "unknown")
        self.assertEqual(relationship("Q30", 1900, rules)["status"], "unknown")


class PipelineChecks(unittest.TestCase):
    def setUp(self):
        self.quiet = contextlib.redirect_stdout(io.StringIO())
        self.quiet.__enter__()
        self.addCleanup(self.quiet.__exit__, None, None, None)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.out = self.root / "out"
        helper = self.root / "col_match/kg/place_canon.py"
        helper.parent.mkdir(parents=True)
        helper.write_text("fixture")
        for corpus in ("kg", "iol"):
            for name in ("places", "career_events"):
                self.write_rows(f"data/{corpus}/graph_stage3/{name}.jsonl", [])
        self.write_rows("data/kg/graph_stage3/places.jsonl", [
            {"place": "Washington", "qid": "Q61", "label": "Washington, D.C.", "instance_of": ["capital city"]},
            {"place": "Washington DC", "qid": "Q61", "label": "Washington, D.C."},
        ])
        self.write_rows("data/kg/graph_stage3/career_events.jsonl", [
            {"person_id": "PRIVATE", "place_qid": "Q61", "year_start": 1880,
             "place_label": "Washington, D.C.", "colony_qid": "WRONG"},
        ])
        self.write_rows("data/kg/bios/col1901.jsonl", [
            {"surname": "PRIVATE", "edition_year": 1901,
             "raw_text": "Washington, 1900; Washington DC, 1890",
             "events": [{"place": "Washington", "year_start": 1900, "text_span": "Washington, 1900"},
                        {"place": "Washington DC", "year_start": 1890, "text_span": "Washington DC, 1890"}]},
        ])
        self.config = self.root / "rules.json"
        self.config.write_text(json.dumps({"version": 1, "place_decisions": {}, "imperial_relationships": []}))

    def write_rows(self, name, records):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("".join(json.dumps(r) + "\n" for r in records))

    def tsv(self, name):
        with (self.out / name).open() as f:
            return list(csv.DictReader(f, delimiter="\t"))

    def test_candidates_keep_discrete_years_and_no_people(self):
        report = run(self.root, self.out, self.config)
        p = json.loads((self.out / "places.jsonl").read_text())
        self.assertEqual(p["candidate_event_years"], [1880])
        self.assertEqual(p["direct_historical_years"], [1890, 1900])
        self.assertEqual(p["source_publication_years"], [1901])
        self.assertIsNone(p["geometry"])
        self.assertEqual(report["counts"]["ready_places"], 0)
        self.assertEqual(self.tsv("whg-ready.tsv"), [])
        self.assertEqual(self.tsv("whg-preview.tsv")[0]["attestation_year"], "1901")
        for filename in ("places.jsonl", "evidence.jsonl", "whg-preview.tsv"):
            self.assertNotIn("PRIVATE", (self.out / filename).read_text())

    def test_approval_requires_evidence_and_type(self):
        self.config.write_text(json.dumps({"version": 1, "place_decisions": {"Q61": {"approved": True}}}))
        with self.assertRaises(ValueError):
            run(self.root, self.out, self.config)
        self.config.write_text(json.dumps({"version": 1, "place_decisions": {
            "Q61": {"approved": True, "evidence": "test:identity-check", "fclass": "P"}}}))
        run(self.root, self.out, self.config)
        self.assertEqual(len(self.tsv("whg-ready.tsv")), 1)

    def test_preview_year_belongs_to_selected_name(self):
        self.write_rows("data/kg/bios/col1890.jsonl", [{
            "edition_year": 1890, "raw_text": "Washington DC, 1885",
            "events": [{"place": "Washington DC", "year_start": 1885,
                        "text_span": "Washington DC, 1885"}]}])
        self.config.write_text(json.dumps({"version": 1, "place_decisions": {
            "Q61": {"title": "Washington", "fclass": "P"}}}))
        run(self.root, self.out, self.config)
        row = self.tsv("whg-preview.tsv")[0]
        self.assertEqual(row["title"], "Washington")
        self.assertEqual(row["attestation_year"], "1901")

    def test_approval_cannot_release_an_inherited_place(self):
        self.write_rows("data/kg/bios/col1901.jsonl", [{
            "edition_year": 1901, "raw_text": "Washington, 1900",
            "events": [{"place": "Washington", "year_start": 1900,
                        "text_span": "Washington, 1900", "place_inherited": True}]}])
        self.config.write_text(json.dumps({"version": 1, "place_decisions": {
            "Q61": {"approved": True, "evidence": "test:identity", "fclass": "P"}}}))
        run(self.root, self.out, self.config)
        self.assertEqual(self.tsv("whg-ready.tsv"), [])

    def test_dirty_variants_stay_in_evidence_but_not_export(self):
        self.write_rows("data/kg/bios/col1902.jsonl", [{
            "edition_year": 1902, "raw_text": '"Washington, 1900',
            "events": [{"place": '"Washington', "year_start": 1900,
                        "text_span": '"Washington, 1900'}]}])
        run(self.root, self.out, self.config)
        place = json.loads((self.out / "places.jsonl").read_text())
        self.assertIn('"Washington', place["directly_attested_variants"])
        self.assertIn('"Washington', place["name_variants_held_from_export"])
        self.assertNotIn('"', (self.out / "whg-preview.tsv").read_text())
        self.assertEqual(len(self.tsv("whg-preview.tsv")), 1)

    def test_ambiguous_identity_does_not_get_source_evidence(self):
        path = self.root / "data/kg/graph_stage3/places.jsonl"
        with path.open("a") as f:
            f.write(json.dumps({"place": "Washington", "qid": "Q1223", "label": "Washington state"}) + "\n")
        report = run(self.root, self.out, self.config)
        self.assertEqual(report["counts"]["source_identity_ambiguous"], 1)
        self.assertEqual(report["counts"]["direct_evidence_records"], 1)

    def test_cache_checks_outputs_too(self):
        run(self.root, self.out, self.config)
        original = (self.out / "evidence.jsonl").read_bytes()
        (self.out / "evidence.jsonl").write_text("corrupted")
        run(self.root, self.out, self.config)
        self.assertEqual((self.out / "evidence.jsonl").read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
