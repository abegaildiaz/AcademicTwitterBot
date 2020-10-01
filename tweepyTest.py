import json
import tweepy

with open('creds.json') as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys["api_key"], keys["api_key_secret"])
auth.set_access_token
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
