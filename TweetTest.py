import json
import tweepy
from scholarly import scholarly

with open('creds.json') as f:
    keys = json.load(f)

# authenticate to Twitter
auth = tweepy.OAuthHandler(keys["api_key"], keys["api_key_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])

# Create API object
api = tweepy.API(auth)

print(next(scholarly.search_author('Adam Moule')))

# Create a tweet
# api.update_status("Tweet Test")

new_tweet = api.update_status()
for tweet in new_tweet:
    print(tweet.text)