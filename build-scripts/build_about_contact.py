from gen_pages import shell, hero, write, PHONE_TEL, PHONE_DISP
BASE = "https://805aerial.com"

about_body = f"""
{hero("About 805 Aerial", "FAA Part 107 licensed aerial video and photography production, based on California's Central Coast.", "/images/portfolio/11-aerial-drone-photos-mdo.jpg", '<a href="/">Home</a> / About')}
<section class="block"><div class="wrap article-body" style="max-width:900px">

<p>805 Aerial is a Central Coast aerial video and photography production company serving San Luis Obispo County. We've flown for real estate agents, wineries, hospitality groups, and commercial clients across the region, from vineyard rows in Paso Robles to the coastline at Morro Bay and Pismo Beach.</p>

<h2>FAA Part 107 Licensed</h2>
<p>Every flight is operated under an FAA Part 107 remote pilot certificate, the federal license required to legally fly a drone for paid commercial work. That means every project is planned around real airspace rules, not guesswork, particularly important in a county with controlled airspace near two regional airports and protected coastal and wildlife areas.</p>

<h2>Trusted by Central Coast Businesses</h2>
<p>805 Aerial has worked with agents from Century 21, RE/MAX, Haven Properties, and Pacifica Commercial Realty, along with wineries, hospitality businesses, and individual homeowners throughout San Luis Obispo County.</p>

<div class="trust-bar" style="justify-content:flex-start">
  <img src="/images/clients/logo-century21.jpg" alt="Century 21">
  <img src="/images/clients/logo-remax.jpg" alt="RE/MAX">
  <img src="/images/clients/logo-haven.jpg" alt="Haven Properties">
  <img src="/images/clients/logo-pacifica.jpg" alt="Pacifica Commercial Realty">
</div>

<h2>Why We Also Publish a Local Blog</h2>
<p>Beyond production work, 805 Aerial publishes local guides on drone regulations, real estate photography trends, and how Central Coast businesses use aerial media, part of a broader effort to be a useful resource for the local business community, not just a vendor. See the full <a href="/blog/">805 Aerial blog</a>.</p>

<h2>Get in Touch</h2>
<p>Call <a href="tel:{PHONE_TEL}">{PHONE_DISP}</a> or visit our <a href="/contact/">contact page</a> to talk through a project. We serve <a href="/locations/">all of San Luis Obispo County</a>.</p>

</div></section>
<section class="cta-strip"><div class="wrap"><h2>Let's Talk About Your Project</h2><a href="tel:{PHONE_TEL}" class="btn">Call {PHONE_DISP}</a></div></section>
"""
write("about/index.html", shell("About 805 Aerial | San Luis Obispo County Drone Production",
    "805 Aerial is an FAA Part 107 licensed aerial video and photography production company serving San Luis Obispo County.",
    f"{BASE}/about/", "", about_body))

contact_body = f"""
{hero("Contact 805 Aerial", "Call or send a message to get a quote for aerial video or photography anywhere in San Luis Obispo County.", "/images/portfolio/1-aerial-drone-photos-805-aerial.jpg", '<a href="/">Home</a> / Contact')}
<section class="block"><div class="wrap">
<div class="grid grid-2" style="align-items:start">
  <div>
    <h2>Get a Quote</h2>
    <p>805 Aerial serves all of San Luis Obispo County by appointment. We do not operate a public walk-in office; every project begins with a phone call or form submission.</p>
    <p style="font-size:1.4rem;font-weight:700"><a href="tel:{PHONE_TEL}" style="color:var(--gold);text-decoration:none">{PHONE_DISP}</a></p>
    <p class="gf-service-area" style="color:var(--muted)">Available by phone and on-location appointment only. This is a mailing-free, service-area business; no walk-ins are accepted at a physical address.</p>
    <p>Serving: <a href="/locations/san-luis-obispo/">San Luis Obispo</a>, <a href="/locations/paso-robles/">Paso Robles</a>, <a href="/locations/atascadero/">Atascadero</a>, <a href="/locations/arroyo-grande/">Arroyo Grande</a>, <a href="/locations/pismo-beach/">Pismo Beach</a>, <a href="/locations/morro-bay/">Morro Bay</a>, <a href="/locations/cambria/">Cambria</a>, <a href="/locations/nipomo/">Nipomo</a>.</p>
    <p><a href="https://vimeo.com/805aerial" target="_blank" rel="noopener">View our portfolio on Vimeo &rarr;</a></p>
  </div>
  <div class="card">
    <h3>Send a Message</h3>
    <form onsubmit="return false;">
      <div style="margin-bottom:1rem"><label style="display:block;margin-bottom:.3rem;font-weight:600">Name</label><input type="text" required style="width:100%;padding:.7rem;border:1px solid var(--line);border-radius:8px"></div>
      <div style="margin-bottom:1rem"><label style="display:block;margin-bottom:.3rem;font-weight:600">Phone</label><input type="tel" required style="width:100%;padding:.7rem;border:1px solid var(--line);border-radius:8px"></div>
      <div style="margin-bottom:1rem"><label style="display:block;margin-bottom:.3rem;font-weight:600">What do you need?</label><select style="width:100%;padding:.7rem;border:1px solid var(--line);border-radius:8px"><option>Aerial Drone Video</option><option>Real Estate Aerial Photography</option><option>Commercial Video</option><option>Event / Wedding Aerial Video</option><option>Drone Photography</option><option>Not Sure Yet</option></select></div>
      <button type="submit" class="btn" style="width:100%;text-align:center;border:none;cursor:pointer">Request a Quote</button>
    </form>
  </div>
</div>
</div></section>
"""
write("contact/index.html", shell("Contact 805 Aerial | San Luis Obispo County",
    "Contact 805 Aerial for aerial video and photography anywhere in San Luis Obispo County. Call 805-242-8186.",
    f"{BASE}/contact/", "", contact_body))

print("about + contact done")
