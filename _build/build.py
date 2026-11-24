#!/usr/bin/env python3
"""Builds one case page per site: <slug>/index.html + og.jpg + shot.jpg. Run: python3 _build/build.py <shots_dir>"""
import sys, os, html
from PIL import Image
BASE = "https://samirww.github.io/work"
SITES = [
 dict(slug="renee-youssef", shot="01-renee-youssef.jpg", name="Renee Youssef", kind="Violinist profile website",
      url="https://reneeyoussef.com",
      desc="Profile website for a concert violinist. Art direction, design and build: dark editorial look, serif typography, loading animation and a mobile-first layout."),
]
TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} | {kind}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Samir Wehbe, Senior Art Director">
<meta property="og:title" content="{name} | {kind}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{base}/{slug}/">
<meta property="og:image" content="{base}/{slug}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{name} | {kind}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{base}/{slug}/og.jpg">
<link rel="canonical" href="{base}/{slug}/">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0e0e0e;color:#ece8e1;font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;line-height:1.55}}
main{{max-width:1080px;margin:0 auto;padding:56px 24px 72px}}
.kind{{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#a39b8e}}
h1{{font-family:Georgia,"Times New Roman",serif;font-weight:400;font-size:clamp(34px,6vw,64px);line-height:1.08;margin:14px 0 18px}}
p{{max-width:60ch;font-size:17px;color:#cfc9bf}}
.btn{{display:inline-block;margin:28px 0 40px;padding:14px 26px;border:1px solid #ece8e1;color:#0e0e0e;background:#ece8e1;text-decoration:none;font-size:14px;letter-spacing:.08em;text-transform:uppercase}}
.btn:hover{{background:transparent;color:#ece8e1}}
.frame{{border:1px solid #2a2927;border-radius:10px;overflow:hidden;background:#161616}}
.bar{{height:34px;display:flex;align-items:center;gap:7px;padding:0 14px;border-bottom:1px solid #2a2927}}
.bar i{{width:10px;height:10px;border-radius:50%;background:#3a3836;display:block}}
.frame img{{display:block;width:100%;height:auto}}
footer{{margin-top:44px;font-size:13px;color:#8a8479}}
</style>
</head>
<body>
<main>
<div class="kind">{kind}</div>
<h1>{name}</h1>
<p>{desc}</p>
<a class="btn" href="{url}" rel="noopener">Visit live site</a>
<div class="frame"><div class="bar"><i></i><i></i><i></i></div><a href="{url}" rel="noopener"><img src="shot.jpg" width="1440" height="900" alt="{name} website home page"></a></div>
<footer>Art direction, design and build: Samir Wehbe, Senior Art Director.</footer>
</main>
</body>
</html>
"""
shots = sys.argv[1]
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for s in SITES:
    d = os.path.join(root, s["slug"]); os.makedirs(d, exist_ok=True)
    im = Image.open(os.path.join(shots, s["shot"])).convert("RGB")
    im.save(os.path.join(d, "shot.jpg"), quality=86, optimize=True)
    w, h = im.size; r = im.resize((1200, int(h*1200/w)), Image.LANCZOS)
    r.crop((0, 0, 1200, 630)).save(os.path.join(d, "og.jpg"), quality=88, optimize=True)
    esc = {k: html.escape(v, quote=True) for k, v in s.items()}
    open(os.path.join(d, "index.html"), "w").write(TPL.format(base=BASE, **esc))
    print("built", s["slug"])
