import json
import tweepy

with open('creds.json') as f:
    keys = json.load(f)

# class API([auth_handler=None],[host='api.twitter.com'],[search_host='search.twitter.com'],[cache=None]
#     [api_root='/1'],[search_root=''],[retry_count=0],[retry_delay=0],[retry_errors=None],[timeout=60]
#     [parser=ModelParser],[compression=False],[wait_on_rate_limit=False],[wait_on_rate_limit_notify=False],[proxy=None])

# authenticate to Twitter
auth = tweepy.OAuthHandler(keys["api_key"], keys["api_key_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Tweet Test")