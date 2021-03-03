import requests
import json

base_url = "https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?"

with open('creds.json') as f:
    keys = json.load(f)
secondary_key = keys["microsoft_secondary_key"]
# Search expression
expression = "expr=And(Composite(AA.AuId=2100780784),Y>=2020)"

# Response Attributes
attributes = "attributes=DOI,Ti,D"

# Order By 0=relevance 1=newest first
order_by = "orderby=D:desc"

# API Key
key = "subscription-key="+secondary_key


url = base_url + expression + '&' + attributes + '&' + order_by + '&' + key
response = requests.get(url)
response_json = response.json()

with open('recent_pubs.json', 'w') as outfile:
    json.dump(response_json, outfile)
newest_doi = response_json["entities"][0]["DOI"]