import json, urllib.request, urllib.parse, os

with open('/Volumes/samsung/_WEB/ClaudeCode/credentials/unsplash_agency.json') as f:
    KEY = json.load(f)['access_key']

queries = {
    "morro-rock": "Morro Rock California",
    "avila-beach-pier": "Avila Beach pier California",
    "pismo-beach": "Pismo Beach California dunes",
    "paso-robles-vineyard": "Paso Robles vineyard California",
    "downtown-slo": "San Luis Obispo California downtown",
    "cambria-coast": "Cambria California coast",
    "bishop-peak": "Bishop Peak San Luis Obispo",
    "central-coast-sunset": "California central coast sunset ocean",
}

out_dir = os.path.dirname(__file__)
unsplash_dir = os.path.join(out_dir, "unsplash")
os.makedirs(unsplash_dir, exist_ok=True)
sources = []

for slug, q in queries.items():
    url = "https://api.unsplash.com/search/photos?" + urllib.parse.urlencode({"query": q, "per_page": 1, "orientation": "landscape"})
    req = urllib.request.Request(url, headers={"Authorization": f"Client-ID {KEY}"})
    try:
        with urllib.request.urlopen(req) as r:
            data = json.load(r)
        results = data.get("results", [])
        if not results:
            print("NO RESULTS", slug, q)
            continue
        photo = results[0]
        img_url = photo["urls"]["full"] + "&w=1920&q=80"
        link = photo["links"]["html"]
        author = photo["user"]["name"]
        fpath = os.path.join(unsplash_dir, f"{slug}.jpg")
        urllib.request.urlretrieve(img_url, fpath)
        sources.append(f"{slug}.jpg -- \"{q}\" -- Photo by {author} on Unsplash -- {link}")
        print("OK", slug)
    except Exception as e:
        print("FAIL", slug, e)

with open(os.path.join(out_dir, "..", "unsplash_sources.txt"), "w") as f:
    f.write("\n".join(sources) + "\n")
print("done")
