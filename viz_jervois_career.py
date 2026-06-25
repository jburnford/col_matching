#!/usr/bin/env python3
"""Animate Sir William Jervois's colonial career on a world map -> GIF.

Sequences his dated postings (from the LadybugDB KG), places each on a world map,
and grows the travel path posting-by-posting with a year/role caption. Great-circle
arcs connect consecutive postings. Output: docs/jervois_career.gif
"""
from __future__ import annotations
import numpy as np
import geopandas as gpd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import imageio.v2 as imageio
from pathlib import Path

WORLD = "/tmp/wmap/world.geojson"
OUT = Path("docs/jervois_career.gif")

# Jervois's career itinerary (from the KG), one representative posting per stop,
# with a coordinate for the colony/territory he served in.
ITIN = [
    (1842, "Brigade Major",                         "Cape Colony",            -33.92,  18.42),
    (1845, "Survey mission to Natal",               "Natal",                  -29.88,  31.05),
    (1846, "Served in the Cape Frontier War",       "Cape Colony",            -33.92,  18.42),
    (1852, "Imperial defence works (Alderney/London)", "United Kingdom",       51.51,  -0.13),
    (1863, "Reported on the defences of Canada",     "Canada",                 44.65, -63.58),
    (1869, "Defence reports, Bermuda",               "Bermuda",                32.29, -64.78),
    (1875, "Governor of the Straits Settlements",    "Straits Settlements",     1.29, 103.85),
    (1877, "Governor of South Australia",            "South Australia",       -34.93, 138.60),
    (1882, "Governor of New Zealand",                "New Zealand",           -41.29, 174.78),
]

def great_circle(lat1, lon1, lat2, lon2, n=60):
    """Interpolate a great-circle path; returns lon, lat arrays (deg)."""
    f = np.linspace(0, 1, n)
    p1 = np.radians([lat1, lon1]); p2 = np.radians([lat2, lon2])
    d = 2 * np.arcsin(np.sqrt(np.sin((p2[0]-p1[0])/2)**2 +
            np.cos(p1[0])*np.cos(p2[0])*np.sin((p2[1]-p1[1])/2)**2))
    if d == 0:
        return np.array([lon1, lon2]), np.array([lat1, lat2])
    a = np.sin((1-f)*d)/np.sin(d); b = np.sin(f*d)/np.sin(d)
    x = a*np.cos(p1[0])*np.cos(p1[1]) + b*np.cos(p2[0])*np.cos(p2[1])
    y = a*np.cos(p1[0])*np.sin(p1[1]) + b*np.cos(p2[0])*np.sin(p2[1])
    z = a*np.sin(p1[0]) + b*np.sin(p2[0])
    lat = np.degrees(np.arctan2(z, np.sqrt(x*x+y*y)))
    lon = np.degrees(np.arctan2(y, x))
    return lon, lat

def ensure_world():
    p = Path(WORLD)
    if not p.exists():
        import urllib.request
        p.parent.mkdir(parents=True, exist_ok=True)
        url = ("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/"
               "master/geojson/ne_110m_admin_0_countries.geojson")
        print("fetching world map…")
        urllib.request.urlretrieve(url, p)
    return str(p)

def main():
    world = gpd.read_file(ensure_world())
    frames = []
    SEA, LAND, EDGE = "#0b1f3a", "#274060", "#3d5a80"
    TRAIL, HILITE, TXT = "#e0a458", "#ffd166", "#f4f1de"

    # render: for each stop i, several frames easing the arc from i-1 -> i, then a hold
    def base_ax():
        fig, ax = plt.subplots(figsize=(11, 6.2), dpi=110)
        fig.patch.set_facecolor(SEA); ax.set_facecolor(SEA)
        world.plot(ax=ax, color=LAND, edgecolor=EDGE, linewidth=0.4)
        ax.set_xlim(-180, 180); ax.set_ylim(-62, 84)
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values(): s.set_visible(False)
        return fig, ax

    def draw(ax, upto, prog):
        # full path drawn for stops 0..upto-1; partial arc into stop `upto` by prog
        pts = ITIN[:upto+1]
        for j in range(1, upto+1):
            _, _, _, la1, lo1 = pts[j-1]; _, _, _, la2, lo2 = pts[j]
            lon, lat = great_circle(la1, lo1, la2, lo2)
            if j == upto and prog < 1.0:
                k = max(2, int(len(lon)*prog)); lon, lat = lon[:k], lat[:k]
            ax.plot(lon, lat, color=TRAIL, lw=2.0, alpha=0.9, zorder=3)
        for j, (yr, role, col, la, lo) in enumerate(pts):
            cur = (j == upto)
            ax.scatter([lo],[la], s=170 if cur else 70, color=HILITE if cur else TRAIL,
                       edgecolor="white", linewidth=1.1, zorder=5)
            ax.annotate(col, (lo, la), xytext=(6, 6), textcoords="offset points",
                        color=TXT, fontsize=8.5 if cur else 7,
                        fontweight="bold" if cur else "normal", zorder=6)
        yr, role, col, _, _ = ITIN[upto]
        ax.text(0.5, 1.06, "Sir William Jervois — a career across the Empire",
                transform=ax.transAxes, ha="center", color=TXT, fontsize=14, fontweight="bold")
        ax.text(0.012, 0.045, f"{int(yr)}", transform=ax.transAxes, color=HILITE,
                fontsize=30, fontweight="bold", va="bottom")
        ax.text(0.012, 0.015, f"{role}", transform=ax.transAxes, color=TXT,
                fontsize=11, va="bottom")
        ax.text(0.985, 0.02, f"{upto+1} / {len(ITIN)} postings · {len(set(c for *_, c, _, _ in [(0,0,p[2],0,0) for p in ITIN[:upto+1]]))} colonies",
                transform=ax.transAxes, ha="right", color="#94a3b8", fontsize=8)

    for i in range(len(ITIN)):
        steps = [0.0] if i == 0 else list(np.linspace(0.15, 1.0, 10))
        for prog in steps:
            fig, ax = base_ax(); draw(ax, i, prog)
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba())[..., :3]
            frames.append(buf.copy()); plt.close(fig)
        # hold on the arrival
        fig, ax = base_ax(); draw(ax, i, 1.0); fig.canvas.draw()
        buf = np.asarray(fig.canvas.buffer_rgba())[..., :3]
        for _ in range(8): frames.append(buf.copy())
        plt.close(fig)

    OUT.parent.mkdir(exist_ok=True)
    imageio.mimsave(OUT, frames, duration=0.09, loop=0)
    print(f"wrote {OUT} ({len(frames)} frames, {OUT.stat().st_size//1024} KB)")

if __name__ == "__main__":
    main()
