import twitter
import json
import pprint
from collections import Counter
from prettytable import PrettyTable


def oauth_login():
	"""
		Get keys and tokens from twitter API.
		Returns API handle.
	"""

	with open('twitter_oauth.json') as f:
		tokens = json.load(f)

	CONSUMER_KEY = tokens['CONSUMER_KEY']
	CONSUMER_SECRET = tokens['CONSUMER_SECRET']
	OAUTH_TOKEN = tokens['OAUTH_TOKEN']
	OAUTH_TOKEN_SECRET = tokens['OAUTH_TOKEN_SECRET']

	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	twitter_api = twitter.Twitter(auth=auth)

	return twitter_api


def twitter_search(twitter_api, q, **kw):
	"""
		Search tweets with specified criteria.
		Returns statuses.
	"""

	search_results = twitter_api.search.tweets(q=q, count=1, **kw)
	statuses = search_results['statuses']

	return statuses


def print_recent_tweets(statuses, **kw):
	"""
		Print tweets with names and hashtags corresponding to
		keywords searched
	"""

	status_texts = [status['text'] for status in statuses]
	screen_names = [user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions']]
	hashtags = [hashtag['text'] for status in statuses for hashtag in status['entities']['hashtags']]
	words = [w for t in status_texts for w in t.split()]

	# Pretty Print words, names and hashtags
	for label, data in (('Word', words), ('Screen Name', screen_names), ('Hashtag', hashtags)):
		pt = PrettyTable(field_names=[label, 'Count'])
		c = Counter(data)
		[pt.add_row(kv) for kv in c.most_common()[:50]]
		pt.align[label], pt.align['Count'] = 'l', 'r'
		print pt


def print_stream(twitter_api, q, **kw):
	"""
		Get a stream of tweets. See https://dev.twitter.com/streaming/overview
	"""

	twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
	stream = twitter_stream.statuses.filter(track=q)

	for tweet in stream:
		print tweet


twitter_api = oauth_login()

# Search for specific keywords
# See https://dev.twitter.com/rest/public/search
q = "@Orange_France"
statuses = twitter_search(twitter_api, q)

# print_recent_tweets(statuses)
print_stream(twitter_api, q)
