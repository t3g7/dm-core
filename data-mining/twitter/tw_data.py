import twitter
import json
import pprint
from collections import Counter
from prettytable import PrettyTable

# Get tokens for Twitter API
with open('twitter_oauth.json') as f:
	tokens = json.load(f)

CONSUMER_KEY = tokens['CONSUMER_KEY']
CONSUMER_SECRET = tokens['CONSUMER_SECRET']
OAUTH_TOKEN = tokens['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = tokens['OAUTH_TOKEN_SECRET']

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

# Keywords and parameters for data mining
q = '@Orange_France+orange'
count = 1000
lang = 'fr'
locale = 'fr'
time_zone = 'Paris'

search_results = twitter_api.search.tweets(q=q, count=count, lang=lang)

with open('result.txt','w') as f:
	for status in search_results['statuses']:
		f.write(status['text'].encode('utf-8')+'\n')

statuses = search_results['statuses']

status_texts = [status['text'] for status in statuses]
screen_names = [user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions']]
hashtags = [hashtag['text'] for status in statuses for hashtag in status['entities']['hashtags']]
words = [w for t in status_texts for w in t.split()]

# Pretty Print words, names and hashtags
for label, data in (('Word', words), ('Screen Name', screen_names), ('Hashtag', hashtags)):
	pt = PrettyTable(field_names=[label, 'Count'])
	c = Counter(data)
	[ pt.add_row(kv) for kv in c.most_common()[:20] ]
	pt.align[label], pt.align['Count'] = 'l', 'r'
	print pt

