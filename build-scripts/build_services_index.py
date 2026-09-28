from gen_pages import shell, hero, write, PHONE_TEL, PHONE_DISP
BASE = "https://805aerial.com"
body = f"""
{hero("Aerial Video &amp; Photography Services", "FAA Part 107 licensed drone video and photography production across San Luis Obispo County.", "/images/portfolio/6-aerial-drone-photos-805-aerial.jpg", '<a href="/">Home</a> / Services')}
<section class="block"><div class="wrap">
<div class="grid grid-3">
  <div class="card"><h3><a href="/services/aerial-drone-video-production/">Aerial Drone Video Production</a></h3><p>Cinematic aerial video for real estate, tourism, agriculture and events.</p></div>
  <div class="card"><h3><a href="/services/real-estate-aerial-photography/">Real Estate Aerial Photography</a></h3><p>High-resolution aerial photos for listings, wineries, and ranch properties.</p></div>
  <div class="card"><h3><a href="/services/commercial-video-production/">Commercial Video Production</a></h3><p>Brand and marketing video for Central Coast businesses.</p></div>
  <div class="card"><h3><a href="/services/event-and-wedding-aerial-video/">Event &amp; Wedding Aerial Video</a></h3><p>Discreet aerial coverage for weddings and events.</p></div>
  <div class="card"><h3><a href="/services/drone-photography/">Drone Photography</a></h3><p>Still aerial photography for marketing, insurance, and construction.</p></div>
  <div class="card"><h3><a href="/blog/">Local Media Blog</a></h3><p>Guides on drone permits and how Central Coast businesses use aerial media.</p></div>
</div>
<p style="margin-top:2rem">Serving <a href="/locations/san-luis-obispo/">San Luis Obispo</a>, <a href="/locations/paso-robles/">Paso Robles</a>, <a href="/locations/atascadero/">Atascadero</a>, <a href="/locations/arroyo-grande/">Arroyo Grande</a>, <a href="/locations/pismo-beach/">Pismo Beach</a>, <a href="/locations/morro-bay/">Morro Bay</a>, <a href="/locations/cambria/">Cambria</a>, and <a href="/locations/nipomo/">Nipomo</a>.</p>
</div></section>
<section class="cta-strip"><div class="wrap"><h2>Call for a Same-Week Quote</h2><a href="tel:{PHONE_TEL}" class="btn">Call {PHONE_DISP}</a></div></section>
"""
write("services/index.html", shell("Services | 805 Aerial | San Luis Obispo County",
    "Aerial drone video, real estate photography, commercial video, and event coverage across San Luis Obispo County.",
    f"{BASE}/services/", "", body))
print("services index done")
