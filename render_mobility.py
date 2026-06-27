from playwright.sync_api import sync_playwright
import pathlib, os
os.makedirs("/tmp/mframes", exist_ok=True)
for f in pathlib.Path("/tmp/mframes").glob("*.png"): f.unlink()
url = "file://" + str(pathlib.Path("docs/mobility_anim.html").resolve())
Y0 = 1820                       # data epoch (renderFrame takes years-since-Y0)
FPS = 24
START_Y, END_Y = 1835, 1966     # clock range shown
BUILD = 108 * FPS               # 108s build
OUTRO = 14 * FPS                # 14s hold on final web  (~122s total ~ 2 min)
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
        pg.screenshot(path=f"/tmp/mframes/f{k:05d}.png")
    b.close()
print("rendered", len(frames), "frames")
