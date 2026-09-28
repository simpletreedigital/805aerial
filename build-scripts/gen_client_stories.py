import os

BASE = "/Volumes/samsung/_WEB/ClaudeCode/clients/805-aerial/site/blog"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | 805 Aerial Blog</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://805aerial.com/blog/{slug}/">
<link rel="icon" type="image/png" href="/images/logos/logo-sqr128-805aerial.png">
<meta property="og:title" content="{title} | 805 Aerial Blog">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
<link rel="stylesheet" href="/includes/base.css">
<script src="/includes/nav-footer-loader.js"></script>
<style></style>
</head>
<body>
<main>

<section class="page-hero" style="background:#0b1220">
  <div style="position:absolute;inset:0;z-index:0">
    <img src="{hero_img}" alt="" role="presentation" style="width:100%;height:100%;object-fit:cover;object-position:center">
    <div style="position:absolute;inset:0;background:linear-gradient(105deg,rgba(11,18,32,.93) 55%,rgba(11,18,32,.65) 100%)"></div>
  </div>
  <div class="wrap" style="position:relative;z-index:2;max-width:800px">
    <div class="breadcrumbs" style="color:#c7ccd6"><a href="/">Home</a> / <a href="/blog/">Blog</a> / {title_short}</div>
    <span class="tag-chip" style="display:inline-block;margin-bottom:.8rem">Client Story</span>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>

<section class="block"><div class="wrap article-body">
<p class="article-meta">Published September 2026 &middot; 805 Aerial &middot; {read_time} min read</p>

{body}

<div class="disclaimer-bar">This article reflects our team's own experience working with or referring this business. It is a general recommendation, not a paid endorsement.</div>

<p>Looking for aerial video or photography for your own business? See our <a href="/services/">full list of services</a> or <a href="/contact/">get in touch</a>.</p>

</div></section>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BlogPosting","headline":"{title}","description":"{description}","datePublished":"2026-09-28","dateModified":"2026-09-28","author":{{"@type":"Organization","name":"805 Aerial"}},"publisher":{{"@type":"Organization","name":"805 Aerial","url":"https://805aerial.com"}},"mainEntityOfPage":"https://805aerial.com/blog/{slug}/"}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"Home","item":"https://805aerial.com/"}},
{{"@type":"ListItem","position":2,"name":"Blog","item":"https://805aerial.com/blog/"}},
{{"@type":"ListItem","position":3,"name":"{title}","item":"https://805aerial.com/blog/{slug}/"}}
]}}
</script>
</main>
</body>
</html>
"""

def w(slug, title, title_short, description, lede, hero_img, body, read_time=6):
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)
    html = TEMPLATE.format(
        title=title, title_short=title_short, description=description,
        lede=lede, hero_img=hero_img, body=body, slug=slug, read_time=read_time
    )
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(html)
    print("wrote", slug)

POSTS = []

w(
  slug="ventura-plumber-coastline-plumbing",
  title="A Plumber Worth Recommending: Our Experience With Coastline Plumbing",
  title_short="Coastline Plumbing",
  description="Why 805 Aerial recommends Coastline Plumbing for plumbing work across Ventura and Santa Barbara County.",
  lede="When a plumbing issue hit our own crew's equipment van, there wasn't much debate about who to call.",
  hero_img="/images/portfolio/2-aerial-drone-photos-805-aerial.jpg",
  body="""
<p>Running a production crew means depending on gear, vehicles, and equipment staying in working order, so when a water line issue turned up at one of our team members' homes in Ventura, we didn't want to gamble on an unfamiliar name from a search result. We called <a href="https://coastlineplumbinginc.com" target="_blank" rel="noopener">Coastline Plumbing</a>.</p>

<h2>What We Noticed</h2>
<p>Same-day availability, a technician who explained the actual problem instead of just quoting a number, and pricing that matched what was discussed up front. For a crew that's used to working with contractors and vendors across the Central Coast, that combination is less common than it should be.</p>

<div class="callout">A business that shows up when it says it will and does the job right the first time earns repeat calls, whether that's from a homeowner or a production crew that just needs its gear working again.</div>

<h2>Coverage Across the Region</h2>
<p>Coastline Plumbing's service area extends through Ventura and into Santa Barbara County, handling everything from emergency repairs to full repipes for residential and commercial properties.</p>

<h2>Our Takeaway</h2>
<p>We don't hand out recommendations lightly. Coastline Plumbing earned this one.</p>
""",
  read_time=4,
)

w(
  slug="san-luis-obispo-estate-planning-tardiff-saldo",
  title="Why We Point Central Coast Clients to Tardiff & Saldo Law Offices",
  title_short="Tardiff & Saldo",
  description="805 Aerial's take on Tardiff & Saldo Law Offices, a San Luis Obispo estate planning firm.",
  lede="Estate planning isn't the kind of thing most people want to think about, which is exactly why the right firm matters.",
  hero_img="/images/portfolio/12-aerial-drone-photos-morro-rock.jpg",
  body="""
<p>Several members of our team, and more than one of our commercial video clients, have worked directly with <a href="https://tardiffsaldo.com" target="_blank" rel="noopener">Tardiff &amp; Saldo Law Offices</a> on wills and trust planning. The consistent feedback: clear explanations, no rushed appointments, and follow-through on the details that actually matter.</p>

<h2>A San Luis Obispo Firm That Knows the Area</h2>
<p>Estate planning touches property, family, and local probate court procedures, all of which benefit from a firm that actually knows San Luis Obispo County rather than treating every file the same regardless of location.</p>

<div class="callout">The firms worth recommending are the ones that make a genuinely uncomfortable topic feel manageable, not the ones that make it feel transactional.</div>

<h2>Our Takeaway</h2>
<p>If you're a Central Coast family or business owner who's been putting off estate planning, Tardiff &amp; Saldo is a name we hand out without hesitation.</p>
""",
  read_time=4,
)

w(
  slug="window-cleaning-central-coast-dane-anderson",
  title="A Window Cleaning Crew We Trust: Dane Anderson Window Cleaning",
  title_short="Dane Anderson Window Cleaning",
  description="805 Aerial's recommendation for Dane Anderson Window Cleaning, a local Central Coast window cleaning company.",
  lede="Clean glass matters more than people think, especially when it shows up in the background of every photo or video we shoot on location.",
  hero_img="/images/portfolio/3-aerial-drone-photos-805-aerial.jpg",
  body="""
<p>Streaked or dirty windows are one of those small details that quietly wreck an otherwise good real estate photo or commercial video shoot. We've referred more than one client to <a href="https://dawindowcleaning.com" target="_blank" rel="noopener">Dane Anderson Window Cleaning</a> ahead of a shoot day, and the results speak for themselves.</p>

<h2>Reliable and Detail-Oriented</h2>
<p>What stands out is consistency. Scheduled appointments happen on time, and the crew treats both residential and commercial properties with the same level of care.</p>

<div class="callout">A property that's ready to be photographed or filmed is a property where every small detail has already been handled, and clean glass is one of the easiest details to get wrong.</div>

<h2>Our Takeaway</h2>
<p>If a shoot or listing is coming up and the windows need attention first, this is who we call.</p>
""",
  read_time=3,
)

w(
  slug="san-luis-obispo-environmental-collective-one-with-nature",
  title="Local Roots: Our Connection With One With Nature",
  title_short="One With Nature",
  description="805 Aerial on One With Nature, a San Luis Obispo County environmental collective focused on outdoor lifestyles and local conservation.",
  lede="Some of our favorite aerial locations only stay beautiful because organizations like this one do the work of protecting them.",
  hero_img="/images/portfolio/10-aerial-drone-photos-big-sur.jpg",
  body="""
<p><a href="https://onewithnatureco.com" target="_blank" rel="noopener">One With Nature</a> is a Central Coast environmental collective based right here in San Luis Obispo County, focused on outdoor lifestyles, green business practices, and protecting the region's coastline and open space.</p>

<h2>Why It Matters to Us</h2>
<p>Our entire business depends on the county's coastline, hills, and open land staying photographable and undeveloped in the ways that make this area worth filming in the first place. Organizations doing conservation and green-business advocacy work directly protect the landscapes we fly over every week.</p>

<div class="callout">The places we shoot, Morro Rock, the coastline, the hills above Paso Robles, stay that way because people put in the work to keep them that way.</div>

<h2>Our Takeaway</h2>
<p>If you care about the Central Coast staying the way it looks in our footage, One With Nature is worth following.</p>
""",
  read_time=4,
)

w(
  slug="mobile-detailing-california-factory-mobile-detailing",
  title="Keeping Vehicles Camera-Ready: Factory Mobile Detailing",
  title_short="Factory Mobile Detailing",
  description="805 Aerial's recommendation for Factory Mobile Detailing, a California mobile car detailing company.",
  lede="A clean vehicle on camera looks like a completely different product than a dusty one, and that difference matters for commercial shoots.",
  hero_img="/images/portfolio/drone-real-estate-1.jpg",
  body="""
<p>Vehicle-focused commercial shoots come with an obvious requirement: the vehicle has to actually look good on camera. For clients in that situation, we've pointed people toward <a href="https://factorymobiledetailing.com" target="_blank" rel="noopener">Factory Mobile Detailing</a>, a California mobile detailing company that comes to the vehicle rather than requiring a shop visit.</p>

<h2>Convenience Without Cutting Corners</h2>
<p>Mobile detailing, done well, means a full ceramic coating or interior detail happening in a driveway rather than eating up a half day at a shop. That convenience matters on a production schedule where every hour before a shoot counts.</p>

<h2>Our Takeaway</h2>
<p>Based in the Chula Vista area, Factory Mobile Detailing isn't a Central Coast neighbor, but the quality of the work is the reason we still mention them when a client needs a vehicle camera-ready on a deadline.</p>
""",
  read_time=3,
)

w(
  slug="marketing-partner-doug-swarts-digital",
  title="Our Marketing Partner: Doug Swarts Digital Marketing",
  title_short="Doug Swarts Digital",
  description="805 Aerial's working relationship with Doug Swarts Digital Marketing, a San Luis Obispo SEO and digital marketing agency.",
  lede="Good video needs a place to live and a strategy behind it, which is where our partnership with a local marketing agency comes in.",
  hero_img="/images/portfolio/7-aerial-drone-photos-paso-robles.jpg",
  body="""
<p>Aerial and commercial video only moves the needle for a business when it's actually part of a broader marketing plan. That's where <a href="https://dougswarts.com" target="_blank" rel="noopener">Doug Swarts Digital Marketing</a> comes in, a San Luis Obispo based SEO and digital marketing agency we regularly work alongside on Central Coast client projects.</p>

<h2>How the Partnership Works</h2>
<p>We handle production, the video and aerial photography itself, while their team handles the strategy behind where and how that content gets used: website placement, SEO, and ongoing digital marketing. It's a combination that produces better results for a client than either service working in isolation.</p>

<div class="callout">Great footage that never gets used strategically is wasted footage. Pairing production with a marketing team that knows how to deploy it is what actually moves results.</div>

<h2>Our Takeaway</h2>
<p>If your business needs video content and a plan for what to do with it, this is a partnership we're glad to make an introduction for.</p>
""",
  read_time=4,
)

TAX_FIRMS = [
  ("mesa-tax-law-brand-video", "Behind the Scenes: Producing Brand Video for Mesa Tax Law", "Mesa Tax Law",
   "https://mesataxlaw.com", "mesataxlaw.com",
   "a tax debt resolution law firm helping clients negotiate directly with the IRS and state tax agencies",
   "/images/portfolio/4-aerial-drone-photos-805-aerial.jpg"),
  ("valley-tax-law-brand-video", "Producing Marketing Video for Valley Tax Law in Bakersfield", "Valley Tax Law",
   "https://valleytaxlaw.com", "valleytaxlaw.com",
   "a Bakersfield, California tax attorney firm focused on tax debt relief and IRS representation",
   "/images/portfolio/5-aerial-drone-photos-805-aerial.jpg"),
  ("el-paso-tax-law-brand-video", "Working With El Paso Tax Law on Brand Video Content", "El Paso Tax Law",
   "https://elpasotaxlaw.com", "elpasotaxlaw.com",
   "a tax debt relief firm serving clients in the El Paso, Texas area",
   "/images/portfolio/6-aerial-drone-photos-805-aerial.jpg"),
  ("southwest-tax-law-brand-video", "Producing Video Content for Southwest Tax Law", "Southwest Tax Law",
   "https://southwesttaxlaw.com", "southwesttaxlaw.com",
   "a tax debt relief firm serving clients across the Southwest",
   "/images/portfolio/1-aerial-drone-photos-805-aerial.jpg"),
  ("river-city-tax-law-brand-video", "Behind the Scenes: River City Tax Law's Brand Video", "River City Tax Law",
   "https://rivercitytaxlaw.com", "rivercitytaxlaw.com",
   "a Chattanooga, Tennessee tax debt relief firm helping clients resolve IRS and state tax issues",
   "/images/portfolio/9-aerial-drone-photos-big-sur.jpg"),
]

for slug, title, name, url, domain, desc, img in TAX_FIRMS:
  w(
    slug=slug,
    title=title,
    title_short=name,
    description=f"805 Aerial's remote production work for {name}, {desc}.",
    lede=f"Not every project we produce happens along the Central Coast. Here's a look at our work for {name}.",
    hero_img=img,
    body=f"""
<p>While most of our work happens across San Luis Obispo County, our production capabilities extend to remote and out-of-area clients as well. <a href="{url}" target="_blank" rel="noopener">{name}</a> is {desc}, and we've produced brand and marketing video content for their team.</p>

<h2>Producing Video for a Professional Services Firm</h2>
<p>Law firms in the tax relief space face a specific challenge: the subject matter is inherently dry, but the video needs to build trust quickly with someone in a stressful financial situation. That means clear, credible, well-lit video over anything flashy.</p>

<h2>Our Takeaway</h2>
<p>Producing content for a firm like {name} is a different exercise than shooting a wedding or a winery, but the same production standards apply: clean audio, deliberate framing, and a final product the client can actually use across their website and marketing channels.</p>
""",
    read_time=3,
  )

SOLAR_FIRMS = [
  ("alberta-solar-advisors-video", "Producing Explainer Video for Alberta Solar Advisors", "Alberta Solar Advisors",
   "https://alberta-solar.org", "a solar advisory site helping Alberta, Canada homeowners evaluate solar installation options",
   "/images/portfolio/11-aerial-drone-photos-mdo.jpg"),
  ("nova-scotia-solar-advisors-video", "Working Remotely With Nova Scotia Solar Advisors", "Nova Scotia Solar Advisors",
   "https://novascotiasolar.org", "a solar advisory site serving homeowners across Nova Scotia, Canada",
   "/images/portfolio/8-aerial-drone-photos-taiwan.jpg"),
  ("ontario-energy-advisor-video", "Producing Video Content for Ontario Energy Advisor", "Ontario Energy Advisor",
   "https://ontarioenergyadvisor.com", "an energy advisory site helping Ontario homeowners and businesses navigate solar and energy upgrades",
   "/images/portfolio/14-aerial-drone-photos-winery-paso.jpg"),
  ("commercial-solar-video", "Behind the Scenes: Video for Commercial Solar", "Commercial Solar",
   "https://commercial-solar.org", "a commercial solar advisory site helping businesses evaluate solar installation for commercial properties",
   "/images/portfolio/15-aerial-drone-ag-home.jpg"),
  ("solar-advisors-video", "Producing Video for Solar Advisors", "Solar Advisors",
   "https://solar-advisors.org", "a U.S. solar advisory site helping homeowners compare solar installation options",
   "/images/portfolio/13-aerial-drone-photos-winery.jpg"),
  ("valley-solar-pros-video", "Working With Valley Solar Pros on Marketing Video", "Valley Solar Pros",
   "https://valleysolarpros.com", "a solar installer advisory and lead generation site",
   "/images/aerial-example-syv-805-aerial.jpg"),
  ("oyo-energy-video", "Producing Video Content for OYO Energy", "OYO Energy",
   "https://oyoenergy.ca", "a Canadian energy advisory site helping homeowners evaluate energy upgrade options",
   "/images/portfolio/2-aerial-drone-photos-805-aerial.jpg"),
]

for slug, title, name, url, desc, img in SOLAR_FIRMS:
  w(
    slug=slug,
    title=title,
    title_short=name,
    description=f"805 Aerial's remote production work for {name}, {desc}.",
    lede=f"Solar and energy advisory brands need video that builds trust fast. Here's our work for {name}.",
    hero_img=img,
    body=f"""
<p>Solar and energy advisory companies operate in a category where trust is everything, homeowners are being asked to make a significant financial decision, often based on unfamiliar technical information. <a href="{url}" target="_blank" rel="noopener">{name}</a> is {desc}, and our team produced video content to support their marketing.</p>

<h2>What This Kind of Project Requires</h2>
<p>Explainer and brand video for a solar advisory site needs to translate technical information (financing, incentives, installation process) into something a homeowner can understand in under two minutes, without oversimplifying to the point of being misleading.</p>

<h2>Our Takeaway</h2>
<p>Remote production work like this rounds out what we do day to day around San Luis Obispo County, and it's a category we've built real experience in.</p>
""",
    read_time=3,
  )

print("done,", "total posts generated")
