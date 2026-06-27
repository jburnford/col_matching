#!/usr/bin/env python3
"""Animated MP4 (Bluesky-ready) of Canada within the imperial personnel system.

Connections between Canada and every colony its officials also served in FADE IN
(no directional drawing), and carry particles flowing in BOTH directions -- the point
is circulation, not departure-from-Canada. Frames captured from the live Leaflet/CARTO
map via Playwright, encoded H.264 yuv420p for social media.
"""
import json, collections

data = json.load(open("/tmp/canada_map_data.json"))
coords = json.load(open("/tmp/canada_map_coords.json"))
coords.update({"Q21815597": (25.06, -77.35), "Q21821453": (-4.62, 55.45),
    "Q116282722": (10.5, -61.3), "Q4806993": (-32.0, 22.0), "Q130386222": (17.1, -61.8),
    "Q2376315": (21.9, 96.0), "Q107987587": (16.3, -86.5)})
CAN = coords.get("Q16", (56.0, -96.0))
qual, ocnames = data["qual"], data["other_qids"]

node_off = collections.defaultdict(set)
for pid, p in qual.items():
    for q in p["other"]:
        if q in coords or q in ocnames:
            node_off[q].add(pid)
arcs = []
for q, offs in node_off.items():
    c = coords.get(q)
    if not c: continue
    arcs.append({"q": q, "label": ocnames.get(q, q), "lat": c[0], "lon": c[1], "w": len(offs)})
arcs.sort(key=lambda a: a["lon"])
maxw = max(a["w"] for a in arcs)
total = len(qual)

HTML = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
 html,body{margin:0;height:100%%;background:#0b1722;overflow:hidden;
   font-family:Georgia,'Times New Roman',serif}
 #map{height:100%%;background:#0b1722}
 #title{position:absolute;z-index:1000;top:26px;left:36px;color:#f3e7c9;
   text-shadow:0 2px 10px #000;max-width:640px}
 #title h1{margin:0;font-size:34px;letter-spacing:.3px;color:#ffd98a}
 #title p{margin:8px 0 0;font-size:18px;color:#dfe7ef;font-family:system-ui,sans-serif;line-height:1.35}
 #counter{position:absolute;z-index:1000;bottom:30px;left:36px;color:#fff;
   font-family:system-ui,sans-serif;text-shadow:0 2px 8px #000}
 #counter .big{font-size:46px;font-weight:700;color:#ffd98a}
 #counter .sub{font-size:16px;color:#cfdae6}
 #credit{position:absolute;z-index:1000;bottom:14px;right:14px;color:#7e8ea0;
   font-size:12px;font-family:system-ui,sans-serif}
 .leaflet-control-attribution{display:none}
 .clbl{background:none;border:none;box-shadow:none;color:#ffcaa8;font-size:12px;
   font-family:system-ui,sans-serif;text-shadow:0 1px 4px #000;font-weight:600}
</style></head><body>
<div id="title"><h1>Canada in the British Empire</h1>
 <p id="sub"></p></div>
<div id="counter"><div class="big" id="cnum">0</div>
 <div class="sub">colonies that shared officials with Canada</div></div>
<div id="credit">Colonial Office List career data &middot; Wikidata</div>
<div id="map"></div>
<script>
const CAN=%(can)s, ARCS=%(arcs)s, MAXW=%(maxw)d, TOTAL=%(total)d;
const map=L.map('map',{zoomControl:false,attributionControl:false,
  worldCopyJump:false}).setView([18,8],2.4);
L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
 {subdomains:'abcd',maxZoom:8}).addTo(map);

function arcPts(a,b,n){
 const dlat=b[0]-a[0], dlon=b[1]-a[1], len=Math.hypot(dlat,dlon)||1;
 const lift=Math.min(len*0.16, 22);
 const pts=[];
 for(let i=0;i<=n;i++){const t=i/n, s=Math.sin(Math.PI*t);
  pts.push([a[0]+dlat*t + lift*s*(-dlon)/len, a[1]+dlon*t + lift*s*(dlat)/len]);}
 return pts;
}
const FULL=ARCS.map((A,i)=>({A,pts:arcPts(CAN,[A.lat,A.lon],44),
  off:(i*0.37)%%1}));            // phase offset so particles aren't synced
let baseLayer=L.layerGroup().addTo(map);   // arcs + dest markers (rebuilt on reveal change)
let dotLayer =L.layerGroup().addTo(map);   // particles (rebuilt every frame)
const N=ARCS.length;

function reveal(p,i){const A0=0.08,A1=0.80,dur=0.16;
 const st=A0+(A1-A0)*(i/Math.max(1,N-1));
 return Math.max(0,Math.min(1,(p-st)/dur));}

// renderFrame(p=build progress 0..1, t=seconds for particle flow)
window.renderFrame=function(p,t){
 baseLayer.clearLayers(); dotLayer.clearLayers();
 const sub=document.getElementById('sub');
 sub.style.opacity=Math.min(1,p/0.06);
 sub.textContent=TOTAL+" colonial officials served in Canada — incl. the pre-Confederation "
   +"colonies & Newfoundland — and in two or more other colonies. They circulated through "
   +"the imperial system; movement ran both ways.";
 let done=0;
 FULL.forEach((f,i)=>{
  const rv=reveal(p,i); if(rv<=0) return;
  // faint connecting arc (fades in place -- no directional draw)
  L.polyline(f.pts,{color:'#9ec9ff',weight:0.5+2.4*f.A.w/MAXW,
    opacity:(0.10+0.32*f.A.w/MAXW)*rv,lineCap:'round'}).addTo(baseLayer);
  if(rv>=0.99){
   done++;
   const r=3+9*Math.sqrt(f.A.w/MAXW);
   L.circleMarker([f.A.lat,f.A.lon],{radius:r,color:'#ff8a5c',weight:1.2,
     fillColor:'#ff8a5c',fillOpacity:0.85}).addTo(baseLayer);
   if(f.A.w>=14) L.marker([f.A.lat,f.A.lon],{opacity:0}).addTo(baseLayer)
     .bindTooltip(f.A.label,{permanent:true,direction:'right',className:'clbl',offset:[8,0]});
  }
  // BIDIRECTIONAL particles once the link is mostly established
  if(rv>0.4){
   const L0=f.pts.length-1, speed=0.22, np=2;
   for(let d=0; d<np; d++){
    for(const dir of [1,-1]){
     let ph=((t*speed)+f.off+d/np)%%1; if(ph<0)ph+=1;
     const pos=dir>0?ph:1-ph;
     const pt=f.pts[Math.max(0,Math.min(L0,Math.floor(pos*L0)))];
     L.circleMarker(pt,{radius:2.4,weight:0,
       fillColor: dir>0?'#fff1c9':'#bfe0ff',fillOpacity:0.85*rv}).addTo(dotLayer);
    }
   }
  }
 });
 // Canada hub (steady, prominent -- a node in the web, not a launch pad)
 const cr=6+14*Math.min(1,p/0.06);
 L.circleMarker(CAN,{radius:cr,color:'#ffd98a',weight:2,fillColor:'#ffd98a',
   fillOpacity:0.92}).addTo(baseLayer);
 L.marker(CAN,{opacity:0}).addTo(baseLayer).bindTooltip('CANADA',
   {permanent:true,direction:'top',className:'clbl',offset:[0,-6]});
 document.getElementById('cnum').textContent=done;
};
window.renderFrame(0,0);
window.__ready=true;
</script></body></html>"""

out = HTML % {"can": json.dumps([CAN[0], CAN[1]]), "arcs": json.dumps(arcs),
              "maxw": maxw, "total": total}
open("docs/canada_career_anim.html", "w").write(out)
print(f"wrote docs/canada_career_anim.html  ({len(arcs)} arcs, {total} officials)")
