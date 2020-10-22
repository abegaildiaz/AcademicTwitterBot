import json
import tweepy

with open('creds.json') as f:
    keys = json.load(f)

# authenticate to Twitter
auth = tweepy.OAuthHandler(keys["api_key"], keys["api_key_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Tweet Test")