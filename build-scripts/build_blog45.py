from gen_pages import shell, write
BASE = "https://805aerial.com"

def article_schema(slug, title, desc, date):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{desc}","datePublished":"{date}","dateModified":"{date}","author":{{"@type":"Organization","name":"805 Aerial"}},"publisher":{{"@type":"Organization","name":"805 Aerial"}}}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"Home","item":"{BASE}/"}},
{{"@type":"ListItem","position":2,"name":"Blog","item":"{BASE}/blog/"}},
{{"@type":"ListItem","position":3,"name":"{title}","item":"{BASE}/blog/{slug}/"}}
]}}
</script>"""

# ------------------------------------------------------------- ARTICLE 4
slug = "small-business-spotlight-central-coast-video"
title = "Small Business Spotlight: How Central Coast Businesses Use Video to Grow"
desc = "How San Luis Obispo County small businesses, from hospitality to agriculture, are using video and aerial content to reach customers."
date = "2026-09-27"
body = f"""
<section class="page-hero" style="background:#0b1220">
  <div style="position:absolute;inset:0;z-index:0">
    <img src="/images/portfolio/6-aerial-drone-photos-805-aerial.jpg" alt="" role="presentation" style="width:100%;height:100%;object-fit:cover;object-position:center">
    <div style="position:absolute;inset:0;background:linear-gradient(105deg,rgba(11,18,32,.93) 55%,rgba(11,18,32,.65) 100%)"></div>
  </div>
  <div class="wrap" style="position:relative;z-index:2;max-width:800px">
    <div class="breadcrumbs" style="color:#c7ccd6"><a href="/">Home</a> / <a href="/blog/">Blog</a> / Small Business Spotlight</div>
    <h1>{title}</h1>
    <p class="lede">A look at how small businesses across San Luis Obispo County are using video, including aerial footage, to compete for customers.</p>
  </div>
</section>

<section class="block"><div class="wrap article-body">
<p class="article-meta">Published September 2026 &middot; 805 Aerial &middot; 9 min read</p>

<p>Most conversations about video marketing focus on big brands with big budgets. But across San Luis Obispo County, small, independently owned businesses, restaurants, boutique hotels, farm stands, service businesses, are increasingly the ones investing in video, often because they're competing directly against national chains and larger tourism operators with far bigger marketing budgets. This piece looks at how and why that's happening, and where video actually moves the needle for a small local business.</p>

<h2>Why Small Businesses Are Investing in Video Now</h2>
<p>A few forces are pushing Central Coast small businesses toward video that weren't as strong even five years ago:</p>
<ul>
  <li><strong>Social platforms reward video over static posts.</strong> Instagram, TikTok, and even Google Business Profile now favor video content in terms of reach and engagement, which changes the math for a small business deciding where to put a limited marketing budget.</li>
  <li><strong>Tourists research destinations visually before they arrive.</strong> A visitor deciding between two Central Coast towns, or two restaurants in the same town, is often making that decision based on a 15-second video, not a paragraph of text.</li>
  <li><strong>Production costs have come down.</strong> What used to require a full production crew and a large budget can now be produced efficiently by a small local video team, including aerial footage that would have been prohibitively expensive a decade ago.</li>
</ul>

<h2>Patterns Across Different Types of Local Businesses</h2>
<h3>Hospitality and Tourism</h3>
<p>Boutique hotels and vacation rental operators along the coast, particularly around Pismo Beach, Morro Bay, and Cambria, use aerial and ground video to sell the setting itself, proximity to the water, views, the character of the town, since that's frequently the deciding factor for a visitor choosing between similar-priced options.</p>

<h3>Agriculture and Farm-Direct Businesses</h3>
<p>Beyond wineries, farm stands, ranches, and specialty agriculture operations across the county increasingly use video to explain their product and process directly to consumers, something that's become more valuable as more buyers care about where their food comes from and want to see the actual land and operation behind a brand.</p>

<h3>Service Businesses</h3>
<p>Even businesses without an obviously "visual" product, contractors, professional services, local retailers, use video for a simpler reason: trust. A short video showing a real business, a real team, and a real location performs better with local search and social audiences than stock photography or a text-only website ever could.</p>

<div class="scenario-box">
<strong>Illustrative example:</strong> a family-owned business in Atascadero wanted to differentiate itself from a national competitor that had recently opened nearby. Rather than competing on price, the business invested in a short video showing its actual location, staff, and process, including an aerial shot establishing its setting along the El Camino Real corridor. The video became the business's top-performing social content for the following quarter, outperforming every static post from the prior year.
</div>

<h2>What Small Businesses Get Wrong About Video</h2>
<ul>
  <li><strong>Trying to do too much in one video.</strong> The most effective small business videos are short and focused on one clear message, not an attempt to cover every product or service in 90 seconds.</li>
  <li><strong>Skipping planning.</strong> A five-minute conversation about what the video actually needs to accomplish, before any filming happens, consistently produces better results than showing up and filming whatever looks interesting.</li>
  <li><strong>Underusing the footage.</strong> A single shoot can usually be cut into multiple pieces, a full video, several short social clips, a still photo set, but many small businesses only use the single main edit and leave the rest of the value on the table.</li>
</ul>

<h2>Frequently Asked Questions</h2>
<div class="faq">
<details><summary>Is aerial video worth it for a small local business, not just a big destination brand?</summary><p>Often yes, particularly for businesses where setting, location, or scale is part of the value story, hospitality, agriculture, and businesses in visually distinct parts of the county.</p></details>
<details><summary>How much video content does a small business actually need?</summary><p>Most small businesses do well starting with one strong primary video and a handful of shorter cuts from the same shoot, rather than trying to produce a large content library all at once.</p></details>
<details><summary>Can a single video work across multiple platforms?</summary><p>Yes, with the right planning, one shoot can typically be edited into different formats for a website, Instagram, and Google Business Profile without needing separate shoots for each.</p></details>
</div>

<h2>Getting Started</h2>
<p>805 Aerial works with small businesses across San Luis Obispo County on both <a href="/services/commercial-video-production/">commercial video production</a> and <a href="/services/aerial-drone-video-production/">aerial drone video</a>, scaled to what an individual business actually needs rather than a one-size-fits-all package.</p>

<div class="disclaimer-bar">This article is for general informational purposes only and does not constitute business or marketing advice specific to any individual company.</div>

<p>For local business resources, see the <a href="https://www.slochamber.org/" target="_blank" rel="noopener">San Luis Obispo Chamber of Commerce</a> and <a href="https://www.visitslo.com/" target="_blank" rel="noopener">Visit SLO CAL</a>.</p>

</div></section>
""" + article_schema(slug, title, desc, date)
write(f"blog/{slug}/index.html", shell(f"{title} | 805 Aerial Blog", desc, f"{BASE}/blog/{slug}/", "", body))
print("article 4 done")

# ------------------------------------------------------------- ARTICLE 5
slug = "slo-county-tourism-aerial-footage-destination-marketing"
title = "SLO County Tourism and Media: How Aerial Footage Shapes Central Coast Destination Marketing"
desc = "How aerial video and photography support San Luis Obispo County's tourism and destination marketing across hospitality, wine, and coastal towns."
date = "2026-09-27"
body = f"""
<section class="page-hero" style="background:#0b1220">
  <div style="position:absolute;inset:0;z-index:0">
    <img src="/images/portfolio/12-aerial-drone-photos-morro-rock.jpg" alt="" role="presentation" style="width:100%;height:100%;object-fit:cover;object-position:center">
    <div style="position:absolute;inset:0;background:linear-gradient(105deg,rgba(11,18,32,.93) 55%,rgba(11,18,32,.65) 100%)"></div>
  </div>
  <div class="wrap" style="position:relative;z-index:2;max-width:800px">
    <div class="breadcrumbs" style="color:#c7ccd6"><a href="/">Home</a> / <a href="/blog/">Blog</a> / Tourism &amp; Aerial Footage</div>
    <h1>{title}</h1>
    <p class="lede">How aerial video and photography have become part of the standard toolkit for marketing San Luis Obispo County as a destination.</p>
  </div>
</section>

<section class="block"><div class="wrap article-body">
<p class="article-meta">Published September 2026 &middot; 805 Aerial &middot; 10 min read</p>

<p>San Luis Obispo County markets itself against every other stretch of California coastline, and against wine regions across the state, for the same limited pool of visitor attention and spending. Destination marketing here increasingly relies on aerial footage, not as a decorative flourish, but because the county's actual selling points, Morro Rock, the Pismo Beach dunes, Paso Robles vineyards spread across rolling hills, are geographic features that photograph dramatically better from the air than from the ground.</p>

<h2>Why Aerial Footage Fits This County Specifically</h2>
<p>Compare San Luis Obispo County's landmarks to a typical inland town: Morro Rock rising out of the bay, the Pismo Beach dune complex, the patchwork of vineyard rows across Paso Robles' hillsides, the Cambria coastline giving way to the pine forests heading north. These are geographic features defined by scale and topography, exactly what aerial photography and video capture that ground-level photography cannot.</p>

<h2>Who Uses Aerial Footage for Destination Marketing</h2>
<ul>
  <li><strong>Tourism boards and visitor bureaus.</strong> Organizations like <a href="https://www.visitslo.com/" target="_blank" rel="noopener">Visit SLO CAL</a>, the county's tourism marketing organization, rely heavily on aerial and drone footage to market the region as a whole, since destination marketing is fundamentally about selling a place, not a single business.</li>
  <li><strong>Individual hospitality businesses.</strong> Hotels, resorts, and vacation rental operators use aerial footage of their specific property alongside the surrounding landscape to connect their business to the broader destination appeal.</li>
  <li><strong>Wineries and agricultural tourism.</strong> As covered in our related article on <a href="/blog/paso-robles-wineries-aerial-video-marketing/">Paso Robles wineries and aerial video</a>, wine tourism specifically leans on aerial footage to show the scale of the region's vineyards.</li>
  <li><strong>City and county government.</strong> Aerial footage increasingly appears in official destination marketing and public information content produced by cities and the county itself.</li>
</ul>

<h2>What Effective Destination Aerial Footage Looks Like</h2>
<div class="scenario-box">
<strong>Illustrative example:</strong> a hospitality group with properties in both Pismo Beach and Cambria wanted a single video campaign connecting the two locations under one destination narrative, "the Central Coast experience," rather than marketing each property separately. Aerial footage connecting the coastline between the two towns, combined with ground footage of each specific property, gave the campaign a sense of geographic continuity that two separate, unconnected property videos couldn't achieve.
</div>
<p>The strongest destination marketing footage typically does two things at once: it captures the specific landmark or feature that makes a location recognizable (Morro Rock, a particular stretch of coastline, a vineyard-covered hillside), and it connects that landmark to the specific business or experience being marketed, rather than functioning as generic stock-style scenery.</p>

<h2>The Seasonal Dimension</h2>
<p>Central Coast tourism has real seasonal patterns, summer coastal tourism, fall wine harvest season, and shoulder seasons that many businesses specifically want to market against to smooth out visitor demand throughout the year. Aerial footage captured across different seasons, vineyard color in the fall, clear summer coastal light, can support marketing campaigns aimed at extending visitor interest beyond the busiest months.</p>

<h2>Frequently Asked Questions</h2>
<div class="faq">
<details><summary>Do individual businesses need their own aerial footage, or can they use stock destination footage?</summary><p>Generic stock footage of a coastline or vineyard doesn't connect to a specific business the way footage of that business's actual property and setting does. Most hospitality and tourism businesses get more value from footage of their own location.</p></details>
<details><summary>Are there restrictions on flying drones near popular tourist landmarks like Morro Rock?</summary><p>Yes, some landmark and coastal areas have habitat or state park restrictions. See our <a href="/blog/filming-drone-permits-san-luis-obispo-county/">guide to filming and drone permits</a> for more detail before planning a shoot near a specific landmark.</p></details>
<details><summary>How does destination marketing footage differ from a single business's marketing video?</summary><p>Destination footage tends to emphasize geography and place, while a single business's video needs to connect that sense of place back to its specific product or property, ideally within the same piece of content.</p></details>
</div>

<h2>Producing Destination-Quality Aerial Content</h2>
<p>805 Aerial produces aerial video and photography for hospitality and tourism businesses across <a href="/locations/pismo-beach/">Pismo Beach</a>, <a href="/locations/morro-bay/">Morro Bay</a>, <a href="/locations/cambria/">Cambria</a>, and the rest of San Luis Obispo County, through <a href="/services/commercial-video-production/">commercial video production</a> and <a href="/services/aerial-drone-video-production/">aerial drone video</a> services built around what makes each specific location distinct.</p>

<div class="disclaimer-bar">This article is for general informational purposes only and does not constitute marketing or legal advice specific to any individual business or destination campaign.</div>

<p>For county-wide tourism resources, see <a href="https://www.visitslo.com/" target="_blank" rel="noopener">Visit SLO CAL</a> and the <a href="https://www.slochamber.org/" target="_blank" rel="noopener">San Luis Obispo Chamber of Commerce</a>.</p>

</div></section>
""" + article_schema(slug, title, desc, date)
write(f"blog/{slug}/index.html", shell(f"{title} | 805 Aerial Blog", desc, f"{BASE}/blog/{slug}/", "", body))
print("article 5 done")
