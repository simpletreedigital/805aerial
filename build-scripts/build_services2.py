from gen_pages import shell, hero, write, PHONE_TEL, PHONE_DISP
BASE = "https://805aerial.com"
def crumbs(label): return f'<a href="/">Home</a> / <a href="/services/">Services</a> / {label}'
def cta(): return f"""<section class="cta-strip"><div class="wrap"><h2>Get a Quote for Your Project</h2><a href="tel:{PHONE_TEL}" class="btn">Call {PHONE_DISP}</a></div></section>"""

def bc_schema(slug, name):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"Home","item":"{BASE}/"}},
{{"@type":"ListItem","position":2,"name":"Services","item":"{BASE}/services/"}},
{{"@type":"ListItem","position":3,"name":"{name}","item":"{BASE}/services/{slug}/"}}
]}}
</script>"""

def svc_schema(name):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","serviceType":"{name}","provider":{{"@type":"ProfessionalService","name":"805 Aerial","telephone":"+1-805-242-8186"}},"areaServed":{{"@type":"AdministrativeArea","name":"San Luis Obispo County, California"}}}}
</script>"""

# ------------------------------------------------------------- SERVICE 2: Real Estate Aerial Photography
slug = "real-estate-aerial-photography"; name = "Real Estate Aerial Photography"
h1 = "Real Estate Aerial Photography in San Luis Obispo County"
lede = "High-resolution aerial photos that help San Luis Obispo County listings, wineries, and ranch properties stand out on the MLS and in marketing."
body = f"""
{hero(h1, lede, "/images/portfolio/15-aerial-drone-ag-home.jpg", crumbs("Real Estate Aerial Photography"))}
<section class="block"><div class="wrap article-body" style="max-width:900px">

<p>On the Central Coast, where lot size, ocean proximity, and hillside views often matter as much as square footage, a ground-level listing photo rarely tells the full story. Real estate aerial photography from 805 Aerial gives San Luis Obispo County agents and sellers a wider, more accurate picture of a property, its lot, its neighbors, its view corridor, and its proximity to the coast, vineyards, or downtown.</p>

<p>805 Aerial has worked with agents from Century 21, RE/MAX, Haven Properties, and Pacifica Commercial Realty across the county, producing aerial stills that get used directly in MLS listings, print flyers, and social marketing.</p>

<h2>Why Aerial Photos Help Central Coast Listings</h2>
<p>Buyers relocating to San Luis Obispo County from out of the area are often comparing a property's setting as much as its interior. An aerial photo answers questions a street-level photo cannot: how close is the property to the vineyard rows, how big is the usable flat pad on a hillside lot, how far is the walk to the beach from a Pismo Beach or Avila Beach property. For agricultural and ranch properties around Paso Robles and Creston, an aerial photo is often the only practical way to show the full parcel.</p>

<h2>What's Included</h2>
<ul>
  <li><strong>Multiple altitude and angle options.</strong> Straight-down parcel shots for boundary clarity, and angled establishing shots for marketing appeal.</li>
  <li><strong>High-resolution stills</strong> sized correctly for MLS upload limits and for large-format print flyers.</li>
  <li><strong>Twilight and golden hour options</strong> for listings where lighting materially changes how the property presents.</li>
  <li><strong>Fast turnaround</strong>, typically next-business-day delivery so photos are ready before a listing goes live.</li>
</ul>

<div class="callout"><strong>Local note:</strong> Many Central Coast lots are irregular, hillside, or bordered by agricultural land, which makes an accurate aerial parcel shot more valuable here than in a flat suburban tract market.</div>

<h2>Featured Client Work</h2>
<div class="case-panel">
  <span class="gold-label">Featured Client Work</span>
  <h3>Listing Photography for a Central Coast Agricultural Property</h3>
  <div class="case-grid">
    <div><span class="col-label">The Setting</span><p>A ranch-style property near Arroyo Grande needed photography that showed the full parcel, including outbuildings and usable pasture, not visible from the road.</p></div>
    <div><span class="col-label">The Approach</span><p>805 Aerial captured a full parcel overview alongside closer angled shots of the home and outbuildings during the golden hour window.</p></div>
    <div><span class="col-label">The Result</span><p>The listing agent used the aerial set as the lead images across the MLS listing and print marketing.</p></div>
  </div>
  <p class="case-disclaimer">Client work described from an actual 805 Aerial project. Specific figures and identifying details are generalized for privacy.</p>
</div>

<h2>Process</h2>
<ol>
  <li>Book by phone, ideally 3 to 5 days before a listing goes live.</li>
  <li>805 Aerial coordinates access with the listing agent or homeowner.</li>
  <li>On-site shoot, typically 30 to 60 minutes.</li>
  <li>Edited photos delivered within 24 to 48 hours.</li>
</ol>

<h2>Frequently Asked Questions</h2>
<div class="faq">
<details><summary>How many photos are included in a typical shoot?</summary><p>Most listing shoots include a set of 8 to 15 edited stills covering multiple angles and, where useful, a straight-down parcel overview.</p></details>
<details><summary>Can you shoot at twilight for a premium listing?</summary><p>Yes. Twilight aerial photography is available and often used for higher-end listings where lighting changes the property's presentation significantly.</p></details>
<details><summary>Do you provide both video and photos in the same visit?</summary><p>Often, yes. Many clients combine this service with <a href="/services/aerial-drone-video-production/">aerial drone video</a> in the same flight to save time and cost.</p></details>
<details><summary>What if the property is near an airport?</summary><p>San Luis Obispo County Regional Airport and Paso Robles Municipal Airport both have controlled airspace nearby. We check every address against current FAA airspace maps before booking.</p></details>
</div>

<h2>Related Services</h2>
<p>Pair this with <a href="/services/aerial-drone-video-production/">aerial drone video production</a> for a combined video and photo listing package, or see <a href="/services/drone-photography/">drone photography</a> for non-real-estate still photography needs. We regularly shoot listings in <a href="/locations/paso-robles/">Paso Robles</a>, <a href="/locations/arroyo-grande/">Arroyo Grande</a>, and <a href="/locations/nipomo/">Nipomo</a>. For more on what's changed in this market, see our article on <a href="/blog/real-estate-photography-trends-central-coast/">real estate photography trends on the Central Coast</a>.</p>
<p>Reference points for local real estate context: the <a href="https://www.car.org/" target="_blank" rel="noopener">California Association of Realtors</a> and the <a href="https://www.visitslo.com/" target="_blank" rel="noopener">Visit SLO CAL</a> tourism site, which is a useful gauge of what draws buyers to the area in the first place.</p>

</div></section>
{cta()}
""" + svc_schema(name) + bc_schema(slug, name)
write(f"services/{slug}/index.html", shell(f"{name} | San Luis Obispo County | 805 Aerial",
    "Real estate aerial photography for San Luis Obispo County listings, ranches, and wineries. Fast turnaround. Call 805-242-8186.",
    f"{BASE}/services/{slug}/", "", body))

# ------------------------------------------------------------- SERVICE 3: Commercial Video Production
slug = "commercial-video-production"; name = "Commercial Video Production"
h1 = "Commercial Video Production in San Luis Obispo County"
lede = "Brand and marketing video for Central Coast businesses, wineries, hospitality groups, and local government, combining ground and aerial footage."
body = f"""
{hero(h1, lede, "/images/portfolio/13-aerial-drone-photos-winery.jpg", crumbs("Commercial Video Production"))}
<section class="block"><div class="wrap article-body" style="max-width:900px">

<p>Commercial video production from 805 Aerial goes beyond a single drone flyover. It's full brand and marketing video, combining ground-level interviews, product and location footage, and aerial establishing shots, built for San Luis Obispo County businesses that need video for their website, social channels, or paid ad campaigns.</p>

<p>This service is most often used by tourism and hospitality businesses, wineries, and local service businesses that want a professional video presence but don't have an in-house production team.</p>

<h2>What a Commercial Video Project Typically Includes</h2>
<ul>
  <li><strong>Pre-production planning</strong>, including a shot list built around the business's actual goals, whether that's bookings, brand awareness, or a specific campaign.</li>
  <li><strong>Ground and aerial cinematography</strong>, mixing both for a video that feels bigger than a single-angle drone clip.</li>
  <li><strong>Interviews and voiceover coordination</strong> where a business wants an owner or staff member speaking on camera.</li>
  <li><strong>Editing, music licensing, and color grading</strong> for a finished, broadcast-ready video.</li>
  <li><strong>Multiple export formats</strong>, including vertical cuts for Instagram Reels and TikTok, and horizontal masters for a website or YouTube.</li>
</ul>

<h2>Why Central Coast Businesses Invest in Video</h2>
<p>San Luis Obispo County competes for tourism and relocation dollars against the rest of California's coastline, and video consistently outperforms static images for engagement on the platforms most local businesses rely on. A winery, a hotel, or a destination business benefits from footage that captures both the setting, the vineyards, the coastline, the downtown corridor, and the specific experience a visitor gets.</p>

<div class="callout"><strong>Local note:</strong> businesses along the coast, particularly around Morro Bay and Pismo Beach, benefit from footage timed around the marine layer, since fog burning off midday often produces the clearest, most marketable shots.</div>

<h2>Featured Client Work</h2>
<div class="case-panel">
  <span class="gold-label">Featured Client Work</span>
  <h3>Brand Video for a Central Coast Hospitality Business</h3>
  <div class="case-grid">
    <div><span class="col-label">The Setting</span><p>A hospitality business wanted a single brand video that could run across its website, social ads, and email marketing.</p></div>
    <div><span class="col-label">The Approach</span><p>805 Aerial combined ground interviews with staff, product and property footage, and aerial establishing shots into one edited piece.</p></div>
    <div><span class="col-label">The Result</span><p>The business used the finished video as its primary homepage asset and cut shorter versions for paid social campaigns.</p></div>
  </div>
  <p class="case-disclaimer">Client work described from an actual 805 Aerial project. Specific figures and identifying details are generalized for privacy.</p>
</div>

<h2>Frequently Asked Questions</h2>
<div class="faq">
<details><summary>How long does a commercial video project take?</summary><p>Most projects take 1 to 3 weeks from planning to final delivery, depending on the scope and how many locations or interviews are involved.</p></details>
<details><summary>Do you handle music licensing?</summary><p>Yes, licensed music is included in every finished edit so the final video can be used commercially without copyright issues.</p></details>
<details><summary>Can you produce shorter cuts for social media from the same shoot?</summary><p>Yes, most projects include a main edit plus several shorter cuts sized for Instagram, TikTok, and paid ad formats.</p></details>
<details><summary>Do you work with local government or tourism boards?</summary><p>Yes, aerial and commercial video is commonly used by destination marketing organizations and local government for tourism and public information content.</p></details>
</div>

<h2>Related Services</h2>
<p>Commercial projects often pair ground footage with <a href="/services/aerial-drone-video-production/">aerial drone video</a> and still <a href="/services/drone-photography/">drone photography</a> for marketing collateral. See how local wineries use this approach in our article on <a href="/blog/paso-robles-wineries-aerial-video-marketing/">Paso Robles wineries and aerial video marketing</a>, and how it fits into the county's broader tourism strategy in <a href="/blog/slo-county-tourism-aerial-footage-destination-marketing/">SLO County tourism and aerial footage</a>. We produce commercial video throughout <a href="/locations/san-luis-obispo/">San Luis Obispo</a>, <a href="/locations/morro-bay/">Morro Bay</a>, and <a href="/locations/cambria/">Cambria</a>.</p>
<p>For destination marketing context, see <a href="https://www.visitslo.com/" target="_blank" rel="noopener">Visit SLO CAL</a> and the <a href="https://www.slochamber.org/" target="_blank" rel="noopener">San Luis Obispo Chamber of Commerce</a>.</p>

</div></section>
{cta()}
""" + svc_schema(name) + bc_schema(slug, name)
write(f"services/{slug}/index.html", shell(f"{name} | San Luis Obispo County | 805 Aerial",
    "Commercial video production for Central Coast businesses, wineries, and hospitality groups. Ground and aerial footage. Call 805-242-8186.",
    f"{BASE}/services/{slug}/", "", body))

# ------------------------------------------------------------- SERVICE 4: Event & Wedding Aerial Video
slug = "event-and-wedding-aerial-video"; name = "Event & Wedding Aerial Video"
h1 = "Event and Wedding Aerial Video in San Luis Obispo County"
lede = "Discreet, permitted aerial coverage for weddings and events at Central Coast venues, from vineyard estates to coastal bluffs."
body = f"""
{hero(h1, lede, "/images/portfolio/9-aerial-drone-photos-big-sur.jpg", crumbs("Event & Wedding Aerial Video"))}
<section class="block"><div class="wrap article-body" style="max-width:900px">

<p>San Luis Obispo County's wedding and event venues, vineyard estates near Paso Robles, oceanfront properties around Cambria and Pismo Beach, historic downtown venues in San Luis Obispo, are part of what makes weddings here memorable. Aerial video captures the scale and setting of a venue in a way a ground photographer or videographer working alone cannot.</p>

<p>805 Aerial provides aerial video coverage that supplements, rather than replaces, a couple's primary photography and videography team. We work alongside a couple's existing vendors, coordinating flight windows around the ceremony and key moments without disrupting them.</p>

<h2>What Event Aerial Coverage Includes</h2>
<ul>
  <li><strong>Venue establishing shots</strong>, typically captured before guests arrive to avoid any privacy or noise concerns during the ceremony itself.</li>
  <li><strong>Reception and celebration footage</strong>, flown at a respectful altitude and distance during appropriate moments such as a first dance or send-off.</li>
  <li><strong>Coordination with the couple's photographer and videographer</strong> so aerial footage integrates cleanly into the final wedding film rather than competing with it.</li>
  <li><strong>Venue permission handling</strong>, since many Central Coast wedding venues have their own drone policies that need to be confirmed before the event.</li>
</ul>

<div class="callout"><strong>Local note:</strong> some Central Coast venues, particularly those near vineyards, coastal bluffs, or shared agricultural land, have specific drone policies or quiet-hour restrictions. We confirm venue-specific rules as part of every booking, not after arriving on site.</div>

<h2>Featured Client Work</h2>
<div class="case-panel">
  <span class="gold-label">Featured Client Work</span>
  <h3>Aerial Coverage for a Paso Robles Vineyard Wedding</h3>
  <div class="case-grid">
    <div><span class="col-label">The Setting</span><p>A couple booked a vineyard estate wedding and wanted footage that showed the full scale of the property alongside their ground photography.</p></div>
    <div><span class="col-label">The Approach</span><p>805 Aerial flew a pre-ceremony establishing shot of the vineyard and venue, then returned during the reception for a respectful, low-noise pass during the couple's exit.</p></div>
    <div><span class="col-label">The Result</span><p>The aerial footage was cut into the couple's wedding film by their videographer as the opening and closing shots.</p></div>
  </div>
  <p class="case-disclaimer">Client work described from an actual 805 Aerial project. Specific figures and identifying details are generalized for privacy.</p>
</div>

<h2>Frequently Asked Questions</h2>
<div class="faq">
<details><summary>Will the drone be noisy or disruptive during the ceremony?</summary><p>We plan flights around the ceremony itself, typically capturing aerial footage before guests arrive or during lower-key moments, rather than flying directly over the ceremony.</p></details>
<details><summary>Do we need to get permission from our venue?</summary><p>Most venues require advance notice or approval for drone use. We contact the venue directly as part of booking to confirm any restrictions.</p></details>
<details><summary>Can you work alongside our own photographer and videographer?</summary><p>Yes, this is the standard setup. We coordinate directly with a couple's existing vendors so the aerial footage complements rather than competes with their work.</p></details>
<details><summary>What happens if it's too windy to fly on the wedding day?</summary><p>Safety comes first. If wind or weather makes flying unsafe, we discuss options in advance, including a backup date scout or skipping the aerial segment for that event.</p></details>
</div>

<h2>Related Services</h2>
<p>For non-wedding event coverage, see <a href="/services/commercial-video-production/">commercial video production</a>, and for standalone aerial stills of a venue, see <a href="/services/drone-photography/">drone photography</a>. We cover venues throughout <a href="/locations/paso-robles/">Paso Robles</a>, <a href="/locations/cambria/">Cambria</a>, and <a href="/locations/pismo-beach/">Pismo Beach</a>.</p>
<p>For drone rules that can affect event flights near public land or beaches, see our guide to <a href="/blog/filming-drone-permits-san-luis-obispo-county/">filming and drone permits in San Luis Obispo County</a>, and the <a href="https://www.faa.gov/uas" target="_blank" rel="noopener">FAA's official drone regulations page</a>.</p>

</div></section>
{cta()}
""" + svc_schema(name) + bc_schema(slug, name)
write(f"services/{slug}/index.html", shell(f"{name} | San Luis Obispo County | 805 Aerial",
    "Aerial video coverage for weddings and events at Central Coast venues. Coordinated with your existing vendors. Call 805-242-8186.",
    f"{BASE}/services/{slug}/", "", body))

# ------------------------------------------------------------- SERVICE 5: Drone Photography
slug = "drone-photography"; name = "Drone Photography"
h1 = "Drone Photography in San Luis Obispo County"
lede = "Still aerial photography for marketing, insurance documentation, construction progress, and agriculture across the Central Coast."
body = f"""
{hero(h1, lede, "/images/portfolio/7-aerial-drone-photos-paso-robles.jpg", crumbs("Drone Photography"))}
<section class="block"><div class="wrap article-body" style="max-width:900px">

<p>Not every project needs video. Drone photography from 805 Aerial covers still aerial imagery for San Luis Obispo County businesses and property owners who need a single strong image, or a documented series of images, rather than a full video production.</p>

<h2>Common Uses for Drone Photography</h2>
<ul>
  <li><strong>Marketing imagery</strong> for a website, brochure, or ad campaign that needs one striking aerial shot rather than a full video.</li>
  <li><strong>Insurance and roofing documentation</strong>, capturing roof condition or storm damage from angles inaccessible without a ladder or lift.</li>
  <li><strong>Construction progress documentation</strong>, photographed from a consistent vantage point over the life of a project.</li>
  <li><strong>Agricultural monitoring</strong>, useful for vineyard and ranch operations across Paso Robles and the North County that want a periodic overview of crop or land condition.</li>
</ul>

<h2>Why Choose Aerial Stills Over Video</h2>
<p>Photography is often the right call when a project needs a single high-impact image rather than a full edited video, when budget or timeline is tighter, or when the use case, insurance claims, construction documentation, is inherently about a still record rather than motion. Many clients start with drone photography and add video later once they see what the imagery captures.</p>

<div class="callout"><strong>Local note:</strong> agricultural and ranch clients around Paso Robles and Creston often book recurring seasonal photography to track vineyard growth or land condition over a full growing season, rather than a single one-time shoot.</div>

<h2>Featured Client Work</h2>
<div class="case-panel">
  <span class="gold-label">Featured Client Work</span>
  <h3>Construction Progress Photography</h3>
  <div class="case-grid">
    <div><span class="col-label">The Setting</span><p>A developer needed a documented photo record of a project's progress from the same vantage point over several months.</p></div>
    <div><span class="col-label">The Approach</span><p>805 Aerial returned to the site on a set schedule, photographing from the same altitude and angle each visit for a consistent before-and-after record.</p></div>
    <div><span class="col-label">The Result</span><p>The developer used the photo series for internal reporting and for marketing the completed project.</p></div>
  </div>
  <p class="case-disclaimer">Client work described from an actual 805 Aerial project. Specific figures and identifying details are generalized for privacy.</p>
</div>

<h2>Frequently Asked Questions</h2>
<div class="faq">
<details><summary>Can you photograph roof damage for an insurance claim?</summary><p>Yes, aerial roof photography is a common request and can document damage from angles a ground photo or ladder inspection can't easily capture.</p></details>
<details><summary>Do you offer recurring photography for ongoing projects?</summary><p>Yes, construction and agricultural clients often book recurring visits on a weekly, monthly, or seasonal schedule.</p></details>
<details><summary>What resolution are the final images?</summary><p>Images are delivered at full camera resolution, suitable for large-format print as well as digital use.</p></details>
</div>

<h2>Related Services</h2>
<p>For a moving-image version of this coverage, see <a href="/services/aerial-drone-video-production/">aerial drone video production</a>, and for property listings specifically, see <a href="/services/real-estate-aerial-photography/">real estate aerial photography</a>. We shoot regularly around <a href="/locations/paso-robles/">Paso Robles</a> and <a href="/locations/atascadero/">Atascadero</a>.</p>
<p>For flight rules affecting agricultural and construction sites, see our <a href="/blog/filming-drone-permits-san-luis-obispo-county/">drone permits guide</a> and the <a href="https://www.faa.gov/uas" target="_blank" rel="noopener">FAA UAS regulations page</a>.</p>

</div></section>
{cta()}
""" + svc_schema(name) + bc_schema(slug, name)
write(f"services/{slug}/index.html", shell(f"{name} | San Luis Obispo County | 805 Aerial",
    "Still drone photography for marketing, insurance, construction, and agriculture across San Luis Obispo County. Call 805-242-8186.",
    f"{BASE}/services/{slug}/", "", body))

print("all remaining services done")
