import json
import tweepy
import datetime
import requests
import random 
import time

def update_recent_pubs():
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

    
    # Return most recent responses as json object
    return response_json
while True:
    time.sleep(24*60*60)
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
    # print(recent_pubs_json)

    # Difference between today and yesterday
    prev_pubs = prev_pubs_json["entities"]
    recent_pubs = recent_pubs_json["entities"]
    prev_pubs_doi = []
    for pub in prev_pubs:
        try:
            prev_pubs_doi.append(pub['DOI'])
        except:
            continue
    new_pubs = []
    for pub in recent_pubs:
        try:
            temp_doi = pub['DOI']
            if not temp_doi in prev_pubs_doi:
                new_pubs.append(pub)
        except:
            continue


    # https://doi.org/(DOI)

    # list of sayings
    tweets = ['Check out our latest paper!','Here is a new paper to read!', 'Read the latest from our group!',
        'Find our newest paper at the link below!', 'Read our newest paper!', 'Here is the latest paper from our group!',
            'Check out what is new with our group!', 'Find a new paper here!']
    for pub in new_pubs:
        tweet = random.choice(tweets)
        doi = pub['DOI']
        tweet += " https://doi.org/"+doi
        api.update_status(tweet)
        print(tweet)

# Loop through each new result and tweet the paper
# api.update_status()
