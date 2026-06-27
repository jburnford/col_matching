from playwright.sync_api import sync_playwright
import pathlib, os
os.makedirs("/tmp/iolframes", exist_ok=True)
for f in pathlib.Path("/tmp/iolframes").glob("*.png"): f.unlink()
url = "file://" + str(pathlib.Path("docs/iol_mobility_anim.html").resolve())
Y0 = 1821                       # data epoch (renderFrame takes years-since-Y0)
FPS = 24
START_Y, END_Y = 1821, 1947     # clock range shown
BUILD = 46 * FPS                # 46s build
OUTRO = 6 * FPS                 # 6s hold on final web  (~52s total, Bluesky-safe)
frames = []
for j in range(BUILD):
    yr = START_Y + (END_Y - START_Y) * j / (BUILD - 1)
    frames.append(yr - Y0)
frames += [ (END_Y + 3) - Y0 ] * OUTRO   # +3y so every flight completes & counter hits total
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
    pg.goto(url); pg.wait_for_function("window.__ready===true"); pg.wait_for_timeout(1500)
    for k, ty in enumerate(frames):
        pg.evaluate(f"window.renderFrame({ty})")
        pg.screenshot(path=f"/tmp/iolframes/f{k:05d}.png")
    b.close()
print("rendered", len(frames), "frames")
