from playwright.sync_api import sync_playwright
import pathlib, os
os.makedirs("/tmp/cframes", exist_ok=True)
for f in pathlib.Path("/tmp/cframes").glob("*.png"): f.unlink()
url = "file://" + str(pathlib.Path("docs/canada_career_anim.html").resolve())
FPS = 24
START, BUILD, END = 12, 336, 110           # ~19s @ 24fps (longer hold to enjoy the flow)
ps = [0.0]*START + [j/(BUILD-1) for j in range(BUILD)] + [1.0]*END
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
    pg.goto(url); pg.wait_for_function("window.__ready===true"); pg.wait_for_timeout(4000)
    for k, pr in enumerate(ps):
        t = k / FPS                        # continuous time -> particles flow every frame
        pg.evaluate(f"window.renderFrame({pr},{t})")
        pg.screenshot(path=f"/tmp/cframes/f{k:05d}.png")
    b.close()
print("rendered", len(ps), "frames")
