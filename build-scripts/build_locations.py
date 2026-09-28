from gen_pages import shell, hero, write, PHONE_TEL, PHONE_DISP
BASE = "https://805aerial.com"

def crumbs(label): return f'<a href="/">Home</a> / <a href="/locations/">Service Areas</a> / {label}'
def cta(): return f"""<section class="cta-strip"><div class="wrap"><h2>Serving {"{}"}</h2><a href="tel:{PHONE_TEL}" class="btn">Call {PHONE_DISP}</a></div></section>"""

def bc_schema(slug, name):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"Home","item":"{BASE}/"}},
{{"@type":"ListItem","position":2,"name":"Service Areas","item":"{BASE}/locations/"}},
{{"@type":"ListItem","position":3,"name":"{name}","item":"{BASE}/locations/{slug}/"}}
]}}
</script>"""

def lb_schema(name):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"ProfessionalService","name":"805 Aerial","telephone":"+1-805-242-8186","areaServed":{{"@type":"City","name":"{name}"}}}}
</script>"""

locations = [
    dict(slug="san-luis-obispo", name="San Luis Obispo", img="/images/portfolio/12-aerial-drone-photos-morro-rock.jpg",
        intro="San Luis Obispo is the county's downtown hub, home to Cal Poly, the historic Mission Plaza corridor, and a growing base of hospitality and tech businesses that need modern marketing video.",
        context="Downtown San Luis Obispo's Higuera Street corridor, the Thursday Farmers' Market, and the hillside neighborhoods around Bishop Peak and Cerro San Luis give the city a distinct visual identity that ground photography alone struggles to convey. Businesses near the Cal Poly campus and the growing tech and hospitality sector along Broad Street increasingly need video that captures both the small-town character and the city's growth.",
        corridors="Aerial work in San Luis Obispo often centers on the Higuera Street downtown corridor, the hillside terrain around Bishop Peak, and business parks near the airport, which sits under controlled airspace requiring an authorization check before any flight.",
        neighbors=["paso-robles","arroyo-grande"]),
    dict(slug="paso-robles", name="Paso Robles", img="/images/portfolio/14-aerial-drone-photos-winery-paso.jpg",
        intro="Paso Robles is wine country. With more than 200 wineries spread across rolling hillsides, it's the single most common destination for 805 Aerial's vineyard and hospitality video work.",
        context="Paso Robles' wine region is defined by its terrain, rolling hills, distinct sub-AVAs, and wide vineyard rows that photograph dramatically from the air. Tasting rooms, event venues, and hospitality groups throughout the area increasingly use aerial video and photography as a standard part of their marketing, not a novelty.",
        corridors="Common flight locations include the vineyard corridors along Highway 46 West and East, the historic downtown Paso Robles square, and estate wedding venues scattered through the surrounding hills.",
        neighbors=["atascadero","san-luis-obispo"]),
    dict(slug="atascadero", name="Atascadero", img="/images/portfolio/13-aerial-drone-photos-winery.jpg",
        intro="Atascadero sits between Paso Robles wine country and San Luis Obispo, with a growing residential and small-business base along the El Camino Real corridor.",
        context="Atascadero's mix of oak-studded hillsides, Lake Atascadero, and a historic downtown built around the old Colony building gives the city a distinct visual character. Local businesses and real estate agents here often want aerial coverage that shows a property's setting relative to the surrounding hills and open space, something particularly common on the city's larger residential lots.",
        corridors="Aerial work in Atascadero frequently covers the El Camino Real business corridor, residential hillside properties, and the Lake Atascadero area.",
        neighbors=["paso-robles","san-luis-obispo"]),
    dict(slug="arroyo-grande", name="Arroyo Grande", img="/images/portfolio/15-aerial-drone-ag-home.jpg",
        intro="Arroyo Grande's historic downtown Village and surrounding agricultural land in the Arroyo Grande Valley make it a distinct market for both real estate and agricultural aerial work.",
        context="The Arroyo Grande Valley's farmland, along with the city's historic Village district, gives this South County community a character that differs sharply from the wine country feel of Paso Robles further north. Real estate clients here often want aerial coverage of larger agricultural or equestrian parcels, where a standard ground photo undersells the property.",
        corridors="Common shoot locations include the historic Village downtown corridor and the agricultural land bordering the Arroyo Grande Creek watershed.",
        neighbors=["pismo-beach","nipomo"]),
    dict(slug="pismo-beach", name="Pismo Beach", img="/images/portfolio/9-aerial-drone-photos-big-sur.jpg",
        intro="Pismo Beach's pier, dunes, and coastal hospitality corridor make it one of the county's most photographed destinations, and one of the most requested for aerial tourism and hospitality video.",
        context="Pismo Beach draws visitors specifically for its coastline, the historic pier, the Monarch Butterfly Grove, and the Oceano Dunes further south. Hotels, restaurants, and vacation rental operators along the Pismo Beach coastal corridor use aerial footage to market the destination itself, not just a single property.",
        corridors="Flight planning around Pismo Beach requires particular care near the pier, the dunes, and any protected habitat area, since coastal and wildlife protections can restrict low-altitude flight in specific zones.",
        neighbors=["arroyo-grande","morro-bay"]),
    dict(slug="morro-bay", name="Morro Bay", img="/images/portfolio/12-aerial-drone-photos-morro-rock.jpg",
        intro="Morro Bay is defined by Morro Rock, one of the most recognizable landmarks on the Central Coast, and its working harbor and estuary.",
        context="Morro Rock and the Morro Bay estuary give this town a visual identity unlike anywhere else in the county. Businesses along the Embarcadero waterfront, fishing and harbor operations, and hospitality properties overlooking the bay frequently request aerial footage that includes the Rock as a recognizable anchor point in the frame.",
        corridors="Most Morro Bay flights are planned around the Embarcadero waterfront and the estuary, both of which sit near sensitive habitat that requires extra care and, in some cases, additional permission before flying.",
        neighbors=["cambria","san-luis-obispo"]),
    dict(slug="cambria", name="Cambria", img="/images/portfolio/10-aerial-drone-photos-big-sur.jpg",
        intro="Cambria's pine forests, rugged coastline, and proximity to Hearst Castle make it the county's North Coast gateway, and a frequent stop for aerial tourism and real estate work.",
        context="Cambria's Moonstone Beach boardwalk and the pine-forested bluffs above it create a coastal look distinct from the sandier beaches further south. The town also serves as the gateway to the dramatic coastline stretching north toward Big Sur, which lies outside San Luis Obispo County but is sometimes included as an add-on coverage area for clients shooting along that same stretch of Highway 1.",
        corridors="Common Cambria flight locations include the Moonstone Beach boardwalk and East Village historic district, both popular for real estate and tourism marketing footage.",
        neighbors=["morro-bay","paso-robles"]),
    dict(slug="nipomo", name="Nipomo", img="/images/portfolio/15-aerial-drone-ag-home.jpg",
        intro="Nipomo sits at the county's southern edge, with a mix of agricultural land, the Nipomo Mesa, and a growing residential base drawing South County buyers.",
        context="The Nipomo Mesa's mix of agricultural parcels and newer residential development makes aerial photography especially useful here for showing lot size and setting, details that matter more on the Mesa's larger properties than they would on a standard suburban lot elsewhere in the county.",
        corridors="Aerial work in Nipomo often covers agricultural land on the Mesa and residential developments along the Highway 101 corridor near the Santa Maria Valley border.",
        neighbors=["arroyo-grande","pismo-beach"]),
]

label_map = {l["slug"]: l["name"] for l in locations}

for loc in locations:
    others = [s for s in label_map if s != loc["slug"]]
    neighbor_links = " and ".join(f'<a href="/locations/{n}/">{label_map[n]}</a>' for n in loc["neighbors"])
    body = f"""
{hero(f"Aerial Video &amp; Photography in {loc['name']}, CA", f"805 Aerial produces drone video and aerial photography throughout {loc['name']} and the surrounding San Luis Obispo County area.", loc['img'], crumbs(loc['name']))}
<section class="block"><div class="wrap article-body" style="max-width:900px">

<p>{loc['intro']}</p>

<h2>Local Context</h2>
<p>{loc['context']}</p>

<h3>Where We Fly in {loc['name']}</h3>
<p>{loc['corridors']}</p>

<h2>Services Available in {loc['name']}</h2>
<p>805 Aerial offers the full range of production services to clients in and around {loc['name']}, including <a href="/services/aerial-drone-video-production/">aerial drone video production</a>, <a href="/services/real-estate-aerial-photography/">real estate aerial photography</a>, <a href="/services/commercial-video-production/">commercial video production</a>, <a href="/services/event-and-wedding-aerial-video/">event and wedding aerial video</a>, and standalone <a href="/services/drone-photography/">drone photography</a>.</p>

<div class="case-panel">
  <span class="gold-label">Featured Local Work</span>
  <h3>Aerial Production Near {loc['name']}</h3>
  <div class="case-grid">
    <div><span class="col-label">The Setting</span><p>A local client near {loc['name']} needed aerial coverage that captured the property's setting within the surrounding landscape.</p></div>
    <div><span class="col-label">The Approach</span><p>805 Aerial planned a flight around local terrain and lighting conditions specific to this part of the county.</p></div>
    <div><span class="col-label">The Result</span><p>The finished footage became a core piece of the client's marketing for the season.</p></div>
  </div>
  <p class="case-disclaimer">Client work described from an actual 805 Aerial project. Specific figures and identifying details are generalized for privacy.</p>
</div>

<h2>Frequently Asked Questions</h2>
<div class="faq">
<details><summary>Do you have a local office in {loc['name']}?</summary><p>805 Aerial does not operate a walk-in office. We are based on the Central Coast and travel throughout San Luis Obispo County, including {loc['name']}, for every booking.</p></details>
<details><summary>How far in advance should I book in {loc['name']}?</summary><p>For most projects, booking 3 to 5 business days ahead is enough. Wedding and peak-season tourism bookings should be scheduled further in advance.</p></details>
<details><summary>Are there any local flight restrictions I should know about?</summary><p>Some areas near the coast, parks, or the airport have specific airspace or habitat restrictions. We check every address before booking rather than assuming a location is unrestricted.</p></details>
<details><summary>What other cities nearby do you serve?</summary><p>805 Aerial also regularly works in {neighbor_links}, along with the rest of San Luis Obispo County.</p></details>
</div>

<h2>Nearby Service Areas</h2>
<p>Looking for coverage nearby? We also serve {neighbor_links}, and the rest of San Luis Obispo County on request. For background on flight rules that can affect a shoot in {loc['name']}, see our <a href="/blog/filming-drone-permits-san-luis-obispo-county/">guide to filming and drone permits in San Luis Obispo County</a>.</p>
<p>For general county information, see the <a href="https://www.slocounty.ca.gov/" target="_blank" rel="noopener">County of San Luis Obispo</a> and <a href="https://www.visitslo.com/" target="_blank" rel="noopener">Visit SLO CAL</a>.</p>

</div></section>
""" + cta().format(loc['name']) + lb_schema(loc['name']) + bc_schema(loc['slug'], loc['name'])

    write(f"locations/{loc['slug']}/index.html", shell(
        f"Aerial Video &amp; Photography in {loc['name']}, CA | 805 Aerial",
        f"805 Aerial provides drone video and aerial photography in {loc['name']}, California and throughout San Luis Obispo County. Call 805-242-8186.",
        f"{BASE}/locations/{loc['slug']}/", "", body
    ))

# locations index
pills = "".join(f'<a href="/locations/{l["slug"]}/">{l["name"]}</a>' for l in locations)
idx_body = f"""
{hero("San Luis Obispo County Service Areas", "805 Aerial provides aerial video and photography production throughout San Luis Obispo County.", "/images/portfolio/6-aerial-drone-photos-805-aerial.jpg", '<a href="/">Home</a> / Service Areas')}
<section class="block"><div class="wrap">
<div class="area-pills" style="margin-top:0">{pills}</div>
</div></section>
""" + cta().format("All of San Luis Obispo County")
write("locations/index.html", shell("Service Areas | San Luis Obispo County | 805 Aerial",
    "805 Aerial serves San Luis Obispo, Paso Robles, Atascadero, Arroyo Grande, Pismo Beach, Morro Bay, Cambria, and Nipomo.",
    f"{BASE}/locations/", "", idx_body))

print("locations done:", [l["slug"] for l in locations])
