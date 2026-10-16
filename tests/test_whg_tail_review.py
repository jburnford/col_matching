import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from build_whg_gazetteer import run as build
from build_whg_tail_review import (authority_bounds, clause_context, frequency_band,
                                   image_availability, risk_signals, run,
                                   source_path, temporal_questions)


class TailHelpers(unittest.TestCase):
    def test_bands_do_not_conflate_absence_and_singleton(self):
        self.assertEqual([frequency_band(n) for n in (0, 1, 2, 5, 6, 20, 21, 100, 101)],
                         ["0", "1", "2-5", "2-5", "6-20", "6-20", "21-100", "21-100", ">100"])

    def test_context_keeps_date_with_clause_without_borrowing_next_clause(self):
        raw = "educated, 1880; district officer, Ohakune, 1922; promoted, 1924"
        start = raw.index("Ohakune")
        context = clause_context(raw, start, start + 7)
        self.assertIn("1922", context)
        self.assertNotIn("1924", context)
        with self.assertRaises(ValueError):
            clause_context(raw, -1, 5)

    def test_authority_dates_are_screening_not_replacements(self):
        def statement(year, precision=9):
            return {"mainsnak": {"datavalue": {"value": {
                "time": f"+{year}-01-01T00:00:00Z", "precision": precision}}}}
        bounds = authority_bounds({"claims": {"P571": [statement(1926), statement(1900, 7)],
                                               "P576": [statement(1932)]}})
        self.assertEqual(bounds["inception_years"], [1926])
        self.assertEqual(temporal_questions([1925, 1927, 1933], bounds), {
            "before_candidate_entity_inception": [1925],
            "after_candidate_entity_dissolution": [1933]})

    def test_city_district_mismatch_is_flagged(self):
        place = {"candidate_variants": ["Mbale district"], "grounded_labels": ["Mbale City"],
                 "proposed_fclass": "P", "direct_evidence_count": 0, "corpora": ["kg"]}
        self.assertIn("settlement_vs_administrative_area", risk_signals(place, {"mbale district": {"Q1"}}))

    def test_no_source_traversal_and_no_assumed_scan(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(ValueError):
                source_path(root, "../outside")
            self.assertEqual(image_availability(root, "volume", 4, {})["status"], "source_image_missing")


class TailIntegration(unittest.TestCase):
    def test_repeated_passage_retained_and_image_packet_is_not_visual_review(self):
        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()):
            root = Path(directory)
            def write(relative, records):
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("".join(json.dumps(r) + "\n" for r in records))
            helper = root / "col_match/kg/place_canon.py"
            helper.parent.mkdir(parents=True)
            helper.write_text("fixture")
            (root / "build_whg_gazetteer.py").write_text("fixture")
            for corpus in ("kg", "iol"):
                write(f"data/{corpus}/graph_stage3/places.jsonl", [])
                write(f"data/{corpus}/graph_stage3/career_events.jsonl", [])
            write("data/kg/graph_stage3/places.jsonl", [{
                "place": "Ohakune", "label": "Ohakune", "qid": "Q2016369", "instance_of": ["town"]}])
            write("data/kg/graph_stage3/career_events.jsonl", [{
                "place_qid": "Q2016369", "year_start": 1922, "person_id": "PRIVATE"},
                {"place_qid": "Q2016369", "year_start": 1924, "person_id": "PRIVATE"}])
            provenance = {"doc": "col", "edition_year": 1933, "page": 0, "block": 0, "bbox": [1, 2, 3, 4]}
            exact_provenance = {**provenance, "block": 1, "bbox": [5, 6, 7, 8]}
            for edition in (1933, 1934):
                write(f"data/kg/bios/col{edition}.jsonl", [{
                    "edition_year": edition, "raw_text": "district officer, Ohakune, 1922",
                    "events": [{"place": "Ohakune", "year_start": 1922,
                                "text_span": "district officer, Ohakune, 1922"}],
                    "provenance": [provenance, exact_provenance]}])
            ocr = root / "raw_ocr/json/ColonialOfficeList1933.pdf/result.json"
            ocr.parent.mkdir(parents=True)
            ocr.write_text(json.dumps([[{"bbox": [1, 2, 3, 4], "text": "Ohakune, 1922"},
                                        {"bbox": [5, 6, 7, 8], "text": "district officer, Ohakune, 1922"}]]))
            rules = root / "rules.json"
            rules.write_text(json.dumps({"version": 1, "place_decisions": {}}))
            build(root, root / "gazetteer", rules)
            summary = run(root, root / "gazetteer", root / "tail")
            self.assertEqual(summary["tail_places"], 1)
            self.assertEqual(summary["automatically_excluded"], 0)
            detail = json.loads((root / "tail/tail-details.jsonl").read_text())
            self.assertEqual(detail["distinct_excerpt_signatures"], 1)
            self.assertEqual(detail["source_publication_years"], [1933, 1934])
            self.assertEqual(detail["candidate_years_without_retrieved_clause_support"], [1924])
            packet = json.loads((root / "tail/image-review-packets.jsonl").read_text())
            self.assertEqual(packet["review_state"], "awaiting_image")
            target = packet["image_targets"][0]
            self.assertEqual(target["localization"], "excerpt_supported_in_original_ocr_block")
            self.assertEqual(len(packet["image_targets"]), 1)
            self.assertEqual(packet["source_provenance_entries"], 2)
            self.assertFalse(packet["quote_location_verified"])
            self.assertEqual(target["image"]["status"], "source_image_missing")
            self.assertNotIn("PRIVATE", json.dumps(packet))
            # Stale evidence cannot silently be mixed with a changed raw source.
            with (root / "data/kg/bios/col1933.jsonl").open("a") as handle:
                handle.write("{}\n")
            with self.assertRaisesRegex(ValueError, "Source changed"):
                run(root, root / "gazetteer", root / "tail")


if __name__ == "__main__":
    unittest.main()
