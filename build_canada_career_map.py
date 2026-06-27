#!/usr/bin/env python3
"""Leaflet map of colonial officials who served in Canada + >=2 other colonies.

Nodes = colonies (Canada highlighted), radius ~ number of these officials who served
there. Edges = colony pairs co-served by an official (the imperial-career network),
width/opacity ~ number of shared officials. Self-contained HTML (Leaflet via CDN).
"""
import json, html, collections, math

data = json.load(open("/tmp/canada_map_data.json"))
coords = json.load(open("/tmp/canada_map_coords.json"))
# fill historical entities WDQS lacks P625 for
coords.update({
    "Q21815597": (25.06, -77.35),   # Bahamas Colony
    "Q21821453": (-4.62, 55.45),    # Seychelles
    "Q116282722": (10.5, -61.3),    # Trinidad and Tobago
    "Q4806993": (-32.0, 22.0),      # Cape Colony
    "Q130386222": (17.1, -61.8),    # Antigua Colony
    "Q2376315": (21.9, 96.0),       # British Burma
    "Q107987587": (16.3, -86.5),    # Bay Islands
})
CANADA_LL = coords.get("Q16", (56.0, -96.0))

qual = data["qual"]; ocnames = data["other_qids"]

# node -> set of officials ; edge(a,b)-> set of officials  (a,b colony QIDs; 'CAN'=Canada)
node_off = collections.defaultdict(set)
edge_off = collections.defaultdict(set)
node_label = {"CAN": "Canada"}
for pid, p in qual.items():
    cols = ["CAN"] + list(p["other"].keys())
    for q in p["other"]:
        node_label[q] = ocnames.get(q, q)
    for c in cols:
        node_off[c].add(pid)
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            a, b = sorted((cols[i], cols[j]))
            edge_off[(a, b)].add(pid)

def ll(q): return CANADA_LL if q == "CAN" else coords.get(q)

# build JS arrays
nodes = []
for q, offs in node_off.items():
    p = ll(q)
    if not p: continue
    names = sorted({ (qual[o]["wlab"] or f"{qual[o]['sur']}, {qual[o]['giv'] or ''}").strip()
                     for o in offs })
    nodes.append({"id": q, "lat": p[0], "lon": p[1], "label": node_label.get(q, q),
                  "n": len(offs), "is_canada": q == "CAN",
                  "people": names[:60]})
edges = []
for (a, b), offs in edge_off.items():
    pa, pb = ll(a), ll(b)
    if not pa or not pb: continue
    edges.append({"a": [pa[0], pa[1]], "b": [pb[0], pb[1]], "w": len(offs)})

maxn = max(n["n"] for n in nodes)
maxe = max(e["w"] for e in edges)
total = len(qual)
grounded = sum(1 for p in qual.values() if p["wqid"])

HTML = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Colonial officials: Canada + two other colonies</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
 html,body{margin:0;height:100%%;font-family:system-ui,Segoe UI,Roboto,sans-serif}
 #map{height:100%%;background:#0b1722}
 .hdr{position:absolute;z-index:1000;top:10px;left:10px;background:rgba(12,22,34,.9);
      color:#e8eef5;padding:12px 16px;border-radius:8px;max-width:340px;box-shadow:0 2px 12px rgba(0,0,0,.4)}
 .hdr h1{margin:0 0 4px;font-size:16px} .hdr p{margin:4px 0;font-size:12.5px;color:#aebfd0}
 .leaflet-popup-content{font-size:12.5px} .leaflet-popup-content b{font-size:13px}
 .ppl{max-height:200px;overflow:auto;margin-top:5px;font-size:11.5px;color:#334}
</style></head><body>
<div class="hdr">
 <h1>Imperial careers anchored on Canada</h1>
 <p>%(total)d colonial officials who served in <b>Canada</b> (incl. pre-Confederation
    colonies &amp; Newfoundland) <b>and at least two other colonies</b>. %(grounded)d are
    grounded to Wikidata.</p>
 <p>Circles = colonies, sized by how many of these officials served there. Lines connect
    colonies that shared an official; thicker = more shared careers. Click a circle for names.</p>
</div>
<div id="map"></div>
<script>
const NODES=%(nodes)s, EDGES=%(edges)s, MAXN=%(maxn)d, MAXE=%(maxe)d;
const map=L.map('map',{worldCopyJump:true}).setView([20,-20],2);
L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
 {attribution:'&copy; OpenStreetMap, &copy; CARTO',subdomains:'abcd',maxZoom:8}).addTo(map);
EDGES.forEach(e=>{
 L.polyline([e.a,e.b],{color:'#5b9bd5',weight:0.4+3.2*e.w/MAXE,
   opacity:0.12+0.5*e.w/MAXE}).addTo(map);
});
NODES.forEach(n=>{
 const r=4+18*Math.sqrt(n.n/MAXN);
 const m=L.circleMarker([n.lat,n.lon],{radius:r,
   color:n.is_canada?'#ffd24a':'#ff7b5a',weight:1.5,
   fillColor:n.is_canada?'#ffd24a':'#ff7b5a',fillOpacity:0.78}).addTo(map);
 const ppl=n.people.map(x=>'&bull; '+x).join('<br>');
 m.bindPopup('<b>'+n.label+'</b><br>'+n.n+' official'+(n.n>1?'s':'')+
   '<div class="ppl">'+ppl+'</div>',{maxWidth:280});
 if(n.n>=8) L.marker([n.lat,n.lon],{opacity:0}).addTo(map)
   .bindTooltip(n.label,{permanent:true,direction:'right',className:'lbl',offset:[6,0]});
});
</script></body></html>"""

out = HTML % {"total": total, "grounded": grounded, "nodes": json.dumps(nodes),
              "edges": json.dumps(edges), "maxn": maxn, "maxe": maxe}
open("docs/canada_career_map.html", "w").write(out)
print(f"officials: {total} (grounded {grounded})  nodes: {len(nodes)}  edges: {len(edges)}")
print(f"busiest colonies: " + ", ".join(f"{n['label']}({n['n']})"
      for n in sorted(nodes, key=lambda x: -x['n'])[:10]))
print("wrote docs/canada_career_map.html")
