import requests
import json

query = """
SELECT ?componentLabel ?lifespan WHERE {
  ?component wdt:P31 wd:Q182181;
             wdt:P366 ?lifespan.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ru". }
}
LIMIT 10
"""

url = "https://query.wikidata.org/sparql"
headers = {"Accept": "application/sparql-results+json"}
r = requests.get(url, params={"query": query, "format": "json"}, headers=headers)
data = r.json()

with open("../data/wikidata_export.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)