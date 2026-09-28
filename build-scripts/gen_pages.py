import os

ROOT = os.path.dirname(__file__)
PHONE_TEL = "8052428186"
PHONE_DISP = "805-242-8186"

def shell(title, desc, canonical, h1_block, body, extra_style=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="/images/logos/logo-sqr128-805aerial.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="/includes/base.css">
<script src="/includes/nav-footer-loader.js"></script>
<style>{extra_style}</style>
</head>
<body>
<main>
{h1_block}
{body}
</main>
</body>
</html>
"""

def hero(h1, lede, bg_img, breadcrumb_html):
    return f"""<section class="page-hero" style="background:#0b1220">
  <div style="position:absolute;inset:0;z-index:0">
    <img src="{bg_img}" alt="" role="presentation" style="width:100%;height:100%;object-fit:cover;object-position:center">
    <div style="position:absolute;inset:0;background:linear-gradient(105deg,rgba(11,18,32,.93) 55%,rgba(11,18,32,.65) 100%)"></div>
  </div>
  <div class="wrap" style="position:relative;z-index:2">
    <div class="breadcrumbs" style="color:#c7ccd6">{breadcrumb_html}</div>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <a href="tel:{PHONE_TEL}" class="btn">Call {PHONE_DISP}</a>
  </div>
</section>"""

def write(path, content):
    fp = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w") as f:
        f.write(content)
    print("wrote", path)
