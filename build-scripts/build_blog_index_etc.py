from gen_pages import shell, hero, write, PHONE_TEL, PHONE_DISP
BASE = "https://805aerial.com"

articles = [
    dict(slug="filming-drone-permits-san-luis-obispo-county", title="A Guide to Filming and Drone Permits in San Luis Obispo County", excerpt="What FAA, state, and local rules apply before flying a drone or filming a production in the county.", tag="Regulations", img="/images/portfolio/8-aerial-drone-photos-taiwan.jpg", read="9 min"),
    dict(slug="real-estate-photography-trends-central-coast", title="Real Estate Photography Trends for the Central Coast Market", excerpt="Why aerial imagery has become standard for higher-end San Luis Obispo County listings.", tag="Real Estate", img="/images/portfolio/15-aerial-drone-ag-home.jpg", read="10 min"),
    dict(slug="paso-robles-wineries-aerial-video-marketing", title="How Paso Robles Wineries Use Aerial Video for Marketing", excerpt="Why more wine country brands are investing in drone footage, and what makes it work.", tag="Wine Country", img="/images/portfolio/14-aerial-drone-photos-winery-paso.jpg", read="10 min"),
    dict(slug="small-business-spotlight-central-coast-video", title="Small Business Spotlight: How Central Coast Businesses Use Video to Grow", excerpt="How local businesses across the county are using video and aerial content to reach customers.", tag="Local Business", img="/images/portfolio/6-aerial-drone-photos-805-aerial.jpg", read="9 min"),
    dict(slug="slo-county-tourism-aerial-footage-destination-marketing", title="SLO County Tourism and Media: How Aerial Footage Shapes Central Coast Destination Marketing", excerpt="How aerial video and photography support the county's tourism and destination marketing.", tag="Tourism", img="/images/portfolio/12-aerial-drone-photos-morro-rock.jpg", read="10 min"),
]

cards = ""
for a in articles:
    cards += f"""
    <a href="/blog/{a['slug']}/" style="text-decoration:none;color:inherit">
    <div class="card blog-card">
      <img src="{a['img']}" alt="">
      <div class="bc-body">
        <span class="tag-chip">{a['tag']}</span>
        <h3 style="margin-top:.7rem">{a['title']}</h3>
        <p style="color:var(--muted);font-size:.92rem">{a['excerpt']}</p>
        <span style="font-size:.8rem;color:var(--muted)">{a['read']} read</span>
      </div>
    </div>
    </a>"""

body = f"""
{hero("Central Coast Media &amp; Business Blog", "Local guides on drone regulations, real estate media trends, wine country marketing, and Central Coast business video, from 805 Aerial.", "/images/portfolio/11-aerial-drone-photos-mdo.jpg", '<a href="/">Home</a> / Blog')}
<section class="block"><div class="wrap">
<div class="blog-grid">
{cards}
  <div class="card blog-card" style="display:flex;flex-direction:column;justify-content:center;align-items:center;min-height:280px;text-align:center;padding:1.4rem">
    <span class="eyebrow">Coming Soon</span>
    <h3>More Central Coast Media Guides</h3>
    <p style="color:var(--muted);font-size:.92rem">New local business and media guides are added regularly. Check back soon.</p>
  </div>
</div>
</div></section>
<section class="cta-strip"><div class="wrap"><h2>Have a Project in Mind?</h2><a href="tel:{PHONE_TEL}" class="btn">Call {PHONE_DISP}</a></div></section>
"""
write("blog/index.html", shell("Blog | 805 Aerial | Central Coast Media &amp; Business Guides",
    "Local guides on drone permits, real estate photography trends, and how Central Coast businesses use aerial video, from 805 Aerial.",
    f"{BASE}/blog/", "", body))
print("blog index done")

# ---------------------------------------------------------------- SITEMAP HTML
services = ["aerial-drone-video-production","real-estate-aerial-photography","commercial-video-production","event-and-wedding-aerial-video","drone-photography"]
locations = ["san-luis-obispo","paso-robles","atascadero","arroyo-grande","pismo-beach","morro-bay","cambria","nipomo"]

def li_list(slugs, base, label_fn):
    return "".join(f'<li><a href="/{base}/{s}/">{label_fn(s)}</a></li>' for s in slugs)

svc_labels = {"aerial-drone-video-production":"Aerial Drone Video Production","real-estate-aerial-photography":"Real Estate Aerial Photography","commercial-video-production":"Commercial Video Production","event-and-wedding-aerial-video":"Event & Wedding Aerial Video","drone-photography":"Drone Photography"}
loc_labels = {"san-luis-obispo":"San Luis Obispo","paso-robles":"Paso Robles","atascadero":"Atascadero","arroyo-grande":"Arroyo Grande","pismo-beach":"Pismo Beach","morro-bay":"Morro Bay","cambria":"Cambria","nipomo":"Nipomo"}

sitemap_body = f"""
{hero("Sitemap", "Every page on 805aerial.com.", "/images/portfolio/6-aerial-drone-photos-805-aerial.jpg", '<a href="/">Home</a> / Sitemap')}
<section class="block"><div class="wrap">
<div class="grid grid-3">
<div><h3>Services</h3><ul>{li_list(services,"services",lambda s: svc_labels[s])}<li><a href="/services/">All Services</a></li></ul></div>
<div><h3>Service Areas</h3><ul>{li_list(locations,"locations",lambda s: loc_labels[s])}<li><a href="/locations/">All Locations</a></li></ul></div>
<div><h3>Blog</h3><ul>{"".join(f'<li><a href="/blog/{a["slug"]}/">{a["title"]}</a></li>' for a in articles)}<li><a href="/blog/">Blog Index</a></li></ul></div>
<div><h3>Company</h3><ul><li><a href="/">Home</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li></ul></div>
</div>
</div></section>
"""
write("sitemap/index.html", shell("Sitemap | 805 Aerial", "Full sitemap of 805aerial.com.", f"{BASE}/sitemap/", "", sitemap_body))
print("html sitemap done")

# ---------------------------------------------------------------- sitemap.xml
urls = ["/", "/about/", "/contact/", "/services/", "/locations/", "/blog/"]
urls += [f"/services/{s}/" for s in services]
urls += [f"/locations/{s}/" for s in locations]
urls += [f"/blog/{a['slug']}/" for a in articles]
xml_entries = "".join(f"  <url><loc>{BASE}{u}</loc></url>\n" for u in urls)
xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{xml_entries}</urlset>\n'
write("sitemap.xml", xml)
print("sitemap.xml done, total urls:", len(urls))

# ---------------------------------------------------------------- llms.txt
llms = f"""# 805 Aerial
> Aerial video and photography production serving San Luis Obispo County, California.

805 Aerial produces FAA Part 107 licensed drone video, aerial photography, and commercial video for real estate agents, wineries, hospitality businesses, and events across San Luis Obispo County. The company also publishes a local media and business blog covering drone regulations, real estate photography trends, and Central Coast marketing topics.

## Services
- **Aerial Drone Video Production**: Cinematic drone video for real estate, tourism, agriculture, and events.
- **Real Estate Aerial Photography**: High-resolution aerial stills for property listings.
- **Commercial Video Production**: Brand and marketing video combining ground and aerial footage.
- **Event & Wedding Aerial Video**: Discreet, permitted aerial coverage for weddings and events.
- **Drone Photography**: Still aerial photography for marketing, insurance, and construction documentation.

## Service Areas
- San Luis Obispo, CA (primary market)
- Paso Robles, CA
- Atascadero, CA
- Arroyo Grande, CA
- Pismo Beach, CA
- Morro Bay, CA
- Cambria, CA
- Nipomo, CA

## Business Information
- **Phone**: 805-242-8186
- **Website**: https://805aerial.com
- **Portfolio**: https://vimeo.com/805aerial
- **Service Area**: San Luis Obispo County, California (no public office, service-area business)

## Key Differentiators
- FAA Part 107 licensed remote pilot
- Trusted by Century 21, RE/MAX, Haven Properties, and Pacifica Commercial Realty agents
- Local knowledge of San Luis Obispo County airspace, coastal, and habitat restrictions

## Pages
- Home: https://805aerial.com/
- Services: https://805aerial.com/services/
- Service Areas: https://805aerial.com/locations/
- About: https://805aerial.com/about/
- Contact: https://805aerial.com/contact/
- Blog: https://805aerial.com/blog/

## Resources
- A Guide to Filming and Drone Permits in San Luis Obispo County: https://805aerial.com/blog/filming-drone-permits-san-luis-obispo-county/
- Real Estate Photography Trends for the Central Coast Market: https://805aerial.com/blog/real-estate-photography-trends-central-coast/
- How Paso Robles Wineries Use Aerial Video for Marketing: https://805aerial.com/blog/paso-robles-wineries-aerial-video-marketing/
- Small Business Spotlight: How Central Coast Businesses Use Video to Grow: https://805aerial.com/blog/small-business-spotlight-central-coast-video/
- SLO County Tourism and Media: How Aerial Footage Shapes Central Coast Destination Marketing: https://805aerial.com/blog/slo-county-tourism-aerial-footage-destination-marketing/
"""
write("llms.txt", llms)
print("llms.txt done")
