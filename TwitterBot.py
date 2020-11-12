import json
import tweepy
from scholarly import scholarly , ProxyGenerator
import datetime
from fp.fp import FreeProxy

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

# pg = ProxyGenerator()
# proxy = FreeProxy(rand=True, timeout=1, country_id=['US']).get()
# pg.SingleProxy(http =proxy, https =proxy)
# scholarly.use_proxy(pg)

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_pubs('Adam Moule', year_low=current_year)
publication_results = []
for i in range(len(search_query._rows)):
    publication_results.append(next(search_query).fill())
print(publication_results)
adam_publications = []

#Build list of actual publications Adam is an author on.
for pub in publication_results:
    if adam_id in pub['author_id']:
        adam_publications.append(pub)
print(adam_publications)

# print(titles[0])


#link = ([pub.bib['url'] for pub in author.publications])
#print(link)

# Tweet last paper
# api.update_status("Check out our latest paper!" + str(titles[0]) + str(link))

# print("Check out our latest paper!" + str(title[0]))