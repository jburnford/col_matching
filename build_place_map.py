#!/usr/bin/env python3
"""Build a self-contained Leaflet HTML map of every grounded place in the cache.

Joins places_grounding.jsonl (surface->QID) with the worklist (surface->mention
count), fetches coordinates+label+country from WDQS, and emits an interactive map
where each distinct location is a circle marker scaled by total mention count.

Usage:  python3 build_place_map.py
Output: docs/grounded_places_map.html
"""
import json, subprocess, collections, math, html, time

CACHE = "data/kg/places_grounding.jsonl"
WORKLIST = "data/kg/places_worklist.grounding.jsonl"
OUT = "docs/grounded_places_map.html"
WDQS = "https://query.wikidata.org/sparql"
UA = "col_matching-place-map/1.0 (cljim22@gmail.com)"

def sparql(query):
    out = subprocess.run(
        ["curl", "-s", "-G", WDQS, "--data-urlencode", "query=" + query,
         "-H", "Accept: application/sparql-results+json", "-H", "User-Agent: " + UA],
        capture_output=True, text=True, timeout=90).stdout
    return json.loads(out)["results"]["bindings"]

def qid(uri): return uri.rsplit("/", 1)[-1] if uri else None
def chunks(l, n):
    for i in range(0, len(l), n): yield l[i:i+n]

# --- join surface -> qid -> (count, surfaces) ---
rows = [json.loads(l) for l in open(CACHE)]
s2q = {r["place"]: r["qid"] for r in rows if r.get("qid")}
wl = [json.loads(l) for l in open(WORKLIST) if not l.startswith("#")]
qcount = collections.Counter(); qsurf = collections.defaultdict(set)
for r in wl:
    surfaces = [r["query"]] + [x[0] for x in r.get("variants", [])]
    for s in surfaces:
        if s in s2q:
            q = s2q[s]; qcount[q] += r["count"]
            qsurf[q].update(surfaces); break
qids = sorted(qcount)
print(f"grounded QIDs: {len(qids)}")

# --- fetch coord + label + country ---
info = {}
for ci, ch in enumerate(chunks(qids, 150)):
    vals = " ".join("wd:" + q for q in ch)
    q = (f"SELECT ?item ?itemLabel ?coord ?countryLabel WHERE {{ "
         f"VALUES ?item {{ {vals} }} "
         f"OPTIONAL {{ ?item wdt:P625 ?coord }} "
         f"OPTIONAL {{ ?item wdt:P17 ?country }} "
         f"SERVICE wikibase:label {{ bd:serviceParam wikibase:language 'en'. }} }}")
    for b in sparql(q):
        it = qid(b["item"]["value"])
        rec = info.setdefault(it, {"label": None, "lat": None, "lon": None, "country": None})
        if "itemLabel" in b: rec["label"] = b["itemLabel"]["value"]
        if "countryLabel" in b: rec["country"] = b["countryLabel"]["value"]
        if "coord" in b and rec["lat"] is None:
            w = b["coord"]["value"]            # "Point(lon lat)"
            try:
                lon, lat = w[w.find("(")+1:w.find(")")].split()
                rec["lat"], rec["lon"] = float(lat), float(lon)
            except Exception: pass
    print(f"  chunk {ci+1}/{(len(qids)+149)//150}")
    time.sleep(1)

# --- assemble marker list ---
feats, no_coord = [], []
for q in qids:
    r = info.get(q, {})
    cnt = qcount[q]
    surfaces = sorted(qsurf[q], key=lambda s: (s != r.get("label"), s.lower()))[:6]
    if r.get("lat") is None:
        no_coord.append((q, r.get("label") or q, cnt)); continue
    feats.append({"q": q, "label": r.get("label") or q, "lat": r["lat"], "lon": r["lon"],
                  "country": r.get("country") or "", "count": cnt, "surfaces": surfaces})
feats.sort(key=lambda f: -f["count"])
total_mentions = sum(qcount.values())
mapped_mentions = sum(f["count"] for f in feats)
print(f"mapped {len(feats)} locations ({mapped_mentions} mentions); "
      f"{len(no_coord)} QIDs without coords ({total_mentions-mapped_mentions} mentions)")

data_json = json.dumps(feats, ensure_ascii=False)
nc_rows = "".join(f"<tr><td>{html.escape(l)}</td><td>{c}</td>"
                  f"<td><a href='https://www.wikidata.org/wiki/{q}' target='_blank'>{q}</a></td></tr>"
                  for q, l, c in sorted(no_coord, key=lambda x: -x[2]))

HTML = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Grounded places — col_matching</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
 body{margin:0;font:14px/1.4 system-ui,sans-serif}
 #map{height:78vh}
 header{padding:10px 16px;background:#1b2a4a;color:#fff}
 header h1{margin:0 0 3px;font-size:18px}
 header .sub{font-size:12px;opacity:.85}
 .panel{padding:10px 16px;max-height:18vh;overflow:auto;background:#f6f7f9;border-top:1px solid #ddd}
 .panel h2{font-size:13px;margin:0 0 6px}
 table{border-collapse:collapse;font-size:12px}
 td{border-bottom:1px solid #e3e3e3;padding:2px 10px 2px 0}
 .leaflet-popup-content{font-size:13px}
 .leaflet-popup-content b{font-size:14px}
 .legend{background:#fff;padding:6px 9px;border-radius:5px;box-shadow:0 1px 5px rgba(0,0,0,.3);font-size:12px;line-height:1.6}
 .legend i{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:6px;opacity:.8;border:1px solid #555}
</style></head><body>
<header><h1>Grounded places — col_matching place cache</h1>
<div class="sub">__N__ distinct locations mapped · __MM__ of __TM__ grounded mentions · marker size ∝ mention count · click for details</div></header>
<div id="map"></div>
<div class="panel"><h2>Grounded entities without point coordinates (__NC__ — mostly colonies/regions, not shown on map)</h2>
<table>__NCROWS__</table></div>
<script>
const FEATS = __DATA__;
const map = L.map('map',{worldCopyJump:true}).setView([10,20],2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  {maxZoom:18, attribution:'&copy; OpenStreetMap'}).addTo(map);
function color(c){return c>=1000?'#7a0177':c>=200?'#c51b8a':c>=50?'#f768a1':c>=10?'#fa9fb5':'#feebe2';}
function radius(c){return Math.max(3, Math.min(34, 2.2*Math.sqrt(c)));}
const bounds=[];
for(const f of FEATS){
  bounds.push([f.lat,f.lon]);
  const m=L.circleMarker([f.lat,f.lon],{radius:radius(f.count),color:'#333',weight:.6,
     fillColor:color(f.count),fillOpacity:.78});
  const surf=f.surfaces.map(s=>'<code>'+s.replace(/</g,'&lt;')+'</code>').join(', ');
  m.bindPopup('<b>'+f.label.replace(/</g,'&lt;')+'</b>'+(f.country?' · '+f.country:'')+
    '<br>'+f.count+' mention'+(f.count==1?'':'s')+
    '<br><span style="color:#666">surfaces:</span> '+surf+
    '<br><a href="https://www.wikidata.org/wiki/'+f.q+'" target="_blank">'+f.q+'</a>');
  m.addTo(map);
}
if(bounds.length) map.fitBounds(bounds,{padding:[20,20]});
const lg=L.control({position:'bottomright'});
lg.onAdd=function(){const d=L.DomUtil.create('div','legend');
 d.innerHTML='<b>mentions</b><br><i style="background:#7a0177"></i>1000+<br>'+
 '<i style="background:#c51b8a"></i>200–999<br><i style="background:#f768a1"></i>50–199<br>'+
 '<i style="background:#fa9fb5"></i>10–49<br><i style="background:#feebe2"></i>1–9';return d;};
lg.addTo(map);
</script></body></html>"""
out = (HTML.replace("__DATA__", data_json).replace("__N__", str(len(feats)))
       .replace("__MM__", f"{mapped_mentions:,}").replace("__TM__", f"{total_mentions:,}")
       .replace("__NC__", str(len(no_coord))).replace("__NCROWS__", nc_rows))
open(OUT, "w").write(out)
print(f"wrote {OUT} ({len(out)//1024} KB)")
