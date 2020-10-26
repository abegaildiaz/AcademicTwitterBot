import json
import tweepy
from scholarly import scholarly # ProxyGenerator

# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)

with open('creds.json') as f:
    keys = json.load(f)
# authenticate to Twitter
auth = tweepy.OAuthHandler(keys["api_key"], keys["api_key_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
# Create API object
api = tweepy.API(auth)

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Adam Moule')
author = next(search_query).fill()
# print(author.fill(sections=['basics']))
# author = next(search_query)
# print(author)

# Count number of author's publications
titles = ([pub.bib['title'] for pub in author.publications])
num = len(titles) - 1 
# print(num)

# Take a closer look at the last publication
last_pub = author.publications[num].fill()
for pub in author.publications:
    pub.fill()
    print(pub.bib['url'])
titles.reverse()

# print(titles[0])


#link = ([pub.bib['url'] for pub in author.publications])
#print(link)

# Tweet last paper
# api.update_status("Check out our latest paper!" + str(titles[0]) + str(link))

# print("Check out our latest paper!" + str(title[0]))