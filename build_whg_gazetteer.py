#!/usr/bin/env python3
"""Offline, place-only WHG gazetteer of every location in the biographies.

Every place mention in the two career graphs (Colonial Office + India Office
Lists) is resolved to exactly one outcome:

  * a Wikidata place (graph grounding, period rule, curated surface rule, or
    the project's reviewed grounding tables),
  * a local place (config/whg_place_identities.json: no adequate period-correct
    Wikidata item),
  * a name-only place (printed toponym, no authority match yet), or
  * a review/exclusion bucket with a reason (offices, campaigns, generic words,
    unexpanded abbreviations, descriptive phrases).

Each mention is checked against every edition of the person's biography: is the
printed name in the text, and does the same clause also print the year? That
yields three evidence tiers per mention (same_clause / printed / structured_only).
No person fields enter any public output; evidence locators point into the
biography files for audit.

Outputs (default out/whg/): whg-places.tsv (LP-TSV 0.5), whg-places.lpf.json
(Linked Places Format 1.3), places.jsonl, evidence.jsonl, review.tsv,
excluded-mentions.tsv, report.json, manifest.json.
"""
import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import unicodedata

from col_match.kg.ground import suspected_noise
from col_match.kg.place_canon import canon_key, canonicalize, is_institution

ROOT = Path(__file__).resolve().parent
VERSION = 2
STATUSES = {"british_empire", "outside_british_empire", "mixed_or_contested", "unknown"}
ID_BASE = "https://jimclifford.ca/col_matching/whg/places/"
LPF_CONTEXT = "https://raw.githubusercontent.com/LinkedPasts/linked-places/master/linkedplaces-context-v1.1.jsonld"
TIERS = ("same_clause", "printed", "structured_only")
CORPUS_TITLE = {"kg": "Colonial Office List", "iol": "India Office List"}
MAX_CITATIONS = 5


# ----------------------------------------------------------------- text utils
def rows(path):
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if line.strip():
                yield number, json.loads(line)


def norm(text):
    return " ".join(re.findall(r"\w+", unicodedata.normalize("NFKC", text or "").casefold()))


def contains(text, phrase):
    needle = norm(phrase)
    return bool(needle) and f" {needle} " in f" {norm(text)} "


def valid_year(value):
    return value if type(value) is int and 1500 <= value <= 1966 else None


_LEAD = re.compile(r"^[\s.,:;&\-–—*\"“”]+")
_TRAIL = re.compile(r"[\s,:;&\-–—*\"“”‘’]+$")


def clean_toponym(name):
    """Strip OCR furniture at the edges ('. Cyprus', 'Kedah &', 'Cyprus:')."""
    name = _TRAIL.sub("", _LEAD.sub("", name or "")).strip()
    name = re.sub(r"(\w)- ([a-z])", r"\1\2", name)  # line-break hyphen: "Esse- quibo"
    if re.fullmatch(r"\([^()]+\)", name):
        name = name[1:-1].strip()
    while name.endswith(")") and name.count(")") > name.count("("):
        name = _TRAIL.sub("", name[:-1]).strip()
    while name.startswith("(") and name.count("(") > name.count(")"):
        name = _LEAD.sub("", name[1:]).strip()
    return name


_ABBR_TOKEN = re.compile(r"^(?!(?:St|Mt|Ft|Pt|Co|Ste)\.$)[A-Za-z]{1,6}\.$")


def is_abbreviated(name):
    """'Nig.', 'H.K.', 'B. Hond.', "S'pore" — but not 'St. Vincent' or "St. John's"."""
    return (any(_ABBR_TOKEN.match(t) for t in name.split())
            or bool(re.fullmatch(r"(?:[A-Z]\.\s?){1,6}", name))
            or bool(re.search(r"[A-Za-z]'[a-rt-z]", name)))


def exportable_name(name):
    """Hold delimiters/OCR furniture; preserve originals in evidence."""
    if not name or any(ch in name for ch in ';\t\r\n"“”@|'):
        return False
    if name[0] in "([{" or name[-1] in "([{&,:-" or name != name.strip():
        return False
    if len(re.findall(r"[A-Za-zÀ-ÿ]", name)) < 2:
        return False
    return name.count("(") == name.count(")") and name.count("[") == name.count("]")


def slug(text):
    s = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60] or "x"


# ----------------------------------------------------------- identity layers
_ORG = re.compile(
    r"\b(govt|government|gov|survey|dept|department|depot|dep[oô]t|mint|board|ministry|"
    r"establishment|army|branch|office|posts?|tels|telegraphs?|railways?|rlys?|ry|ryis|"
    r"service|services|corps|regiment|police|force|forces|bank|company|commission|"
    r"council|court|secretariat|treasury|customs|audit|museum|college|coll|school|schl|"
    r"university|univ|hospital|conf|conference|committee|staff|division of|circle of|"
    r"admiralty|treasur(?:y|ies)|plebiscite|front|engineers?|artillery|hussars|rifles|"
    r"infantry|cavalry|lancers|dragoons|fusiliers|guards|volunteers?|militia|battalion|"
    r"brigade|command|commons|lords|exhibn|exhibition|acad|academy|diocese|asylum|"
    r"establish|adminstn|admn|administration|constabulary|const|observatory|institute|inst|"
    r"laboratory|lab|library|press|gazette|legation|consulate|embassy|mission to|"
    r"delegation|squadron|fleet|navy|naval|flotilla|hq|headquarters|secrt|secretary|"
    r"cabinet|legislative|legislature|society|soc|assoc|association|inf|highlanders|volrs|"
    r"h\.?m\.?s|league|trust|education|system|inspectorate|conservancy|chamber|syndicate|"
    r"delegates?|delegation|volns|vols|hosp|hosps|census|boundary|asylums?|mortuary|transport|"
    r"workshops?|improvements?|harbrs|instns|institutions|infirmary|admlty|miny|ministry|"
    r"c\.s|treasy|secretariat|camp of instruction|depot|stores|works|scheme|organ|orgn|"
    r"organization|organisation|bureau|parltr|parlt|parliament|teacher|teachers|kach|ach|"
    r"defences|lit|res|vet|agric|agricl|educ|med|medical|sanitary|survey|surveys|times|"
    r"gazette|newspaper|club|lodge|exhibn|exhibition|conference|sectt|ltd|limited|colleges|"
    r"schools|rlways|rlwys|rlys|rly|hajj|pilgrimage|cabinet|assembly|irrigation|marine|"
    r"revenues?|agents?|radio|project|d[eé]p[oô]t|broadcasting|museum|zoo|bureau|tour|"
    r"corporation|kachcheri|kach|cutcherry|authy|authority|estab|ecclesiastical|section|"
    r"h\. of a|h\. of r|waters|dispensary)\b", re.I)
_REGIMENT = re.compile(r"\b\d+(?:st|nd|rd|th)\b|\b(foot|punjabis|sikhs|gurkhas|pathans|baluchis|"
                       r"rajputs|jats|dogras|mahrattas|grenadiers|f\.f|pioneers|rifles|lancers)\b", re.I)
_GENERIC_ONLY = re.compile(r"^(?:(?:n|s|e|w|ne|nw|se|sw|north|south|east|west|northern|southern|eastern|"
                           r"western|central|cent|upper|lower|middle|mid|district|dist|divn|division|"
                           r"circle|province|prov|coast|coasts|canal|of|the|and|africa|india|area|areas|"
                           r"region|zone|section|sub)\.?\s*)+$", re.I)
_MILITARY = re.compile(r"\b(infantry|inf|cavalry|regiment|regt|rifles|hussars|lancers|dragoons|"
                       r"fusiliers|guards|artillery|battalion|brigade|division|force|forces|"
                       r"command|front|expedition|exped|expedit|corps|volunteers?|militia|"
                       r"light horse|horse|sappers|pioneers|highlanders|squadron|fleet|navy|naval|"
                       r"volns|vols)\b", re.I)
_ADMIN = re.compile(r"\b(district|dist|dists|distr|province|provs?|provinces|division|divn|"
                    r"presidency|state|states|agency|territory|colony|protectorate|prot|prots|"
                    r"circle|county|co|parish|tahsil|taluk|taluka|zillah|zila|collectorate|"
                    r"commissionership|residency|settlements?|sttlmts?|confederation|federation|"
                    r"union|dominion|emirate|sultanate|kingdom|chiefdom|cantonment)\b", re.I)
_WATER = re.compile(r"\b(river|riv|lake|bay|creek|harbour|harbor|gulf|strait|straits|sea|lagoon|canal)\b", re.I)
_LAND = re.compile(r"\b(island|islands|isl|isle|isles|archipelago|peninsula|cape|mountain|mount|mt|"
                    r"hill|hills|range|plateau|valley)\b", re.I)
_SITE = re.compile(r"\b(fort|station|mission|camp|observatory|gaol|jail|prison|mine|mines|"
                   r"goldfield|lighthouse|cantonments|barracks|estate|plantation)\b", re.I)
_REGION = re.compile(r"\b(coast|region|frontier|hinterland|interior|country|tract|tracts|"
                     r"highlands|lowlands|delta)\b", re.I)


def fclass_from_name(name):
    """Feature-class proposal for a name with no authority record."""
    for code, pattern in (("A", _ADMIN), ("H", _WATER), ("T", _LAND), ("S", _SITE), ("L", _REGION)):
        if pattern.search(name):
            return code
    return "P"


# One code per class label, first match wins: settlement and polity terms
# outrank the geographic nouns inside compounds ("port city", "island country",
# "hill station", "cantonment town").
CLASS_RULES = [
    ("P", r"\b(city|town|village|settlement|hamlet|capital|municipality|suburb|neighbou?rhood|"
          r"locality|borough|census town|populated place|township|hill station|area of london|"
          r"metropolis|conurbation)\b"),
    ("A", r"\b(colony|protectorate|province|district|presidency|country|state|territory|county|"
          r"dominion|division|administrative|polity|kingdom|empire|federation|union|mandate|"
          r"emirate|sultanate|sovereign|dependency|agency|residency|commonwealth|realm|crown|"
          r"princely|nation|republic|tehsil|taluka|subdivision|governorate|regency|parish)\b"),
    ("H", r"\b(river|lake|bay|gulf|sea|strait|harbou?r|lagoon|body of water|watercourse|canal|ocean)\b"),
    ("T", r"\b(island|islands|archipelago|atoll|mountain|hill|peninsula|cape|volcano|landform|"
          r"plateau|valley|island group)\b"),
    ("S", r"\b(fort|fortress|castle|building|station|mission|observatory|prison|mine|lighthouse|"
          r"military base|cantonment|archaeological site|port|garden|botanical garden|park|"
          r"cemetery|dock|bridge|dam|structure)\b"),
    ("L", r"\b(region|geographic|historical region|area|continent|subcontinent|cultural region|"
          r"physiographic|ecoregion|coast|landscape)\b"),
]
NON_PLACE_CLASSES = re.compile(
    r"\b(organization|organisation|government agency|government department|ministry|"
    r"department|office|company|business|institution|university|college|school|"
    r"academic|court|legislature|parliament|military unit|army|regiment|police|"
    r"bank|newspaper|person|war|battle|conflict|event|religious order)\b|^human$", re.I)


class Authority:
    """Wikidata facts cached by whg_fetch_wikidata.py (property lookups only)."""

    def __init__(self, path):
        data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        self.entities = data.get("entities", {})
        self.classes = data.get("classes", {})

    def class_chain(self, cls, depth=3):
        seen, frontier = [], [cls]
        for _ in range(depth + 1):
            nxt = []
            for c in frontier:
                if c in seen or c not in self.classes:
                    continue
                seen.append(c)
                nxt += self.classes[c].get("parents", [])
            frontier = nxt
        return seen

    def types(self, qid):
        """[(label, aat)] for direct classes, AAT from nearest classed ancestor."""
        out = []
        for cls in self.entities.get(qid, {}).get("classes", []):
            info = self.classes.get(cls, {})
            label = info.get("label")
            if not label:
                continue
            aat = next((self.classes[c]["aat"][0] for c in self.class_chain(cls)
                        if self.classes.get(c, {}).get("aat")), "")
            out.append((label, aat))
        return out

    def fclasses(self, qid):
        classes = self.entities.get(qid, {}).get("classes", [])
        pools = ([self.classes.get(c, {}).get("label") or "" for c in classes],
                 [self.classes.get(c, {}).get("label") or "" for cls in classes
                  for c in self.class_chain(cls, 2)])
        for pool in pools:
            found = []
            for label in pool:
                code = next((code for code, pat in CLASS_RULES if re.search(pat, label, re.I)), None)
                if code and code not in found:
                    found.append(code)
            if {"P", "A"} & set(found):
                found = [c for c in found if c != "L"]
            if found:
                return found[:2]
        return []

    def non_place(self, qid):
        """Organisation-type entity with no place class (e.g. India Office)."""
        ent = self.entities.get(qid)
        if not ent or not ent.get("classes"):
            return False
        direct = [self.classes.get(c, {}).get("label") or "" for c in ent["classes"]]
        # An organisation label never counts as a place label, even when it
        # names a polity ("department of the United Kingdom Government").
        if any(not NON_PLACE_CLASSES.search(x) and any(re.search(pat, x, re.I) for _, pat in CLASS_RULES)
               for x in direct):
            return False
        return any(NON_PLACE_CLASSES.search(x) for x in direct)

    def bounds(self, qid):
        ent = self.entities.get(qid, {})
        return (min(ent["inception"]) if ent.get("inception") else None,
                max(ent["dissolved"]) if ent.get("dissolved") else None)


class Resolver:
    """Mention → identity, for mentions the graph left without a place_qid."""

    def __init__(self, root, identities):
        self.periods = collections.defaultdict(list)
        for rule in identities.get("period_identities", []):
            for surface in rule["surfaces"]:
                self.periods[canon_key(surface)].append(rule)
        self.surfaces = {canon_key(k): v for k, v in identities.get("surface_identities", {}).items()}
        self.non_place = {canon_key(t) for t in identities.get("non_place_terms", [])}
        # Reviewed graph assignments per corpus: printed surface -> QID votes.
        self.votes = {c: collections.defaultdict(collections.Counter) for c in ("kg", "iol")}
        for corpus in ("kg", "iol"):
            path = root / f"data/{corpus}/graph_stage3/career_events.jsonl"
            if path.exists():
                for _, e in rows(path):
                    if e.get("place_qid") and e.get("place_raw"):
                        self.votes[corpus][canon_key(e["place_raw"])][e["place_qid"]] += 1
        self.corpus_table = {c: collections.defaultdict(set) for c in ("kg", "iol")}
        self.table = collections.defaultdict(set)
        for corpus in ("kg", "iol"):
            for name in (f"data/{corpus}/places_grounding.jsonl", f"data/{corpus}/graph_stage3/places.jsonl"):
                path = root / name
                if not path.exists():
                    continue
                for _, r in rows(path):
                    if r.get("qid") and re.fullmatch(r"Q\d+", r["qid"]):
                        for s in {r["place"], r.get("query") or ""}:
                            if s:
                                for k in (canon_key(s), canon_key(canonicalize(s))):
                                    self.table[k].add(r["qid"])
                                    self.corpus_table[corpus][k].add(r["qid"])

    def single(self, surface, corpus, year):
        surface = clean_toponym(surface) or surface
        key = canon_key(surface)
        for rule in self.periods.get(key, []):
            if rule.get("corpora") and corpus not in rule["corpora"]:
                continue
            if year is None:
                continue  # undated: fall through to the graph's usual reading
            for p in rule["periods"]:
                if p["start"] <= year < p["end"]:
                    return (("local", p["local"]) if p.get("local") else ("wd", p["qid"])), "period_rule"
        if key in self.surfaces:
            rule = self.surfaces[key]
            if rule.get("qid"):
                return ("wd", rule["qid"]), "surface_rule"
            if rule.get("same_as") and canon_key(rule["same_as"]) != key:  # OCR/alias form
                ident, _ = self.single(rule["same_as"], corpus, year)
                if ident:
                    return ident, "surface_rule"
        ckey = canon_key(canonicalize(surface))
        for k in (key, ckey):
            votes = self.votes.get(corpus, {}).get(k)
            if votes:
                top, n = votes.most_common(1)[0]
                if n >= 0.8 * sum(votes.values()):
                    return ("wd", top), "graph_surface_vote"
        for k in (key, ckey):  # the other corpus's reviewed usage
            votes = collections.Counter()
            for c in self.votes:
                votes.update(self.votes[c].get(k, {}))
            if votes:
                top, n = votes.most_common(1)[0]
                if n >= 0.6 * sum(votes.values()):
                    return ("wd", top), "graph_surface_vote"
        ambiguous = False
        for table in (self.corpus_table.get(corpus, {}), self.table):
            for k in (key, ckey):
                hits = table.get(k, set())
                if len(hits) == 1:
                    return ("wd", next(iter(hits))), "grounding_table"
                ambiguous |= len(hits) > 1
        return None, "ambiguous_surface" if ambiguous else "unresolved"

    def classify_unresolved(self, surface):
        p = surface.strip()
        key = canon_key(p)
        if self.surfaces.get(key, {}).get("exclude"):
            return self.surfaces[key]["exclude"]
        if key in self.non_place or not re.search(r"[A-Za-z]{2}", p):
            return "generic_or_non_place_term"
        flag, why = suspected_noise(p)
        if flag:
            return "institution_or_office" if "office" in why or "institution" in why else "campaign_or_noise"
        if _REGIMENT.search(p):
            return "military_unit"
        if re.search(r"\bexped\w*", p, re.I):
            return "campaign_or_noise"
        if _ORG.search(p):
            return "institution_or_office"
        if _GENERIC_ONLY.match(p.strip()):
            return "generic_or_non_place_term"
        if p.count("(") != p.count(")") or re.search(r"^\W|\)\s*\w", p):
            return "malformed_string"
        if re.search(r"\b(to|via)\b", p):
            return "route_phrase"
        letters = re.sub(r"[^A-Za-z]", "", p)
        tokens = re.findall(r"[A-Za-z]+", p)
        if tokens and all(len(t) <= 2 or t.isupper() for t in tokens) and ("." in p or letters.isupper()):
            return "unexpanded_abbreviation"
        if len(tokens) == 1 and len(tokens[0]) <= 5 and p.rstrip().endswith("."):
            return "unexpanded_abbreviation"  # truncated: "Rhod.", "Wind.", "Cols."
        if p[0].islower():
            return "descriptive_phrase"
        return None

    def place_in_institution(self, surface, corpus, year):
        """'Natal treasury' -> Natal; '(Eastern Bengal)' -> Eastern Bengal. Civil
        bodies only: a regiment's name is not where it served. Resolved
        identities only, never a new name-only record."""
        if _MILITARY.search(surface):
            return None
        candidates = re.findall(r"\(([^()]+)\)", surface)
        tokens = re.sub(r"\([^()]*\)", " ", surface).split()
        candidates += [" ".join(tokens[:n]) for n in range(len(tokens) - 1, 0, -1)]
        for cand in candidates:
            cand = clean_toponym(cand)
            if not cand or not cand[0].isupper() or _ORG.search(cand):
                continue
            ident, how = self.single(cand, corpus, year)
            if ident:
                return cand, ident, "institution_place:" + how
        return None

    def resolve(self, surface, corpus, year):
        """[(part, identity, method)] — identity None means excluded (method=reason)."""
        rule = self.surfaces.get(canon_key(clean_toponym(surface) or surface), {})
        if rule.get("exclude"):
            return [(surface, None, rule["exclude"])]
        identity, method = self.single(surface, corpus, year)
        if identity:
            return [(surface, identity, method)]
        parts = [x for x in re.split(r"\s*(?:,|;|&|\band\b|/)\s*", surface) if x and x.strip(" .")]
        if len(parts) > 1:
            out = []
            for part in parts:
                ident, how = self.single(part, corpus, year)
                if ident:
                    out.append((part, ident, "composite:" + how))
                    continue
                reason = self.classify_unresolved(part)
                out.append((part, None if reason else ("name", self.name_key(part)),
                            reason or "composite:name_only"))
            if any(i for _, i, _ in out):
                return out
        reason = self.classify_unresolved(surface)
        if reason == "institution_or_office":
            found = self.place_in_institution(surface, corpus, year)
            if found:
                return [found]
        if reason:
            return [(surface, None, reason)]
        if method == "ambiguous_surface":
            return [(surface, ("name", self.name_key(surface)), "name_only_ambiguous_surface")]
        return [(surface, ("name", self.name_key(surface)), "name_only")]

    @staticmethod
    def name_key(surface):
        return canon_key(canonicalize(clean_toponym(surface)))


# -------------------------------------------------------------- source texts
class Sources:
    """Raw biography text per bio_id across editions, with clause splits."""

    def __init__(self, root):
        self.root, self.loc, self.text, self.edition = root, {}, {}, {}
        self.files = []
        for corpus in ("kg", "iol"):
            for path in sorted((root / f"data/{corpus}/bios").glob("*.jsonl")):
                if path.name.endswith(".xref.jsonl"):
                    continue
                self.files.append(path)
                for line, bio in rows(path):
                    bid = bio.get("bio_id")
                    if not bid:
                        continue
                    self.text[bid] = bio.get("raw_text") or ""
                    self.loc[bid] = (str(path.relative_to(root)), line)
                    self.edition[bid] = (bio.get("edition_year"), path.stem)
        self._norm, self._clauses = {}, {}

    def get(self, bid):
        if bid in self.text:
            return bid
        base = re.sub(r"_s\d+$", "", bid)
        return base if base in self.text else None

    def normalized(self, bid):
        if bid not in self._norm:
            self._norm[bid] = f" {norm(self.text[bid])} "
        return self._norm[bid]

    def clauses(self, bid):
        if bid not in self._clauses:
            raw = self.text[bid]
            spans, start = [], 0
            for m in re.finditer(r";|\.\s+(?=[A-Z])", raw):
                spans.append((start, m.start()))
                start = m.end()
            spans.append((start, len(raw)))
            self._clauses[bid] = [(a, b, f" {norm(raw[a:b])} ") for a, b in spans if b > a]
        return self._clauses[bid]


def edition_label(corpus, stem, year):
    m = re.search(r"_(jan|jul)\b", stem or "")
    month = {"jan": "January ", "jul": "July "}.get(m[1], "") if m else ""
    return f"{CORPUS_TITLE[corpus]} ({month}{year})"


def locate(sources, bid, printed, year):
    """Return (tier, clause-level locator) for one attestation bio."""
    needle = f" {norm(printed)} "
    if needle == "  " or needle not in sources.normalized(bid):
        return None, None
    raw = sources.text[bid]
    yr = re.compile(rf"(?<!\d){year}(?!\d)") if year else None
    best = None
    for a, b, nclause in sources.clauses(bid):
        if needle in nclause:
            hit = {"clause_start": a, "clause_end": b}
            m = re.search(re.escape(printed), raw[a:b], re.I)
            if m:  # exact printed-name offsets only when the string occurs literally
                hit.update(char_start=a + m.start(), char_end=a + m.end())
            if yr and yr.search(raw[a:b]):
                return "same_clause", hit
            best = best or hit
    if best is None:  # name straddles a clause split
        m = re.search(re.escape(printed), raw, re.I)
        best = {"char_start": m.start(), "char_end": m.end()} if m else {}
    return "printed", best


# ------------------------------------------------------------------- statuses
def relationship(qid, year, rules):
    matches = [r for r in rules if r["qid"] == qid and year is not None
               and r["start"] <= year <= r["end"]]
    if not matches:
        return {"status": "unknown", "sources": []}
    statuses = {r["status"] for r in matches}
    return {"status": next(iter(statuses)) if len(statuses) == 1 else "mixed_or_contested",
            "sources": sorted({r["source"] for r in matches})}


def validate_rules(config):
    if config.get("version") != 1:
        raise ValueError("Unsupported rules version")
    for rule in config.get("imperial_relationships", []):
        if (rule.get("status") not in STATUSES or not rule.get("source")
                or type(rule.get("start")) is not int or type(rule.get("end")) is not int
                or rule["start"] > rule["end"] or not re.fullmatch(r"Q\d+", rule.get("qid", ""))):
            raise ValueError(f"Invalid status rule: {rule}")


def validate_identities(config):
    if config.get("version") != 1:
        raise ValueError("Unsupported identities version")
    local = config.get("local_places", {})
    for rule in config.get("period_identities", []):
        last = None
        for p in sorted(rule["periods"], key=lambda p: p["start"]):
            if p["start"] >= p["end"] or (last is not None and p["start"] < last):
                raise ValueError(f"Overlapping or empty period in {rule['surfaces']}")
            if bool(p.get("qid")) == bool(p.get("local")):
                raise ValueError("Each period needs exactly one of qid/local")
            if p.get("qid") and not re.fullmatch(r"Q\d+", p["qid"]):
                raise ValueError(f"Bad QID {p['qid']}")
            if p.get("local") and p["local"] not in local:
                raise ValueError(f"Unknown local place {p['local']}")
            last = p["end"]


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def write_json(path, value, indent=2):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=indent) + "\n", encoding="utf-8")


# ------------------------------------------------------------ name contexts
SOVEREIGN_UMBRELLAS = {"Q145", "Q174193", "Q161885", "Q8680", "Q179876"}


def context_links(qid, authority):
    """The context plus its non-umbrella countries (P17): contexts sharing any
    of these are one group (Madras Presidency and British Raj; Ontario and Canada)."""
    return [qid] + [c for c in authority.entities.get(qid, {}).get("countries", []) if c not in SOVEREIGN_UMBRELLAS]


def context_group(qid, authority):
    """Country-level group for a colony context: provinces of the Raj or of
    Canada collapse to their country; Crown colonies (P17 = UK) stay separate."""
    countries = [c for c in authority.entities.get(qid, {}).get("countries", []) if c not in SOVEREIGN_UMBRELLAS]
    return countries[0] if len(countries) == 1 else qid


def merge_place(dst, src):
    dst["mentions"] += src["mentions"]
    for field in ("tiers", "methods", "toponyms", "printed_surfaces", "raw_surfaces", "contexts",
                  "printed_parents"):
        dst[field].update(src[field])
    dst["corpora"] |= src["corpora"]
    dst["fallback_editions"] |= src["fallback_editions"]
    for name, rank in src["toponym_tiers"].items():
        dst["toponym_tiers"][name] = min(rank, dst["toponym_tiers"].get(name, 9))
    for name, cites in src["citations"].items():
        dst["citations"][name] |= cites
    for tier in TIERS:
        dst["years"][tier] |= src["years"][tier]
    dst["examples"] = (dst["examples"] + src["examples"])[:3]


def merge_name_contexts(places, authority):
    """Fold per-context name records into one record per context group.
    Context-free mentions join the group only when there is exactly one."""
    remap, bases = {}, collections.defaultdict(list)
    for key in list(places):
        if key.startswith("name:"):
            bases[key[5:].split("|")[0]].append(key)
    for base, keys in bases.items():
        groups = collections.defaultdict(list)
        loose = []
        parent = {}

        def find(x):
            while parent.setdefault(x, x) != x:
                x = parent[x]
            return x
        ctxs = {key: key.split("|")[1] for key in keys if "|" in key}
        for ctx in set(ctxs.values()):
            for c in context_links(ctx, authority):
                parent[find(c)] = find(ctx)
        for key in keys:
            (groups[find(ctxs[key])] if key in ctxs else loose).append(key)
        # No minority folding: a stray one-mention context is a cheaper error
        # than merging two real places (St. Thomas, Ontario into Jamaica).
        targets = {}
        for group, members in groups.items():
            members.sort(key=lambda k: -places[k]["mentions"])
            target = f"name:{base}" if len(groups) == 1 else f"name:{base}|{group}"
            targets[group] = target
            for key in members:
                remap[key] = target
        if loose:
            target = next(iter(targets.values())) if len(targets) == 1 else f"name:{base}"
            for key in loose:
                remap[key] = target
        merged = {}
        for key in keys:
            target = remap[key]
            p = places.pop(key)
            if target in merged:
                merge_place(merged[target], p)
            else:
                p["key"] = target
                merged[target] = p
        places.update(merged)
    return remap


# ----------------------------------------------------------------------- run
def attestations(root, corpus):
    """person_id → bio_ids of every edition that printed the biography."""
    out = {}
    for name in ("llm_struct_corpus.stage3.jsonl", "llm_struct_corpus.stage3.deduped.jsonl"):
        path = root / f"data/{corpus}/{name}"
        if path.exists():
            for _, r in rows(path):
                out[r["person_id"]] = list(r.get("attestations") or [])
    return out


def run(root, output, rules_path, identities_path, authority_path, force=False):
    rules = json.loads(rules_path.read_text(encoding="utf-8"))
    validate_rules(rules)
    identities = json.loads(identities_path.read_text(encoding="utf-8"))
    validate_identities(identities)
    inputs = [rules_path, identities_path, authority_path, Path(__file__)]
    for corpus in ("kg", "iol"):
        graph = root / f"data/{corpus}/graph_stage3"
        inputs += [graph / "places.jsonl", graph / "career_events.jsonl"]
        inputs += [p for p in (root / f"data/{corpus}/places_grounding.jsonl",
                               root / f"data/{corpus}/llm_struct_corpus.stage3.jsonl",
                               root / f"data/{corpus}/llm_struct_corpus.stage3.deduped.jsonl") if p.exists()]
        inputs += sorted((root / f"data/{corpus}/bios").glob("*.jsonl"))
    inputs += [root / "col_match/kg/place_canon.py", root / "col_match/kg/ground.py"]
    inputs = [p for p in inputs if p.exists()]
    manifest = {str(p.relative_to(root)) if p.is_relative_to(root) else str(p): digest(p) for p in inputs}
    output.mkdir(parents=True, exist_ok=True)
    outputs = ["whg-places.tsv", "whg-places.lpf.json", "places.jsonl", "evidence.jsonl",
               "review.tsv", "excluded-mentions.tsv", "held-names.tsv", "report.json"]
    previous = output / "manifest.json"
    if not force and previous.exists():
        old = json.loads(previous.read_text())
        if old.get("inputs") == manifest and all(
                (output / n).exists() and digest(output / n) == old.get("outputs", {}).get(n) for n in outputs):
            print("Unchanged inputs and outputs; reused", output)
            return json.loads((output / "report.json").read_text())

    authority = Authority(authority_path)
    resolver = Resolver(root, identities)
    sources = Sources(root)
    local_places = identities.get("local_places", {})
    counts = collections.Counter()
    graph_labels = collections.defaultdict(set)
    for corpus in ("kg", "iol"):
        for _, r in rows(root / f"data/{corpus}/graph_stage3/places.jsonl"):
            if r.get("qid") and r.get("label"):
                graph_labels[r["qid"]].add(r["label"])

    def graph_label(q):
        return sorted(graph_labels[q])[0] if graph_labels.get(q) else q

    places = {}
    excluded = collections.defaultdict(lambda: {"count": 0, "corpora": set(), "years": set(), "examples": []})

    def place(key):
        if key not in places:
            places[key] = {"key": key, "mentions": 0, "tiers": collections.Counter(),
                           "corpora": set(), "methods": collections.Counter(),
                           "toponyms": collections.Counter(), "toponym_tiers": {},
                           "citations": collections.defaultdict(set),
                           "years": {t: set() for t in TIERS}, "printed_surfaces": collections.Counter(),
                           "raw_surfaces": collections.Counter(), "contexts": collections.Counter(),
                           "printed_parents": collections.Counter(),
                           "fallback_editions": set(),
                           "examples": []}
        return places[key]

    with (output / "evidence.jsonl").open("w", encoding="utf-8") as evidence:
        for corpus in ("kg", "iol"):
            attest = attestations(root, corpus)
            career = collections.defaultdict(list)
            for _, e in rows(root / f"data/{corpus}/graph_stage3/career_events.jsonl"):
                if e.get("colony_qid"):
                    career[e["person_id"]].append((e.get("seq") or 0, e["colony_qid"], e.get("colony_label")))
            for line_no, event in rows(root / f"data/{corpus}/graph_stage3/career_events.jsonl"):
                counts[f"{corpus}_events"] += 1
                raw_place = (event.get("place_raw") or "").strip()
                year = valid_year(event.get("year_start"))
                if event.get("place_qid"):
                    targets = [(raw_place or event.get("place_label") or "", ("wd", event["place_qid"]), "graph")]
                    # The graph also grounded office and campaign strings ("Bahamas
                    # census", "Nandi expedit."): keep the place word or exclude.
                    reason = resolver.classify_unresolved(raw_place) if raw_place else None
                    if reason and resolver.surfaces.get(canon_key(clean_toponym(raw_place)), {}).get("exclude"):
                        targets = [(raw_place, None, reason)]
                    elif reason in ("institution_or_office", "campaign_or_noise", "military_unit"):
                        found = (resolver.place_in_institution(raw_place, corpus, year)
                                 if reason == "institution_or_office" else None)
                        targets = ([(found[0], ("wd", event["place_qid"]), "graph:place_in_institution")]
                                   if found and found[1] == ("wd", event["place_qid"])
                                   else [(raw_place, None, reason)])
                elif raw_place:
                    if is_institution(raw_place)[0]:
                        targets = [(raw_place, None, "institution_or_office")]
                        parts = re.split(r"\s*,\s*", raw_place)
                        found = resolver.place_in_institution(raw_place, corpus, year)
                        if len(parts) > 1:  # "S. African museum, Capetown" keeps Capetown
                            tail = resolver.resolve(parts[-1], corpus, year)
                            if any(i for _, i, _ in tail):
                                targets = tail
                                found = None
                        if found:
                            targets = [found]
                    else:
                        targets = resolver.resolve(raw_place, corpus, year)
                else:
                    counts["events_without_place"] += 1
                    continue
                counts[f"{corpus}_place_mentions"] += 1
                bios = [b for b in (sources.get(x) for x in attest.get(event["person_id"], [])) if b]
                if not bios:
                    m = re.match(r"kgp_(.+?)(?:_s\d+)?$", event["person_id"])
                    b = sources.get(m[1]) if m else None
                    bios = [b] if b else []
                for t_index, (printed, identity, method) in enumerate(targets):
                    if identity is None:
                        e = excluded[(method, printed)]
                        e["count"] += 1
                        e["corpora"].add(corpus)
                        if year:
                            e["years"].add(year)
                        counts["excluded:" + method] += 1
                        continue
                    if identity[0] == "wd" and authority.non_place(identity[1]):
                        e = excluded[("non_place_entity:" + identity[1], printed)]
                        e["count"] += 1
                        e["corpora"].add(corpus)
                        counts["excluded:non_place_entity"] += 1
                        continue
                    context, printed_parent = None, None
                    if identity[0] == "name":
                        # A qualifier printed in the same string ("Kalgoorlie, W.A.")
                        # is evidence; otherwise the previous posting is only a key
                        # for keeping homonyms apart, never an exported parent.
                        qualifiers = [i for _, i, _ in targets[t_index + 1:] if i and i[0] == "wd"] \
                            if "," in raw_place else []
                        if qualifiers:
                            q = qualifiers[0][1]
                            printed_parent = (q, authority.entities.get(q, {}).get("label") or graph_label(q))
                            context = printed_parent
                        else:
                            seq = event.get("seq") or 0
                            near = sorted(career.get(event["person_id"], []),
                                          key=lambda c: (c[0] > seq, abs(c[0] - seq)))
                            if near:
                                context = near[0][1:]
                        if context:
                            identity = ("name", f"{identity[1]}|{context[0]}")
                    key = ":".join(identity)
                    p = place(key)
                    if context:
                        p["contexts"][context] += 1
                    if printed_parent:
                        p["printed_parents"][printed_parent] += 1
                    p["mentions"] += 1
                    p["corpora"].add(corpus)
                    p["methods"][method.split(":")[-1] if method.startswith("composite") else method.split(":")[0]] += 1
                    p["raw_surfaces"][printed] += 1
                    m = re.match(r"kgp_(col|iol)(\d{4})", event["person_id"])
                    if m and valid_year(int(m[2])):
                        p["fallback_editions"].add((int(m[2]), corpus))
                    best_tier, best_loc, best_bid, printed_in = "structured_only", None, None, []
                    for bid in bios:
                        edition = sources.edition[bid][0]
                        if year and type(edition) is int and edition < year:
                            continue  # an earlier edition cannot attest this posting
                        tier, loc = locate(sources, bid, printed, year) if printed else (None, None)
                        if not tier:
                            continue
                        printed_in.append(bid)
                        if best_tier != "same_clause" and (tier == "same_clause" or best_tier == "structured_only"):
                            best_tier, best_loc, best_bid = tier, loc, bid
                    p["tiers"][best_tier] += 1
                    counts["tier:" + best_tier] += 1
                    if year:
                        p["years"][best_tier].add(year)
                        if valid_year(event.get("year_end")):
                            p["years"][best_tier].add(event["year_end"])
                    if printed_in and not method.endswith("surface_rule"):  # aliases repair OCR; not name forms
                        name = clean_toponym(printed)
                        p["printed_surfaces"][printed] += 1
                        if exportable_name(name):
                            p["toponyms"][name] += 1
                            rank = TIERS.index(best_tier)
                            p["toponym_tiers"][name] = min(rank, p["toponym_tiers"].get(name, 9))
                            for bid in printed_in:
                                ed_year, stem = sources.edition[bid]
                                if valid_year(ed_year):
                                    p["citations"][name].add((ed_year, edition_label(corpus, stem, ed_year)))
                        else:
                            counts["toponyms_held_for_punctuation"] += 1
                    record = {"place_id": key, "printed_name": printed, "historical_year": year,
                              "corpus": corpus, "identity_method": method, "evidence_tier": best_tier,
                              "graph_event": {"path": f"data/{corpus}/graph_stage3/career_events.jsonl",
                                              "line": line_no}}
                    if best_bid:
                        path, line = sources.loc[best_bid]
                        record["source"] = {"path": path, "line": line, **best_loc}
                        record["publication_year"] = sources.edition[best_bid][0]
                        record["printed_in_editions"] = sorted(
                            {sources.edition[b][0] for b in printed_in if sources.edition[b][0]})
                        if len(p["examples"]) < 3:
                            p["examples"].append(record["source"])
                    evidence.write(json.dumps(record, ensure_ascii=False) + "\n")

    # Name-only homonyms: one record per country-level context group.
    remap = merge_name_contexts(places, authority)

    # ------------------------------------------------------------- export
    fields = ["id", "title", "title_source", "attestation_year", "start", "end", "fclasses",
              "aat_types", "types", "matches", "variants", "parent_name", "parent_id",
              "lon", "lat", "geo_source", "geo_id", "description"]
    features, review_rows, used_ids, held_rows = [], [], set(), []
    with ((output / "places.jsonl").open("w", encoding="utf-8") as place_file,
          (output / "whg-places.tsv").open("w", encoding="utf-8", newline="") as tsv_file):
        tsv = csv.DictWriter(tsv_file, fieldnames=fields, delimiter="\t", lineterminator="\n",
                             quoting=csv.QUOTE_NONE, escapechar=None)
        tsv.writeheader()
        for key, p in sorted(places.items()):
            kind, ident = key.split(":", 1)
            qid = ident if kind == "wd" else None
            local = local_places.get(ident, {}) if kind == "local" else {}
            ent = authority.entities.get(qid, {}) if qid else {}
            wd_label = ent.get("label") or (sorted(graph_labels[qid])[0] if qid and graph_labels[qid] else None)
            issues = []
            # Years: the strongest evidence tier that has any year.
            years, year_tier = set(), None
            for tier in TIERS:
                if p["years"][tier]:
                    years, year_tier = p["years"][tier], tier
                    break
            inception, dissolved = authority.bounds(qid) if qid else (None, None)
            out_of_period = sorted(y for y in years if (inception and y < inception - 1)
                                   or (dissolved and y > dissolved + 1))
            if out_of_period:
                issues.append("years_outside_authority_entity_dates")
            in_period = sorted(set(years) - set(out_of_period)) or sorted(years)
            # Title: the most-attested printed toponym, strongest tier first.
            toponyms = sorted(p["toponyms"], key=lambda n: (is_abbreviated(n), p["toponym_tiers"][n],
                                                            -p["toponyms"][n], n))
            if toponyms and (not is_abbreviated(toponyms[0]) or not (wd_label or local.get("title"))):
                title = toponyms[0]
                first = min(p["citations"][title])
                title_source, attestation_year = first[1], first[0]
            elif toponyms:  # only abbreviations printed ("H.K."): authority label, cited honestly
                printed_as = toponyms[0]
                first = min(p["citations"][printed_as])
                title = local.get("title") or wd_label
                title_source = f"{first[1]}, printed as {printed_as}; full form from Wikidata {qid}" if qid else \
                               f"{first[1]}, printed as {printed_as}"
                attestation_year = first[0]
                issues.append("title_from_authority_label")
            else:
                title = local.get("title") or wd_label or (p["raw_surfaces"].most_common(1)[0][0] if p["raw_surfaces"] else ident)
                title = clean_toponym(title) or ident
                title_source, attestation_year = None, None
                if p["fallback_editions"]:
                    fy, fc = min(p["fallback_editions"])
                    title_source = (f"{CORPUS_TITLE[fc]} ({fy}), structured biography; "
                                    + (f"name form from Wikidata {qid}" if qid and wd_label else "printed form not matched verbatim"))
                    attestation_year = fy
                else:
                    title_source = f"Wikidata {qid}" if qid else "Career graph (structured)"
                issues.append("title_not_printed_in_source")
            if not exportable_name(title):
                issues.append("title_needs_punctuation_review")
                title = re.sub(r'[;\t"“”@|]', " ", title).strip()
            # Types and feature classes.
            types = authority.types(qid)[:3] if qid else []
            fcl = authority.fclasses(qid) if qid else []
            if kind == "local":
                fcl = [local.get("fclass", "A")]
            if not fcl:
                fcl = [fclass_from_name(title)]
                issues.append("feature_class_from_name")
            if kind == "name":
                issues.append("no_authority_match")
            if not p["tiers"]["same_clause"] and not p["tiers"]["printed"]:
                issues.append("not_found_in_source_text")
            # Geometry: Wikidata point (or curated local point); never atlas seats.
            lon = lat = geo_source = geo_id = ""
            override = identities.get("geometry_overrides", {}).get(qid) if qid else None
            if override:
                lon, lat, geo_source = override["lon"], override["lat"], override["geo_source"]
                issues.append("reviewed_geometry_override")
            elif ent.get("coords"):
                lon, lat = ent["coords"][0]
                geo_source, geo_id = "Wikidata", f"https://www.wikidata.org/wiki/{qid}"
                if len(ent["coords"]) > 1:
                    issues.append("multiple_authority_coordinates")
            elif local.get("lon") is not None:
                lon, lat, geo_source = local["lon"], local["lat"], local.get("geo_source", "")
            else:
                issues.append("no_geometry")
            pid = ("ip-" + qid) if qid else (f"ip-local-{ident}" if kind == "local" else f"ip-name-{slug(ident)}")
            if pid in used_ids:  # slug collision ("Bala-Pitimodara" vs "Bala Pitimodara")
                pid += "-" + hashlib.sha1(key.encode()).hexdigest()[:6]
            used_ids.add(pid)
            seen_norm = {norm(title)}
            variants = []
            for n in toponyms:
                if n == title or "," in n or norm(n) in seen_norm:
                    continue  # comma-qualified forms stay in the evidence
                seen_norm.add(norm(n))
                variants.append(n)
            parent_name = parent_id = ""
            if kind == "name" and p["printed_parents"]:
                (cq, clabel), _ = p["printed_parents"].most_common(1)[0]
                parent_name = clabel or cq
                parent_id = f"https://www.wikidata.org/wiki/{cq}"
                issues.append("parent_printed_with_name")
            description = (f"Place named in British imperial career biographies ({', '.join(CORPUS_TITLE[c] for c in sorted(p['corpora']))}); "
                           f"{p['mentions']} dated career reference(s). Years give the span of those references, not the place's existence.")
            if local.get("description"):
                description = local["description"] + " " + description
            start = end = ""
            if in_period:
                start, end = str(in_period[0]), str(in_period[-1])
            if attestation_year is None and not start and p["fallback_editions"]:
                fy, fc = min(p["fallback_editions"])
                title_source, attestation_year = f"{CORPUS_TITLE[fc]} ({fy}), structured biography", fy
                issues.append("attestation_year_from_biography_edition")
            if attestation_year is None and not start:
                issues.append("no_dated_attestation")
            row = {"id": pid, "title": title, "title_source": title_source,
                   "attestation_year": attestation_year or "", "start": start,
                   "end": end if end != start else "", "fclasses": ";".join(fcl),
                   "aat_types": ";".join(a for _, a in types) if any(a for _, a in types) else "",
                   "types": ";".join(t.replace(";", ",") for t, _ in types),
                   "matches": f"wd:{qid}" if qid else "", "variants": ";".join(f"{v}@en" for v in variants),
                   "parent_name": parent_name.replace(";", ","), "parent_id": parent_id,
                   "lon": lon, "lat": lat, "geo_source": geo_source, "geo_id": geo_id,
                   "description": description}
            # Single-mention unmatched names made only of abbreviations are the
            # junkiest class (organisations, fragments): held for review, listed.
            held = kind == "name" and p["mentions"] < 2 and is_abbreviated(title)
            if held:
                issues.append("held_single_abbreviated_name")
                held_rows.append({"id": pid, "title": title, "mentions": p["mentions"],
                                  "title_source": title_source, "start": start, "end": end})
            else:
                tsv.writerow(row)
            # LPF names: citations carry publication years; the feature's `when`
            # carries the event years. Every name has a citation.
            names = []
            for n in toponyms or [title]:
                cites = sorted(p["citations"].get(n, set()))
                item = {"toponym": n, "lang": "en"}
                if cites:
                    item["citations"] = [{"label": label, "year": y} for y, label in cites[:MAX_CITATIONS]]
                else:
                    item["citations"] = [{"label": title_source, **({"year": attestation_year} if attestation_year else {})}]
                names.append(item)
            if title not in [n["toponym"] for n in names]:
                names.insert(0, {"toponym": title, "lang": "en",
                                 "citations": [{"label": f"Wikidata {qid}" if qid else title_source,
                                                **({"@id": f"https://www.wikidata.org/wiki/{qid}"} if qid else {})}]})
            when = {"timespans": [{"start": {"in": start}, "end": {"in": end or start}}]} if start else \
                   ({"timespans": [{"start": {"in": str(attestation_year)}}]} if attestation_year else None)
            feature = {"@id": ID_BASE + pid, "type": "Feature",
                       "properties": {"title": title, "fclasses": fcl},
                       "names": names,
                       "types": [{"identifier": f"aat:{a}", "label": t} for t, a in types if a],
                       "geometry": {"type": "Point", "coordinates": [lon, lat]} if lon != "" else None,
                       "links": [{"type": "closeMatch", "identifier": f"wd:{qid}"}] if qid else [],
                       "descriptions": [{"value": description, "lang": "en"}]}
            if parent_id:
                feature["relations"] = [{"relationType": "gvp:broaderPartitive", "relationTo": parent_id,
                                         "label": f"within {parent_name} (printed with the name in the source)",
                                         "certainty": "certain"}]
            if when:
                feature["when"] = when
            if not held:
                features.append(feature)
            result = {"id": pid, "key": key, "qid": qid, "title": title, "wikidata_label": wd_label,
                      "local": bool(local), "fclasses": fcl, "types": types,
                      "mentions": p["mentions"], "evidence_tiers": dict(p["tiers"]),
                      "identity_methods": dict(p["methods"]), "corpora": sorted(p["corpora"]),
                      "printed_toponyms": dict(p["toponyms"].most_common()),
                      "years_by_tier": {t: sorted(v) for t, v in p["years"].items()},
                      "year_tier_used": year_tier, "out_of_period_years": out_of_period,
                      "authority_inception": inception, "authority_dissolved": dissolved,
                      "imperial_relationships_by_year": {str(y): relationship(qid, y, rules.get("imperial_relationships", []))
                                                         for y in in_period} if qid else {},
                      "source_examples": p["examples"], "review_issues": issues}
            place_file.write(json.dumps(result, ensure_ascii=False) + "\n")
            review_rows.append({"key": key, "id": pid, "qid": qid or "", "title": title, "mentions": p["mentions"],
                                "same_clause": p["tiers"]["same_clause"], "printed": p["tiers"]["printed"],
                                "structured_only": p["tiers"]["structured_only"],
                                "start": start, "end": end, "fclasses": ";".join(fcl),
                                "issues": ";".join(issues)})
            if held:
                counts["held_name_only"] += 1
            else:
                counts["export_places"] += 1
                counts[f"export_{kind}"] += 1
            for issue in issues:
                counts["issue:" + issue] += 1

    write_json(output / "whg-places.lpf.json", {"type": "FeatureCollection", "@context": LPF_CONTEXT,
                                                "features": features}, indent=None)
    review_rows.sort(key=lambda r: (-len(r["issues"].split(";")) if r["issues"] else 0, -r["mentions"], r["id"]))
    with (output / "review.tsv").open("w", encoding="utf-8", newline="") as handle:
        w = csv.DictWriter(handle, fieldnames=list(review_rows[0]) if review_rows else ["id"],
                           delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(sorted(review_rows, key=lambda r: (-r["mentions"], r["id"])))
    with (output / "held-names.tsv").open("w", encoding="utf-8", newline="") as handle:
        w = csv.DictWriter(handle, fieldnames=["id", "title", "mentions", "title_source", "start", "end"],
                           delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(sorted(held_rows, key=lambda r: r["title"]))
    with (output / "excluded-mentions.tsv").open("w", encoding="utf-8", newline="") as handle:
        w = csv.writer(handle, delimiter="\t", lineterminator="\n")
        w.writerow(["reason", "printed_name", "mentions", "corpora", "first_year", "last_year"])
        for (reason, printed), e in sorted(excluded.items(), key=lambda x: (x[0][0], -x[1]["count"], x[0][1])):
            w.writerow([reason, printed.replace("\t", " "), e["count"], ";".join(sorted(e["corpora"])),
                        min(e["years"]) if e["years"] else "", max(e["years"]) if e["years"] else ""])
    export_ids = {r["key"]: r["id"] for r in review_rows}
    tmp = output / "evidence.jsonl.tmp"
    with (output / "evidence.jsonl").open(encoding="utf-8") as src, tmp.open("w", encoding="utf-8") as dst:
        for line in src:
            record = json.loads(line)
            record["place_id"] = export_ids[remap.get(record["place_id"], record["place_id"])]
            dst.write(json.dumps(record, ensure_ascii=False) + "\n")
    tmp.replace(output / "evidence.jsonl")
    report = {"pipeline_version": VERSION, "counts": dict(sorted(counts.items())),
              "scope": "Every place mention in both career graphs; no people or career networks in exports.",
              "notes": [
                  "Graph place_qid identities are the reviewed career-graph grounding; others via config/whg_place_identities.json and the project's grounding tables.",
                  "Name-only places have no authority match yet; WHG reconciliation can propose one.",
                  "Years are the span of dated career references printed in the Lists, not place lifespans.",
                  "Excluded mentions are listed with reasons in excluded-mentions.tsv; nothing is dropped silently.",
                  "Geometry is the Wikidata point (or a curated local point), never an atlas plotting seat.",
                  "No network calls, WHG upload, or publication performed by this build."]}
    write_json(output / "report.json", report)
    write_json(previous, {"inputs": manifest, "outputs": {n: digest(output / n) for n in outputs}})
    print(json.dumps(report, indent=2))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--out", type=Path, default=ROOT / "out/whg")
    parser.add_argument("--rules", type=Path, default=ROOT / "config/whg_rules.json")
    parser.add_argument("--identities", type=Path, default=ROOT / "config/whg_place_identities.json")
    parser.add_argument("--authority", type=Path, default=ROOT / "data/whg/wikidata_places.json")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    run(args.root.resolve(), args.out.resolve(), args.rules.resolve(), args.identities.resolve(),
        args.authority.resolve(), args.force)


if __name__ == "__main__":
    main()
