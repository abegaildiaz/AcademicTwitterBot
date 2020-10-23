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

# Create a tweet
# api.update_status("Tweet Test")
# new_tweet = api.update_status()

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Adam Moule')
author = next(search_query).fill()
# print(author.fill(sections=['basics']))

# Print the titles of the author's publications
# print([pub.bib['title'] for pub in author.publications])

# Count number of author's publications
titles = ([pub.bib['title'] for pub in author.publications])
num = len(titles) - 1 
# print(num)

# Take a closer look at the __ publication
pub = author.publications[num].fill()
print(pub)

# # Which papers cited that publication?
# print([citation.bib['title'] for citation in pub.citedby])