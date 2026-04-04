import requests
import json

query = """
SELECT ?communityLabel ?members WHERE {
  ?community wdt:P31 wd:Q8685;
              wdt:P1082 ?members.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ru". }
}
ORDER BY DESC(?members)
LIMIT 10
"""

url = "https://query.wikidata.org/sparql"
headers = {"Accept": "application/sparql-results+json"}
r = requests.get(url, params={"query": query, "format": "json"}, headers=headers)
data = r.json()

with open("../data/wikidata_export.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)