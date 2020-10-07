import json
import tweepy
from scholarly import scholarly

with open('creds.json') as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys["api_key"], keys["api_key_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
api = tweepy.API(auth)
print(next(scholarly.search_author('Adam Moule')))
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
