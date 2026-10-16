import csv
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from build_whg_gazetteer import (Authority, Resolver, clean_toponym, context_group,
                                 exportable_name, fclass_from_name, relationship, run,
                                 validate_identities)

IDENTITIES = {
    "version": 1,
    "period_identities": [{"surfaces": ["Natal"], "periods": [
        {"start": 1843, "end": 1910, "qid": "Q1301901"},
        {"start": 1910, "end": 1995, "qid": "Q917867"}]},
        {"surfaces": ["Assam"], "periods": [{"start": 1500, "end": 1905, "local": "assam-pre-1905"}]}],
    "surface_identities": {"Kong": {"same_as": "Hong Kong"}},
    "local_places": {"assam-pre-1905": {"title": "Assam", "fclass": "A"}},
    "non_place_terms": ["union", "various stations"],
}


class Names(unittest.TestCase):
    def test_edge_furniture_is_cleaned_but_apostrophes_kept(self):
        self.assertEqual(clean_toponym(". Cyprus"), "Cyprus")
        self.assertEqual(clean_toponym("Kedah &"), "Kedah")
        self.assertEqual(clean_toponym("Cyprus:"), "Cyprus")
        self.assertEqual(clean_toponym("'Iraq"), "'Iraq")
        self.assertEqual(clean_toponym("Oudh)"), "Oudh")
        self.assertEqual(clean_toponym("(Ceylon"), "Ceylon")
        self.assertEqual(clean_toponym("Kut (Iraq)"), "Kut (Iraq)")

    def test_exportable_names(self):
        for name in ['" Ceylon', '(Ceylon', 'Name;Other', 'Name@en', 'Trinidad &', '.']:
            self.assertFalse(exportable_name(name))
        for name in ["St. John's", "'Iraq", "Washington, D.C.", "F.M.S.", "Kut-el-Amarah"]:
            self.assertTrue(exportable_name(name))

    def test_feature_class_from_name(self):
        self.assertEqual(fclass_from_name("Klip River Division"), "A")
        self.assertEqual(fclass_from_name("Luangwa valley"), "T")
        self.assertEqual(fclass_from_name("Nairobi prison"), "S")
        self.assertEqual(fclass_from_name("Pusa"), "P")

    def test_status_is_entity_and_date_specific(self):
        rules = [{"qid": "Q61", "start": 1801, "end": 1966,
                  "status": "outside_british_empire", "source": "test:source"}]
        self.assertEqual(relationship("Q61", 1900, rules)["status"], "outside_british_empire")
        self.assertEqual(relationship("Q61", 1799, rules)["status"], "unknown")

    def test_identity_config_rejects_overlaps_and_unknown_locals(self):
        bad = json.loads(json.dumps(IDENTITIES))
        bad["period_identities"][0]["periods"][1]["start"] = 1900
        with self.assertRaises(ValueError):
            validate_identities(bad)
        bad = json.loads(json.dumps(IDENTITIES))
        bad["period_identities"][1]["periods"][0]["local"] = "missing"
        with self.assertRaises(ValueError):
            validate_identities(bad)


class Fixture(unittest.TestCase):
    def setUp(self):
        self.quiet = contextlib.redirect_stdout(io.StringIO())
        self.quiet.__enter__()
        self.addCleanup(self.quiet.__exit__, None, None, None)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.out = self.root / "out"
        for corpus in ("kg", "iol"):
            for name in ("places", "career_events"):
                self.write_rows(f"data/{corpus}/graph_stage3/{name}.jsonl", [])
        self.write_rows("data/kg/graph_stage3/places.jsonl", [
            {"place": "Washington", "qid": "Q61", "label": "Washington, D.C."},
            {"place": "Hong Kong", "qid": "Q1054923", "label": "British Hong Kong"},
            {"place": "Aden", "qid": "Q49910", "label": "Aden"},
        ])
        self.write_rows("data/iol/graph_stage3/places.jsonl", [
            {"place": "Aden", "qid": "Q17509767", "label": "Aden Province"}])
        self.events = [
            {"person_id": "kgp_col1901-p1b1", "seq": 0, "place_raw": "Washington", "place_qid": "Q61",
             "colony_qid": "Q30", "colony_label": "United States", "year_start": 1900},
            {"person_id": "kgp_col1901-p1b1", "seq": 1, "place_raw": "Natal", "place_qid": None,
             "year_start": 1913, "historical_corrections": ["reviewed-jurisdiction-outside-period"]},
            {"person_id": "kgp_col1901-p1b1", "seq": 2, "place_raw": "Kong", "place_qid": None, "year_start": 1899},
            {"person_id": "kgp_col1901-p1b1", "seq": 3, "place_raw": "Pusa", "place_qid": None, "year_start": 1898},
            {"person_id": "kgp_col1901-p1b1", "seq": 4, "place_raw": "Government of India", "place_qid": None,
             "year_start": 1897},
            {"person_id": "kgp_col1901-p1b1", "seq": 5, "place_raw": "Natal and Hong Kong", "place_qid": None,
             "year_start": 1890},
            {"person_id": "kgp_col1901-p1b1", "seq": 6, "place_raw": "Assam", "place_qid": None, "year_start": 1880},
        ]
        self.write_rows("data/kg/graph_stage3/career_events.jsonl", self.events)
        self.write_rows("data/kg/bios/col1901.jsonl", [
            {"bio_id": "col1901-p1b1", "surname": "PRIVATE", "edition_year": 1901,
             "raw_text": "PRIVATE, A.—Washington, 1900; Natal, 1913; Kong, 1899; Pusa, 1898; "
                         "Government of India, 1897; Natal and Hong Kong, 1890; Assam, 1880."}])
        self.rules = self.root / "rules.json"
        self.rules.write_text(json.dumps({"version": 1, "imperial_relationships": []}))
        self.identities = self.root / "identities.json"
        self.identities.write_text(json.dumps(IDENTITIES))
        self.authority = self.root / "authority.json"
        self.authority.write_text(json.dumps({"entities": {
            "Q61": {"label": "Washington, D.C.", "classes": ["Q5119"], "coords": [[-77.0, 38.9]],
                    "inception": [1790], "dissolved": [], "countries": ["Q30"]},
            "Q1301901": {"label": "Colony of Natal", "classes": ["Q133156"], "coords": [],
                         "inception": [1843], "dissolved": [1910], "countries": ["Q145"]},
            "Q769779": {"label": "India Office", "classes": ["Q327333"], "coords": [[0, 51]],
                        "inception": [1858], "dissolved": [1947], "countries": []}},
            "classes": {"Q5119": {"label": "capital city", "aat": ["300008389"], "parents": []},
                        "Q133156": {"label": "colony", "aat": [], "parents": ["Q1"]},
                        "Q1": {"label": "dependent territory", "aat": ["300387086"], "parents": []},
                        "Q327333": {"label": "government agency", "aat": [], "parents": []}}}))

    def write_rows(self, name, records):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("".join(json.dumps(r) + "\n" for r in records))

    def build(self):
        return run(self.root, self.out, self.rules, self.identities, self.authority)

    def tsv(self, name):
        with (self.out / name).open() as f:
            return list(csv.DictReader(f, delimiter="\t"))


class ResolverChecks(Fixture):
    def test_period_rule_alias_composite_and_exclusion(self):
        r = Resolver(self.root, IDENTITIES)
        self.assertEqual(r.single("Natal", "kg", 1913)[0], ("wd", "Q917867"))
        self.assertEqual(r.single("Natal", "kg", 1900)[0], ("wd", "Q1301901"))
        self.assertEqual(r.single("Assam", "iol", 1880)[0], ("local", "assam-pre-1905"))
        self.assertEqual(r.single("Kong", "kg", 1899)[0], ("wd", "Q1054923"))
        parts = r.resolve("Natal and Hong Kong", "kg", 1890)
        self.assertEqual([i for _, i, _ in parts], [("wd", "Q1301901"), ("wd", "Q1054923")])
        self.assertIsNone(r.resolve("Government of India", "iol", 1900)[0][1])
        self.assertIsNone(r.resolve("various stations", "iol", 1900)[0][1])
        self.assertIsNone(r.resolve("N.S.", "kg", 1900)[0][1])
        self.assertEqual(r.resolve("Pusa", "iol", 1900)[0][1][0], "name")

    def test_corpus_table_breaks_cross_corpus_ties(self):
        r = Resolver(self.root, IDENTITIES)
        self.assertEqual(r.single("Aden", "kg", 1900)[0], ("wd", "Q49910"))
        self.assertEqual(r.single("Aden", "iol", 1900)[0], ("wd", "Q17509767"))

    def test_raj_provinces_group_but_crown_colonies_do_not(self):
        a = Authority(self.authority)
        a.entities.update({"Q1": {"countries": ["Q129286"]}, "Q2": {"countries": ["Q129286"]},
                           "Q3": {"countries": ["Q145"]}, "Q4": {"countries": ["Q145"]}})
        self.assertEqual(context_group("Q1", a), context_group("Q2", a))
        self.assertNotEqual(context_group("Q3", a), context_group("Q4", a))


class PipelineChecks(Fixture):
    def test_every_mention_is_exported_or_excluded_with_reason(self):
        report = self.build()
        table = self.tsv("whg-places.tsv")
        rows = {r["title"]: r for r in table}
        # "Kong" is an OCR alias folded into Hong Kong; Natal splits by period.
        self.assertEqual(sorted(r["title"] for r in table),
                         ["Assam", "Hong Kong", "Natal", "Natal", "Pusa", "Washington"])
        self.assertEqual(sorted(r["matches"] for r in table if r["title"] == "Natal"),
                         ["wd:Q1301901", "wd:Q917867"])
        self.assertIn("Kong@en", rows["Hong Kong"]["variants"])
        self.assertEqual(report["counts"]["excluded:institution_or_office"], 1)
        excluded = (self.out / "excluded-mentions.tsv").read_text()
        self.assertIn("Government of India", excluded)
        self.assertEqual(rows["Pusa"]["matches"], "")
        self.assertEqual(rows["Assam"]["id"], "ip-local-assam-pre-1905")

    def test_lp_tsv_has_required_fields_years_and_geometry(self):
        self.build()
        rows = {r["title"]: r for r in self.tsv("whg-places.tsv")}
        w = rows["Washington"]
        self.assertEqual((w["title_source"], w["attestation_year"], w["start"]),
                         ("Colonial Office List (1901)", "1901", "1900"))
        self.assertEqual((w["fclasses"], w["aat_types"], w["types"]), ("P", "300008389", "capital city"))
        self.assertEqual((w["lon"], w["lat"], w["geo_source"]), ("-77.0", "38.9", "Wikidata"))
        for row in rows.values():
            self.assertTrue(row["id"] and row["title"] and row["title_source"])
            self.assertTrue(row["fclasses"] or row["aat_types"])
            self.assertTrue(row["attestation_year"] or row["start"])

    def test_same_clause_evidence_and_no_people_in_public_files(self):
        self.build()
        evidence = [json.loads(line) for line in (self.out / "evidence.jsonl").read_text().splitlines()]
        wash = next(e for e in evidence if e["printed_name"] == "Washington")
        self.assertEqual(wash["evidence_tier"], "same_clause")
        self.assertEqual(wash["place_id"], "ip-Q61")
        raw = json.loads((self.root / "data/kg/bios/col1901.jsonl").read_text())["raw_text"]
        self.assertEqual(raw[wash["source"]["char_start"]:wash["source"]["char_end"]], "Washington")
        for filename in ("whg-places.tsv", "whg-places.lpf.json", "places.jsonl"):
            self.assertNotIn("PRIVATE", (self.out / filename).read_text())

    def test_editions_older_than_the_posting_do_not_cite_it(self):
        self.write_rows("data/kg/llm_struct_corpus.stage3.jsonl", [{
            "person_id": "kgp_col1901-p1b1", "attestations": ["col1895-p1b1", "col1901-p1b1"]}])
        self.write_rows("data/kg/bios/col1895.jsonl", [
            {"bio_id": "col1895-p1b1", "edition_year": 1895, "raw_text": "Washington, 1890."}])
        self.build()
        evidence = [json.loads(line) for line in (self.out / "evidence.jsonl").read_text().splitlines()]
        wash = next(e for e in evidence if e["printed_name"] == "Washington")
        self.assertEqual(wash["printed_in_editions"], [1901])

    def test_non_place_entity_from_graph_is_excluded(self):
        events = self.events + [{"person_id": "kgp_col1901-p1b1", "seq": 7, "place_raw": "India Office",
                                 "place_qid": "Q769779", "year_start": 1905}]
        self.write_rows("data/kg/graph_stage3/career_events.jsonl", events)
        report = self.build()
        self.assertEqual(report["counts"]["excluded:non_place_entity"], 1)
        self.assertNotIn("India Office", (self.out / "whg-places.tsv").read_text())

    def test_lpf_features_carry_citations_and_when(self):
        self.build()
        lpf = json.loads((self.out / "whg-places.lpf.json").read_text())
        self.assertEqual(lpf["type"], "FeatureCollection")
        feature = next(f for f in lpf["features"] if f["properties"]["title"] == "Washington")
        self.assertEqual(feature["names"][0]["citations"][0], {"label": "Colonial Office List (1901)", "year": 1901})
        self.assertEqual(feature["when"]["timespans"][0]["start"]["in"], "1900")
        self.assertEqual(feature["links"], [{"type": "closeMatch", "identifier": "wd:Q61"}])
        self.assertEqual(feature["geometry"]["coordinates"], [-77.0, 38.9])

    def test_cache_checks_outputs_too(self):
        self.build()
        original = (self.out / "evidence.jsonl").read_bytes()
        (self.out / "evidence.jsonl").write_text("corrupted")
        self.build()
        self.assertEqual((self.out / "evidence.jsonl").read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
