import requests
import json

query = """
SELECT ?studyLabel ?year WHERE {
  ?study wdt:P31 wd:Q13442814;
         wdt:P921 wd:Q5421392;
         wdt:P577 ?date.
  BIND(YEAR(?date) AS ?year)
}
LIMIT 10
"""

url = "https://query.wikidata.org/sparql"
headers = {"Accept": "application/sparql-results+json"}
r = requests.get(url, params={"query": query, "format": "json"}, headers=headers)
data = r.json()

with open("../data/wikidata_export.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)