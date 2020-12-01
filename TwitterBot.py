import json
import tweepy
from scholarly import scholarly , ProxyGenerator
import datetime
from fp.fp import FreeProxy
import requests

def update_recent_pubs():
    base_url = "https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?"

    with open('creds.json') as f:
        keys = json.load(f)
    secondary_key = keys["microsoft_secondary_key"]
    # Search expression
    expression = "expr=Composite(AA.AuId=2100780784)"

    # Response Attributes
    attributes = "attributes=DOI,Ti"

    # Order By 0=relevance 1=newest first
    order_by = "orderby=D"

    # API Key
    key = "subscription-key="+secondary_key


    url = base_url + expression + '&' + attributes + '&' + order_by + '&' + key
    response = requests.get(url)
    response_json = response.json()

    with open('recent_pubs.json', 'w') as outfile:
        json.dump(response_json, outfile)
    
    # Return most recent responses as json object
    return response_json

now = datetime.datetime.now()
current_year = now.year
adam_id = 'GqBRrLMAAAAJ'

with open('creds.json') as f:
    keys = json.load(f)
# authenticate to Twitter
auth = tweepy.OAuthHandler(keys["api_key"], keys["api_key_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
# Create API object
api = tweepy.API(auth)

# prev_pubs_json contains results from previous day
with open('recent_pubs.json') as f:
    prev_pubs_json = json.load(f)

# recent_pubs_json contains results from today
recent_pubs_json = update_recent_pubs()

# Difference between today and yesterday

# Loop through each new result and tweet the paper



#link = ([pub.bib['url'] for pub in author.publications])
#print(link)

# Tweet last paper
# api.update_status("Check out our latest paper!" + str(titles[0]) + str(link))

# print("Check out our latest paper!" + str(title[0]))