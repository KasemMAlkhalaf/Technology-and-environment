import requests
import json

query = """
SELECT ?year (COUNT(?item) AS ?count) WHERE {
  ?item wdt:P31 wd:Q1255572;
        wdt:P577 ?date.
  BIND(YEAR(?date) AS ?year)
}
GROUP BY ?year
ORDER BY ?year
"""

url = "https://query.wikidata.org/sparql"
headers = {"Accept": "application/sparql-results+json"}
r = requests.get(url, params={"query": query, "format": "json"}, headers=headers)
data = r.json()

with open("../data/wikidata_export.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)