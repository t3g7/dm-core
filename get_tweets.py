#!/usr/bin/env python

import tweepy
import json
import os

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

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	return auth


class StreamListener(tweepy.StreamListener):

	def on_data(self, data):
		"""
			Export data to a text file
		"""

		dataset_dir = 'tweets_dataset'
		if not os.path.exists(dataset_dir):
			os.mkdir(dataset_dir)

		try:
			json_data = json.loads(data)
			print json_data['text']
			with open(dataset_dir + os.sep + 'tweets.txt', 'a') as f:
				f.write(data)
			return True
		except Exception, e:
			print 'Failed on data,', str(e)
			pass

	def on_error(self, status):
		print status


if __name__ == '__main__':

	auth = oauth_login()
	sl = StreamListener()
	stream = tweepy.Stream(auth=auth, listener=sl)

	# Search for specific keywords
	# See https://dev.twitter.com/rest/public/search
	languages = ['fr']
	keywords = ['orange', 'orange_france', 'sosh', 'sosh_fr', 'orange_conseil']
	stream.filter(languages=languages, track=keywords)
