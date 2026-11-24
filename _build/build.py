#!/usr/bin/env python3
"""Builds one case page per site: <slug>/index.html + og.jpg + shot.jpg. Run: python3 _build/build.py <shots_dir>"""
import sys, os, html
from PIL import Image
BASE = "https://samirww.github.io/work"
SITES = [
 dict(slug="renee-youssef", shot="01-renee-youssef.jpg", x=0, name="Renee Youssef", kind="Violinist profile website",
      url="https://reneeyoussef.com",
      desc="Profile website for a concert violinist. Art direction, design and build: dark editorial look, serif typography, loading animation and a mobile-first layout."),
 dict(slug="rima-wehbi-photography", shot="03-rima-wehbi.jpg", x=270, name="Rima Wehbi Photography", kind="Gift voucher website",
      url="https://rimawehbi.com",
      desc="Gift voucher page for a newborn photographer. A quiet black and white design that puts the voucher first, with session packages and a direct WhatsApp order flow."),
 dict(slug="oum-eich", shot="04-oum-eich.jpg", x=0, name="OUM EICH", kind="Streetwear store website",
      url="https://oumeich.samirww.workers.dev",
      desc="Online store for a Beirut streetwear brand with a cause. Bold bilingual Arabic and English design, tees shown large on mobile, and a share of every sale going to cancer patients."),
 dict(slug="monty-holiday-home", shot="05-monty.jpg", x=0, name="Monty Holiday Home", kind="Holiday home company website",
      url="https://montyholidayhome.com",
      desc="Website for a Dubai holiday home operator. Serif headlines, a warm luxury look and clear paths for owners and guests, built to be found on Google and AI search."),
 dict(slug="aridi-clinic", shot="07-aridi-clinic.jpg", x=30, name="Aridi Clinic", kind="Dental clinic website",
      url="https://aridiclinic.com",
      desc="Bilingual Arabic and English website for two dental clinics. Clean clinical look with WhatsApp booking up front, plus treatments, doctors and both branches in one flow."),
 dict(slug="promoehub", shot="08-promoehub.jpg", x=140, name="PromoeHub", kind="Marketing agency website",
      url="https://promoehub.com",
      desc="Website for a digital marketing agency in Beirut and Dubai. Bold type, an animated search demo in the hero, and clear service and work sections."),
 dict(slug="ghaya", shot="10-ghaya.jpg", x=120, wide=True, name="GHAYA", kind="Corporate home page design",
      url="https://ghaya.ae",
      desc="Home page design for a sustainable development organisation. Cinematic hero, confident typography and a clear path into its programmes."),
 dict(slug="mina-fishing-skills", shot="11-mina-fishing.jpg", x=0, name="Mina Fishing Skills", kind="Kids' fishing school website",
      url="https://mina-fishing-skills.vercel.app",
      desc="Website for a kids' fishing school at Old Doha Port. Bright, playful UI and UX direction with a short, clear booking flow, in English and Arabic."),
 dict(slug="dfordiva", shot="13-dfordiva.jpg", x=270, name="DforDiva", kind="Jewellery brand launch page",
      url="https://dfordiva.com",
      desc="Pre-launch page for a gold-plated accessories brand. Dark, golden atmosphere with a private preview gate ahead of the store opening."),
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
<meta property="og:image:height" content="1200">
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
    w, h = im.size
    # Upwork crops the share image to a square thumbnail, so og.jpg is a square cut of the hero.
    if s.get("wide"):
        # Hero text too wide for a square cut: keep a 1200px-wide slice and pad it top and bottom.
        sq = Image.new("RGB", (1200, 1200), "#0e0e0e"); sq.paste(im.crop((s["x"], 0, s["x"]+1200, h)), (0, (1200-h)//2))
    else:
        sq = im.crop((s["x"], 0, s["x"]+h, h)).resize((1200, 1200), Image.LANCZOS)
    sq.save(os.path.join(d, "og.jpg"), quality=86, optimize=True)
    esc = {k: html.escape(str(v), quote=True) for k, v in s.items()}
    open(os.path.join(d, "index.html"), "w").write(TPL.format(base=BASE, **esc))
    print("built", s["slug"])

links = "\n".join(f'<a href="{s["slug"]}/">{html.escape(s["name"])}, {html.escape(s["kind"].lower())}</a>' for s in SITES)
open(os.path.join(root, "index.html"), "w").write("""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Selected website design work | Samir Wehbe</title>
<meta name="description" content="Selected website design work by Samir Wehbe, Senior Art Director.">
<style>body{background:#0e0e0e;color:#ece8e1;font-family:-apple-system,"Helvetica Neue",Arial,sans-serif;padding:56px 24px;max-width:1080px;margin:0 auto}h1{font-family:Georgia,serif;font-weight:400;font-size:44px;margin-bottom:24px}a{color:#ece8e1;display:block;padding:10px 0;font-size:18px}</style></head>
<body><h1>Selected website design work</h1>
""" + links + """
</body></html>
""")
